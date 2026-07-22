from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AddressBase(BaseModel):
    country: str
    state: Optional[str] = None
    city: str
    postal_code: Optional[str] = None
    address_line_1: str
    address_line_2: Optional[str] = None
    is_default: bool = False


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    is_default: Optional[bool] = None


class AddressOut(AddressBase):
    id: int
    customer_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True