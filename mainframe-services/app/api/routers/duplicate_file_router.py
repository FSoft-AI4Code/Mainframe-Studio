from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.database import get_database
from app.controllers import duplicate_file_controller
from app.schemas.common_schema import PaginationParams
from app.schemas.duplicate_file_schema import GetDuplicateFilesByRepositoryResponse
from app.security import auth

router = APIRouter()


@router.get("/{repository_id}", response_model=GetDuplicateFilesByRepositoryResponse)
async def get_duplicate_files_by_repository(
    repository_id: str,
    pagination: PaginationParams = Depends(),
    db: AsyncIOMotorClient = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user),
):
    """
    Get duplicate files for a specific repository, grouped by type of duplication.
    
    Args:
        repository_id: Repository ID to filter by
        pagination: Pagination parameters
        db: Database connection
        current_user: Current authenticated user
        
    Returns:
        Structured response with duplicate files grouped by duplication type
    """
    duplicates_response = await duplicate_file_controller.get_duplicate_files_by_repository(
        db=db,
        repository_id=repository_id,
        skip=pagination.skip,
        limit=pagination.limit
    )
    
    return GetDuplicateFilesByRepositoryResponse(
        data=duplicates_response,
        success=True
    )
