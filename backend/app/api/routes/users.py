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