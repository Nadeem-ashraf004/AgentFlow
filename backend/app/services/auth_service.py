from uuid import UUID
from fastapi import HTTPException , status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password, access_token
def register_user() -> None:
    """
    User registration logic will be implemented in Phase 3.
    """
    raise NotImplementedError("Authentication is not implemented yet.")


def authenticate_user() -> None:
    """
    User authentication logic will be implemented in Phase 3.
    """
    raise NotImplementedError("Authentication is not implemented yet.")