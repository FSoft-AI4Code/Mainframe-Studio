from fastapi import HTTPException
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
import csv
from io import StringIO
from typing import Literal, AsyncGenerator

from app.schemas.common_schema import ErrorResponse
from app.schemas.dataset_assignment_schema import (
    GetDatasetAssignmentByRepositoryResponse,
    JclDatasetAssignment,
    DatasetAssignmentFilter,
    DatasetStatisticsByRepositoryResponse,
    DatasetAssignmentFilterResponse
)


async def get_dataset_assignments_by_repository(
    db: AsyncIOMotorDatabase,
    repository_id: str,
    filters: DatasetAssignmentFilter,
    skip: int = 0,
    limit: int = 100,
) -> GetDatasetAssignmentByRepositoryResponse:
    """
    Retrieve dataset assignments of a repository with pagination and filtering

    Args:
        repository_id: ID of the repository to filter dataset assignments
        db: Database connection
        skip: Number of records to skip
        limit: Maximum number of records to return

    Returns:
        Dict containing dataset assignments and count
    """
    repo_obj_id = await __get_valid_repo_obj_id(db, repository_id)
    filter = __build_dataset_assignment_filter(repo_obj_id, filters)

    total = await db.dataset_assignments.count_documents(filter)
    cursor = db.dataset_assignments.find(filter).skip(skip).limit(limit)
    dataset_objs = await cursor.to_list(length=limit)

    dataset_assignments = [
        JclDatasetAssignment(**dataset_obj) for dataset_obj in dataset_objs
    ]

    response = GetDatasetAssignmentByRepositoryResponse(
        dataset_assignments=dataset_assignments,
        total=total,
        skip=skip,
        limit=limit,
    )

    return response


async def export_dataset_assignments_csv(
    db: AsyncIOMotorDatabase,
    repository_id: str,
    filters: DatasetAssignmentFilter,
    view: Literal["job", "file"]
) -> AsyncGenerator[str, None]:
    """
    Retrieve dataset assignments of a repository and build CSV content.

    Args:
        repository_id: ID of the repository to filter dataset assignments
        db: Database connection
        filters: Filter criteria for dataset assignments
        view: The view type ("job-view" or "file-view")

    Yields:
        str: A chunk of CSV content, including headers and rows.
    """

    # Validate repository ID
    repo_obj_id = await __get_valid_repo_obj_id(db, repository_id)

    # Build query filter
    filter = __build_dataset_assignment_filter(repo_obj_id, filters)

    # Define CSV columns based on view
    view_config = {
        "job": {
            "headers": [
                "JCL Name",
                "Step",
                "Exec Program",
                "Physical File",
                "Assign Name",
                "File Type",
                "Open Mode",
            ],
            "fields": [
                "jcl_name",
                "step",
                "exec_program_id",
                "dataset_name",
                "ddname",
                "dataset_type",
                "open_mode",
            ],
        },
        "file": {
            "headers": [
                "File Name",
                "Assign Name",
                "File Type",
                "Open Mode",
                "Job Name",
                "Step Name",
                "Program Name",
            ],
            "fields": [
                "dataset_name",
                "ddname",
                "dataset_type",
                "open_mode",
                "jcl_name",
                "step",
                "exec_program_id",
            ],
        },
    }
    config = view_config.get(view, view_config["file"])
    headers = config["headers"]
    fields = config["fields"]

    cursor = db.dataset_assignments.find(filter)
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    yield output.getvalue()
    output.seek(0)
    output.truncate(0)
    async for item in cursor:
        row = {}
        for header, field in zip(headers, fields):
            if field == "open_mode":
                row[header] = "; ".join(
                    op.get(field, "") for op in item.get("access_operations", [])
                )
            else:
                row[header] = item.get(field, "")
        writer.writerow(row)
        yield output.getvalue()
        output.seek(0)
        output.truncate(0)


async def get_dataset_statistics_by_repository(
    db: AsyncIOMotorDatabase, repository_id: str, filters: DatasetAssignmentFilter
) -> DatasetStatisticsByRepositoryResponse:
    repo_obj_id = await __get_valid_repo_obj_id(db, repository_id)
    filter = __build_dataset_assignment_filter(repo_obj_id, filters)

    # Define $facet stages to run multiple aggregations in parallel
    facet = {
        "jobs": [{"$group": {"_id": "$jcl_name"}}, {"$count": "count"}],
        "steps": [{"$group": {"_id": {"step": "$step", "jcl_name": "$jcl_name"}}}, {"$count": "count"}],
        "programs": [
            {"$unwind": "$access_operations"},
            {"$group": {"_id": "$access_operations.open_by_program_id"}},
            {"$count": "count"},
        ],
        "files": [{"$group": {"_id": "$dataset_name"}}, {"$count": "count"}]
    }

    # Build $project stage to extract count values from each facet result
    # Defaults to 0 if the array is empty (no matching records)
    project = {
        field: {"$ifNull": [{"$arrayElemAt": [f"${field}.count", 0]}, 0]}
        for field in facet.keys()
    }

    pipeline = [
        {"$match": filter},
        {"$facet": facet},
        {"$project": project},
    ]

    result = await db.dataset_assignments.aggregate(pipeline).to_list(length=1)
    stats = result[0]
    return DatasetStatisticsByRepositoryResponse(**stats)

async def get_dataset_available_filters(
    repository_id: str,
    db: AsyncIOMotorDatabase
) -> DatasetAssignmentFilterResponse:
    """
    Retrieve available filters for dataset assignments in a given repository

    Args:
        repository_id: ID of the repository to filter dataset assignments
        db: Database connection
        
    Returns:
        Dict containing available filters for dataset assignments
    """
    repo_obj_id = await __get_valid_repo_obj_id(db, repository_id)

    result = await db.dataset_assignments.distinct("dataset_type", {"repository_id": repo_obj_id})
    dataset_type_distinct = [value for value in result if value is not None]

    result = await db.dataset_assignments.distinct("access_operations.open_mode", {"repository_id": repo_obj_id})
    open_mode_distinct =  [value for value in result if value is not None]
    response = DatasetAssignmentFilterResponse(
        dataset_type=dataset_type_distinct,
        open_mode=open_mode_distinct
    )
    return response


async def __get_valid_repo_obj_id(
    db: AsyncIOMotorDatabase, repository_id: str
) -> ObjectId:
    """
    Validate the repository ID and ensure the repository exists.
    Return ObjectId of the repository.
    """
    try:
        repo_obj_id = ObjectId(repository_id)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message="Invalid repository ID",
                error_code="INVALID_REPOSITORY_ID",
            ).model_dump(),
        )

    repo_exists = await db.repositories.find_one({"_id": repo_obj_id})
    if not repo_exists:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Repository not found",
                error_code="REPOSITORY_NOT_FOUND",
            ).model_dump(),
        )

    return repo_obj_id


def __build_dataset_assignment_filter(
    repo_obj_id: ObjectId, filters: DatasetAssignmentFilter
) -> dict:
    """Construct MongoDB query filter for dataset assignments"""
    query = {"repository_id": repo_obj_id}

    filter_dict = filters.model_dump(exclude_none=True)
    for key, value in filter_dict.items():
        query_key = (
            f"access_operations.{key}"
            if key in ["open_by_program_id", "open_mode"]
            else key
        )

        # case-insensitive, substring match
        query[query_key] = {
            "$regex": value,
            "$options": "i",
        }

    return query
