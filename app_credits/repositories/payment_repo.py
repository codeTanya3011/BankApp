from sqlalchemy import select
from ..models import Payment
from .base_repo import BaseRepo
from sqlalchemy.orm import joinedload


class PaymentRepo(BaseRepo):

    async def get_credit_payments(self, credit_id: int) -> list[Payment]:
        stmt = (
            select(Payment)
            .options(joinedload(Payment.payment_type))
            .where(Payment.credit_id == credit_id)
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def create_payment(self, **payment_data) -> None:
        new_payment = Payment(**payment_data)
        self.db.add(new_payment)