from pydantic import BaseModel, ConfigDict, EmailStr, Field ,model_validator
from uuid import UUID
class UserRegisterRequest(BaseModel):
    full_name: str = Field(
        ...,
        min_length=3,
        max_length=50
        ) 
    email: EmailStr = Field(
        ..., 
        min_length=5, 
        max_length=50
        )
    password: str = Field(
        ...,
        min_length=4,
        max_length=50
        )
    confirm_password: str = Field(
        ..., 
        min_length=4, 
        max_length=50
        )
    @model_validator(mode="after")
    def validate_passwords(self)->"UserRegisterRequest":
        if self.password!= self.confirm_password:
            raise ValueError("password and confirm password do not match")
        else :
            return self


class UserLoginRequest(BaseModel):
   email: EmailStr = Field(
       ..., 
       min_length=5, 
       max_length=50,
       )
   password: str = Field(
       ..., 
       min_length=8, 
       max_length=50
       )

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    full_name: str
    email: EmailStr
    is_active: bool = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
