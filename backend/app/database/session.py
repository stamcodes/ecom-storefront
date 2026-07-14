from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# Create our asynchronous database engine using modern Asyncio wrappers
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Shows SQL queries in terminal (disable in production)
    future=True
)

# Create an asynchronous session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

# Database Dependency - Yields an AsyncSession instead of a synchronous Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()