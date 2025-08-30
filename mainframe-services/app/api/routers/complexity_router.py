from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.database import get_database
from app.schemas.complexity_schema import (
    ComplexityCreate,
    ComplexityCreateResponse,
    GetComplexityResponse,
    GetComplexitiesResponse,
    GetComplexitiesByRepositoryResponse,
    UpdateComplexityRequest,
    UpdateComplexityResponse,
    DeleteComplexityResponse
)
from app.schemas.common_schema import ResponseBase, PaginationParams, ErrorResponse
from app.controllers import complexity_controller, reverse_controller
from app.security import auth

router = APIRouter()


@router.post("/", response_model=ResponseBase[ComplexityCreateResponse])
async def create_complexity(
    complexity: ComplexityCreate,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    dist = await reverse_controller.get_complexity_distribution(db, complexity.repository_id)
    aggregated_data = await reverse_controller.get_complexity_aggregated_data_of_repository_id(db, complexity.repository_id)
    result = await complexity_controller.create_complexity(db=db, complexity=complexity, dist=dist, aggregated_data=aggregated_data)
    return ResponseBase(data=result)


@router.get("/{complexity_id}", response_model=ResponseBase[GetComplexityResponse])
async def read_complexity(complexity_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    complexity = await complexity_controller.get_complexity(db, complexity_id=complexity_id)
    if complexity is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Complexity not found",
                error_code="COMPLEXITY_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=complexity)


@router.get("/", response_model=ResponseBase[GetComplexitiesResponse])
async def read_complexities(
    pagination: PaginationParams = Depends(),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    result = await complexity_controller.get_complexities(
        db, 
        skip=pagination.skip,
        limit=pagination.limit
    )
    return ResponseBase(data={
        "complexities": result["complexities"],
        "total": result["total"],
        "skip": pagination.skip,
        "limit": pagination.limit
    })


@router.get("/repository/{repository_id}", response_model=ResponseBase[GetComplexitiesByRepositoryResponse])
async def read_complexities_by_repository(
    repository_id: str,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    complexities = await complexity_controller.get_complexities_by_repository(
        db, 
        repository_id=repository_id
    )
    aggregated_data = await reverse_controller.get_complexity_aggregated_data_of_repository_id(db, repository_id)
    return ResponseBase(data={"complexities": complexities, **aggregated_data})


# @router.get("/repository/{repository_id}/dist", response_model=ResponseBase[GetComplexityDistributionResponse])
@router.get("/repository/{repository_id}/dist", response_model=ResponseBase)
async def get_complexity_distribution_by_repository(
    repository_id: str,
    reprocess: bool = False,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    complexity = await complexity_controller.get_complexity_by_repository(db, repository_id=repository_id)

    if complexity and not reprocess:
        return ResponseBase(data=complexity)

    if complexity is None or reprocess:

        dist = await reverse_controller.get_complexity_distribution(db, repository_id)
        aggregated_data = await reverse_controller.get_complexity_aggregated_data_of_repository_id(db, repository_id)
        if complexity is not None:
            result = await complexity_controller.create_complexity_dist(db, repository_id, dist, aggregated_data, complexity.id)
        else:
            result = await complexity_controller.create_complexity_dist(db, repository_id, dist, aggregated_data)
        return ResponseBase(data=result)
    return ResponseBase(data=complexity)




@router.patch("/{complexity_id}", response_model=ResponseBase[UpdateComplexityResponse])
async def update_complexity(
    complexity_id: str,
    complexity: UpdateComplexityRequest,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    update_data = complexity.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message="No fields to update",
                error_code="NO_UPDATES"
            ).model_dump()
        )

    updated_complexity = await complexity_controller.update_complexity(
        db, 
        complexity_id=complexity_id,
        complexity=update_data
    )
    if updated_complexity is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Complexity not found",
                error_code="ASSESSMENT_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=updated_complexity)


@router.delete("/{complexity_id}", response_model=ResponseBase[DeleteComplexityResponse])
async def delete_complexity(
    complexity_id: str,
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    result = await complexity_controller.delete_complexity(db, complexity_id=complexity_id)
    if not result:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Complexity not found",
                error_code="COMPLEXITY_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(
        data=DeleteComplexityResponse(
            message=f"AssessComplexityent {complexity_id} successfully deleted"
        )
    )
