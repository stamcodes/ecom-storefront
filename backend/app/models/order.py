from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int | None] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="SET NULL"), nullable=True
    )
    guest_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    guest_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    guest_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)

    shipping_address_id: Mapped[int | None] = mapped_column(
        ForeignKey("addresses.id", ondelete="SET NULL"), nullable=True
    )
    billing_address_id: Mapped[int | None] = mapped_column(
        ForeignKey("addresses.id", ondelete="SET NULL"), nullable=True
    )
    coupon_id: Mapped[int | None] = mapped_column(
        ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True
    )

    order_status: Mapped[str] = mapped_column(String(20), nullable=False, default="open")

    subtotal: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    discount_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    shipping_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    tax_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    placed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    def __init__(self, **kwargs):
        if "status" in kwargs and "order_status" not in kwargs:
            kwargs["order_status"] = kwargs.pop("status")
        if "customer_name" in kwargs:
            self._customer_name = kwargs.pop("customer_name")
        super().__init__(**kwargs)

    @property
    def status(self) -> str:
        return self.order_status

    @status.setter
    def status(self, value: str) -> None:
        self.order_status = value

    @property
    def customer_name(self) -> str | None:
        return getattr(self, "_customer_name", None)

    @customer_name.setter
    def customer_name(self, value: str | None) -> None:
        self._customer_name = value

    # Relationships
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
    customer: Mapped["CustomerProfile"] = relationship()