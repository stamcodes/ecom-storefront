import pytest

pytestmark = pytest.mark.asyncio


async def test_get_profile_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profileget@example.com")
    headers = auth_headers(user)

    resp = await client.get("/me", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["email"] == "profileget@example.com"
    assert body["id"] == user.id


async def test_get_profile_unauthenticated(client):
    resp = await client.get("/me")
    assert resp.status_code == 401


async def test_get_profile_invalid_token(client):
    resp = await client.get("/me", headers={"Authorization": "Bearer not-a-real-token"})
    assert resp.status_code == 401


async def test_update_profile_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profileupdate@example.com")
    headers = auth_headers(user)

    resp = await client.put("/me", json={"name": "Updated Name"}, headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "Updated Name"


async def test_update_profile_partial_fields_unchanged(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profilepartial@example.com")
    headers = auth_headers(user)

    resp = await client.put("/me", json={"phone_number": "+19998887777"}, headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["phone_number"] == "+19998887777"
    assert body["name"] == "Test Customer"


async def test_update_profile_unauthenticated(client):
    resp = await client.put("/me", json={"name": "Nope"})
    assert resp.status_code == 401


async def test_list_addresses_empty(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrlistempty@example.com")
    headers = auth_headers(user)

    resp = await client.get("/addresses", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == []


async def test_create_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrcreate@example.com")
    headers = auth_headers(user)

    payload = {
        "country": "USA",
        "state": "CA",
        "city": "Los Angeles",
        "postal_code": "90001",
        "address_line_1": "123 Main St",
        "address_line_2": None,
        "is_default": True,
    }
    resp = await client.post("/addresses", json=payload, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["city"] == "Los Angeles"
    assert body["is_default"] is True


async def test_create_address_unauthenticated(client):
    payload = {
        "country": "USA",
        "city": "Los Angeles",
        "address_line_1": "123 Main St",
    }
    resp = await client.post("/addresses", json=payload)
    assert resp.status_code == 401


async def test_create_second_default_address_unsets_first(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdefault@example.com")
    headers = auth_headers(user)

    first_payload = {
        "country": "USA",
        "city": "Austin",
        "address_line_1": "1 First St",
        "is_default": True,
    }
    first_resp = await client.post("/addresses", json=first_payload, headers=headers)
    assert first_resp.status_code == 201
    first_id = first_resp.json()["id"]

    second_payload = {
        "country": "USA",
        "city": "Dallas",
        "address_line_1": "2 Second St",
        "is_default": True,
    }
    second_resp = await client.post("/addresses", json=second_payload, headers=headers)
    assert second_resp.status_code == 201

    list_resp = await client.get("/addresses", headers=headers)
    addresses = {a["id"]: a["is_default"] for a in list_resp.json()}
    assert addresses[first_id] is False


async def test_update_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdate@example.com")
    headers = auth_headers(user)

    create_payload = {
        "country": "USA",
        "city": "Denver",
        "address_line_1": "1 Old St",
    }
    create_resp = await client.post("/addresses", json=create_payload, headers=headers)
    address_id = create_resp.json()["id"]

    update_resp = await client.put(
        f"/addresses/{address_id}", json={"city": "Boulder"}, headers=headers
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["city"] == "Boulder"


async def test_update_address_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdatenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.put("/addresses/999999", json={"city": "Nowhere"}, headers=headers)
    assert resp.status_code == 404


async def test_update_address_belonging_to_another_customer(client, make_customer, auth_headers):
    owner, _ = await make_customer(email="addrowner@example.com")
    intruder, _ = await make_customer(email="addrintruder@example.com")

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Miami", "address_line_1": "1 Owner St"},
        headers=auth_headers(owner),
    )
    address_id = create_resp.json()["id"]

    resp = await client.put(
        f"/addresses/{address_id}",
        json={"city": "Hacked"},
        headers=auth_headers(intruder),
    )
    assert resp.status_code == 404


async def test_update_address_set_default_unsets_others(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdatedefault@example.com")
    headers = auth_headers(user)

    first_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Seattle", "address_line_1": "1 A St", "is_default": True},
        headers=headers,
    )
    first_id = first_resp.json()["id"]

    second_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Portland", "address_line_1": "2 B St", "is_default": False},
        headers=headers,
    )
    second_id = second_resp.json()["id"]

    await client.put(f"/addresses/{second_id}", json={"is_default": True}, headers=headers)

    list_resp = await client.get("/addresses", headers=headers)
    addresses = {a["id"]: a["is_default"] for a in list_resp.json()}
    assert addresses[first_id] is False
    assert addresses[second_id] is True


async def test_delete_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdelete@example.com")
    headers = auth_headers(user)

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Phoenix", "address_line_1": "1 Delete St"},
        headers=headers,
    )
    address_id = create_resp.json()["id"]

    delete_resp = await client.delete(f"/addresses/{address_id}", headers=headers)
    assert delete_resp.status_code == 204

    list_resp = await client.get("/addresses", headers=headers)
    assert all(a["id"] != address_id for a in list_resp.json())


async def test_delete_address_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdeletenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/addresses/999999", headers=headers)
    assert resp.status_code == 404


async def test_delete_address_belonging_to_another_customer(client, make_customer, auth_headers):
    owner, _ = await make_customer(email="addrdelowner@example.com")
    intruder, _ = await make_customer(email="addrdelintruder@example.com")

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Tampa", "address_line_1": "1 Owner Ave"},
        headers=auth_headers(owner),
    )
    address_id = create_resp.json()["id"]

    resp = await client.delete(f"/addresses/{address_id}", headers=auth_headers(intruder))
    assert resp.status_code == 404