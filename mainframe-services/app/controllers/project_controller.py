from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.project import Project
from bson import ObjectId
from typing import List, Optional
from loguru import logger
from fastapi import HTTPException
from app.schemas.common_schema import ErrorResponse

async def create_project(db: AsyncIOMotorDatabase, project: Project) -> Project:
    """Create a new project."""
    project_dict = project.model_dump(exclude={"id"})
    project_dict["user_id"] = ObjectId(project_dict["user_id"])
    result = await db.projects.insert_one(project_dict)
    project.id = result.inserted_id
    return project


async def get_project(db: AsyncIOMotorDatabase, project_id: str) -> Optional[Project]:
    """Get a project by ID."""
    project = await db.projects.find_one({"_id": ObjectId(project_id)})
    if project:
        return Project(**project)
    return None


async def get_projects(
    db: AsyncIOMotorDatabase, 
    user_id: str,
    skip: int = 0, 
    limit: int = 100
) -> List[Project]:
    """Get a list of projects for a specific user using aggregation pipeline."""
    pipeline = [
        # Match user first
        {"$match": {"_id": ObjectId(user_id)}},
        # Unwind permissions array
        {"$unwind": "$permissions"},
        # Lookup projects
        {
            "$lookup": {
                "from": "projects",
                "localField": "permissions.project_id",
                "foreignField": "_id",
                "as": "project"
            }
        },
        {"$unwind": "$project"},
        # Add role to project
        {
            "$addFields": {
                "project.role": "$permissions.role"
            }
        },
        # Group projects
        {
            "$group": {
                "_id": None,
                "projects": {"$push": "$project"},
                "total": {"$sum": 1}
            }
        },
        # Pagination
        {
            "$project": {
                "projects": {"$slice": ["$projects", skip, limit]},
                "total": 1
            }
        }
    ]
    
    result = await db.users.aggregate(pipeline).to_list(1)
    if not result:
        return [], 0
        
    projects = [Project(**proj) for proj in result[0]["projects"]]
    total = result[0]["total"]
    return projects, total


async def update_project(
    db: AsyncIOMotorDatabase, 
    project_id: str, 
    project: Project
) -> Optional[Project]:
    """Update a project."""
    # Get existing project
    existing_project = await db.projects.find_one({"_id": ObjectId(project_id)})
    if not existing_project:
        return None
        
    # Only update fields that are provided
    update_data = project.model_dump(exclude={"id"}, exclude_unset=True)
    
    result = await db.projects.update_one(
        {"_id": ObjectId(project_id)},
        {"$set": update_data}
    )
    
    if result.modified_count:
        # Merge existing data with updates
        updated_project = {**existing_project, **update_data}
        return Project(**updated_project)
    return None


async def delete_project(db: AsyncIOMotorDatabase, project_id: str) -> bool:
    """Delete a project."""
    result = await db.projects.delete_one({"_id": ObjectId(project_id)})
    return result.deleted_count > 0


async def check_project_access(db: AsyncIOMotorDatabase, project_id: str, user_id: str, required_role: str = None) -> tuple[Project, str]:
    """Optimized check_project_access using a single aggregation query."""
    pipeline = [
        {"$match": {"_id": ObjectId(user_id)}},
        {"$unwind": "$permissions"},
        {"$match": {"permissions.project_id": ObjectId(project_id)}},
        {
            "$lookup": {
                "from": "projects",
                "localField": "permissions.project_id",
                "foreignField": "_id",
                "as": "project"
            }
        },
        {"$unwind": "$project"},
        {
            "$project": {
                "project": 1,
                "role": "$permissions.role"
            }
        }
    ]
    
    result = await db.users.aggregate(pipeline).to_list(1)
    
    if not result:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Project not found or no access",
                error_code="PROJECT_NOT_FOUND"
            ).model_dump()
        )

    if required_role and result[0]["role"] != required_role:
        raise HTTPException(
            status_code=403,
            detail=ErrorResponse(
                message=f"User does not have {required_role} permission",
                error_code="INSUFFICIENT_PERMISSIONS"
            ).model_dump()
        )

    return Project(**result[0]["project"]), result[0]["role"]
