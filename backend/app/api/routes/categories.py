from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryOut, CategoryCreate, CategoryUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/categories", response_model=list[CategoryOut])
def get_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    return db.query(Category).all()


@router.get("/categories/{category_id}", response_model=CategoryOut)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/categories", response_model=CategoryOut, status_code=201)
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    existing = db.query(Category).filter(Category.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category name already exists")

    new_category = Category(
        name=payload.name,
        description=payload.description,
        branch_id=None,  # categories are always global
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.put("/categories/{category_id}", response_model=CategoryOut)
def update_category(
    category_id: int,
    payload: CategoryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)

    db.commit()
    db.refresh(category)
    return category


@router.delete("/categories/{category_id}", status_code=204)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()
    return None