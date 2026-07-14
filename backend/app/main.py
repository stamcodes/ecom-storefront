from fastapi import FastAPI
from sqlalchemy import text
import app.models
from app.database.session import engine 
from app.core.config import settings
from app.api.routes.users import router as users_router
from app.api.routes.roles import router as roles_router
from app.api.routes.branches import router as branches_router
from app.api.routes.permissions import router as permissions_router
from app.api.routes.role_permissions import router as role_permissions_router
from app.api.routes.user_branches import router as user_branches_router
from app.api.routes.categories import router as categories_router
from app.api.routes.products import router as products_router
from app.api.routes.product_categories import router as product_categories_router
from app.api.routes.product_variants import router as product_variants_router
from app.api.routes.orders import router as orders_router
from app.api.routes.order_items import router as order_items_router
from app.api.routes.auth import router as auth_router

app = FastAPI()
app.include_router(users_router)
app.include_router(roles_router)
app.include_router(branches_router)
app.include_router(permissions_router)
app.include_router(role_permissions_router)
app.include_router(user_branches_router)
app.include_router(categories_router)
app.include_router(products_router)
app.include_router(product_categories_router)
app.include_router(product_variants_router)
app.include_router(orders_router)
app.include_router(order_items_router)
app.include_router(auth_router)


print("Database URL:", settings.DATABASE_URL)
print("Algorithm:", settings.ALGORITHM)
print("Access Token Expiry:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)

@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT current_database();"))
            db_name = result.scalar()

        return {
            "status": "Connected successfully!",
            "database": db_name
        }

    except Exception as e:
        return {
            "status": "Connection failed",
            "error": str(e)
        }