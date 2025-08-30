from app.models.user import User
from app.schemas import user_schema
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from passlib.context import CryptContext

# Add this at the top of the file
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(db: AsyncIOMotorDatabase, user: user_schema.UserCreate):
    user_dict = user.model_dump()
    user_dict["hashed_password"] = pwd_context.hash(user_dict.pop("password"))
    user_dict["permissions"] = []
    result = await db.users.insert_one(user_dict)
    return result.inserted_id


async def get_user(db: AsyncIOMotorDatabase, user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return User(**user)


async def get_user_by_email(db: AsyncIOMotorDatabase, email: str):
    try:
        user = await db.users.find_one({"email": email})
        if user:
            return User(**user)
        return None
    except Exception:
        return None


async def get_users(db: AsyncIOMotorDatabase, skip: int = 0, limit: int = 100):
    users = await db.users.find().skip(skip).limit(limit).to_list(length=limit)
    return [User(**user) for user in users]


async def update_user(db: AsyncIOMotorDatabase, user_id: str, user: user_schema.UserCreate):
    await db.users.update_one(
        {"_id": ObjectId(user_id)}, 
        {"$set": user.model_dump(exclude_unset=True)}
    )
    return await get_user(db, user_id)


async def delete_user(db: AsyncIOMotorDatabase, user_id: str):
    result = await db.users.delete_one({"_id": user_id})
    return result.deleted_count > 0
