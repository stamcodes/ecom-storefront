from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.category import CategoryOut


class ProductCategoryOut(BaseModel):
    id: int
    product_id: int
    category_id: int
    category: CategoryOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductCategoryCreate(BaseModel):
    category_id: int
    