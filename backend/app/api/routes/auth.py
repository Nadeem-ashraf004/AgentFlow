from fastapi import APIRouter, HTTPException, status

from app.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def register_user(request: UserRegisterRequest) -> None:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Registration will be implemented in Phase 3.",
    )


@router.post("/login", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def login_user(request: UserLoginRequest) -> TokenResponse:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Login will be implemented in Phase 3.",
    )