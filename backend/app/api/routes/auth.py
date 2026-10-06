from fastapi import APIRouter, HTTPException, status ,Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from app.api.dependencies import CurrentUser
from app.db.session import get_db
from app.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
    UserResponse,
)
from app.services.auth_service import authentication_user , register_user



router = APIRouter(
    prefix="/auth", 
    tags=["Authentication"]
    )


@router.post(
        "/register", 
        response_model=UserResponse,
         status_code=status.HTTP_201_CREATED
         )
def register_user(
    request: UserRegisterRequest,
    db: Annotated[Session,Depends(get_db)],
    ) -> UserResponse:
    #register a new user
    return register_user(db,request)

@router.post(
        "/login", 
        response_model= TokenResponse,
        status_code=status.HTTP_200_OK
        )
def login_user(
    request: UserLoginRequest,
    db : Annotated[Session,Depends(get_db)]
    ) -> TokenResponse:

    return authentication_user(db,request)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: CurrentUser,
) -> UserResponse:
    """Return the currently authenticated user."""

    return UserResponse.model_validate(current_user)