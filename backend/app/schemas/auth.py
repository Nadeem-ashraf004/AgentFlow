from pydantic import BaseModel, EmailSte , field, ConfigDict,EmailStr

class UserRegistraterRequest(BaseModel):
    full_name: str = field(..., min_length=3, max_length=50)
    email: EmailStr =field(..., min_length=5 ,max_length=50)
    password: str = field(..., min_length=8, max_length=50)
    confirm_password: str = field(..., min_length=8, max_length=50)

class UserLoginRequest(BaseModel):
    email:EmailStr = field(..., min_length=5, max_length=50)
    password:str = field(..., min_length=8, max_length=50)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : str
    email: EmailStr
    is_active: bool = True

class TokenResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    access_token: str
    token_types : str = "bearer"
        

