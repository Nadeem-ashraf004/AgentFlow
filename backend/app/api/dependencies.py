from typing import Annotated
from uuid import UUID
from fastapi import HTTPException , Depends , status    
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
from jwt import InvalidTokenError
from sqlalchemy.orm import Session



from app.core.security import decode_access_token
from app.db.session import get_db
from app.models.user import User
from app.services.auth_service import get_user_by_id


bearer_scheme = HTTPBearer()

def get_current_user(
        credencials : Annotated[
            HTTPAuthorizationCredentials,
            Depends(bearer_scheme)
        ],
        db: Annotated[Session,Depends(get_db)],
)-> User:
    # return the  authentication user from jwt access token
     token = credencials.credentials

     try:
        payload = decode_access_token(token)
     except InvalidTokenError:
         raise HTTPException(
             status_code= status.HTTP_401_UNAUTHORIZED,
             detail="invalid or expired access token",
             headers={"WWW-authenticate ":"Bearer"},
         )
     user_id= payload.get("sub")

     if not user_id:
         raise HTTPException(
             status_code=status.HTTP_401_UNAUTHORIZED,
             detail="invalid access token",
             headers={"WWW-authenticate":"Bearer"},
         )
     try:
         user_id = UUID(user_id)
     except(ValueError,AttributeError):
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user identity in access token.",
            headers={"WWW-Authenticate": "Bearer"},
         )    
     user = get_user_by_id(db,user_uuid)
     if user is None:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User associated with this token no longer exists.",
            headers={"WWW-Authenticate": "Bearer"},
         )
     if not user.is_active:
         raise HTTPException(
             status_code=status.HTTP_403_FORBIDDEN,
             detail="User account is inactive",
         )
     return user

CurrentUser = Annotated[User, Depends(get_user_by_id)]