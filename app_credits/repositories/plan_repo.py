from datetime import date
from sqlalchemy import select, func
from ..models import Plan, Credit, Payment, Dictionary
from .base_repo import BaseRepo
from sqlalchemy.orm import joinedload


class PlanRepo(BaseRepo):

    async def get_category_by_name(self, name: str) -> Dictionary | None:
        stmt = select(Dictionary).where(Dictionary.name == name)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def plan_exists(self, period: date, category_id: int) -> bool:
        stmt = select(Plan.id).where(
            Plan.period == period,
            Plan.category_id == category_id
        )
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none() is not None

    async def create_plan(self, **plan_data) -> None:
        new_plan = Plan(**plan_data)
        self.db.add(new_plan)

    async def get_plans_by_year(self, year: int) -> list[Plan]:
        stmt = (
            select(Plan)
            .options(joinedload(Plan.category))
            .where(func.extract("year", Plan.period) == year)
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_plans_for_month(self, year: int, month: int) -> list[Plan]:
        stmt = (
            select(Plan)
            .options(joinedload(Plan.category))
            .where(
                func.extract("year", Plan.period) == year,
                func.extract("month", Plan.period) == month
            )
        )
        result = await self.db.execute(stmt)
        return list(result.scalars().all())

    async def get_issued_credits(
        self,
        date_from: date,
        date_to: date
    ) -> tuple[int, float]:
        stmt = select(
            func.count(Credit.id),
            func.coalesce(func.sum(Credit.body), 0)
        ).where(
            Credit.issuance_date.between(date_from, date_to)
        )
        result = await self.db.execute(stmt)
        count, total = result.one()
        return count, float(total)

    async def get_percent_payments(
        self,
        date_from: date,
        date_to: date
    ) -> tuple[int, float]:
        stmt = select(
            func.count(Payment.id),
            func.coalesce(func.sum(Payment.sum), 0)
        ).join(Dictionary, Payment.type_id == Dictionary.id).where(
            Payment.payment_date.between(date_from, date_to),
            Dictionary.name.in_(["відсотки", "тіло"])
        )
        result = await self.db.execute(stmt)
        count, total = result.one()
        return count, float(total)
