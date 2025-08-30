from io import BytesIO
from typing import List, Optional

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.database import get_database
from app.constants.cobol import FileType
from app.controllers import reverse_controller
from app.controllers.assessment_controller import get_assessments_by_repository
from app.controllers.repository_controller import get_repository
from app.schemas.common_schema import ErrorResponse, PaginationParams, ResponseBase
from app.schemas.reverse_schema import (
    ReverseAssetsCoverageResponse,
    ReverseEngineering,
    ReverseEngineeringCreate,
    ReverseEngineeringReportResponse,
    ReverseEngineeringOutputResponse,
    UpdateNodeLabelRequest,
    UpdateNodeLabelResponse,
)
from app.security import auth
from app.tasks.utils import produce_parse_task_mq

router = APIRouter()


@router.post("/", response_model=ResponseBase[ReverseEngineering])
async def create_reverse_engineering(
        reverse: ReverseEngineeringCreate,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    result = await reverse_controller.create_reverse_engineering(db=db, reverse=reverse)
    return ResponseBase(data=result)


@router.get("/{reverse_id}", response_model=ResponseBase[ReverseEngineering])
async def read_reverse_engineering(
        reverse_id: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    reverse = await reverse_controller.get_reverse_engineering(db, reverse_id=reverse_id)
    if reverse is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Reverse engineering task not found",
                error_code="REVERSE_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=reverse)


@router.get("/", response_model=ResponseBase[List[ReverseEngineering]])
async def read_reverse_engineerings(
        pagination: PaginationParams = Depends(),
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    reverses = await reverse_controller.get_reverse_engineerings(
        db,
        skip=pagination.skip,
        limit=pagination.limit
    )
    return ResponseBase(data=reverses)


@router.patch("/{reverse_id}", response_model=ResponseBase[ReverseEngineering])
async def update_reverse_engineering(
        reverse_id: str,
        reverse: ReverseEngineeringCreate,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    updated_reverse = await reverse_controller.update_reverse_engineering(
        db,
        reverse_id=reverse_id,
        reverse=reverse
    )
    if updated_reverse is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Reverse engineering task not found",
                error_code="REVERSE_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=updated_reverse)


@router.delete("/{reverse_id}", response_model=ResponseBase[bool])
async def delete_reverse_engineering(
        reverse_id: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    success = await reverse_controller.delete_reverse_engineering(db, reverse_id=reverse_id)
    if not success:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Reverse engineering task not found",
                error_code="REVERSE_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=success)


@router.get("/repository/{repository_id}/type/{type}/name/{name}",
            response_model=ResponseBase[ReverseEngineeringOutputResponse])
async def get_reverse_engineering_report(
        repository_id: str,
        type: str,
        name: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Get reverse engineering reports by repository ID with optional type and name filters.
    
    Args:
        repository_id: ID of the repository
        type: Optional type of reverse engineering report
        name: Optional name of the file
    """
    reverse = await reverse_controller.get_reverse_engineering_report(
        db,
        repository_id=repository_id,
        type=type,
        name=name
    )
    if not reverse:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Reverse engineering reports not found",
                error_code="REVERSE_REPORTS_NOT_FOUND"
            ).model_dump()
        )

    return ResponseBase(data=ReverseEngineeringOutputResponse(**reverse.model_dump()))


@router.get("/repository/{repository_id}", response_model=ResponseBase[List[ReverseEngineeringReportResponse]])
async def list_reverse_engineering_reports(
        repository_id: str,
        type: Optional[str] = Query(None, description="Type of reverse engineering report"),
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    List reverse engineering reports by repository ID with optional type filter.
    
    Args:
        repository_id: ID of the repository
        type: Optional type of reverse engineering report to filter by
    """
    reports = await reverse_controller.list_reverse_engineering_reports(
        db,
        repository_id=repository_id,
        type=type
    )
    if not reports:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="No reverse engineering reports found",
                error_code="REVERSE_REPORTS_NOT_FOUND"
            ).model_dump()
        )

    return ResponseBase(data=reports)


@router.get("/systems/{system_name}/patterns")
async def get_system_patterns(
        system_name: str,
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Download system patterns Excel file from Azure Blob Storage
    
    Args:
        system_name: Name of the system to get patterns for
    """
    try:
        file_content = await reverse_controller.get_system_patterns(system_name)
        return StreamingResponse(
            BytesIO(file_content),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": f"attachment; filename={system_name}_patterns.xlsx"
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message=f"Error downloading patterns file: {str(e)}",
                error_code="PATTERNS_FILE_NOT_FOUND"
            ).model_dump()
        )


@router.get("/repository/{repository_id}/coverage", response_model=ResponseBase[ReverseAssetsCoverageResponse])
async def get_reverse_assets_coverage(
        repository_id: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Retrieve reverse engineering assets coverage for a given repository
    
    Args:
        repository_id: ID of the repository
    """
    data = await reverse_controller.get_reverse_assets_coverage(
        db,
        repository_id=repository_id,
    )

    if not data:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message=f"Reverse engineering data not found for repository: {repository_id}",
                error_code="REVERSE_DATA_NOT_FOUND"
            ).model_dump()
        )

    return ResponseBase(data=data)


@router.post("/reports", response_model=ResponseBase[ReverseEngineeringOutputResponse])
async def create_report(
        repository_id: str,
        type: str,
        name: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    if type == FileType.COBOL.value:
        repository = await get_repository(db, repository_id)
        if not repository:
            raise HTTPException(
                status_code=404,
                detail=ErrorResponse(
                    message="Repository not found", error_code="REPOSITORY_NOT_FOUND"
                ).model_dump(),
            )

        assessments = await get_assessments_by_repository(db, repository_id)
        if not ((len(assessments) > 0 and
                 assessments[0].result is not None and
                 (name, FileType.COBOL.value) in ((d['name'], d['label']) for d in
                                                  assessments[0].result.get('assessment', [])))):
            raise HTTPException(
                status_code=404,
                detail=ErrorResponse(
                    message="Reverse engineering reports not found",
                    error_code="REVERSE_REPORTS_NOT_FOUND"
                ).model_dump()
            )

        system_type = repository.system_type.value if repository.system_type else "IBM"
        produce_parse_task_mq(repository_id, type, name, system_type=system_type)
        return await get_reverse_engineering_report(
            repository_id, type, name, db, current_user
        )
    else:
        raise HTTPException(
            status_code=406,
            detail=ErrorResponse(
                message="Getting reports for this file type is not supported.",
                error_code="REVERSE_REPORTS_NOT_SUPPORTED"
            ).model_dump()
        )


@router.post(
    "/repositories/{repository_id}/nodes/label",
    response_model=ResponseBase[UpdateNodeLabelResponse],
    summary="Update node label",
    description="""
    Update the label of a node in the repository.
    
    Args:
        repository_id: ID of the repository
        request: UpdateNodeLabelRequest containing the update details
        
    Returns:
        Updated node data
        
    Raises:
        - 404: If node is not found
        - 500: For any server errors
    """
)
async def update_node_label(
        repository_id: str,
        request: UpdateNodeLabelRequest,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    updated_node = await reverse_controller.update_label(
        db=db,
        repository_id=repository_id,
        file_name=request.file_name,
        old_label=request.label,
        new_label=request.new_label,
        comment=request.comment,
        description=request.description,
        current_user=current_user
    )
    return ResponseBase(data=updated_node.model_dump())
