from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.order import Order
from app.models.product_variant import ProductVariant
from app.models.order_item import OrderItem
from app.models.user import User
from app.schemas.order_item import OrderItemOut, OrderItemCreate, OrderItemUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


def recalculate_total(order: Order, db: Session):
    total = sum(item.quantity * float(item.price_at_purchase) for item in order.items)
    order.total_amount = total
    db.commit()


@router.get("/orders/{order_id}/items", response_model=list[OrderItemOut])
def get_order_items(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return db.query(OrderItem).filter(OrderItem.order_id == order_id).all()


@router.post("/orders/{order_id}/items", response_model=OrderItemOut, status_code=201)
def add_order_item(
    order_id: int,
    payload: OrderItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    variant = db.query(ProductVariant).filter(ProductVariant.id == payload.product_variant_id).first()
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
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid product_variant_id")

    db.refresh(new_item)
    db.refresh(order)
    recalculate_total(order, db)
    db.refresh(new_item)
    return new_item


@router.put("/order-items/{item_id}", response_model=OrderItemOut)
def update_order_item(
    item_id: int,
    payload: OrderItemUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    update_data = payload.model_dump(exclude_unset=True)

    if "quantity" in update_data:
        variant = db.query(ProductVariant).filter(ProductVariant.id == item.product_variant_id).first()
        old_quantity = item.quantity
        new_quantity = update_data["quantity"]
        diff = new_quantity - old_quantity  # positive = needs more stock, negative = returns stock

        if diff > 0 and variant.stock_quantity < diff:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
            )

        variant.stock_quantity -= diff

    for field, value in update_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)

    order = db.query(Order).filter(Order.id == item.order_id).first()
    recalculate_total(order, db)
    db.refresh(item)
    return item


@router.delete("/order-items/{item_id}", status_code=204)
def delete_order_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    variant = db.query(ProductVariant).filter(ProductVariant.id == item.product_variant_id).first()
    if variant:
        variant.stock_quantity += item.quantity

    order_id = item.order_id
    db.delete(item)
    db.commit()

    order = db.query(Order).filter(Order.id == order_id).first()
    recalculate_total(order, db)
    return None