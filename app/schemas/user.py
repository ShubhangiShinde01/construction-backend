from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username  : str
    email     : EmailStr
    password  : str
    full_name : str
    role      : Optional[str] = "manager"

class UserLogin(BaseModel):
    username : str
    password : str

class UserResponse(BaseModel):
    id        : int
    username  : str
    email     : str
    full_name : str
    role      : str
    is_active : bool

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token : str
    token_type   : str
    role         : str
    full_name    : str