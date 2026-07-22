from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.core.jwt import verify_access_token

# HTTP Bearer for strictly-authenticated routes
security = HTTPBearer()

# HTTP Bearer for optional-auth routes (guest-or-user) — does NOT auto-error
# when missing, but DOES register the security requirement so Swagger/OpenAPI
# attaches the Authorize token to requests on these routes.
security_optional = HTTPBearer(auto_error=False)


async def _get_current_user_by_token(token: str, db: AsyncSession) -> User:
    payload = verify_access_token(token)

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    stmt = select(User).options(selectinload(User.role)).where(User.id == int(user_id))
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    return await _get_current_user_by_token(credentials.credentials, db)


async def get_current_user_optional(
    credentials: HTTPAuthorizationCredentials | None = Depends(security_optional),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """
    Returns the authenticated User if a valid Bearer token is present.
    Returns None if no token is present, or if the token is invalid/expired
    (silently — callers fall back to guest-token logic in that case).
    """
    if not credentials:
        return None

    try:
        return await _get_current_user_by_token(credentials.credentials, db)
    except HTTPException:
        return None