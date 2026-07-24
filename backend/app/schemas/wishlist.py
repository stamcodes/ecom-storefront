from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WishlistCreate(BaseModel):
    product_id: int


class WishlistResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    product_id: int
    created_at: datetime