from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.models.customer_order import Order, OrderItem, ReturnRequest
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.schemas.customer_order import (
    CustomerOrderOut,
    ReturnRequestCreate,
    ReturnRequestStatusUpdate,
    ReturnRequestOut,
)
from app.core.auth import get_current_user
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter(tags=["Customer Orders"])

CANCELLABLE_STATUSES = {"open", "pending"}


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _get_own_order(db: AsyncSession, order_id: int, profile: CustomerProfile) -> Order:
    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
    )
    order = result.scalar_one_or_none()
    if not order or order.customer_id != profile.id:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# ---- Orders ----

@router.post("/orders/{order_id}/cancel", response_model=CustomerOrderOut)
async def cancel_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    order = await _get_own_order(db, order_id, profile)

    if order.order_status not in CANCELLABLE_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Order in status '{order.order_status}' cannot be cancelled",
        )

    order.order_status = "cancelled"
    await db.commit()
    order = await _get_own_order(db, order_id, profile)
    return order


@router.post("/orders/{order_id}/reorder", response_model=CustomerOrderOut, status_code=201)
async def reorder(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    old_order = await _get_own_order(db, order_id, profile)

    result = await db.execute(select(Cart).where(Cart.customer_id == profile.id))
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(customer_id=profile.id)
        db.add(cart)
        await db.flush()

    for old_item in old_order.items:
        if old_item.product_variant_id is None:
            continue
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == cart.id,
                CartItem.product_variant_id == old_item.product_variant_id,
            )
        )
        cart_item = result.scalar_one_or_none()
        if cart_item:
            cart_item.quantity += old_item.quantity
        else:
            db.add(CartItem(
                cart_id=cart.id,
                product_variant_id=old_item.product_variant_id,
                quantity=old_item.quantity,
            ))

    await db.commit()
    old_order = await _get_own_order(db, order_id, profile)
    return old_order


@router.get("/orders/{order_id}/invoice", response_model=CustomerOrderOut)
async def get_invoice(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    order = await _get_own_order(db, order_id, profile)
    return order


# ---- Return Requests ----

@router.post("/return-requests", response_model=ReturnRequestOut, status_code=status.HTTP_201_CREATED)
async def create_return_request(
    payload: ReturnRequestCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(OrderItem).join(Order, Order.id == OrderItem.order_id).where(
            OrderItem.id == payload.order_item_id,
            Order.customer_id == profile.id,
        )
    )
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    existing = await db.execute(
        select(ReturnRequest).where(ReturnRequest.order_item_id == payload.order_item_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Return request already exists for this item")

    return_request = ReturnRequest(
        order_item_id=payload.order_item_id,
        customer_id=profile.id,
        reason=payload.reason,
    )
    db.add(return_request)
    await db.commit()
    await db.refresh(return_request)
    return return_request


@router.get("/return-requests", response_model=list[ReturnRequestOut])
async def list_return_requests(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(
        select(ReturnRequest).where(ReturnRequest.customer_id == profile.id)
    )
    return result.scalars().all()


@router.patch("/return-requests/{request_id}/status", response_model=ReturnRequestOut)
async def update_return_request_status(
    request_id: int,
    payload: ReturnRequestStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF)),
):
    result = await db.execute(select(ReturnRequest).where(ReturnRequest.id == request_id))
    return_request = result.scalar_one_or_none()
    if not return_request:
        raise HTTPException(status_code=404, detail="Return request not found")

    return_request.status = payload.status
    if payload.refund_amount is not None:
        return_request.refund_amount = payload.refund_amount
    if payload.status in ("approved", "rejected", "completed"):
        from datetime import datetime, timezone
        return_request.processed_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(return_request)
    return return_request