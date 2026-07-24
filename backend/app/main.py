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
from backend.app.api.routes.customer_profiles import router as customer_router
from app.api.routes.cart import router as cart_router
from app.api.routes.reviews import router as reviews_router
from app.api.routes.payments import router as payments_router
from app.api.routes.customer_auth import router as customer_auth_router
from app.api.routes.checkout import router as checkout_router

app = FastAPI()

ROUTERS = [
    (users_router, "Users"),
    (auth_router, "Auth-Admin"),
    (roles_router, "Roles"),
    (permissions_router, "Permissions"),
    (role_permissions_router, "Role Permissions"),
    (categories_router, "Categories"),
    (products_router, "Products"),
    (product_categories_router, "Product Categories"),
    (product_variants_router, "Product Variants"),
    (orders_router, "Orders-Admin"),
    (order_items_router, "Order Items"),
    (customer_auth_router, "Customer Auth"),
    (customer_router, "Customer Profile"),
    (cart_router, "Cart"),
    (reviews_router, "Reviews"),
    (payments_router, "Payments"),
    (checkout_router, "Checkout"),
]

for router, tag in ROUTERS:
    app.include_router(router, tags=[tag])


@app.on_event("startup")
async def on_startup():
    if settings.TEST_MODE:
        async with AsyncSessionLocal() as db:
            await ensure_bogus_data(db)
        print("TEST_MODE is ON — bogus product/variant/coupon seeded (id 999001 / code TESTCODE10)")


print("Database URL:", settings.DATABASE_URL)
print("Algorithm:", settings.ALGORITHM)
print("Access Token Expiry:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)