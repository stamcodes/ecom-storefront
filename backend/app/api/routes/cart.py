from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.cart import (
    CartItemCreate,
    CartItemUpdate,
    CartOut,
    CartMergeRequest,
    ApplyCouponRequest,
)
from app.core.auth import get_current_user_optional

router = APIRouter()


def _compute_total(cart: Cart) -> float:
    return sum(item.unit_price_snapshot * item.quantity for item in cart.items)


def _serialize_cart(cart: Cart) -> dict:
    return {
        "id": cart.id,
        "customer_id": cart.customer_id,
        "guest_token": cart.guest_token,
        "coupon_id": cart.coupon_id,
        "items": [
            {
                "id": item.id,
                "product_variant_id": item.product_variant_id,
                "quantity": item.quantity,
                "unit_price_snapshot": item.unit_price_snapshot,
                "subtotal": item.unit_price_snapshot * item.quantity,
            }
            for item in cart.items
        ],
        "total": _compute_total(cart),
    }


async def _get_or_create_cart(
    db: AsyncSession,
    current_user: User | None,
    guest_token: str | None,
) -> Cart:
    if current_user:
        result = await db.execute(
            select(Cart).options(selectinload(Cart.items)).where(Cart.customer_id == current_user.id)
        )
        cart = result.scalar_one_or_none()
        if not cart:
            cart = Cart(customer_id=current_user.id)
            db.add(cart)
            await db.commit()
            await db.refresh(cart)
        return cart

    if not guest_token:
        raise HTTPException(status_code=400, detail="Guest token required for guest cart")

    result = await db.execute(
        select(Cart).options(selectinload(Cart.items)).where(Cart.guest_token == guest_token)
    )
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(guest_token=guest_token)
        db.add(cart)
        await db.commit()
        await db.refresh(cart)
    return cart


async def _reload_cart(db: AsyncSession, cart_id: int) -> Cart:
    result = await db.execute(
        select(Cart).options(selectinload(Cart.items)).where(Cart.id == cart_id)
    )
    return result.scalar_one()


@router.get("/cart", response_model=CartOut)
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    return _serialize_cart(cart)


@router.post("/cart/items", response_model=CartOut, status_code=201)
async def add_cart_item(
    payload: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(
        select(ProductVariant).where(ProductVariant.id == payload.product_variant_id)
    )
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.cart_id == cart.id,
            CartItem.product_variant_id == payload.product_variant_id,
        )
    )
    existing_item = result.scalar_one_or_none()

    if existing_item:
        existing_item.quantity += payload.quantity
    else:
        new_item = CartItem(
            cart_id=cart.id,
            product_variant_id=payload.product_variant_id,
            quantity=payload.quantity,
            unit_price_snapshot=variant.price,
        )
        db.add(new_item)

    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.put("/cart/items/{item_id}", response_model=CartOut)
async def update_cart_item(
    item_id: int,
    payload: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.quantity = payload.quantity
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/items/{item_id}", response_model=CartOut)
async def delete_cart_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    await db.delete(item)
    await db.commit()

    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.post("/cart/merge", response_model=CartOut)
async def merge_cart(
    payload: CartMergeRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user_optional),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Login required to merge cart")

    result = await db.execute(select(Cart).where(Cart.guest_token == payload.guest_token))
    guest_cart = result.scalar_one_or_none()
    if not guest_cart:
        raise HTTPException(status_code=404, detail="Guest cart not found")

    result = await db.execute(select(Cart).where(Cart.customer_id == current_user.id))
    user_cart = result.scalar_one_or_none()
    if not user_cart:
        guest_cart.customer_id = current_user.id
        guest_cart.guest_token = None
        await db.commit()
        return _serialize_cart(guest_cart)

    result = await db.execute(select(CartItem).where(CartItem.cart_id == guest_cart.id))
    guest_items = result.scalars().all()
    for guest_item in guest_items:
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == user_cart.id,
                CartItem.product_variant_id == guest_item.product_variant_id,
            )
        )
        existing_item = result.scalar_one_or_none()
        if existing_item:
            existing_item.quantity += guest_item.quantity
        else:
            db.add(CartItem(
                cart_id=user_cart.id,
                product_variant_id=guest_item.product_variant_id,
                quantity=guest_item.quantity,
                unit_price_snapshot=guest_item.unit_price_snapshot,
            ))

    await db.delete(guest_cart)
    await db.commit()
    user_cart = await _reload_cart(db, user_cart.id)
    return _serialize_cart(user_cart)


@router.post("/cart/apply-coupon", response_model=CartOut)
async def apply_coupon(
    payload: ApplyCouponRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    from app.models.coupon import Coupon

    result = await db.execute(select(Coupon).where(Coupon.code == payload.code))
    coupon = result.scalar_one_or_none()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    cart.coupon_id = coupon.id
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/coupon", response_model=CartOut)
async def remove_coupon(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    cart.coupon_id = None
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)
