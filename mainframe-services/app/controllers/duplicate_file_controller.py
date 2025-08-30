from typing import List, Dict, Any, Set, Tuple
from collections import defaultdict

from bson import ObjectId
from fastapi import HTTPException
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.controllers.assessment_controller import get_file_assessments
from app.schemas.common_schema import ErrorResponse
from app.schemas.duplicate_file_schema import (
    FileInfo, 
    DuplicateNameGroup, 
    DuplicatesResponse
)


async def get_duplicate_files_by_repository(
    db: AsyncIOMotorClient,
    repository_id: str,
    skip: int = 0,
    limit: int = 100
) -> DuplicatesResponse:
    """
    Get duplicate files for a specific repository.
    
    Args:
        db: Database connection
        repository_id: Repository ID to filter by
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        Structured duplicate files response
    """
    try:
        repo_object_id = ObjectId(repository_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message="Invalid repository ID format",
                error_code="invalid_id"
            ).dict()
        )
    
    total_unique_files_count = await db.duplicate_files.aggregate([
        {
            "$match": {
                "repository_id": repo_object_id
            }
        }, {
            "$group": {
                "_id": {
                    "name": "$name", 
                    "label": "$label"
                },
            }
        }, {
            "$count": "total"
        }
    ]).to_list()
    
    total = total_unique_files_count[0]["total"] if total_unique_files_count else 0
    
    unique_files_label_aggregate = await db.duplicate_files.aggregate([
        {
            "$match": {
                "repository_id": repo_object_id
            }
        }, {
            "$group": {
                "_id": {
                    "name": "$name", 
                    "label": "$label"
                }
            }
        }, {
            "$sort": {
                "_id.name": 1
            }
        }, {
            "$skip": skip
        }, {
            "$limit": limit
        }
    ]).to_list()
    
    if not unique_files_label_aggregate:
        return DuplicatesResponse(
            duplicate_name_groups=[],
            total=0
        )
    
    
    operators = []
    for file in unique_files_label_aggregate:
        operators.append({
            "$and": [
                {
                    "name": file["_id"]["name"], 
                    "label": file["_id"]["label"], 
                    "repository_id": repo_object_id
                }
            ]
        })
    
    duplicate_files = await db.duplicate_files.find({"$or": operators}).to_list()
    
    file_assessment = await get_file_assessments(db, repository_id, [file["path"] for file in duplicate_files])
    file_assessment_dict = {file["path"]: file for file in file_assessment}
    
    # Process and transform the files
    for file in duplicate_files:
        file["_id"] = str(file["_id"])
        file["repository_id"] = str(file["repository_id"])
        file["loc"] = file_assessment_dict.get(file["path"], {}).get("code", 0)
        file["path"] = file["path"].replace(f"{repository_id}/", "")
        
        # Remove the repository ID from the path and add the file name
        file["same_content_with"] = [
            path.replace(f"{repository_id}/", "")
            for path in file.get("same_content_with", [])
        ]
    
    name_label_groups = defaultdict(list)
    for file in duplicate_files:
        key = (file.get("name"), file.get("label"))
        name_label_groups[key].append(file)
    
    duplicate_name_groups = []
    
    for (name, label), files in name_label_groups.items():
        file_infos = [
            FileInfo(
                _id=f["_id"],
                repository_id=f["repository_id"],
                name=f["name"],
                label=f["label"],
                path=f["path"],
                encoding=f["encoding"],
                loc=f["loc"],
            ) for f in files
        ]                
        content_groups: List[List[FileInfo]] = []
        for file in files:
            same_content_with = file.get("same_content_with", [])
            if same_content_with:
                for path in same_content_with:
                    content_duplicates = [
                            FileInfo(
                                _id=f["_id"],
                                repository_id=f["repository_id"],
                                name=f["name"],
                                label=f["label"],
                                path=f["path"],
                                encoding=f["encoding"],
                                loc=f["loc"],
                            ) for f in files if f["path"] == path
                        ]
                    content_groups.append(content_duplicates)
        
        has_content_duplicates = len(content_groups) > 0
        duplicate_name_groups.append(
            DuplicateNameGroup(
                name=name,
                label=label,
                files=file_infos,
                has_content_duplicates=has_content_duplicates,
                content_duplicates=content_groups
            )
        )
    # Create the response object
    response = DuplicatesResponse(
        duplicate_name_groups=duplicate_name_groups,
        total=total,
    )
    return response 

        