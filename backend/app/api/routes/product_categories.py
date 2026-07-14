from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.product import Product
from app.models.category import Category
from app.models.product_category import ProductCategory
from app.models.user import User
from app.schemas.product_category import ProductCategoryOut, ProductCategoryCreate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/categories", response_model=list[ProductCategoryOut])
def get_product_categories(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return db.query(ProductCategory).filter(ProductCategory.product_id == product_id).all()


@router.post("/products/{product_id}/categories", response_model=ProductCategoryOut, status_code=201)
def assign_category_to_product(
    product_id: int,
    payload: ProductCategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    category = db.query(Category).filter(Category.id == payload.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    existing = db.query(ProductCategory).filter(
        ProductCategory.product_id == product_id,
        ProductCategory.category_id == payload.category_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="This product is already assigned to this category")

    link = ProductCategory(product_id=product_id, category_id=payload.category_id)
    db.add(link)
    db.commit()
    db.refresh(link)
    return link


@router.delete("/products/{product_id}/categories/{category_id}", status_code=204)
def remove_category_from_product(
    product_id: int,
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    link = db.query(ProductCategory).filter(
        ProductCategory.product_id == product_id,
        ProductCategory.category_id == category_id
    ).first()
    if not link:
        raise HTTPException(status_code=404, detail="This product is not assigned to this category")

    db.delete(link)
    db.commit()
    return None