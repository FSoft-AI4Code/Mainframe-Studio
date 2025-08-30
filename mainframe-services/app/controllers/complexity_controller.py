from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.complexity import Complexity
from app.schemas import complexity_schema
from bson import ObjectId


async def create_complexity(db: AsyncIOMotorDatabase, complexity: complexity_schema.ComplexityCreate):
    complexity_dict = complexity.dict()
    repository_id = ObjectId(complexity_dict["repository_id"])
    # Set complexity ID equal to repository_id
    complexity_dict["_id"] = repository_id
    complexity_dict["repository_id"] = repository_id

    # Use update_one with upsert=True to insert or update the document
    await db.complexities.update_one(
        {"_id": repository_id},
        {"$set": complexity_dict},
        upsert=True
    )
    return await get_complexity(db, str(repository_id))


async def get_complexity(db: AsyncIOMotorDatabase, complexity_id: str):
    complexity = await db.complexities.find_one({"_id": ObjectId(complexity_id)})
    if complexity:
        return Complexity(**complexity)


async def get_complexities(db: AsyncIOMotorDatabase, skip: int = 0, limit: int = 100):
    total = await db.complexities.count_documents({})
    complexities = await db.complexities.find().skip(skip).limit(limit).to_list(length=limit)
    # return [complexity(**complexity) for complexity in complexities]
    return {
        "complexities": [Complexity(**complexity) for complexity in complexities],
        "total": total,
    }


async def get_complexities_by_repository(db: AsyncIOMotorDatabase, repository_id: str):
    complexities = await db.complexities.find({"repository_id": ObjectId(repository_id)}).to_list(length=100)
    return [Complexity(**complexity) for complexity in complexities]


async def get_complexity_by_repository(db: AsyncIOMotorDatabase, repository_id: str):
    complexity = await db.complexities.find_one({"repository_id": ObjectId(repository_id)})
    if complexity:
        return Complexity(**complexity)

async def update_complexity(db: AsyncIOMotorDatabase, complexity_id: str, complexity: complexity_schema.ComplexityCreate):
    await db.complexities.update_one(
        {"_id": ObjectId(complexity_id)},
        {"$set": complexity.dict(exclude_unset=True)}
    )
    return await get_complexity(db, complexity_id)


async def delete_complexity(db: AsyncIOMotorDatabase, complexity_id: str):
    result = await db.complexities.delete_one({"_id": ObjectId(complexity_id)})
    return result.deleted_count > 0


async def create_complexity_dist(db: AsyncIOMotorDatabase, repository_id: str, dist: dict, aggregated_data: dict, complexity_id: ObjectId=ObjectId()):
    repository_id = ObjectId(repository_id)
    complexity_dict = {
        "_id": complexity_id,
        "repository_id": repository_id,
        "result": {
            "dist": dist,
            "average_complexity": aggregated_data["average_complexity"],
            "number_of_complexities": aggregated_data["number_of_complexities"]
        }

    }
    repository_id = ObjectId(complexity_dict["repository_id"])
    # Set complexity ID equal to repository_id
    complexity_dict["_id"] = repository_id
    complexity_dict["repository_id"] = repository_id

    # Use update_one with upsert=True to insert or update the document
    await db.complexities.update_one(
        {"_id": repository_id},
        {"$set": complexity_dict},
        upsert=True
    )
    return await get_complexity(db, str(repository_id))