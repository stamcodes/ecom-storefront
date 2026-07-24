import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.customer_profile import CustomerProfile


async def _get_profile(db: AsyncSession, user) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    return result.scalar_one()


async def _make_order(
    db: AsyncSession,
    customer_id: int,
    order_status: str = "open",
    total_amount: float = 0,
) -> Order:
    order = Order(
        customer_id=customer_id,
        order_status=order_status,
        total_amount=total_amount,
    )
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order


async def _make_order_item(
    db: AsyncSession,
    order_id: int,
    variant,
    quantity: int = 2,
) -> OrderItem:
    item = OrderItem(
        order_id=order_id,
        product_variant_id=variant.id,
        quantity=quantity,
        price_at_purchase=variant.price,
    )
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


# ---- Orders: cancel ----

@pytest.mark.asyncio
async def test_cancel_order_success(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="open")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(user))

    assert response.status_code == 200
    assert response.json()["order_status"] == "cancelled"


@pytest.mark.asyncio
async def test_cancel_order_wrong_status(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="completed")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(user))

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_cancel_order_not_owned(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    owner, _ = await make_customer(email="owner@example.com")
    other, _ = await make_customer(email="other@example.com")
    profile = await _get_profile(db, owner)
    order = await _make_order(db, profile.id, order_status="open")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(other))

    assert response.status_code == 404


# ---- Orders: reorder ----

@pytest.mark.asyncio
async def test_reorder_creates_cart_items(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    await _make_order_item(db, order.id, variant, quantity=3)

    response = await client.post(f"/orders/{order.id}/reorder", headers=auth_headers(user))

    assert response.status_code == 201
    assert response.json()["id"] == order.id


@pytest.mark.asyncio
async def test_reorder_not_owned(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    owner, _ = await make_customer(email="owner2@example.com")
    other, _ = await make_customer(email="other2@example.com")
    profile = await _get_profile(db, owner)
    order = await _make_order(db, profile.id, order_status="completed")

    response = await client.post(f"/orders/{order.id}/reorder", headers=auth_headers(other))

    assert response.status_code == 404


# ---- Orders: invoice ----

@pytest.mark.asyncio
async def test_get_invoice_success(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="completed", total_amount=100)

    response = await client.get(f"/orders/{order.id}/invoice", headers=auth_headers(user))

    assert response.status_code == 200
    assert response.json()["id"] == order.id


@pytest.mark.asyncio
async def test_get_invoice_not_found(client: AsyncClient, make_customer, auth_headers):
    user, _ = await make_customer()

    response = await client.get("/orders/999999/invoice", headers=auth_headers(user))

    assert response.status_code == 404


# ---- Return Requests: create ----

@pytest.mark.asyncio
async def test_create_return_request_success(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size"},
        headers=auth_headers(user),
    )

    assert response.status_code == 201
    body = response.json()
    assert body["order_item_id"] == item.id
    assert body["status"] == "pending"


@pytest.mark.asyncio
async def test_create_return_request_duplicate(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size"},
        headers=auth_headers(user),
    )
    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size again"},
        headers=auth_headers(user),
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_create_return_request_item_not_owned(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    owner, _ = await make_customer(email="owner3@example.com")
    other, _ = await make_customer(email="other3@example.com")
    profile = await _get_profile(db, owner)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Not mine"},
        headers=auth_headers(other),
    )

    assert response.status_code == 404


# ---- Return Requests: list ----

@pytest.mark.asyncio
async def test_list_return_requests_scoped_to_customer(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user4@example.com")
    other, _ = await make_customer(email="other4@example.com")
    profile = await _get_profile(db, user)
    other_profile = await _get_profile(db, other)
    variant = await make_product_variant()

    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)
    other_order = await _make_order(db, other_profile.id, order_status="completed")
    other_item = await _make_order_item(db, other_order.id, variant)

    await client.post("/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user))
    await client.post("/return-requests", json={"order_item_id": other_item.id}, headers=auth_headers(other))

    response = await client.get("/return-requests", headers=auth_headers(user))

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["order_item_id"] == item.id


# ---- Return Requests: status update (staff-only) ----

@pytest.mark.asyncio
async def test_update_return_request_status_as_staff(
    client: AsyncClient, db: AsyncSession, make_customer, make_staff, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user5@example.com")
    staff, _ = await make_staff()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    create_resp = await client.post(
        "/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user)
    )
    request_id = create_resp.json()["id"]

    response = await client.patch(
        f"/return-requests/{request_id}/status",
        json={"status": "approved", "refund_amount": 20.00},
        headers=auth_headers(staff),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "approved"
    assert body["refund_amount"] == 20.00
    assert body["processed_at"] is not None


@pytest.mark.asyncio
async def test_update_return_request_status_as_customer_forbidden(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user6@example.com")
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    create_resp = await client.post(
        "/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user)
    )
    request_id = create_resp.json()["id"]

    response = await client.patch(
        f"/return-requests/{request_id}/status",
        json={"status": "approved"},
        headers=auth_headers(user),
    )

    assert response.status_code == 403


@pytest.mark.asyncio
async def test_update_return_request_status_not_found(client: AsyncClient, make_staff, auth_headers):
    staff, _ = await make_staff()

    response = await client.patch(
        "/return-requests/999999/status",
        json={"status": "approved"},
        headers=auth_headers(staff),
    )

    assert response.status_code == 404