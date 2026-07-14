from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.permission import Permission
from app.models.user import User
from app.schemas.permission import PermissionOut, PermissionCreate, PermissionUpdate
from app.core.permissions import require_role, ADMIN

router = APIRouter()


@router.get("/permissions", response_model=list[PermissionOut])
def get_permissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    return db.query(Permission).all()


@router.get("/permissions/{permission_id}", response_model=PermissionOut)
def get_permission(
    permission_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.post("/permissions", response_model=PermissionOut, status_code=201)
def create_permission(
    payload: PermissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    existing = db.query(Permission).filter(Permission.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Permission name already exists")

    new_permission = Permission(name=payload.name, description=payload.description)
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    return new_permission


@router.put("/permissions/{permission_id}", response_model=PermissionOut)
def update_permission(
    permission_id: int,
    payload: PermissionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(permission, field, value)

    db.commit()
    db.refresh(permission)
    return permission


@router.delete("/permissions/{permission_id}", status_code=204)
def delete_permission(
    permission_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    db.delete(permission)
    db.commit()
    return None