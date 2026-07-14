from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.permission import PermissionOut


class RolePermissionOut(BaseModel):
    id: int
    role_id: int
    permission_id: int
    permission: PermissionOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RolePermissionCreate(BaseModel):
    permission_id: int