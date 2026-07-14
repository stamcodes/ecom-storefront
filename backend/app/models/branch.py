from sqlalchemy import Boolean, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Branch(Base):
    __tablename__ = "branches"
    

    # Primary Key
    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    # Basic Fields
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    location: Mapped[str | None] = mapped_column(String(255), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Timestamps
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

# Relationships
    user_links: Mapped[list["UserBranch"]] = relationship(
        back_populates="branch",
        cascade="all, delete-orphan"
        
    )
     