import stripe
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.auth import get_current_user
from app.core.config import settings
from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User

router = APIRouter()

stripe.api_key = settings.STRIPE_SECRET_KEY  # <-- FLAG: pulled from Settings, confirm STRIPE_SECRET_KEY is set in .env

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _validate_cart_stock(db: AsyncSession, cart: Cart) -> float:
    """Validates stock for every line item, returns computed total."""
    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )
        total += float(variant.price) * item.quantity
    return total


@router.post("/payments/create-intent")
async def create_payment_intent(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = await _validate_cart_stock(db, cart)
    if total <= 0:
        raise HTTPException(status_code=400, detail="Invalid cart total")

    amount_in_cents = int(round(total * 100))

    intent = stripe.PaymentIntent.create(
        amount=amount_in_cents,
        currency="usd",  # <-- FLAG: confirm currency; hardcoded for now
        metadata={
            "cart_id": str(cart.id),
            "customer_id": str(profile.id),
        },
        automatic_payment_methods={"enabled": True},
    )

    return {"client_secret": intent.client_secret}


async def _create_order_from_cart(db: AsyncSession, cart_id: int, customer_id: int) -> None:
    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.id == cart_id, Cart.customer_id == customer_id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        # Cart already processed or emptied — avoid duplicate order creation on webhook retries
        return

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.id == customer_id))
    profile = result.scalar_one_or_none()
    if not profile:
        return

    new_order = Order(
        customer_id=profile.id,
        status="paid",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant:
            continue

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in cart.items:
        await db.delete(item)

    await db.commit()


@router.post("/payments/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET  # <-- FLAG: pulled from Settings, confirm STRIPE_WEBHOOK_SECRET is set in .env
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        metadata = intent.get("metadata", {})
        cart_id = metadata.get("cart_id")
        customer_id = metadata.get("customer_id")

        if cart_id and customer_id:
            await _create_order_from_cart(db, int(cart_id), int(customer_id))

    return {"status": "success"}