from datetime import datetime, timedelta, timezone
from typing import Any

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

# Initialize password hasher
password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Hash the password using the recommended algorithm."""
    return password_hasher.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify the password against the hashed password."""
    return password_hasher.verify(password, hashed_password)


def create_access_token(subject: str) -> str:
    """Create a JWT access token with the given subject and expire time."""
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "sub": subject,
        "exp": expire,
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Decode the JWT access token and return the payload."""
    try:
        # Note: algorithms must be passed as a list/sequence
        return jwt.decode(
            token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
    except jwt.PyJWTError:
        return None