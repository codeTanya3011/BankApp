from datetime import date
from typing import Optional
from decimal import Decimal
from pydantic import ConfigDict, BaseModel


class PaymentBase(BaseModel):
    payment_date: date
    amount: Decimal


class PaymentCreate(PaymentBase):
    credit_id: int
    type_id: int


class PaymentUpdate(BaseModel):
    payment_date: Optional[date] = None
    amount: Optional[Decimal] = None
    credit_id: Optional[int] = None
    type_id: Optional[int] = None


class PaymentResponse(PaymentBase):
    id: int
    credit_id: int
    type_id: int

    model_config = ConfigDict(from_attributes=True)