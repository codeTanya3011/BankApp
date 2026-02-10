from datetime import datetime
from typing import Optional
from pydantic import ConfigDict
from pydantic import BaseModel


class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    login: Optional[str] = None


class UserResponse(UserBase):
    id: int
    registration_date: datetime

    model_config = ConfigDict(from_attributes=True)