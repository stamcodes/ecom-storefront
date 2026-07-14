from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class OrderItemOut(BaseModel):
    id: int
    order_id: int
    product_variant_id: int | None
    quantity: int
    price_at_purchase: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderItemCreate(BaseModel):
    product_variant_id: int
    quantity: int = Field(gt=0)
    price_at_purchase: float = Field(gt=0)


class OrderItemUpdate(BaseModel):
    quantity: int | None = Field(default=None, gt=0)
    price_at_purchase: float | None = Field(default=None, gt=0)