from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings
from app.database.base import Base

# SQLAlchemy Engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,          # Shows SQL queries in terminal (disable in production)
    future=True
)

# Session Factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)



# Database Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()