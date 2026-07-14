from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductOut, ProductCreate, ProductUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products", response_model=list[ProductOut])
def get_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    return db.query(Product).all()


@router.get("/products/{product_id}", response_model=ProductOut)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products", response_model=ProductOut, status_code=201)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    existing = db.query(Product).filter(Product.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Product name already exists")

    new_product = Product(
        name=payload.name,
        description=payload.description,
        price=payload.price,
        is_active=payload.is_active,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.put("/products/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)
    return product


@router.delete("/products/{product_id}", status_code=204)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return None