from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class CustomerRegisterRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: str | None = None


class CustomerRegisterResponse(BaseModel):
    id: int
    name: str
    email: str
    email_verified: bool
    message: str


class CustomerLoginRequest(BaseModel):
    email: EmailStr
    password: str


class CustomerToken(BaseModel):
    access_token: str
    token_type: str


class CustomerVerifyEmailRequest(BaseModel):
    token: str


class CustomerResendVerificationRequest(BaseModel):
    email: EmailStr


class CustomerForgotPasswordRequest(BaseModel):
    email: EmailStr


class CustomerResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)


class MsgResponse(BaseModel):
    message: str