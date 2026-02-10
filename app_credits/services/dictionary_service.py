import pandas as pd
import io
from ..data_base import UnitOfWork


class DictionaryService:

    @staticmethod
    async def import_dictionary_from_csv(file_bytes: bytes, uow: UnitOfWork):
        df = pd.read_csv(io.BytesIO(file_bytes), sep=None, engine='python')
        df.columns = df.columns.str.strip()

        async with uow:
            for _, row in df.iterrows():
                category_id = int(row["id"])
                if not await uow.dicts.get_category_by_id(category_id):

                    dict_payload = {
                        "id": category_id,
                        "name": str(row["name"]).strip()
                    }
                    await uow.dicts.create_category(**dict_payload)

            await uow.commit()