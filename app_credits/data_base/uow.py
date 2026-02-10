from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_db
from fastapi import Depends
from typing import Annotated
from ..repositories import (
    UserRepo, PlanRepo, PaymentRepo, CreditRepo, DictionaryRepo
)


class UnitOfWork:
    def __init__(self, db: AsyncSession):
        self.db = db

        self.users = UserRepo(db)
        self.plans = PlanRepo(db)
        self.payments = PaymentRepo(db)
        self.credits = CreditRepo(db)
        self.dicts = DictionaryRepo(db)

    async def commit(self):
        await self.db.commit()

    async def rollback(self):
        await self.db.rollback()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        else:
            await self.commit()


def get_unit_of_work(db: Annotated[AsyncSession, Depends(get_db)]):
    return UnitOfWork(db)