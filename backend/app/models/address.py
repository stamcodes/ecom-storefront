from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str | None] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=False)
    address_line_2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship(back_populates="addresses")