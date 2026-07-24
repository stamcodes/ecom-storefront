import pytest
from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from app.models.user import User

pytestmark = pytest.mark.asyncio


async def test_register_success(client, mock_emails):
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "password": "StrongPass123!",
        "phone_number": "+1234567890",
    }
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "jane@example.com"
    assert body["email_verified"] is False
    assert len(mock_emails["verification"]) == 1
    assert mock_emails["verification"][0][0] == "jane@example.com"


async def test_register_duplicate_email(client, make_customer):
    user, _ = await make_customer(email="dupe@example.com")
    payload = {
        "name": "Dupe",
        "email": "dupe@example.com",
        "password": "StrongPass123!",
    }
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Email already registered"


async def test_register_invalid_password_too_short(client):
    payload = {"name": "Jane", "email": "jane2@example.com", "password": "short"}
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 422


async def test_login_success(client, make_customer):
    user, password = await make_customer(email="login@example.com")
    resp = await client.post("/customer/auth/login", json={"email": "login@example.com", "password": password})
    assert resp.status_code == 200
    body = resp.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


async def test_login_wrong_password(client, make_customer):
    await make_customer(email="wrongpass@example.com")
    resp = await client.post("/customer/auth/login", json={"email": "wrongpass@example.com", "password": "WrongPass!"})
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid email or password"


async def test_login_nonexistent_email(client):
    resp = await client.post("/customer/auth/login", json={"email": "nouser@example.com", "password": "whatever123"})
    assert resp.status_code == 401


async def test_login_inactive_account(client, make_customer):
    await make_customer(email="inactive@example.com", active=False)
    resp = await client.post("/customer/auth/login", json={"email": "inactive@example.com", "password": "Password123!"})
    assert resp.status_code == 403
    assert resp.json()["detail"] == "Account is inactive"


async def test_verify_email_success(client, make_customer, db):
    user, _ = await make_customer(email="verify@example.com", verified=False)
    user.email_verification_token = "valid-token-123"
    user.email_verification_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post("/customer/auth/verify-email", json={"token": "valid-token-123"})
    assert resp.status_code == 200

    result = await db.execute(select(User).where(User.email == "verify@example.com"))
    refreshed = result.scalar_one()
    assert refreshed.email_verified is True
    assert refreshed.email_verification_token is None


async def test_verify_email_expired_token(client, make_customer, db):
    user, _ = await make_customer(email="expired@example.com", verified=False)
    user.email_verification_token = "expired-token"
    user.email_verification_expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    await db.commit()

    resp = await client.post("/customer/auth/verify-email", json={"token": "expired-token"})
    assert resp.status_code == 400


async def test_verify_email_invalid_token(client):
    resp = await client.post("/customer/auth/verify-email", json={"token": "does-not-exist"})
    assert resp.status_code == 400


async def test_resend_verification_unverified_user(client, make_customer, mock_emails):
    await make_customer(email="resend@example.com", verified=False)
    resp = await client.post("/customer/auth/resend-verification", json={"email": "resend@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["verification"]) == 1


async def test_resend_verification_already_verified(client, make_customer, mock_emails):
    await make_customer(email="already@example.com", verified=True)
    resp = await client.post("/customer/auth/resend-verification", json={"email": "already@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["verification"]) == 0


async def test_resend_verification_nonexistent_email_returns_generic(client, mock_emails):
    resp = await client.post("/customer/auth/resend-verification", json={"email": "ghost@example.com"})
    assert resp.status_code == 200
    assert "If that email exists" in resp.json()["message"]
    assert len(mock_emails["verification"]) == 0


async def test_forgot_password_existing_active_user(client, make_customer, mock_emails):
    await make_customer(email="forgot@example.com")
    resp = await client.post("/customer/auth/forgot-password", json={"email": "forgot@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["reset"]) == 1


async def test_forgot_password_nonexistent_email_returns_generic(client, mock_emails):
    resp = await client.post("/customer/auth/forgot-password", json={"email": "ghost2@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["reset"]) == 0


async def test_reset_password_success(client, make_customer, db):
    user, _ = await make_customer(email="reset@example.com")
    user.password_reset_token = "reset-token-123"
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "reset-token-123", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 200

    login_resp = await client.post(
        "/customer/auth/login", json={"email": "reset@example.com", "password": "NewStrongPass123!"}
    )
    assert login_resp.status_code == 200


async def test_reset_password_expired_token(client, make_customer, db):
    user, _ = await make_customer(email="resetexp@example.com")
    user.password_reset_token = "expired-reset-token"
    user.password_reset_expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "expired-reset-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 400


async def test_reset_password_invalid_token(client):
    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "not-a-real-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 400


async def test_reset_password_inactive_account(client, make_customer, db):
    user, _ = await make_customer(email="resetinactive@example.com", active=False)
    user.password_reset_token = "inactive-reset-token"
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "inactive-reset-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 403