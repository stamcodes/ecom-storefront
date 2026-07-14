from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.core.auth import get_current_user

ADMIN = 1
MANAGER = 2
STAFF = 3


def require_role(*allowed_role_ids: int):
    """
    Returns a FastAPI dependency that checks whether the current user's
    role_id is in the allowed list.

    Usage:
        @router.post("/products")
        def create_product(
            current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
        ):
            ...
    """

    def dependency(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role_id not in allowed_role_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        return current_user

    return dependency


def block_manager_on_admin_target(current_user: User, target_role_id: int):
    """
    Managers can manage roles/permissions for everyone except Admins.
    Call this after fetching the target resource's role_id.
    """
    if current_user.role_id == MANAGER and target_role_id == ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Managers cannot modify Admin-level roles or users",
        )