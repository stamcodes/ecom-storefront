from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.address import Address
from app.schemas.customer_profile import CustomerProfileOut, CustomerProfileUpdate
from app.schemas.address import AddressCreate, AddressUpdate, AddressOut
from app.core.auth import get_current_user

router = APIRouter()


@router.get("/me", response_model=CustomerProfileOut)
async def get_customer_profile(current_user: User = Depends(get_current_user)):
    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.put("/me", response_model=CustomerProfileOut)
async def update_customer_profile(
    payload: CustomerProfileUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    update_data = payload.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)

    await db.commit()
    await db.refresh(current_user)

    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.get("/addresses", response_model=list[AddressOut])
async def list_addresses(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
    result = await db.execute(stmt)
    return list(result.scalars().all())


@router.post("/addresses", response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    payload: AddressCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if payload.is_default:
        stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
        result = await db.execute(stmt)
        for existing in result.scalars().all():
            existing.is_default = False

    address = Address(customer_id=current_user.customer_profile.id, **payload.dict())
    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address


@router.put("/addresses/{address_id}", response_model=AddressOut)
async def update_address(
    address_id: int,
    payload: AddressUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    update_data = payload.dict(exclude_unset=True)

    if update_data.get("is_default"):
        stmt = select(Address).where(
            Address.customer_id == current_user.customer_profile.id,
            Address.id != address_id,
        )
        result = await db.execute(stmt)
        for other in result.scalars().all():
            other.is_default = False

    for field, value in update_data.items():
        setattr(address, field, value)

    await db.commit()
    await db.refresh(address)
    return address


@router.delete("/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
    address_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    await db.delete(address)
    await db.commit()
    return None