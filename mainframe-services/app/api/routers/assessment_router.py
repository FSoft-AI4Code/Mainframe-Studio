from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.database import get_database
from app.controllers import assessment_controller
from app.decorators.error_handling import DLXErrorHandler
from app.schemas.assessment_schema import (
    AssessmentCreate,
    AssessmentCreateResponse,
    GetAssessmentResponse,
    GetAssessmentsResponse,
    GetAssessmentsByRepositoryResponse,
    GetFileCountsByRepositoryResponse,
    GetAssessmentOverviewByRepositoryResponse,
    UpdateAssessmentRequest,
    UpdateAssessmentResponse,
    DeleteAssessmentResponse
)
from app.schemas.common_schema import ResponseBase, PaginationParams, ErrorResponse
from app.security import auth

router = APIRouter()

dlx_assessment_handler = DLXErrorHandler(
    exchange="dlx_exchange",
    queue_name="dlx_assessment_queue",
    routing_key="dlq_assessment_key"
)


def custom_error_handler(exc):
    logger.error(f"Custom assessment handler - captured exception: {exc}")


@router.post("/", response_model=ResponseBase[AssessmentCreateResponse])
@dlx_assessment_handler.error_handling(custom_handler=custom_error_handler)
async def create_assessment(
        assessment: AssessmentCreate,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    result = await assessment_controller.create_assessment(db=db, assessment=assessment)
    return ResponseBase(data=result)


@router.get("/{assessment_id}", response_model=ResponseBase[GetAssessmentResponse])
async def read_assessment(
        assessment_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    assessment = await assessment_controller.get_assessment(db, assessment_id=assessment_id)
    if assessment is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Assessment not found",
                error_code="ASSESSMENT_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=assessment)


@router.get("/", response_model=ResponseBase[GetAssessmentsResponse])
async def read_assessments(
        pagination: PaginationParams = Depends(),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    result = await assessment_controller.get_assessments(
        db,
        skip=pagination.skip,
        limit=pagination.limit
    )

    return ResponseBase(data={
        "assessments": result["assessments"],
        "total": result["total"],
        "skip": pagination.skip,
        "limit": pagination.limit
    })


@router.get("/repository/{repository_id}", response_model=ResponseBase[GetAssessmentsByRepositoryResponse])
async def read_assessments_by_repository(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    assessments = await assessment_controller.get_assessments_by_repository(
        db,
        repository_id=repository_id
    )
    return ResponseBase(data={"assessments": assessments})


@router.patch("/{assessment_id}", response_model=ResponseBase[UpdateAssessmentResponse])
async def update_assessment(
        assessment_id: str,
        assessment: UpdateAssessmentRequest,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    update_data = assessment.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message="No fields to update",
                error_code="NO_UPDATES"
            ).model_dump()
        )

    updated_assessment = await assessment_controller.update_assessment(
        db,
        assessment_id=assessment_id,
        assessment=update_data
    )
    if updated_assessment is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Assessment not found",
                error_code="ASSESSMENT_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=updated_assessment)


@router.delete("/{assessment_id}", response_model=ResponseBase[DeleteAssessmentResponse])
async def delete_assessment(
        assessment_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    result = await assessment_controller.delete_assessment(db, assessment_id=assessment_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Assessment not found",
                error_code="ASSESSMENT_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(
        data=DeleteAssessmentResponse(
            message=f"Assessment {assessment_id} successfully deleted"
        )
    )


@router.get("/repository/{repository_id}/files", response_model=ResponseBase[GetFileCountsByRepositoryResponse])
async def get_file_counts_by_repository(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    file_counts = await assessment_controller.get_file_counts_by_repository(
        db,
        repository_id=repository_id
    )
    data = {
        "total": sum(fc["count"] for fc in file_counts),
        "file_counts": file_counts
    }
    return ResponseBase(data=data)


@router.get("/repository/{repository_id}/overview",
            response_model=ResponseBase[GetAssessmentOverviewByRepositoryResponse])
async def get_assessment_overview_by_repository(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    overview = await assessment_controller.get_assessment_overview_by_repository(
        db,
        repository_id=repository_id
    )
    return ResponseBase(data=overview)
