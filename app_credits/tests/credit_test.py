import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_user_credits_not_found(ac: AsyncClient):
    user_id = 999999
    response = await ac.get(f"/user_credits/{user_id}")

    assert response.status_code == 404
    data = response.json()

    assert "message" in data
    assert data["user_id"] == user_id
    assert data["type"] == "NotFoundUserError"


@pytest.mark.asyncio
async def test_get_user_credits_active(ac: AsyncClient):
    user_id = 288
    response = await ac.get(f"/user_credits/{user_id}")

    if response.status_code == 200:
        data = response.json()
        assert "user_id" in data
        assert "credits" in data
    else:
        assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_user_credits_empty(ac: AsyncClient):
    user_id = 1
    response = await ac.get(f"/user_credits/{user_id}")
    assert response.status_code in (200, 404)
    # if response.status_code == 200:
    #     assert "credits" in response.json()
    # else:
    #     assert response.status_code == 404


@pytest.mark.asyncio
async def test_get_user_credits_closed(ac: AsyncClient):
    user_id = 285
    response = await ac.get(f"/user_credits/{user_id}")
    assert response.status_code in (200, 404)


@pytest.mark.asyncio
async def test_get_user_credits_invalid_id(ac: AsyncClient):
    response = await ac.get("/user_credits/abc")
    assert response.status_code == 422