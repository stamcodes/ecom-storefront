from pydantic import BaseModel, Field
import uuid


class CartItemCreate(BaseModel):
    product_variant_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=1)


class CartItemOut(BaseModel):
    id: int
    product_variant_id: int
    quantity: int
    unit_price: float
    subtotal: float

    class Config:
        from_attributes = True


class CartOut(BaseModel):
    id: int
    customer_id: int | None
    guest_token: uuid.UUID | None
    coupon_id: int | None
    items: list[CartItemOut]
    total: float

    class Config:
        from_attributes = True


class CartMergeRequest(BaseModel):
    guest_token: str


class ApplyCouponRequest(BaseModel):
    code: str