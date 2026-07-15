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
