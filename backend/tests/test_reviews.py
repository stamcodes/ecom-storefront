import pytest
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile

pytestmark = pytest.mark.asyncio


async def test_get_product_reviews_empty(client, make_product_variant):
    variant = await make_product_variant()
    resp = await client.get(f"/products/{variant.product_id}/reviews")
    assert resp.status_code == 200
    assert resp.json() == []


async def test_get_product_reviews_product_not_found(client):
    resp = await client.get("/products/999999/reviews")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_create_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewcreate@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 5, "comment": "Great product"}
    resp = await client.post(f"/products/{product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["rating"] == 5
    assert body["comment"] == "Great product"
    assert body["product_id"] == product_id


async def test_create_review_product_not_found(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewproductnotfound@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, _ = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 4}
    resp = await client.post("/products/999999/reviews", json=payload, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_create_review_order_item_not_found(client, make_customer, auth_headers, make_product_variant):
    user, _ = await make_customer(email="reviewitemnotfound@example.com")
    headers = auth_headers(user)

    variant = await make_product_variant()

    payload = {"order_item_id": 999999, "rating": 3}
    resp = await client.post(f"/products/{variant.product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Order item not found"


async def test_create_review_invalid_rating(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewinvalidrating@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 6}
    resp = await client.post(f"/products/{product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 422


async def test_create_review_unauthenticated(client, make_product_variant):
    variant = await make_product_variant()
    payload = {"order_item_id": 1, "rating": 5}
    resp = await client.post(f"/products/{variant.product_id}/reviews", json=payload)
    assert resp.status_code == 401


async def test_get_product_reviews_after_creation(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewlistafter@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 4, "comment": "Nice"},
        headers=headers,
    )

    resp = await client.get(f"/products/{product_id}/reviews")
    assert resp.status_code == 200
    body = resp.json()
    assert len(body) == 1
    assert body[0]["rating"] == 4


async def test_update_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewupdate@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 2, "comment": "Meh"},
        headers=headers,
    )
    review_id = create_resp.json()["id"]

    update_resp = await client.put(
        f"/reviews/{review_id}", json={"rating": 5, "comment": "Actually great"}, headers=headers
    )
    assert update_resp.status_code == 200
    body = update_resp.json()
    assert body["rating"] == 5
    assert body["comment"] == "Actually great"


async def test_update_review_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="reviewupdatenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.put("/reviews/999999", json={"rating": 3}, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Review not found"


async def test_update_review_belonging_to_another_customer(client, make_customer, auth_headers, make_order_item, db):
    owner, _ = await make_customer(email="reviewowner@example.com")
    intruder, _ = await make_customer(email="reviewintruder@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == owner.id))
    owner_profile = result.scalar_one()

    order_item, product_id = await make_order_item(owner_profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 5},
        headers=auth_headers(owner),
    )
    review_id = create_resp.json()["id"]

    resp = await client.put(
        f"/reviews/{review_id}", json={"rating": 1}, headers=auth_headers(intruder)
    )
    assert resp.status_code == 403
    assert resp.json()["detail"] == "You can only edit your own reviews"


async def test_update_review_unauthenticated(client, make_customer, make_order_item, db):
    user, _ = await make_customer(email="reviewupdateunauth@example.com")
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()
    order_item, product_id = await make_order_item(profile.id)

    resp = await client.put("/reviews/1", json={"rating": 3})
    assert resp.status_code == 401


async def test_delete_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewdelete@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 3},
        headers=headers,
    )
    review_id = create_resp.json()["id"]

    delete_resp = await client.delete(f"/reviews/{review_id}", headers=headers)
    assert delete_resp.status_code == 204

    list_resp = await client.get(f"/products/{product_id}/reviews")
    assert all(r["id"] != review_id for r in list_resp.json())


async def test_delete_review_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="reviewdeletenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/reviews/999999", headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Review not found"


async def test_delete_review_belonging_to_another_customer(client, make_customer, auth_headers, make_order_item, db):
    owner, _ = await make_customer(email="reviewdelowner@example.com")
    intruder, _ = await make_customer(email="reviewdelintruder@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == owner.id))
    owner_profile = result.scalar_one()

    order_item, product_id = await make_order_item(owner_profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 4},
        headers=auth_headers(owner),
    )
    review_id = create_resp.json()["id"]

    resp = await client.delete(f"/reviews/{review_id}", headers=auth_headers(intruder))
    assert resp.status_code == 403
    assert resp.json()["detail"] == "You can only delete your own reviews"