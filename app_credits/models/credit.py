from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from typing import List
from sqlalchemy import ForeignKey, Date, Numeric
from datetime import date


class Credit(Base):
    __tablename__ = "credits"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    issuance_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    return_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    actual_return_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    body: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    percent: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False)

    payments: Mapped[List["Payment"]] = relationship(
        back_populates="credit",
        cascade="all, delete-orphan"
    )




