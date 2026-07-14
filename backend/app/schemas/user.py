from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.schemas.role import RoleOut


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    role_id: int
    role: RoleOut
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    role_id: int
    is_active: bool = True


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    phone_number: str | None = None
    avatar_url: str | None = None
    role_id: int | None = None
    is_active: bool | None = None