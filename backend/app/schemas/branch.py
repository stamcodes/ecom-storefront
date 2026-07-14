from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class BranchOut(BaseModel):
    id: int
    name: str
    location: str | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class BranchCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    location: str | None = None
    is_active: bool = True


class BranchUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    location: str | None = None
    is_active: bool | None = None

    