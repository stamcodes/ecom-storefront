from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.order_item import OrderItemOut


class OrderOut(BaseModel):
    id: int
    customer_id: int
    created_by_user_id: int | None = None
    total_amount: float
    status: str
    customer_name: str | None = None
    created_at: datetime
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    customer_id: int
    created_by_user_id: int | None = None
    customer_name: str | None = Field(default=None, max_length=100)
    status: str = Field(default="open", max_length=20)


class OrderUpdate(BaseModel):
    status: str | None = Field(default=None, max_length=20)
    customer_name: str | None = Field(default=None, max_length=100)


class OrderStatusUpdate(BaseModel):
    status: str = Field(max_length=20)