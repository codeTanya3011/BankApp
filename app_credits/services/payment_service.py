import pandas as pd
import io
from ..data_base import UnitOfWork
from decimal import Decimal


class PaymentService:

    @staticmethod
    async def import_payments_from_csv(file_bytes: bytes, uow: UnitOfWork):
        df = pd.read_csv(io.BytesIO(file_bytes), sep=None, engine='python')

        async with uow:
            for _, row in df.iterrows():
                payment_payload = {
                    "id": int(row["id"]),
                    "credit_id": int(row["credit_id"]),
                    "payment_date": pd.to_datetime(row["payment_date"], dayfirst=True).date(),
                    "type_id": int(row["type_id"]),
                    "sum": Decimal(str(row["sum"]))
                }
                await uow.payments.create_payment(**payment_payload)

            await uow.commit()