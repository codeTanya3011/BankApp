import pandas as pd
import io
from ..data_base import UnitOfWork


class UserService:

    @staticmethod
    async def import_users_from_csv(file_bytes: bytes, uow: UnitOfWork):
        df = pd.read_csv(io.BytesIO(file_bytes), sep=None, engine='python')
        async with uow:
            for _, row in df.iterrows():
                user_payload = {
                    "id": int(row["id"]),
                    "login": str(row["login"]),
                    "registration_date": pd.to_datetime(
                        row.get("registration_date", pd.Timestamp.now()),
                        dayfirst=True
                    ).to_pydatetime()
                }
                if not await uow.users.get_user_by_id(user_payload["id"]):
                    await uow.users.create_user(**user_payload)

            await uow.commit()

