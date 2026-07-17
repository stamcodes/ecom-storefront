from fastapi import FastAPI
from sqlalchemy import text
from app.seed import seed_database
import app.models
from app.database.session import engine, AsyncSessionLocal
from app.core.config import settings
from app.core.test_seed import ensure_bogus_data
from app.api.routes.users import router as users_router
from app.api.routes.roles import router as roles_router
from app.api.routes.permissions import router as permissions_router
from app.api.routes.role_permissions import router as role_permissions_router
from app.api.routes.categories import router as categories_router
from app.api.routes.products import router as products_router
from app.api.routes.product_categories import router as product_categories_router
from app.api.routes.product_variants import router as product_variants_router
from app.api.routes.orders import router as orders_router
from app.api.routes.order_items import router as order_items_router
from app.api.routes.auth import router as auth_router
from app.api.routes.cart import router as cart_router
from app.api.routes.auth import router as auth_router
from app.api.routes.customer import router as customer_router
from app.api.routes.cart import router as cart_router
from app.api.routes.reviews import router as reviews_router

app = FastAPI()
app.include_router(users_router, tags=["Users"])
app.include_router(roles_router, tags=["Roles"])
app.include_router(permissions_router, tags=["Permissions"])
app.include_router(role_permissions_router, tags=["Role Permissions"])
app.include_router(categories_router, tags=["Categories"])
app.include_router(products_router, tags=["Products"])
app.include_router(product_categories_router, tags=["Product Categories"])
app.include_router(product_variants_router, tags=["Product Variants"])
app.include_router(orders_router, tags=["Orders-Admin"])
app.include_router(order_items_router, tags=["Order Items"])
app.include_router(auth_router, tags=["Auth-Customer"])
app.include_router(customer_router, tags=["Auth-Customer"])
app.include_router(cart_router, tags=["Cart"])
app.include_router(reviews_router, tags=["Reviews"])


@app.on_event("startup")
async def on_startup():
    if settings.TEST_MODE:
        async with AsyncSessionLocal() as db:
            await ensure_bogus_data(db)
        print("TEST_MODE is ON — bogus product/variant/coupon seeded (id 999001 / code TESTCODE10)")


print("Database URL:", settings.DATABASE_URL)
print("Algorithm:", settings.ALGORITHM)
print("Access Token Expiry:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)