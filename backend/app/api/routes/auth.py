from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import CurrentUser, get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
    UserResponse,
)
from app.services.auth_service import (
    authentication_user,
)
from app.services.auth_service import (
    register_user as register_user_service,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    request: UserRegisterRequest,
    db: Annotated[Session, Depends(get_db)],
) -> UserResponse:
    """Register a new user."""
    return register_user_service(db, request)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
def login_user(
    request: UserLoginRequest,
    db: Annotated[Session, Depends(get_db)],
) -> TokenResponse:
    """Authenticate user and return access token."""
    return authentication_user(db, request)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: Annotated[User, Depends(get_current_user)],
    # Alternatively, if CurrentUser is an Annotated type alias:
    # current_user: CurrentUser,
) -> User:
    """Return the currently authenticated user."""
    return current_user