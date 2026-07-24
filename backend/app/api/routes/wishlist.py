from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.wishlist import Wishlist
from app.schemas.wishlist import WishlistCreate, WishlistResponse

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("", response_model=list[WishlistResponse])
async def get_wishlist(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(select(Wishlist).where(Wishlist.customer_id == profile.id))
    return result.scalars().all()


@router.post("", response_model=WishlistResponse, status_code=status.HTTP_201_CREATED)
async def add_to_wishlist(
    payload: WishlistCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    product = await db.execute(select(Product).where(Product.id == payload.product_id))
    if not product.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Product not found")

    existing = await db.execute(
        select(Wishlist).where(
            Wishlist.customer_id == profile.id,
            Wishlist.product_id == payload.product_id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Product already in wishlist")

    item = Wishlist(customer_id=profile.id, product_id=payload.product_id)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_from_wishlist(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(
        select(Wishlist).where(
            Wishlist.customer_id == profile.id,
            Wishlist.product_id == product_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Product not found in wishlist")

    await db.delete(item)
    await db.commit()