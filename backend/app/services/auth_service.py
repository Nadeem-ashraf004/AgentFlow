from uuid import UUID
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

# Fixed import: import create_access_token
from app.core.security import hash_password, verify_password, create_access_token
from app.models.user import User
from app.schemas.auth import (
    TokenResponse,
    UserLoginRequest,
    UserRegisterRequest,
    UserResponse,
)


def register_user(
    db: Session,
    request: UserRegisterRequest,
) -> UserResponse:
    # Check if user already exists
    existing_user = db.scalar(select(User).where(User.email == request.email))
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists",
        )
    
    # Create new user (Ensure field name matches your SQLAlchemy model)
    user = User(
        full_name=request.full_name,
        email=request.email,
        password_hash=hash_password(request.password),  # Change to password_hash if needed
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # Fixed: model_validate instead of model_validator
    return UserResponse.model_validate(user)


def authentication_user(
    db: Session,
    request: UserLoginRequest,
) -> TokenResponse:
    user = db.scalar(select(User).where(User.email == request.email))
    
    # Fixed: WWW-Authenticate header key
    if not user or not verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not active",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Fixed: Variable renaming to avoid shadowing
    token = create_access_token(str(user.id))

    return TokenResponse(
        access_token=token, 
        token_type="bearer"
    )


def get_user_by_id(
    db: Session,
    user_id: UUID,
) -> User | None:
    # Retrieve a user by their ID
    return db.scalar(select(User).where(User.id == user_id))