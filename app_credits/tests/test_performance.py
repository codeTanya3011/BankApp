import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_performance_calculation(ac: AsyncClient):
    check_date = "2021-03-01"
    response = await ac.get(f"/plans/performance?check_date={check_date}")
    assert response.status_code == 200
    data = response.json()
    if data:
        categories = [item["category"] for item in data]
        assert any(cat in categories for cat in ["видача", "збір"])


@pytest.mark.asyncio
async def test_performance_zero_plan(ac: AsyncClient):
    check_date = "2030-01-01"
    response = await ac.get(f"/plans/performance?check_date={check_date}")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_performance_dates_sorting(ac: AsyncClient):
    test_date = "2021-03-01"
    response = await ac.get(f"/plans/performance?check_date={test_date}")
    data = response.json()
    for item in data:
        assert item["period"] == test_date


@pytest.mark.asyncio
async def test_performance_math_accuracy(ac: AsyncClient):
    await ac.post("/plans/setup-database")

    check_date = "2021-03-01"
    response = await ac.get(f"/plans/performance?check_date={check_date}")

    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0, f"Ендпоінт повернув порожній список для дати {check_date} навіть після setup-database"

    target_category = "збір"
    item = next((i for i in data if i["category"].lower() == target_category), None)

    assert item is not None, f"Категорія '{target_category}' не знайдена у відповіді API. Перевір вміст dictionary.csv"

    plan_sum = float(item["plan_sum"])
    fact_sum = float(item["fact_sum"])

    if plan_sum > 0:
        expected_percent = round((fact_sum / plan_sum) * 100, 2)
    else:
        expected_percent = 0.0

    assert float(item["performance_percent"]) == expected_percent, \
        f"Помилка в математиці для {target_category}: очікували {expected_percent}, отримали {item['performance_percent']}"