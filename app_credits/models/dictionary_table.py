from .base_table import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List


class Dictionary(Base):
    __tablename__ = "dicts"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    plans: Mapped[List["Plan"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )

    payments: Mapped[List["Payment"]] = relationship(
        back_populates="payment_type"
    )