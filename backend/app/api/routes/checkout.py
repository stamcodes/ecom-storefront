from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.order import OrderOut
from app.core.auth import get_current_user

router = APIRouter()

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


@router.post("/checkout", response_model=OrderOut, status_code=201)
async def checkout(
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

    # Lock and validate stock for every line before committing anything
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

    new_order = Order(
        customer_id=profile.id,
        customer_name=current_user.name,
        status="open",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()  # assigns new_order.id without committing

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one()

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

    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == new_order.id)
    )
    return result.scalar_one()