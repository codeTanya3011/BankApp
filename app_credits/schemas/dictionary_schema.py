from typing import Optional
from pydantic import ConfigDict, BaseModel


class DictionaryBase(BaseModel):
    name: str


class DictionaryCreate(DictionaryBase):
    pass


class DictionaryUpdate(BaseModel):
    name: Optional[str] = None


class DictionaryResponse(DictionaryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)