from sqlalchemy import select
from ..models import Credit
from .base_repo import BaseRepo


class CreditRepo(BaseRepo):

    async def get_user_credits(self, user_id: int):
        stmt = select(Credit).where(Credit.user_id == user_id)
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def create_credit(self, **credit_data) -> None:
        new_credit = Credit(**credit_data)
        self.db.add(new_credit)

    async def get_credit_by_id(self, credit_id: int):
        stmt = select(Credit).where(Credit.id == credit_id)
        res = await self.db.execute(stmt)
        return res.scalar_one_or_none()


