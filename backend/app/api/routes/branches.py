from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.branch import Branch
from app.models.user import User
from app.schemas.branch import BranchOut, BranchCreate, BranchUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/branches", response_model=list[BranchOut])
def get_branches(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    return db.query(Branch).all()


@router.get("/branches/{branch_id}", response_model=BranchOut)
def get_branch(
    branch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch


@router.post("/branches", response_model=BranchOut, status_code=201)
def create_branch(
    payload: BranchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    existing = db.query(Branch).filter(Branch.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Branch name already exists")

    new_branch = Branch(
        name=payload.name,
        location=payload.location,
        is_active=payload.is_active,
    )
    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)
    return new_branch


@router.put("/branches/{branch_id}", response_model=BranchOut)
def update_branch(
    branch_id: int,
    payload: BranchUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(branch, field, value)

    db.commit()
    db.refresh(branch)
    return branch


@router.delete("/branches/{branch_id}", status_code=204)
def delete_branch(
    branch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    try:
        db.delete(branch)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Cannot delete branch: it is still referenced by orders or other records"
        )
    return None