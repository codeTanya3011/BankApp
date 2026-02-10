from datetime import date
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel
from pydantic import ConfigDict


class CreditBase(BaseModel):
    issuance_date: date
    return_date: date
    body: Decimal
    percent: Decimal


class CreditCreate(CreditBase):
    user_id: int


class CreditUpdate(BaseModel):
    return_date: Optional[date] = None
    actual_return_date: Optional[date] = None
    body: Optional[Decimal] = None
    percent: Optional[Decimal] = None


class CreditResponse(CreditBase):
    id: int
    user_id: int
    actual_return_date: Optional[date] = None

    model_config = ConfigDict(from_attributes=True)


class PaymentResponse(BaseModel):
    id: int
    payment_date: date
    amount: Decimal
    credit_id: int
    type_id: int

    model_config = ConfigDict(from_attributes=True)


class CreditWithPaymentsResponse(CreditResponse):
    payments: List[PaymentResponse]


class UserCreditResponse(BaseModel):
    issuance_date: date
    is_closed: bool

    body: Decimal
    percent: Decimal

    # закрытый кредит
    actual_return_date: Optional[date] = None
    payments_sum: Optional[Decimal] = None

    # открытый кредит
    return_date: Optional[date] = None
    days_overdue: Optional[int] = None
    body_payments_sum: Optional[Decimal] = None
    percent_payments_sum: Optional[Decimal] = None


class UserCreditsListResponse(BaseModel):
    user_id: int
    credits: List[UserCreditResponse]