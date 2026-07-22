from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from datetime import datetime, timedelta, timezone

BOGUS_PRODUCT_ID = 999001
BOGUS_VARIANT_ID = 999001
BOGUS_VARIANT_SKU = "BOGUS-TEST-SKU"
BOGUS_COUPON_CODE = "TESTCODE10"


async def ensure_bogus_data(db: AsyncSession) -> None:
    result = await db.execute(select(Product).where(Product.id == BOGUS_PRODUCT_ID))
    product = result.scalar_one_or_none()
    if not product:
        product = Product(
            id=BOGUS_PRODUCT_ID,
            name="Bogus Test Product",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            price=9.99,
            is_active=True,
        )
        db.add(product)
        await db.flush()

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == BOGUS_VARIANT_ID))
    variant = result.scalar_one_or_none()
    if not variant:
        variant = ProductVariant(
            id=BOGUS_VARIANT_ID,
            product_id=BOGUS_PRODUCT_ID,
            sku=BOGUS_VARIANT_SKU,
            price=9.99,
            stock_quantity=1000,
            is_active=True,
        )
        db.add(variant)

    result = await db.execute(select(Coupon).where(Coupon.code == BOGUS_COUPON_CODE))
    coupon = result.scalar_one_or_none()
    if not coupon:
        coupon = Coupon(
            code=BOGUS_COUPON_CODE,
            name="Bogus Test Coupon",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            discount_type="percentage",
            discount_value=10,
            minimum_order_amount=0,
            usage_limit=None,
            usage_count=0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=365),
            is_active=True,
        )
        db.add(coupon)

    await db.commit()