import os
import sys
import asyncio
from datetime import datetime, timedelta, timezone

os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:admin@localhost:5432/ecommerce_test")
os.environ.setdefault("SECRET_KEY", "test-secret-key-do-not-use-in-prod")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
os.environ.setdefault("STRIPE_SECRET_KEY", "sk_test_dummy")
os.environ.setdefault("STRIPE_WEBHOOK_SECRET", "whsec_dummy")
os.environ.setdefault("TEST_MODE", "false")

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy import select, event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.cart import Cart
from app.models.cart_item import CartItem

from app.database.base import Base
from app.database.session import get_db
from app.core.config import settings
from app.core.jwt import create_access_token
from app.core.security import hash_password
from app.models.user import User
from app.models.role import Role
from app.models.customer_profile import CustomerProfile

import app.models  # noqa: F401  registers all model metadata
from app.main import app as fastapi_app

CUSTOMER_ROLE_ID = 4

test_engine = create_async_engine(settings.DATABASE_URL, future=True, poolclass=NullPool)
TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


@pytest_asyncio.fixture(scope="session", autouse=True, loop_scope="session")
async def setup_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestSessionLocal() as session:
        result = await session.execute(select(Role).where(Role.id == CUSTOMER_ROLE_ID))
        if not result.scalar_one_or_none():
            session.add(Role(id=CUSTOMER_ROLE_ID, name="customer", description="Customer role"))
            await session.commit()
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()


@pytest_asyncio.fixture
async def db():
    connection = await test_engine.connect()
    outer_transaction = await connection.begin()
    session = AsyncSession(bind=connection, expire_on_commit=False)

    await connection.begin_nested()

    def restart_savepoint(sess, transaction):
        if transaction.nested and not transaction._parent.nested:
            connection.sync_connection.begin_nested()

    event.listen(session.sync_session, "after_transaction_end", restart_savepoint)

    try:
        yield session
    finally:
        event.remove(session.sync_session, "after_transaction_end", restart_savepoint)
        await session.close()
        await outer_transaction.rollback()
        await connection.close()


@pytest_asyncio.fixture
async def client(db):
    async def override_get_db():
        yield db

    fastapi_app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    fastapi_app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def make_customer(db):
    async def _make_customer(email="customer@example.com", password="Password123!", verified=True, active=True):
        user = User(
            name="Test Customer",
            email=email,
            password=hash_password(password),
            role_id=CUSTOMER_ROLE_ID,
            is_active=active,
            email_verified=verified,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()

        return user, password

    return _make_customer


@pytest_asyncio.fixture
async def auth_headers():
    def _auth_headers(user):
        token = create_access_token({"sub": str(user.id), "email": user.email, "role_id": user.role_id})
        return {"Authorization": f"Bearer {token}"}

    return _auth_headers


@pytest.fixture(autouse=True)
def mock_emails(monkeypatch):
    sent = {"verification": [], "reset": []}

    def fake_verification(to, token):
        sent["verification"].append((to, token))

    def fake_reset(to, token):
        sent["reset"].append((to, token))

    monkeypatch.setattr("app.api.routes.customer_auth.send_verification_email", fake_verification)
    monkeypatch.setattr("app.api.routes.customer_auth.send_password_reset_email", fake_reset)

    return sent


@pytest_asyncio.fixture
async def make_product_variant(db):
    counter = {"n": 0}

    async def _make_product_variant(price=19.99, stock_quantity=10, is_active=True):
        counter["n"] += 1
        n = counter["n"]

        product = Product(
            name=f"Test Product {n}",
            description="Seeded for checkout tests",
            price=price,
            is_active=True,
        )
        db.add(product)
        await db.flush()

        variant = ProductVariant(
            product_id=product.id,
            sku=f"TEST-SKU-{n}",
            price=price,
            stock_quantity=stock_quantity,
            is_active=is_active,
        )
        db.add(variant)
        await db.commit()
        await db.refresh(variant)

        return variant

    return _make_product_variant


@pytest_asyncio.fixture
async def make_cart_with_item(db):
    async def _make_cart_with_item(customer_profile_id, variant, quantity=1):
        cart = Cart(customer_id=customer_profile_id)
        db.add(cart)
        await db.flush()

        item = CartItem(cart_id=cart.id, product_variant_id=variant.id, quantity=quantity)
        db.add(item)
        await db.commit()
        await db.refresh(cart)

        return cart

    return _make_cart_with_item