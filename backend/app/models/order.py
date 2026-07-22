from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer_profiles.id", ondelete="RESTRICT"), nullable=False)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="open")
    customer_name: Mapped[str | None] = mapped_column(String(100), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # Relationships
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
    customer: Mapped["CustomerProfile"] = relationship()