This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
api/
  routes/
    auth.py
    cart.py
    categories.py
    checkout.py
    customer_auth.py
    customer_profiles.py
    order_items.py
    orders.py
    payments.py
    permissions.py
    product_categories.py
    product_variants.py
    products.py
    reviews.py
    role_permissions.py
    roles.py
    users.py
core/
  auth.py
  cart_helpers.py
  config.py
  email.py
  jwt.py
  permissions.py
  security.py
  test_seed.py
database/
  base.py
  session.py
models/
  __init__.py
  address.py
  cart_item.py
  cart.py
  category.py
  coupon.py
  customer_profile.py
  order_item.py
  order.py
  payment.py
  permission.py
  product_category.py
  product_variant.py
  product.py
  review.py
  role_permission.py
  role.py
  user.py
repositories/
  cart_repository.py
schemas/
  __init__.py
  address.py
  auth.py
  cart.py
  category.py
  customer_auth.py
  customer_profile.py
  order_item.py
  order.py
  permission.py
  product_category.py
  product_variant.py
  product.py
  review.py
  role_permission.py
  role.py
  user.py
main.py
seed.py
```

# Files

## File: api/routes/auth.py
```python
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.schemas.auth import LoginRequest, Token, ForgotPasswordRequest, ResetPasswordRequest
from app.core.jwt import create_access_token
from app.core.security import verify_password, hash_password
from app.core.auth import get_current_user
from app.core.email import send_password_reset_email
from pydantic import BaseModel

router = APIRouter()

RESET_TOKEN_EXPIRE_HOURS = 1


class MsgResponse(BaseModel):
    message: str


@router.post("/login", response_model=Token)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role_id": user.role_id,
        }
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(Permission.name)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .where(RolePermission.role_id == current_user.role_id)
    )
    result = await db.execute(stmt)
    permissions = list(result.scalars().all())

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role_id": current_user.role_id,
        "role": {
            "id": current_user.role.id,
            "name": current_user.role.name,
            "description": current_user.role.description,
        } if current_user.role else None,
        "is_active": current_user.is_active,
        "created_at": current_user.created_at,
        "updated_at": current_user.updated_at,
        "permissions": permissions,
    }


@router.post("/forgot-password", response_model=MsgResponse)
async def forgot_password(payload: ForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(
        message="If that email exists, a password reset link has been sent."
    )

    if not user or not user.is_active:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.password_reset_token = token
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(
        hours=RESET_TOKEN_EXPIRE_HOURS
    )
    await db.commit()

    send_password_reset_email(user.email, token)

    return generic_response


@router.post("/reset-password", response_model=MsgResponse)
async def reset_password(payload: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.password_reset_token == payload.token)
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
        raise HTTPException(status_code=403, detail="User account is inactive")

    user.password = hash_password(payload.new_password)
    user.password_reset_token = None
    user.password_reset_expires_at = None
    await db.commit()

    return MsgResponse(
        message="Password has been reset successfully. Please log in with your new password."
    )
```

## File: api/routes/cart.py
```python
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.schemas.cart import (
    CartItemCreate,
    CartItemUpdate,
    CartOut,
    CartMergeRequest,
    ApplyCouponRequest,
)
from app.core.auth import get_current_user_optional

router = APIRouter()

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


def _compute_total(cart: Cart) -> float:
    return sum(float(item.product_variant.price) * item.quantity for item in cart.items)


def _serialize_cart(cart: Cart) -> dict:
    return {
        "id": cart.id,
        "customer_id": cart.customer_id,
        "guest_token": cart.guest_token,
        "coupon_id": cart.coupon_id,
        "items": [
            {
                "id": item.id,
                "product_variant_id": item.product_variant_id,
                "quantity": item.quantity,
                "unit_price": float(item.product_variant.price),
                "subtotal": float(item.product_variant.price) * item.quantity,
            }
            for item in cart.items
        ],
        "total": _compute_total(cart),
    }


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _get_or_create_cart(
    db: AsyncSession,
    current_user: User | None,
    guest_token: str | None,
) -> Cart:
    if current_user:
        profile = await _get_or_create_customer_profile(db, current_user)

        result = await db.execute(
            select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
        )
        cart = result.scalar_one_or_none()
        if not cart:
            cart = Cart(customer_id=profile.id)
            db.add(cart)
            await db.commit()
            cart = await _reload_cart(db, cart.id)
        return cart

    if not guest_token:
        raise HTTPException(status_code=400, detail="Guest token required for guest cart")

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.guest_token == guest_token)
    )
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(guest_token=guest_token)
        db.add(cart)
        await db.commit()
        cart = await _reload_cart(db, cart.id)
    return cart


async def _reload_cart(db: AsyncSession, cart_id: int) -> Cart:
    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.id == cart_id)
    )
    return result.scalar_one()


@router.get("/cart", response_model=CartOut)
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    return _serialize_cart(cart)


@router.post("/cart/items", response_model=CartOut, status_code=201)
async def add_cart_item(
    payload: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(
        select(ProductVariant).where(ProductVariant.id == payload.product_variant_id)
    )
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.cart_id == cart.id,
            CartItem.product_variant_id == payload.product_variant_id,
        )
    )
    existing_item = result.scalar_one_or_none()

    if existing_item:
        existing_item.quantity += payload.quantity
    else:
        new_item = CartItem(
            cart_id=cart.id,
            product_variant_id=payload.product_variant_id,
            quantity=payload.quantity,
        )
        db.add(new_item)

    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.put("/cart/items/{item_id}", response_model=CartOut)
async def update_cart_item(
    item_id: int,
    payload: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.quantity = payload.quantity
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/items/{item_id}", response_model=CartOut)
async def delete_cart_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    await db.delete(item)
    await db.commit()

    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.post("/cart/merge", response_model=CartOut)
async def merge_cart(
    payload: CartMergeRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user_optional),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Login required to merge cart")

    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Cart).where(Cart.guest_token == payload.guest_token))
    guest_cart = result.scalar_one_or_none()
    if not guest_cart:
        raise HTTPException(status_code=404, detail="Guest cart not found")

    result = await db.execute(select(Cart).where(Cart.customer_id == profile.id))
    user_cart = result.scalar_one_or_none()
    if not user_cart:
        guest_cart.customer_id = profile.id
        guest_cart.guest_token = None
        await db.commit()
        cart = await _reload_cart(db, guest_cart.id)
        return _serialize_cart(cart)

    result = await db.execute(select(CartItem).where(CartItem.cart_id == guest_cart.id))
    guest_items = result.scalars().all()
    for guest_item in guest_items:
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == user_cart.id,
                CartItem.product_variant_id == guest_item.product_variant_id,
            )
        )
        existing_item = result.scalar_one_or_none()
        if existing_item:
            existing_item.quantity += guest_item.quantity
        else:
            db.add(CartItem(
                cart_id=user_cart.id,
                product_variant_id=guest_item.product_variant_id,
                quantity=guest_item.quantity,
            ))

    await db.delete(guest_cart)
    await db.commit()
    user_cart = await _reload_cart(db, user_cart.id)
    return _serialize_cart(user_cart)


@router.post("/cart/apply-coupon", response_model=CartOut)
async def apply_coupon(
    payload: ApplyCouponRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(select(Coupon).where(Coupon.code == payload.code))
    coupon = result.scalar_one_or_none()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    if not coupon.is_active:
        raise HTTPException(status_code=400, detail="Coupon is not active")

    now = datetime.now(timezone.utc)
    if now < coupon.start_date or now > coupon.end_date:
        raise HTTPException(status_code=400, detail="Coupon is not valid at this time")

    if coupon.usage_limit is not None and coupon.usage_count >= coupon.usage_limit:
        raise HTTPException(status_code=400, detail="Coupon usage limit reached")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    cart_total = _compute_total(cart)
    min_order = coupon.minimum_order_amount or 0
    if cart_total < float(min_order):
        raise HTTPException(
            status_code=400,
            detail=f"Order must be at least {min_order} to use this coupon",
        )

    cart.coupon_id = coupon.id
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/coupon", response_model=CartOut)
async def remove_coupon(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    cart.coupon_id = None
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)
```

## File: api/routes/categories.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryOut, CategoryCreate, CategoryUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/categories", response_model=list[CategoryOut])
async def get_categories(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category))
    return result.scalars().all()


@router.get("/categories/{category_id}", response_model=CategoryOut)
async def get_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/categories", response_model=CategoryOut, status_code=201)
async def create_category(
    payload: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Category name already exists")

    new_category = Category(
        name=payload.name,
        description=payload.description,
    )
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category


@router.put("/categories/{category_id}", response_model=CategoryOut)
async def update_category(
    category_id: int,
    payload: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)

    await db.commit()
    await db.refresh(category)
    return category


@router.delete("/categories/{category_id}", status_code=204)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    await db.delete(category)
    await db.commit()
    return None
```

## File: api/routes/checkout.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.order import OrderOut
from app.core.auth import get_current_user

router = APIRouter()

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.post("/checkout", response_model=OrderOut, status_code=201)
async def checkout(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Lock and validate stock for every line before committing anything
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )

    new_order = Order(
        customer_id=profile.id,
        customer_name=current_user.name,
        status="open",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()  # assigns new_order.id without committing

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one()

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in cart.items:
        await db.delete(item)

    await db.commit()

    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == new_order.id)
    )
    return result.scalar_one()
```

## File: api/routes/customer_auth.py
```python
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
```

## File: api/routes/customer_profiles.py
```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.address import Address
from backend.app.schemas.customer_profile import CustomerProfileOut, CustomerProfileUpdate
from app.schemas.address import AddressCreate, AddressUpdate, AddressOut
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/me", response_model=CustomerProfileOut)
async def get_customer_profile(current_user: User = Depends(get_current_user)):
    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.put("/me", response_model=CustomerProfileOut)
async def update_customer_profile(
    payload: CustomerProfileUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    update_data = payload.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)

    await db.commit()
    await db.refresh(current_user)

    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.get("/addresses", response_model=list[AddressOut])
async def list_addresses(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
    result = await db.execute(stmt)
    return list(result.scalars().all())


@router.post("/addresses", response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    payload: AddressCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if payload.is_default:
        stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
        result = await db.execute(stmt)
        for existing in result.scalars().all():
            existing.is_default = False

    address = Address(customer_id=current_user.customer_profile.id, **payload.dict())
    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address


@router.put("/addresses/{address_id}", response_model=AddressOut)
async def update_address(
    address_id: int,
    payload: AddressUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    update_data = payload.dict(exclude_unset=True)

    if update_data.get("is_default"):
        stmt = select(Address).where(
            Address.customer_id == current_user.customer_profile.id,
            Address.id != address_id,
        )
        result = await db.execute(stmt)
        for other in result.scalars().all():
            other.is_default = False

    for field, value in update_data.items():
        setattr(address, field, value)

    await db.commit()
    await db.refresh(address)
    return address


@router.delete("/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
    address_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    await db.delete(address)
    await db.commit()
    return None
```

## File: api/routes/order_items.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.models.order import Order
from app.models.product_variant import ProductVariant
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemOut, OrderItemCreate, OrderItemUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()

# #TODO: final check if completed is the exact status indicator.
LOCKED_STATUS = "completed"


def _assert_order_editable(order: Order) -> None:
    if order.status == LOCKED_STATUS:
        raise HTTPException(
            status_code=400,
            detail=f"Order is '{LOCKED_STATUS}' and can no longer be modified",
        )


async def recalculate_total(order_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    total = sum(item.quantity * float(item.price_at_purchase) for item in result.scalars().all())

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        return

    order.total_amount = total
    await db.commit()


@router.get("/orders/{order_id}/items", response_model=list[OrderItemOut])
async def get_order_items(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    return result.scalars().all()


@router.post("/orders/{order_id}/items", response_model=OrderItemOut, status_code=201)
async def add_order_item(
    order_id: int,
    payload: OrderItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == payload.product_variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    if variant.stock_quantity < payload.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
        )

    new_item = OrderItem(
        order_id=order_id,
        product_variant_id=payload.product_variant_id,
        quantity=payload.quantity,
        price_at_purchase=payload.price_at_purchase,
    )
    variant.stock_quantity -= payload.quantity
    db.add(new_item)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid product_variant_id")

    await db.refresh(new_item)
    await recalculate_total(order_id, db)
    await db.refresh(new_item)
    return new_item


@router.put("/order-items/{item_id}", response_model=OrderItemOut)
async def update_order_item(
    item_id: int,
    payload: OrderItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    result = await db.execute(select(Order).where(Order.id == item.order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    update_data = payload.model_dump(exclude_unset=True)

    if "quantity" in update_data:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if not variant:
            raise HTTPException(status_code=404, detail="Product variant not found")

        old_quantity = item.quantity
        new_quantity = update_data["quantity"]
        diff = new_quantity - old_quantity

        if diff > 0 and variant.stock_quantity < diff:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
            )

        variant.stock_quantity -= diff

    for field, value in update_data.items():
        setattr(item, field, value)

    await db.commit()
    await db.refresh(item)
    await recalculate_total(item.order_id, db)
    await db.refresh(item)
    return item


@router.delete("/order-items/{item_id}", status_code=204)
async def delete_order_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    result = await db.execute(select(Order).where(Order.id == item.order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    if item.product_variant_id is not None:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if variant:
            variant.stock_quantity += item.quantity

    order_id = item.order_id
    await db.delete(item)
    await db.commit()

    await recalculate_total(order_id, db)
    return None
```

## File: api/routes/orders.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.user import User
from app.models.order import Order
from app.schemas.order import OrderOut, OrderCreate, OrderUpdate, OrderStatusUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/orders", response_model=list[OrderOut])
async def get_orders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order))
    return result.scalars().all()


@router.get("/orders/{order_id}", response_model=OrderOut)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/orders", response_model=OrderOut, status_code=201)
async def create_order(
    payload: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(User).where(User.id == payload.created_by_user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_order = Order(
        created_by_user_id=payload.created_by_user_id,
        customer_name=payload.customer_name,
        status=payload.status,
        total_amount=0,
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order


@router.put("/orders/{order_id}", response_model=OrderOut)
async def update_order(
    order_id: int,
    payload: OrderUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(order, field, value)

    await db.commit()
    await db.refresh(order)
    return order


@router.patch("/orders/{order_id}/status", response_model=OrderOut)
async def update_order_status(
    order_id: int,
    payload: OrderStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = payload.status
    await db.commit()
    await db.refresh(order)
    return order


@router.delete("/orders/{order_id}", status_code=204)
async def delete_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    await db.delete(order)
    await db.commit()
    return None
```

## File: api/routes/payments.py
```python
import stripe
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.auth import get_current_user
from app.core.config import settings
from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User

router = APIRouter()

stripe.api_key = settings.STRIPE_SECRET_KEY  # <-- FLAG: pulled from Settings, confirm STRIPE_SECRET_KEY is set in .env

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _validate_cart_stock(db: AsyncSession, cart: Cart) -> float:
    """Validates stock for every line item, returns computed total."""
    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )
        total += float(variant.price) * item.quantity
    return total


@router.post("/payments/create-intent")
async def create_payment_intent(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = await _validate_cart_stock(db, cart)
    if total <= 0:
        raise HTTPException(status_code=400, detail="Invalid cart total")

    amount_in_cents = int(round(total * 100))

    intent = stripe.PaymentIntent.create(
        amount=amount_in_cents,
        currency="usd",  # <-- FLAG: confirm currency; hardcoded for now
        metadata={
            "cart_id": str(cart.id),
            "customer_id": str(profile.id),
        },
        automatic_payment_methods={"enabled": True},
    )

    return {"client_secret": intent.client_secret}


async def _create_order_from_cart(db: AsyncSession, cart_id: int, customer_id: int) -> None:
    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.id == cart_id, Cart.customer_id == customer_id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        # Cart already processed or emptied — avoid duplicate order creation on webhook retries
        return

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.id == customer_id))
    profile = result.scalar_one_or_none()
    if not profile:
        return

    new_order = Order(
        customer_id=profile.id,
        status="paid",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant:
            continue

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in cart.items:
        await db.delete(item)

    await db.commit()


@router.post("/payments/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET  # <-- FLAG: pulled from Settings, confirm STRIPE_WEBHOOK_SECRET is set in .env
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        metadata = intent.get("metadata", {})
        cart_id = metadata.get("cart_id")
        customer_id = metadata.get("customer_id")

        if cart_id and customer_id:
            await _create_order_from_cart(db, int(cart_id), int(customer_id))

    return {"status": "success"}
```

## File: api/routes/permissions.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.permission import Permission
from app.models.user import User
from app.schemas.permission import PermissionOut, PermissionCreate, PermissionUpdate
from app.core.permissions import require_role, ADMIN

router = APIRouter()


@router.get("/permissions", response_model=list[PermissionOut])
async def get_permissions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission))
    return result.scalars().all()


@router.get("/permissions/{permission_id}", response_model=PermissionOut)
async def get_permission(
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.post("/permissions", response_model=PermissionOut, status_code=201)
async def create_permission(
    payload: PermissionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Permission name already exists")

    new_permission = Permission(name=payload.name, description=payload.description)
    db.add(new_permission)
    await db.commit()
    await db.refresh(new_permission)
    return new_permission


@router.put("/permissions/{permission_id}", response_model=PermissionOut)
async def update_permission(
    permission_id: int,
    payload: PermissionUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(permission, field, value)

    await db.commit()
    await db.refresh(permission)
    return permission


@router.delete("/permissions/{permission_id}", status_code=204)
async def delete_permission(
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    await db.delete(permission)
    await db.commit()
    return None
```

## File: api/routes/product_categories.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.category import Category
from app.models.product_category import ProductCategory
from app.models.user import User
from app.schemas.product_category import ProductCategoryOut, ProductCategoryCreate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/categories", response_model=list[ProductCategoryOut])
async def get_product_categories(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductCategory).where(ProductCategory.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/categories", response_model=ProductCategoryOut, status_code=201)
async def assign_category_to_product(
    product_id: int,
    payload: ProductCategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Category).where(Category.id == payload.category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == payload.category_id,
        )
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="This product is already assigned to this category")

    link = ProductCategory(product_id=product_id, category_id=payload.category_id)
    db.add(link)
    await db.commit()
    await db.refresh(link)
    return link


@router.delete("/products/{product_id}/categories/{category_id}", status_code=204)
async def remove_category_from_product(
    product_id: int,
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == category_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="This product is not assigned to this category")

    await db.delete(link)
    await db.commit()
    return None
```

## File: api/routes/product_variants.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.product_variant import ProductVariantOut, ProductVariantCreate, ProductVariantUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/variants", response_model=list[ProductVariantOut])
async def get_product_variants(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductVariant).where(ProductVariant.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/variants", response_model=ProductVariantOut, status_code=201)
async def create_product_variant(
    product_id: int,
    payload: ProductVariantCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_variant = ProductVariant(
        product_id=product_id,
        sku=payload.sku,
        price=payload.price,
        stock_quantity=payload.stock_quantity,
        is_active=payload.is_active,
    )
    db.add(new_variant)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU already exists")

    await db.refresh(new_variant)
    return new_variant


@router.get("/variants/{variant_id}", response_model=ProductVariantOut)
async def get_variant(
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")
    return variant


@router.put("/variants/{variant_id}", response_model=ProductVariantOut)
async def update_variant(
    variant_id: int,
    payload: ProductVariantUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(variant, field, value)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU already exists")

    await db.refresh(variant)
    return variant


@router.delete("/variants/{variant_id}", status_code=204)
async def delete_variant(
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    try:
        await db.delete(variant)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="This variant cannot be deleted because it has existing orders. Deactivate it instead.",
        )

    return None
```

## File: api/routes/products.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductOut, ProductCreate, ProductUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products", response_model=list[ProductOut])
async def get_products(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product))
    return result.scalars().all()


@router.get("/products/{product_id}", response_model=ProductOut)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products", response_model=ProductOut, status_code=201)
async def create_product(
    payload: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Product name already exists")

    new_product = Product(
        name=payload.name,
        description=payload.description,
        price=payload.price,
        is_active=payload.is_active,
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@router.put("/products/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)
    return product


@router.delete("/products/{product_id}", status_code=204)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.delete(product)
    await db.commit()
    return None
```

## File: api/routes/reviews.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.review import Review
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewOut, ReviewUpdate
from app.core.auth import get_current_user

router = APIRouter()


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("/products/{product_id}/reviews", response_model=list[ReviewOut])
async def get_product_reviews(
    product_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Review).where(Review.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/reviews", response_model=ReviewOut, status_code=201)
async def create_product_review(
    product_id: int,
    payload: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    profile = await _get_or_create_customer_profile(db, current_user)

    # TODO: BYPASSED VERIFIED-PURCHASE CHECK.
    # Checkout isn't built yet, so there's no real link from order_item_id -> this
    # customer. Once POST /checkout exists and Order has a customer_id, replace this
    # block with a real check, e.g.:
    #   - fetch OrderItem by payload.order_item_id
    #   - join to Order, confirm Order.customer_id == profile.id
    #   - confirm OrderItem.product_variant -> product_id == product_id
    #   - 404/403 if any of that fails
    # For now we only confirm the order_item_id points to a row that exists.
    from app.models.order_item import OrderItem
    result = await db.execute(select(OrderItem).where(OrderItem.id == payload.order_item_id))
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    new_review = Review(
        customer_id=profile.id,
        product_id=product_id,
        order_item_id=payload.order_item_id,
        rating=payload.rating,
        comment=payload.comment,
    )
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)
    return new_review


@router.put("/reviews/{review_id}", response_model=ReviewOut)
async def update_review(
    review_id: int,
    payload: ReviewUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only edit your own reviews")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(review, field, value)

    await db.commit()
    await db.refresh(review)
    return review


@router.delete("/reviews/{review_id}", status_code=204)
async def delete_review(
    review_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only delete your own reviews")

    await db.delete(review)
    await db.commit()
    return None
```

## File: api/routes/role_permissions.py
```python
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.models.user import User
from app.schemas.permission import PermissionOut
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


class RolePermissionsSync(BaseModel):
    permission_ids: list[int]


@router.get("/roles/permissions", response_model=list[PermissionOut])
async def get_all_permissions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Permission))
    return result.scalars().all()


@router.get("/roles/{role_id}/permissions", response_model=list[PermissionOut])
async def get_role_permissions(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    result = await db.execute(
        select(Permission)
        .join(RolePermission, Permission.id == RolePermission.permission_id)
        .where(RolePermission.role_id == role_id)
    )
    return result.scalars().all()


@router.post("/roles/{role_id}/permissions", status_code=200)
async def assign_permissions_to_role(
    role_id: int,
    payload: RolePermissionsSync,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    result = await db.execute(select(RolePermission).where(RolePermission.role_id == role_id))
    current_links = result.scalars().all()
    current_perm_ids = {link.permission_id for link in current_links}

    target_perm_ids = set(payload.permission_ids)
    to_delete = [link for link in current_links if link.permission_id not in target_perm_ids]
    to_insert_ids = target_perm_ids - current_perm_ids

    for link in to_delete:
        await db.delete(link)

    if to_insert_ids:
        result = await db.execute(select(func.count()).select_from(Permission).where(Permission.id.in_(to_insert_ids)))
        valid_perms_count = result.scalar_one()
        if valid_perms_count != len(to_insert_ids):
            raise HTTPException(status_code=400, detail="One or more permission IDs are invalid")

        for perm_id in to_insert_ids:
            new_link = RolePermission(role_id=role_id, permission_id=perm_id)
            db.add(new_link)

    await db.commit()
    return {"status": "success", "message": "Permissions updated successfully"}


@router.delete("/roles/{role_id}/permissions/{permission_id}", status_code=204)
async def remove_permission_from_role(
    role_id: int,
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    result = await db.execute(
        select(RolePermission).where(
            RolePermission.role_id == role_id,
            RolePermission.permission_id == permission_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="Permission assignment not found")

    await db.delete(link)
    await db.commit()
    return None
```

## File: api/routes/roles.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.role import RoleOut, RoleCreate, RoleUpdate
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


@router.get("/roles", response_model=list[RoleOut])
async def get_roles(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role))
    return result.scalars().all()


@router.get("/roles/{role_id}", response_model=RoleOut)
async def get_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/roles", response_model=RoleOut, status_code=201)
async def create_role(
    payload: RoleCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Role).where(Role.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Role name already exists")

    new_role = Role(name=payload.name, description=payload.description)
    db.add(new_role)
    await db.commit()
    await db.refresh(new_role)
    return new_role


@router.put("/roles/{role_id}", response_model=RoleOut)
async def update_role(
    role_id: int,
    payload: RoleUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(role, field, value)

    await db.commit()
    await db.refresh(role)
    return role


@router.delete("/roles/{role_id}", status_code=204)
async def delete_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    try:
        await db.delete(role)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Cannot delete role: it is still assigned to one or more users"
        )
    return None
```

## File: api/routes/users.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.core.security import hash_password
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER
from app.core.auth import get_current_user_optional

router = APIRouter()

CUSTOMER_ROLE_ID = 4


@router.get("/users", response_model=list[UserOut])
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(User).options(selectinload(User.role)))
    return result.scalars().all()


@router.post("/users", response_model=UserOut, status_code=201)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional)
):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    if current_user is not None and current_user.role_id == 1:
        final_role_id = payload.role_id
    else:
        final_role_id = CUSTOMER_ROLE_ID

    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        phone_number=payload.phone_number,
        avatar_url=payload.avatar_url,
        role_id=final_role_id,
        is_active=payload.is_active,
    )

    db.add(new_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid role_id: role does not exist")

    stmt = (
        select(User)
        .options(selectinload(User.role))
        .where(User.id == new_user.id)
    )
    result = await db.execute(stmt)
    created_user = result.scalar_one()

    return created_user


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    payload: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    block_manager_on_admin_target(current_user, user.role_id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid role_id: role does not exist")

    stmt = (
        select(User)
        .options(selectinload(User.role))
        .where(User.id == user_id)
    )
    result = await db.execute(stmt)
    updated_user = result.scalar_one()

    return updated_user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return None
```

## File: core/auth.py
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.core.jwt import verify_access_token

# HTTP Bearer for strictly-authenticated routes
security = HTTPBearer()

# HTTP Bearer for optional-auth routes (guest-or-user) — does NOT auto-error
# when missing, but DOES register the security requirement so Swagger/OpenAPI
# attaches the Authorize token to requests on these routes.
security_optional = HTTPBearer(auto_error=False)


async def _get_current_user_by_token(token: str, db: AsyncSession) -> User:
    payload = verify_access_token(token)

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    stmt = select(User).options(selectinload(User.role)).where(User.id == int(user_id))
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    return await _get_current_user_by_token(credentials.credentials, db)


async def get_current_user_optional(
    credentials: HTTPAuthorizationCredentials | None = Depends(security_optional),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """
    Returns the authenticated User if a valid Bearer token is present.
    Returns None if no token is present, or if the token is invalid/expired
    (silently — callers fall back to guest-token logic in that case).
    """
    if not credentials:
        return None

    try:
        return await _get_current_user_by_token(credentials.credentials, db)
    except HTTPException:
        return None
```

## File: core/cart_helpers.py
```python

```

## File: core/config.py
```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    SMTP_HOST: str = "sandbox.smtp.mailtrap.io"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = "PLACEHOLDER_USERNAME"
    SMTP_PASSWORD: str = "PLACEHOLDER_PASSWORD"
    FROM_EMAIL: str = "no-reply@yourapp.com"
    FRONTEND_URL: str = "https://yourapp.com"

    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    TEST_MODE: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()
```

## File: core/email.py
```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings

FROM_EMAIL = settings.FROM_EMAIL


def send_email(to: str, subject: str, body: str, html: bool = False) -> None:
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html" if html else "plain"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, [to], msg.as_string())


def send_verification_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    subject = "Verify your email"
    body = f"Click the link to verify your email: {link}\nThis link expires in 24 hours."
    send_email(to, subject, body)


def send_password_reset_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/reset-password?token={token}"
    subject = "Reset your password"
    body = f"Click the link to reset your password: {link}\nThis link expires in 1 hour."
    send_email(to, subject, body)
```

## File: core/jwt.py
```python
from datetime import datetime, timedelta, timezone
from jose import jwt
from jose import JWTError, jwt
from fastapi import HTTPException, status

from app.core.config import settings


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
```

## File: core/permissions.py
```python
from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.core.auth import get_current_user

ADMIN = 1
MANAGER = 2
STAFF = 3


def require_role(*allowed_role_ids: int):
    """
    Returns a FastAPI dependency that checks whether the current user's
    role_id is in the allowed list.

    Usage:
        @router.post("/products")
        def create_product(
            current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
        ):
            ...
    """

    def dependency(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role_id not in allowed_role_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        return current_user

    return dependency


def block_manager_on_admin_target(current_user: User, target_role_id: int):
    """
    Managers can manage roles/permissions for everyone except Admins.
    Call this after fetching the target resource's role_id.
    """
    if current_user.role_id == MANAGER and target_role_id == ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Managers cannot modify Admin-level roles or users",
        )
```

## File: core/security.py
```python
import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)
```

## File: core/test_seed.py
```python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from datetime import datetime, timedelta, timezone

BOGUS_PRODUCT_ID = 999001
BOGUS_VARIANT_ID = 999001
BOGUS_VARIANT_SKU = "BOGUS-TEST-SKU"
BOGUS_COUPON_CODE = "TESTCODE10"


async def ensure_bogus_data(db: AsyncSession) -> None:
    result = await db.execute(select(Product).where(Product.id == BOGUS_PRODUCT_ID))
    product = result.scalar_one_or_none()
    if not product:
        product = Product(
            id=BOGUS_PRODUCT_ID,
            name="Bogus Test Product",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            price=9.99,
            is_active=True,
        )
        db.add(product)
        await db.flush()

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == BOGUS_VARIANT_ID))
    variant = result.scalar_one_or_none()
    if not variant:
        variant = ProductVariant(
            id=BOGUS_VARIANT_ID,
            product_id=BOGUS_PRODUCT_ID,
            sku=BOGUS_VARIANT_SKU,
            price=9.99,
            stock_quantity=1000,
            is_active=True,
        )
        db.add(variant)

    result = await db.execute(select(Coupon).where(Coupon.code == BOGUS_COUPON_CODE))
    coupon = result.scalar_one_or_none()
    if not coupon:
        coupon = Coupon(
            code=BOGUS_COUPON_CODE,
            name="Bogus Test Coupon",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            discount_type="percentage",
            discount_value=10,
            minimum_order_amount=0,
            usage_limit=None,
            usage_count=0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=365),
            is_active=True,
        )
        db.add(coupon)

    await db.commit()
```

## File: database/base.py
```python
from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str


    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
```

## File: database/session.py
```python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# Create our asynchronous database engine using modern Asyncio wrappers
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Shows SQL queries in terminal (disable in production)
    future=True
)

# Create an asynchronous session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

# Database Dependency - Yields an AsyncSession instead of a synchronous Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
```

## File: models/__init__.py
```python
from .user import User
from .role import Role
from .permission import Permission
from .role_permission import RolePermission
from .product import Product
from .product_category import ProductCategory
from .category import Category
from .product_variant import ProductVariant
from .order import Order
from .order_item import OrderItem
from .cart import Cart
from .cart_item import CartItem
from .coupon import Coupon
from .customer_profile import CustomerProfile
from .address import Address
from .review import Review
from app.models.payment import Payment
```

## File: models/address.py
```python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str | None] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=False)
    address_line_2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship(back_populates="addresses")
```

## File: models/cart_item.py
```python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int] = mapped_column(ForeignKey("product_variants.id"), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    cart: Mapped["Cart"] = relationship(back_populates="items")
    product_variant: Mapped["ProductVariant"] = relationship()
```

## File: models/cart.py
```python
import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int | None] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=True, unique=True
    )
    guest_token: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True, unique=True, index=True)
    coupon_id: Mapped[int | None] = mapped_column(ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    expires_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    items: Mapped[list["CartItem"]] = relationship(back_populates="cart", cascade="all, delete-orphan")
    coupon: Mapped["Coupon"] = relationship(back_populates="carts")
    customer: Mapped["CustomerProfile"] = relationship(back_populates="cart")
```

## File: models/category.py
```python
from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product_links: Mapped[list["ProductCategory"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )
```

## File: models/coupon.py
```python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Coupon(Base):
    __tablename__ = "coupons"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    discount_type: Mapped[str] = mapped_column(String(20), nullable=False)
    discount_value: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    minimum_order_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, default=0)
    usage_limit: Mapped[int | None] = mapped_column(Integer, nullable=True)
    usage_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships
    carts: Mapped[list["Cart"]] = relationship(back_populates="coupon")
```

## File: models/customer_profile.py
```python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CustomerProfile(Base):
    __tablename__ = "customer_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

   # Relationships
    user: Mapped["User"] = relationship(back_populates="customer_profile")
    cart: Mapped["Cart"] = relationship(back_populates="customer", uselist=False)
    addresses: Mapped[list["Address"]] = relationship(back_populates="customer")
```

## File: models/order_item.py
```python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int | None] = mapped_column(ForeignKey("product_variants.id", ondelete="SET NULL"), nullable=True)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price_at_purchase: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    order: Mapped["Order"] = relationship(back_populates="items")
    variant: Mapped["ProductVariant | None"] = relationship()
```

## File: models/order.py
```python
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer_profiles.id", ondelete="RESTRICT"), nullable=False)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="open")
    customer_name: Mapped[str | None] = mapped_column(String(100), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationships
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
    customer: Mapped["CustomerProfile"] = relationship()
```

## File: models/payment.py
```python
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)

    payment_method: Mapped[str | None] = mapped_column(String(50), nullable=True)
    provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    stripe_payment_intent_id: Mapped[str | None] = mapped_column(
        String(255), unique=True, nullable=True, index=True
    )
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(10), nullable=False, default="usd")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    order: Mapped["Order"] = relationship()
```

## File: models/permission.py
```python
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    role_links: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
        cascade="all, delete-orphan"
    )
```

## File: models/product_category.py
```python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"
    __table_args__ = (
        UniqueConstraint("product_id", "category_id", name="product_categories_product_id_category_id_unique"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product: Mapped["Product"] = relationship(back_populates="category_links")
    category: Mapped["Category"] = relationship(back_populates="product_links")
```

## File: models/product_variant.py
```python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    sku: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product: Mapped["Product"] = relationship(back_populates="variants")
```

## File: models/product.py
```python
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    category_links: Mapped[list["ProductCategory"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    variants: Mapped[list["ProductVariant"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

    @property
    def categories(self) -> list["Category"]:
        return [link.category for link in self.category_links]
```

## File: models/review.py
```python
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="reviews_rating_check"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    order_item_id: Mapped[int] = mapped_column(
        ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False
    )

    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    customer: Mapped["CustomerProfile"] = relationship()
    product: Mapped["Product"] = relationship()
    order_item: Mapped["OrderItem"] = relationship()
```

## File: models/role_permission.py
```python
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"
    __table_args__ = (
        UniqueConstraint("role_id", "permission_id", name="role_permissions_role_id_permission_id_unique"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    role: Mapped["Role"] = relationship(back_populates="permission_links")
    permission: Mapped["Permission"] = relationship(back_populates="role_links")
```

## File: models/role.py
```python
from sqlalchemy import (
    DateTime,
    Integer,
    String,
    func
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Role(Base):
    __tablename__ = "roles"

    # Primary Key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    # Basic Fields
    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    # Timestamps
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

     # Relationships
    users = relationship("User", back_populates="role")
    permission_links: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan"
    )
```

## File: models/user.py
```python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    phone_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    password_reset_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    password_reset_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    email_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    email_verification_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    email_verification_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    role: Mapped["Role"] = relationship(back_populates="users")
    customer_profile: Mapped["CustomerProfile"] = relationship(
        back_populates="user", uselist=False
    )
```

## File: repositories/cart_repository.py
```python

```

## File: schemas/__init__.py
```python

```

## File: schemas/address.py
```python
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
```

## File: schemas/auth.py
```python
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
```

## File: schemas/cart.py
```python
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
```

## File: schemas/category.py
```python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CategoryOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
```

## File: schemas/customer_auth.py
```python
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
```

## File: schemas/customer_profile.py
```python
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
```

## File: schemas/order_item.py
```python
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
```

## File: schemas/order.py
```python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.order_item import OrderItemOut


class OrderOut(BaseModel):
    id: int
    customer_id: int
    created_by_user_id: int | None = None
    total_amount: float
    status: str
    customer_name: str | None = None
    created_at: datetime
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)


class OrderCreate(BaseModel):
    customer_id: int
    created_by_user_id: int | None = None
    customer_name: str | None = Field(default=None, max_length=100)
    status: str = Field(default="open", max_length=20)


class OrderUpdate(BaseModel):
    status: str | None = Field(default=None, max_length=20)
    customer_name: str | None = Field(default=None, max_length=100)


class OrderStatusUpdate(BaseModel):
    status: str = Field(max_length=20)
```

## File: schemas/permission.py
```python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class PermissionOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PermissionCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class PermissionUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
```

## File: schemas/product_category.py
```python
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
```

## File: schemas/product_variant.py
```python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ProductVariantOut(BaseModel):
    id: int
    product_id: int
    sku: str
    price: float
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductVariantCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    is_active: bool = True


class ProductVariantUpdate(BaseModel):
    sku: str | None = Field(default=None, min_length=1, max_length=100)
    price: float | None = Field(default=None, gt=0)
    stock_quantity: int | None = Field(default=None, ge=0)
    is_active: bool | None = None
```

## File: schemas/product.py
```python
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
```

## File: schemas/review.py
```python
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ReviewCreate(BaseModel):
    order_item_id: int
    rating: int = Field(ge=1, le=5)
    comment: str | None = None


class ReviewUpdate(BaseModel):
    rating: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = None


class ReviewOut(BaseModel):
    id: int
    customer_id: int
    product_id: int
    order_item_id: int
    rating: int
    comment: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
```

## File: schemas/role_permission.py
```python
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.permission import PermissionOut


class RolePermissionOut(BaseModel):
    id: int
    role_id: int
    permission_id: int
    permission: PermissionOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RolePermissionCreate(BaseModel):
    permission_id: int
```

## File: schemas/role.py
```python
from pydantic import BaseModel, ConfigDict, Field


class RoleOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class RoleCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str | None = None


class RoleUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None
```

## File: schemas/user.py
```python
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
```

## File: main.py
```python
from fastapi import FastAPI
from sqlalchemy import text
from app.seed import seed_database
import app.models
from app.database.session import engine, AsyncSessionLocal
from app.core.config import settings
from app.core.test_seed import ensure_bogus_data
from app.api.routes.users import router as users_router
from app.api.routes.roles import router as roles_router
from app.api.routes.permissions import router as permissions_router
from app.api.routes.role_permissions import router as role_permissions_router
from app.api.routes.categories import router as categories_router
from app.api.routes.products import router as products_router
from app.api.routes.product_categories import router as product_categories_router
from app.api.routes.product_variants import router as product_variants_router
from app.api.routes.orders import router as orders_router
from app.api.routes.order_items import router as order_items_router
from app.api.routes.auth import router as auth_router
from app.api.routes.customer_profiles import router as customer_router
from app.api.routes.cart import router as cart_router
from app.api.routes.reviews import router as reviews_router
from app.api.routes.payments import router as payments_router
from app.api.routes.customer_auth import router as customer_auth_router
from app.api.routes.checkout import router as checkout_router

app = FastAPI()

ROUTERS = [
    (users_router, "Users"),
    (auth_router, "Auth-Admin"),
    (roles_router, "Roles"),
    (permissions_router, "Permissions"),
    (role_permissions_router, "Role Permissions"),
    (products_router, "Products"),
    (categories_router, "Categories"),
    (product_categories_router, "Product Categories"),
    (product_variants_router, "Product Variants"),
    (orders_router, "Orders-Admin"),
    (order_items_router, "Order Items"),
    (customer_auth_router, "Customer Auth"),
    (customer_router, "Customer Profile"),
    (cart_router, "Cart"),
    (reviews_router, "Reviews"),
    (payments_router, "Payments"),
    (checkout_router, "Checkout"),
]

for router, tag in ROUTERS:
    app.include_router(router, tags=[tag])


@app.on_event("startup")
async def on_startup():
    if settings.TEST_MODE:
        async with AsyncSessionLocal() as db:
            await ensure_bogus_data(db)
        print("TEST_MODE is ON — bogus product/variant/coupon seeded (id 999001 / code TESTCODE10)")


print("Database URL:", settings.DATABASE_URL)
print("Algorithm:", settings.ALGORITHM)
print("Access Token Expiry:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)
```

## File: seed.py
```python
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.session import AsyncSessionLocal
from app.models.role import Role
from app.models.user import User
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.core.security import hash_password

RESOURCES = [
    "users", "roles", "permissions",
    "categories", "products", "product_categories",
    "product_variants", "orders", "order_items"
]
ACTIONS = ["create", "read", "update", "delete"]

# Updated to include our storefront target
ROLES = ["admin", "manager", "staff", "customer"]

ROLE_ACTIONS = {
    "admin": ["create", "read", "update", "delete"],
    "manager": ["create", "read", "update"],
    "staff": ["read"],
    "customer": ["read"], # Storefront customers can only view catalog items natively
}

async def get_or_create_role(db: AsyncSession, name: str, description: str) -> Role:
    result = await db.execute(select(Role).filter(Role.name == name))
    role = result.scalar_one_or_none()
    if not role:
        role = Role(id=uuid.uuid4(), name=name, description=description)
        db.add(role)
        await db.commit()
        await db.refresh(role)
        print(f"Created role: {role.name} (id={role.id})")
    else:
        print(f"Role already exists: {role.name} (id={role.id})")
    return role

async def get_or_create_permission(db: AsyncSession, name: str, description: str) -> Permission:
    result = await db.execute(select(Permission).filter(Permission.name == name))
    perm = result.scalar_one_or_none()
    if not perm:
        perm = Permission(id=uuid.uuid4(), name=name, description=description)
        db.add(perm)
        await db.commit()
        await db.refresh(perm)
    return perm

async def link_role_permission(db: AsyncSession, role_id: uuid.UUID, permission_id: uuid.UUID) -> None:
    result = await db.execute(
        select(RolePermission).filter(
            RolePermission.role_id == role_id,
            RolePermission.permission_id == permission_id
        )
    )
    exists = result.scalar_one_or_none()
    if not exists:
        db.add(RolePermission(id=uuid.uuid4(), role_id=role_id, permission_id=permission_id))

async def seed_database(db: AsyncSession) -> None:
    """
    Idempotent asynchronous database seeder managing RBAC systems
    and the Customer tier.
    """
    print("Checking database for seed records...")

    # 1. Create all roles asynchronously
    role_objs = {}
    for role_name in ROLES:
        role_objs[role_name] = await get_or_create_role(
            db, role_name, f"{role_name.capitalize()} role"
        )

    # 2. Create all permissions (resource:action)
    permission_objs = {}
    for resource in RESOURCES:
        for action in ACTIONS:
            perm_name = f"{resource}:{action}"
            permission_objs[perm_name] = await get_or_create_permission(
                db, perm_name, f"Can {action} {resource}"
            )
    await db.commit()
    print(f"Ensured {len(permission_objs)} permissions exist")

    # 3. Link roles to permissions
    for role_name, allowed_actions in ROLE_ACTIONS.items():
        role = role_objs[role_name]
        for resource in RESOURCES:
            for action in allowed_actions:
                perm_name = f"{resource}:{action}"
                await link_role_permission(db, role.id, permission_objs[perm_name].id)
    await db.commit()
    print("Linked role-permission mappings")

    # 4. Create admin user
    admin_email = "admin@rbac.com"
    user_query = await db.execute(select(User).filter(User.email == admin_email))
    admin_user = user_query.scalar_one_or_none()

    if not admin_user:
        admin_user = User(
            id=uuid.uuid4(),
            full_name="Admin",
            email=admin_email,
            hashed_password=hash_password("Admin123!"),
            is_active=True,
            role_id=role_objs["admin"].id
        )
        db.add(admin_user)
        await db.commit()
        await db.refresh(admin_user)
        print(f"Created user: {admin_user.email} (id={admin_user.id})")
    else:
        print(f"User already exists: {admin_user.email} (id={admin_user.id})")

    print("Seeding checks complete!")

async def run_seed_cli() -> None:
    """Entry point for manual execution via terminal"""
    async with AsyncSessionLocal() as session:
        await seed_database(session)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_seed_cli())
```
