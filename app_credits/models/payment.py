from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from decimal import Decimal
from sqlalchemy import ForeignKey, Date
from sqlalchemy import Numeric


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)

    sum: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False
    )

    payment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    credit_id: Mapped[int] = mapped_column(
        ForeignKey("credits.id"),
        nullable=False
    )

    type_id: Mapped[int] = mapped_column(
        ForeignKey("dicts.id"),
        nullable=False
    )

    credit: Mapped["Credit"] = relationship(
        back_populates="payments"
    )

    payment_type: Mapped["Dictionary"] = relationship(back_populates="payments")