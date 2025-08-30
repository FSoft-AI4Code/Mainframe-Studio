from enum import Enum
from typing import List
from pydantic import BaseModel, EmailStr
from app.schemas.common_schema import PyObjectId

class Role(str, Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"
class Permission(BaseModel):
    project_id: PyObjectId
    role: Role
class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: PyObjectId
    is_active: bool
    permissions: List[Permission]

    class Config:
        from_attributes = True

class UserCreateResponse(BaseModel):
    id: PyObjectId

class Token(BaseModel):
    access_token: str
    token_type: str
