from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class CustomerRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None


class EmailVerifyRequest(BaseModel):
    token: str


class CustomerProfileOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: Optional[str]
    avatar_url: Optional[str]
    email_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CustomerProfileUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None