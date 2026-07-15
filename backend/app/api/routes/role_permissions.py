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
