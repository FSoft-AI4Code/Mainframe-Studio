from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.database import get_database
from app.controllers import dataset_assignment_controller
from app.schemas.common_schema import PaginationParams, ResponseBase
from typing import Literal
from fastapi.responses import StreamingResponse
from app.schemas.dataset_assignment_schema import (
    DatasetAssignmentFilter,
    GetDatasetAssignmentByRepositoryResponse,
    DatasetStatisticsByRepositoryResponse,
    DatasetAssignmentFilterResponse
)
from app.security import auth

router = APIRouter()


@router.get("/", response_model=ResponseBase[GetDatasetAssignmentByRepositoryResponse])
async def get_dataset_assignments_by_repository(
    repository_id: str,
    pagination: PaginationParams = Depends(),
    filters: DatasetAssignmentFilter = Depends(),
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user),
):
    """
    Retrieve dataset assignments with optional filtering and pagination
    """
    result = await dataset_assignment_controller.get_dataset_assignments_by_repository(
        db,
        repository_id=repository_id,
        filters=filters,
        skip=pagination.skip,
        limit=pagination.limit,
    )
    return ResponseBase(
        data={
            "dataset_assignments": result.dataset_assignments,
            "total": result.total,
            "skip": pagination.skip,
            "limit": pagination.limit,
        }
    )


@router.get("/export")
async def export_dataset_assignments_csv(
    repository_id: str,
    view: Literal["job", "file"],
    filters: DatasetAssignmentFilter = Depends(),
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user),
):
    """
    Stream dataset assignments as a CSV file in chunks with optional filtering
    """

    fileName = f"dataset_assignments_{view}_{repository_id}.csv"
    return StreamingResponse(
        dataset_assignment_controller.export_dataset_assignments_csv(
            db, repository_id=repository_id, filters=filters, view=view
        ),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={fileName}"},
    )


@router.get(
    "/statistics", response_model=ResponseBase[DatasetStatisticsByRepositoryResponse]
)
async def get_dataset_statistics_by_repository(
    repository_id: str,
    db: AsyncIOMotorDatabase = Depends(get_database),
    filters: DatasetAssignmentFilter = Depends(),
    current_user: auth.User = Depends(auth.get_current_user),
):
    """
    Retrieve dataset statistics for a given repository with optional filtering
    """
    result = await dataset_assignment_controller.get_dataset_statistics_by_repository(
        db=db,
        repository_id=repository_id,
        filters=filters
    )
    return ResponseBase(data=result)

@router.get(
    "/available-filters",
    response_model=ResponseBase[DatasetAssignmentFilterResponse]
)
async def get_dataset_available_filters(
    repository_id: str,
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    """
    Retrieve available filters for dataset assignments in a given repository
    """
    result = await dataset_assignment_controller.get_dataset_available_filters(
        db=db,
        repository_id=repository_id
    )
    return ResponseBase(data=result)