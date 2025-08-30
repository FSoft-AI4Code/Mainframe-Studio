from motor.motor_asyncio import AsyncIOMotorDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
from bson import ObjectId
from fastapi import HTTPException

from app.controllers import reverse_controller
from app.schemas.common_schema import ErrorResponse
from app.models.assessment import Assessment
from app.schemas import assessment_schema
from app.worker import queue
from app.constants.graph import NodeStatus
from app.constants.cobol import FileType


async def create_assessment(db: AsyncIOMotorDatabase, assessment: assessment_schema.AssessmentCreate):
    assessment_dict = assessment.model_dump()
    repository_id = ObjectId(assessment_dict["repository_id"])
    # Set assessment ID equal to repository_id
    assessment_dict["_id"] = repository_id
    assessment_dict["repository_id"] = repository_id

    # Use update_one with upsert=True to insert or update the document
    await db.assessments.update_one(
        {"_id": repository_id},
        {"$set": assessment_dict},
        upsert=True
    )

    # Update repo status
    repo = await db.repositories.find_one({"_id": ObjectId(repository_id)})
    repo["status"] = "assessed"
    await db.repositories.update_one({"_id": ObjectId(repository_id)}, {"$set": repo})

    await queue.enqueue("read_content", repo_id=str(repository_id), timeout=10000)
    return await get_assessment(db, str(repository_id))


async def get_assessment(db: AsyncIOMotorDatabase, assessment_id: str):
    assessment = await db.assessments.find_one({"_id": ObjectId(assessment_id)})
    if assessment:
        return Assessment(**assessment)


async def get_assessments(db: AsyncIOMotorDatabase, skip: int = 0, limit: int = 100):
    total = await db.assessments.count_documents({})
    assessments = await db.assessments.find().skip(skip).limit(limit).to_list(length=limit)
    return {
        "assessments": [Assessment(**assessment) for assessment in assessments],
        "total": total,
    }


async def get_assessments_by_repository(db: AsyncIOMotorDatabase, repository_id: str):
    assessments = await db.assessments.find({"repository_id": ObjectId(repository_id)}).to_list(length=100)
    return [Assessment(**assessment) for assessment in assessments]

async def get_file_assessments(db: AsyncIOMotorClient, repository_id: str, paths: List[str]):
    """
    Get the assessment data for specific file paths within a repository.
    
    Args:
        db: Database connection
        repository_id: Repository ID
        paths: List of file paths to filter by
        
    Returns:
        List of assessments for the specified file paths
    """
    try:
        repo_object_id = ObjectId(repository_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message="Invalid repository ID format",
                error_code="INVALID_ID"
            ).model_dump()
        )
    
    repo_assessment = await db.assessments.find_one(
        {"repository_id": repo_object_id}
    )
    
    file_assessment = []
    for assessment in repo_assessment.get("result", {}).get("assessment", []):
        if assessment.get("path") in paths:
            file_assessment.append(assessment)
    
    return file_assessment

async def update_assessment(db: AsyncIOMotorDatabase, assessment_id: str, assessment: assessment_schema.AssessmentCreate):
    await db.assessments.update_one(
        {"_id": ObjectId(assessment_id)},
        {"$set": assessment.dict(exclude_unset=True)}
    )
    return await get_assessment(db, assessment_id)


async def delete_assessment(db: AsyncIOMotorDatabase, assessment_id: str):
    result = await db.assessments.delete_one({"_id": ObjectId(assessment_id)})
    return result.deleted_count > 0


async def get_file_counts_by_repository(db: AsyncIOMotorDatabase, repository_id: str):
    pipeline = [
        {"$match": {"repository_id": ObjectId(repository_id)}},
        {"$unwind": "$result.assessment"}, 
        {"$group": {"_id": "$result.assessment.label", "count": {"$sum": 1}}},  
        {"$project": {"label": "$_id", "count": 1, "_id": 0}}
    ]
    return await db.assessments.aggregate(pipeline).to_list(length=None)


async def get_assessment_overview_by_repository(db: AsyncIOMotorDatabase, repository_id: str):
    # Calculate dead code percentage
    count_nodes_pipeline = [
        {"$match": {"repository_id": ObjectId(repository_id)}},
        {"$group": {
            "_id": None, # group all matching documents
            "total_count": {"$sum": 1},
            "dead_count": {"$sum": {"$cond": [{"$eq": ["$status", NodeStatus.DEAD.value]}, 1, 0]}}
        }},
    ]

    count_nodes_result = await db.nodes.aggregate(count_nodes_pipeline).to_list(1)
    if not count_nodes_result:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message=f"Nodes not found for repository: {repository_id}",
                error_code="NODES_NOT_FOUND"
            ).model_dump()
        )
    
    total_node_count = count_nodes_result[0]["total_count"]
    dead_node_count = count_nodes_result[0]["dead_count"]
    dead_code_percentage = round((dead_node_count / total_node_count) * 100, 2) 

    # Calculate average complexity
    complexity_pipeline = [
        {"$match": {"repository_id": ObjectId(repository_id), "type": FileType.COBOL.value}},
        {"$group": {
            "_id": None, # group all matching documents
            "file_count": {"$sum": 1},
            "total_complexity": {"$sum": "$output.complexity"}
        }},
    ]

    complexity_result = await db.reverse_engineering.aggregate(complexity_pipeline).to_list(1)
    if not complexity_result:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message=f"Reverse engineering data not found for repository: {repository_id}",
                error_code="REVERSE_DATA_NOT_FOUND"
            ).model_dump()
        )
    
    file_count = complexity_result[0]["file_count"]
    total_complexity = complexity_result[0]["total_complexity"]
    average_complexity = round(total_complexity / file_count, 2) 

    coverage = (await reverse_controller.get_reverse_assets_coverage(db, repository_id))["total_coverage"]

    return { 
        "coverage": coverage,
        "average_complexity": average_complexity, 
        "dead_code_percentage": dead_code_percentage 
    }