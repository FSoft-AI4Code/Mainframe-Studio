from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.config.database import get_database
from app.schemas.user_schema import UserCreateResponse, UserCreate, User
from app.controllers import user_controller
from app.security import auth

router = APIRouter()


@router.post("/", response_model=UserCreateResponse)
async def create_user(user: UserCreate, db=Depends(get_database)):
    db_user = await user_controller.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_id = await user_controller.create_user(db=db, user=user)
    return UserCreateResponse(id=user_id)


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str, db=Depends(get_database)):
    db_user = await user_controller.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db=Depends(get_database)):
    users = await user_controller.get_users(db, skip=skip, limit=limit)
    return users
