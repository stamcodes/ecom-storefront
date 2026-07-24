import pytest
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile
from app.models.product_variant import ProductVariant
from app.models.order import Order

pytestmark = pytest.mark.asyncio


async def test_checkout_success(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutsuccess@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=25.00, stock_quantity=10)
    await make_cart_with_item(profile.id, variant, quantity=2)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["status"] == "open"
    assert body["total_amount"] == 50.0
    assert len(body["items"]) == 1
    assert body["items"][0]["quantity"] == 2

    await db.refresh(variant)
    assert variant.stock_quantity == 8


async def test_checkout_empty_cart(client, make_customer, auth_headers):
    user, _ = await make_customer(email="checkoutempty@example.com")
    headers = auth_headers(user)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_checkout_no_cart_at_all(client, make_customer, auth_headers):
    user, _ = await make_customer(email="checkoutnocart@example.com")
    headers = auth_headers(user)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_checkout_insufficient_stock(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutstock@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=1)
    await make_cart_with_item(profile.id, variant, quantity=5)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert "Insufficient stock" in resp.json()["detail"]

    await db.refresh(variant)
    assert variant.stock_quantity == 1


async def test_checkout_inactive_variant(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutinactive@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=10, is_active=False)
    await make_cart_with_item(profile.id, variant, quantity=1)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert "no longer available" in resp.json()["detail"]


async def test_checkout_clears_cart_items(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutclears@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=15.00, stock_quantity=5)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201

    db.expire_all()

    second_resp = await client.post("/checkout", headers=headers)
    assert second_resp.status_code == 400
    assert second_resp.json()["detail"] == "Cart is empty"


async def test_checkout_unauthenticated(client):
    resp = await client.post("/checkout")
    assert resp.status_code == 401


async def test_checkout_multiple_items_total(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutmulti@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant_a = await make_product_variant(price=10.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant_a, quantity=3)

    from app.models.cart_item import CartItem
    variant_b = await make_product_variant(price=5.00, stock_quantity=10)
    db.add(CartItem(cart_id=cart.id, product_variant_id=variant_b.id, quantity=4))
    await db.commit()

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["total_amount"] == 50.0
    assert len(body["items"]) == 2