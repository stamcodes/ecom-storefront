from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.review import Review
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewOut, ReviewUpdate
from app.core.auth import get_current_user

router = APIRouter()


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("/products/{product_id}/reviews", response_model=list[ReviewOut])
async def get_product_reviews(
    product_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Review).where(Review.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/reviews", response_model=ReviewOut, status_code=201)
async def create_product_review(
    product_id: int,
    payload: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    profile = await _get_or_create_customer_profile(db, current_user)

    # TODO: BYPASSED VERIFIED-PURCHASE CHECK.
    # Checkout isn't built yet, so there's no real link from order_item_id -> this
    # customer. Once POST /checkout exists and Order has a customer_id, replace this
    # block with a real check, e.g.:
    #   - fetch OrderItem by payload.order_item_id
    #   - join to Order, confirm Order.customer_id == profile.id
    #   - confirm OrderItem.product_variant -> product_id == product_id
    #   - 404/403 if any of that fails
    # For now we only confirm the order_item_id points to a row that exists.
    from app.models.order_item import OrderItem
    result = await db.execute(select(OrderItem).where(OrderItem.id == payload.order_item_id))
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    new_review = Review(
        customer_id=profile.id,
        product_id=product_id,
        order_item_id=payload.order_item_id,
        rating=payload.rating,
        comment=payload.comment,
    )
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)
    return new_review


@router.put("/reviews/{review_id}", response_model=ReviewOut)
async def update_review(
    review_id: int,
    payload: ReviewUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only edit your own reviews")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(review, field, value)

    await db.commit()
    await db.refresh(review)
    return review


@router.delete("/reviews/{review_id}", status_code=204)
async def delete_review(
    review_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only delete your own reviews")

    await db.delete(review)
    await db.commit()
    return None