from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey
from datetime import date


class Plan(Base):
    __tablename__ = "plans"

    id: Mapped[int] = mapped_column(primary_key=True)

    period: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    sum: Mapped[int] = mapped_column(
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("dicts.id"),
        nullable=False
    )

    category: Mapped["Dictionary"] = relationship(
        back_populates="plans"
    )