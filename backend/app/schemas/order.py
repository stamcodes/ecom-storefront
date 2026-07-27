from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.order_item import OrderItemOut


class OrderOut(BaseModel):
    id: int
    customer_id: int | None = None
    status: str | None = None
    guest_name: str | None = None
    guest_email: str | None = None
    guest_phone: str | None = None
    shipping_address_id: int | None = None
    billing_address_id: int | None = None
    coupon_id: int | None = None
    order_status: str
    subtotal: float
    discount_amount: float
    shipping_amount: float
    tax_amount: float
    total_amount: float
    notes: str | None = None
    created_at: datetime
    placed_at: datetime | None = None
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="before")
    @classmethod
    def populate_status_compat(cls, data):
        if isinstance(data, dict):
            if data.get("status") is None and data.get("order_status") is not None:
                data = dict(data)
                data["status"] = data["order_status"]
        return data


class OrderCreate(BaseModel):
    customer_id: int | None = None
    guest_name: str | None = Field(default=None, max_length=100)
    guest_email: str | None = Field(default=None, max_length=255)
    guest_phone: str | None = Field(default=None, max_length=20)
    order_status: str = Field(default="open", max_length=20)


class OrderUpdate(BaseModel):
    order_status: str | None = Field(default=None, max_length=20)
    notes: str | None = None


class OrderStatusUpdate(BaseModel):
    status: str = Field(max_length=20)