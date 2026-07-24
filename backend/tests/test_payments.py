import json
import pytest
import stripe
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile

pytestmark = pytest.mark.asyncio


class FakePaymentIntent:
    def __init__(self, client_secret="pi_test_secret_123"):
        self.client_secret = client_secret


async def test_create_intent_success(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paycreateintent@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=20.00, stock_quantity=10)
    await make_cart_with_item(profile.id, variant, quantity=3)

    captured = {}

    def fake_create(**kwargs):
        captured.update(kwargs)
        return FakePaymentIntent()

    monkeypatch.setattr(stripe.PaymentIntent, "create", fake_create)

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["client_secret"] == "pi_test_secret_123"
    assert captured["amount"] == 6000
    assert captured["currency"] == "usd"


async def test_create_intent_empty_cart(client, make_customer, auth_headers, monkeypatch):
    user, _ = await make_customer(email="paynocart@example.com")
    headers = auth_headers(user)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_create_intent_insufficient_stock(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="payinsufficientstock@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=1)
    await make_cart_with_item(profile.id, variant, quantity=5)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert "Insufficient stock" in resp.json()["detail"]


async def test_create_intent_inactive_variant(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="payinactivevariant@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=10, is_active=False)
    await make_cart_with_item(profile.id, variant, quantity=1)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert "no longer available" in resp.json()["detail"]


async def test_create_intent_unauthenticated(client, monkeypatch):
    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())
    resp = await client.post("/payments/create-intent")
    assert resp.status_code == 401


async def test_webhook_invalid_payload(client, monkeypatch):
    def fake_construct_event(payload, sig_header, secret):
        raise ValueError("bad payload")

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"not-real-json",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Invalid payload"


async def test_webhook_invalid_signature(client, monkeypatch):
    def fake_construct_event(payload, sig_header, secret):
        raise stripe.error.SignatureVerificationError("bad sig", sig_header)

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Invalid signature"


async def test_webhook_payment_succeeded_creates_order(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhooksuccess@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=30.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=2)

    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile.id),
                }
            }
        },
    }

    def fake_construct_event(payload, sig_header, secret):
        return fake_event

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "success"

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile.id))
    order = order_result.scalar_one_or_none()
    assert order is not None
    assert order.status == "paid"
    assert order.total_amount == 60.0

    await db.refresh(variant)
    assert variant.stock_quantity == 8


async def test_webhook_ignores_other_event_types(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhookother@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=15.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    fake_event = {
        "type": "payment_intent.payment_failed",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile.id),
                }
            }
        },
    }

    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile.id))
    assert order_result.scalar_one_or_none() is None

    await db.refresh(variant)
    assert variant.stock_quantity == 10


async def test_webhook_missing_metadata_no_crash(client, monkeypatch):
    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {"object": {"metadata": {}}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200


async def test_webhook_retry_does_not_duplicate_order(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhookretry@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()
    profile_id = profile.id

    variant = await make_product_variant(price=10.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile_id),
                }
            }
        },
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    first_resp = await client.post(
        "/payments/webhook", content=b"{}", headers={"stripe-signature": "fake-sig"}
    )
    assert first_resp.status_code == 200

    await db.refresh(profile)

    second_resp = await client.post(
        "/payments/webhook", content=b"{}", headers={"stripe-signature": "fake-sig"}
    )
    assert second_resp.status_code == 200

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile_id))
    orders = order_result.scalars().all()
    assert len(orders) == 1