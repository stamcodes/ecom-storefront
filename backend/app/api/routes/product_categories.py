from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.category import Category
from app.models.product_category import ProductCategory
from app.models.user import User
from app.schemas.product_category import ProductCategoryOut, ProductCategoryCreate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/categories", response_model=list[ProductCategoryOut])
async def get_product_categories(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductCategory).where(ProductCategory.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/categories", response_model=ProductCategoryOut, status_code=201)
async def assign_category_to_product(
    product_id: int,
    payload: ProductCategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Category).where(Category.id == payload.category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == payload.category_id,
        )
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="This product is already assigned to this category")

    link = ProductCategory(product_id=product_id, category_id=payload.category_id)
    db.add(link)
    await db.commit()
    await db.refresh(link)
    return link


@router.delete("/products/{product_id}/categories/{category_id}", status_code=204)
async def remove_category_from_product(
    product_id: int,
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == category_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="This product is not assigned to this category")

    await db.delete(link)
    await db.commit()
    return None
