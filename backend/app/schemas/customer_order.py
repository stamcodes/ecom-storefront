from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.order_item import OrderItemOut


class CustomerOrderOut(BaseModel):
    id: int
    customer_name: str | None = None
    status: str
    total_amount: float
    created_at: datetime
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)


class ReturnRequestCreate(BaseModel):
    order_item_id: int
    reason: str | None = Field(default=None, max_length=1000)


class ReturnRequestStatusUpdate(BaseModel):
    status: str = Field(max_length=20)
    refund_amount: float | None = None


class ReturnRequestOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_item_id: int
    customer_id: int
    reason: str | None = None
    status: str
    refund_amount: float | None = None
    requested_at: datetime
    processed_at: datetime | None = None