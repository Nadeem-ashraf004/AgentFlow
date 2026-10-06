from uuid import UUID
from fastapi import HTTPException , status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, access_token
from app.models.user import User
from app.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
    UserResponse
)


def register_user(
        db: Session ,
        request : UserRegisterRequest,
) -> UserResponse:
    # register a new user
    existing_user = db.scalar(select(User).where(User.email==request.email))
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
    user = User(
        full_name=request.full_name,
        email=request.email,
        hashed_password=hash_password(request.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return UserResponse.model_validator(user)
def authentication_user(
        db: Session,
        request: UserLoginRequest,
)-> TokenResponse:
    user = db.scalar(select(User).where(User.email==request.email))
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid email or password",
            headers = {"WWW-Authentication": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not active",
            headers = {"WWW-Authentication": "Bearer"},
        )
    access_token = create_access_token(str(user.id))

    return TokenResponse(
        access_token=access_token, 
        token_type="bearer")
def get_user_by_id(
        db: Session,
        user_id: UUID,
)->User | None:
    #retrieve a user by thier id
    return db.scalar(
        select(User).where(User.id==user_id)
        )