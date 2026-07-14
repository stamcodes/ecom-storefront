from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.role import RoleOut, RoleCreate, RoleUpdate
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


@router.get("/roles", response_model=list[RoleOut])
def get_roles(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    return db.query(Role).all()


@router.get("/roles/{role_id}", response_model=RoleOut)
def get_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/roles", response_model=RoleOut, status_code=201)
def create_role(
    payload: RoleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    existing = db.query(Role).filter(Role.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Role name already exists")

    new_role = Role(name=payload.name, description=payload.description)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role


@router.put("/roles/{role_id}", response_model=RoleOut)
def update_role(
    role_id: int,
    payload: RoleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(role, field, value)

    db.commit()
    db.refresh(role)
    return role


@router.delete("/roles/{role_id}", status_code=204)
def delete_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    try:
        db.delete(role)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Cannot delete role: it is still assigned to one or more users"
        )
    return None