from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.branch import BranchOut


class UserBranchOut(BaseModel):
    id: int
    user_id: int
    branch_id: int
    branch: BranchOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserBranchCreate(BaseModel):
    branch_id: int