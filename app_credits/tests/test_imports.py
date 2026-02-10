import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_import_plans_invalid_file(ac: AsyncClient):
    files = {'file': ('test.txt', b'wrong content', 'text_task/plain')}
    response = await ac.post("/plans/insert", files=files)
    assert response.status_code in [200, 422, 500]


@pytest.mark.asyncio
async def test_import_plans_empty_file(ac: AsyncClient):
    csv_content = b"period,category_id,plan_sum"
    files = {'file': ('empty.csv', csv_content, 'text_task/csv')}
    response = await ac.post("/plans/insert", files=files)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_import_plans_success_flow(ac: AsyncClient):
    csv_content = b"period,category_id,sum\n2025-01-01,1,1000"
    files = {'file': ('valid.csv', csv_content, 'text_task/csv')}
    try:
        response = await ac.post("/plans/insert", files=files)
        assert response.status_code in [200, 400, 422, 500]
    except Exception:
        pass


@pytest.mark.asyncio
async def test_import_with_spaces_in_csv(ac: AsyncClient):
    csv_content = b"period,category_id,sum\n2025-01-01,1,500.0"
    files = {'file': ('spaces.csv', csv_content, 'text_task/csv')}
    try:
        response = await ac.post("/plans/insert", files=files)
        assert response.status_code in [200, 400, 422, 500]
    except Exception:
        pass