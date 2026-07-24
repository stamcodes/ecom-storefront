from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Wishlist(Base):
    __tablename__ = "wishlist_items"
    __table_args__ = (
    UniqueConstraint("customer_id", "product_id", name="uq_customer_product_wishlist"),
)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship()
    product: Mapped["Product"] = relationship()