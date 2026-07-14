from pydantic import BaseModel, ConfigDict, Field


class RoleOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class RoleCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str | None = None


class RoleUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None