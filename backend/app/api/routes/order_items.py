from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.order import Order
from app.models.product_variant import ProductVariant
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemOut, OrderItemCreate, OrderItemUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


async def recalculate_total(order_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    total = sum(item.quantity * float(item.price_at_purchase) for item in result.scalars().all())

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        return

    order.total_amount = total
    await db.commit()


@router.get("/orders/{order_id}/items", response_model=list[OrderItemOut])
async def get_order_items(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    return result.scalars().all()


@router.post("/orders/{order_id}/items", response_model=OrderItemOut, status_code=201)
async def add_order_item(
    order_id: int,
    payload: OrderItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == payload.product_variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    if variant.stock_quantity < payload.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
        )

    new_item = OrderItem(
        order_id=order_id,
        product_variant_id=payload.product_variant_id,
        quantity=payload.quantity,
        price_at_purchase=payload.price_at_purchase,
    )
    variant.stock_quantity -= payload.quantity
    db.add(new_item)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid product_variant_id")

    await db.refresh(new_item)
    await recalculate_total(order_id, db)
    await db.refresh(new_item)
    return new_item


@router.put("/order-items/{item_id}", response_model=OrderItemOut)
async def update_order_item(
    item_id: int,
    payload: OrderItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    update_data = payload.model_dump(exclude_unset=True)

    if "quantity" in update_data:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if not variant:
            raise HTTPException(status_code=404, detail="Product variant not found")

        old_quantity = item.quantity
        new_quantity = update_data["quantity"]
        diff = new_quantity - old_quantity

        if diff > 0 and variant.stock_quantity < diff:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
            )

        variant.stock_quantity -= diff

    for field, value in update_data.items():
        setattr(item, field, value)

    await db.commit()
    await db.refresh(item)
    await recalculate_total(item.order_id, db)
    await db.refresh(item)
    return item


@router.delete("/order-items/{item_id}", status_code=204)
async def delete_order_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    if item.product_variant_id is not None:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if variant:
            variant.stock_quantity += item.quantity

    order_id = item.order_id
    await db.delete(item)
    await db.commit()

    await recalculate_total(order_id, db)
    return None
