from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ReturnRequest(Base):
    __tablename__ = "return_requests"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    order_item_id: Mapped[int] = mapped_column(
        ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False
    )
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )

    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    refund_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)

    requested_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    processed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    order_item: Mapped["OrderItem"] = relationship()
    customer: Mapped["CustomerProfile"] = relationship()