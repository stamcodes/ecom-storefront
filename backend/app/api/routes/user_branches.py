from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.models.branch import Branch
from app.models.user_branch import UserBranch
from app.schemas.user_branch import UserBranchOut, UserBranchCreate
from app.core.permissions import require_role, ADMIN, MANAGER

router = APIRouter()


@router.get("/users/{user_id}/branches", response_model=list[UserBranchOut])
def get_user_branches(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return db.query(UserBranch).filter(UserBranch.user_id == user_id).all()


@router.post("/users/{user_id}/branches", response_model=UserBranchOut, status_code=201)
def assign_branch_to_user(
    user_id: int,
    payload: UserBranchCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    branch = db.query(Branch).filter(Branch.id == payload.branch_id).first()
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    existing = db.query(UserBranch).filter(
        UserBranch.user_id == user_id,
        UserBranch.branch_id == payload.branch_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="This user already has access to this branch")

    link = UserBranch(user_id=user_id, branch_id=payload.branch_id)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


@router.delete("/users/{user_id}/branches/{branch_id}", status_code=204)
def remove_branch_from_user(
    user_id: int,
    branch_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    link = db.query(UserBranch).filter(
        UserBranch.user_id == user_id,
        UserBranch.branch_id == branch_id
    ).first()
    if not link:
        raise HTTPException(status_code=404, detail="This user does not have access to this branch")

    db.delete(link)
    db.commit()
    return None