from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserRegisterRequest(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr = Field(..., min_length=5, max_length=50)
    password: str = Field(..., min_length=8, max_length=50)
    confirm_password: str = Field(..., min_length=8, max_length=50)

class UserLoginRequest(BaseModel):
   email: EmailStr = Field(..., min_length=5, max_length=50)
   password: str = Field(..., min_length=8, max_length=50)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

id: str
email: EmailStr
is_active: bool = True

class TokenResponse(BaseModel):
   access_token: str
   token_type: str = "bearer"
