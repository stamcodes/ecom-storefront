import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.schemas.customer_auth import (
    CustomerRegisterRequest,
    CustomerRegisterResponse,
    CustomerLoginRequest,
    CustomerToken,
    CustomerVerifyEmailRequest,
    CustomerResendVerificationRequest,
    CustomerForgotPasswordRequest,
    CustomerResetPasswordRequest,
    MsgResponse,
)
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token
from app.core.email import send_verification_email, send_password_reset_email

router = APIRouter(prefix="/customer/auth", tags=["Customer Auth"])

CUSTOMER_ROLE_ID = 4
VERIFICATION_TOKEN_EXPIRE_HOURS = 24
RESET_TOKEN_EXPIRE_HOURS = 1


@router.post("/register", response_model=CustomerRegisterResponse, status_code=status.HTTP_201_CREATED)
async def customer_register(payload: CustomerRegisterRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    verification_token = secrets.token_urlsafe(32)

    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        phone_number=payload.phone_number,
        role_id=CUSTOMER_ROLE_ID,
        is_active=True,
        email_verified=False,
        email_verification_token=verification_token,
        email_verification_expires_at=datetime.now(timezone.utc) + timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS),
    )
    db.add(new_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Could not create account")

    await db.refresh(new_user)

    profile = CustomerProfile(user_id=new_user.id)
    db.add(profile)
    await db.commit()

    send_verification_email(new_user.email, verification_token)

    return CustomerRegisterResponse(
        id=new_user.id,
        name=new_user.name,
        email=new_user.email,
        email_verified=new_user.email_verified,
        message="Account created. Check your email to verify your account.",
    )


@router.post("/login", response_model=CustomerToken)
async def customer_login(payload: CustomerLoginRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or user.role_id != CUSTOMER_ROLE_ID:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not verify_password(payload.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account is inactive")

    access_token = create_access_token(
        {"sub": str(user.id), "email": user.email, "role_id": user.role_id}
    )

    return CustomerToken(access_token=access_token, token_type="bearer")


@router.post("/verify-email", response_model=MsgResponse)
async def customer_verify_email(payload: CustomerVerifyEmailRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email_verification_token == payload.token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired verification link")

    if (
        not user.email_verification_expires_at
        or user.email_verification_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired verification link")

    user.email_verified = True
    user.email_verification_token = None
    user.email_verification_expires_at = None
    await db.commit()

    return MsgResponse(message="Email verified successfully. You can now log in.")


@router.post("/resend-verification", response_model=MsgResponse)
async def customer_resend_verification(payload: CustomerResendVerificationRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(message="If that email exists and is unverified, a new link has been sent.")

    if not user or user.email_verified:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.email_verification_token = token
    user.email_verification_expires_at = datetime.now(timezone.utc) + timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS)
    await db.commit()

    send_verification_email(user.email, token)

    return generic_response


@router.post("/forgot-password", response_model=MsgResponse)
async def customer_forgot_password(payload: CustomerForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(message="If that email exists, a password reset link has been sent.")

    if not user or not user.is_active:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.password_reset_token = token
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
    await db.commit()

    send_password_reset_email(user.email, token)

    return generic_response


@router.post("/reset-password", response_model=MsgResponse)
async def customer_reset_password(payload: CustomerResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.password_reset_token == payload.token, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if (
        not user.password_reset_expires_at
        or user.password_reset_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is inactive")

    user.password = hash_password(payload.new_password)
    user.password_reset_token = None
    user.password_reset_expires_at = None
    await db.commit()

    return MsgResponse(message="Password reset successfully. Please log in with your new password.")