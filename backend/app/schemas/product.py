from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.category import CategoryOut


class ProductOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    is_active: bool
    created_at: datetime
    updated_at: datetime
    categories: list[CategoryOut] = []

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(gt=0)
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    is_active: bool | None = None