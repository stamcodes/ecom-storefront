import pytest
from sqlalchemy import select

from app.models.product import Product

pytestmark = pytest.mark.asyncio


async def _make_product(db, name="Test Product"):
    product = Product(name=name, description="test", price=10.0)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def test_get_wishlist_empty(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistempty@example.com")
    headers = auth_headers(user)

    resp = await client.get("/wishlist", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == []


async def test_add_to_wishlist_success(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistadd@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    resp = await client.post(
        "/wishlist",
        json={"product_id": product.id},
        headers=headers,
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["product_id"] == product.id


async def test_add_to_wishlist_product_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistnotfound@example.com")
    headers = auth_headers(user)

    resp = await client.post(
        "/wishlist",
        json={"product_id": 999999},
        headers=headers,
    )
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_add_to_wishlist_duplicate(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistdup@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    await client.post("/wishlist", json={"product_id": product.id}, headers=headers)
    resp = await client.post("/wishlist", json={"product_id": product.id}, headers=headers)

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Product already in wishlist"


async def test_remove_from_wishlist_success(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistremove@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    await client.post("/wishlist", json={"product_id": product.id}, headers=headers)
    resp = await client.delete(f"/wishlist/{product.id}", headers=headers)

    assert resp.status_code == 204


async def test_remove_from_wishlist_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistremovenf@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/wishlist/999999", headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found in wishlist"