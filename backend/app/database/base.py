from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str

    # Automatically generate table names based on class name in lowercase
    @declared_attr.classmethod
    def __tablename__(cls) -> str:
        return cls.__name__.lower()