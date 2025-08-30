from fastapi import APIRouter, Depends, Response
from fastapi import Query
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.database import get_database
from app.controllers import migration_controller
from app.decorators.error_handling import DLXErrorHandler
from app.schemas.common_schema import ResponseBase
from app.schemas.migration_schema import MigrationStructureResponse, FileContentResponse
from app.security import auth

router = APIRouter()

dlx_project_handler = DLXErrorHandler(
    exchange="dlx_exchange",
    queue_name="dlx_migration_queue",
    routing_key="dlq_migration_key"
)


def custom_error_handler(exc):
    logger.error(f"Custom project handler - captured exception: {exc}")


# @dlx_project_handler.error_handling(custom_handler=custom_error_handler)
# @router.post("/copy/{repository_id}/", response_model=ResponseBase)
# async def migration_copybook_file(
#         repository_id: str,
#         cobol_file_name: str = Query(None, alias="cobol_file_name"),
#         bms_file_name: str = Query(None, alias="bms_file_name"),
#         db: AsyncIOMotorDatabase = Depends(get_database),
#         current_user: auth.User = Depends(auth.get_current_user)
# ):
#     response_data = await migration_controller.publish_copybook_migration_task(db, repository_id, bms_file_name, cobol_file_name)
#     return ResponseBase(data=None)


@dlx_project_handler.error_handling(custom_handler=custom_error_handler)
@router.post("/bms/{repository_id}/{bms_file_name}", response_model=ResponseBase)
async def migration_bms_file(
        repository_id: str,
        bms_file_name: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    response_data = await migration_controller.publish_bms_migration_task(db, repository_id, bms_file_name)
    return ResponseBase(data=None)


@dlx_project_handler.error_handling(custom_handler=custom_error_handler)
@router.get("/download/{repository_id}/")
async def download_migration_files(
        repository_id: str,
        bms_file_name: str = Query(None, alias="bms_file_name"),
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    try:
        zip_data = await migration_controller.download_migration_repo(
            db, repository_id, bms_file_name)
        
        # Create a filename for the zip
        filename = f"migration_{repository_id}.zip"
        
        # Return the zip file with appropriate headers
        return Response(
            content=zip_data,
            media_type="application/zip",
            headers={
                "Content-Disposition": f"attachment; filename={filename}",
                "Content-Type": "application/zip"
            }
        )
    except FileNotFoundError:
        return Response(
            content="Migration data not found",
            status_code=404
        )
    except Exception as e:
        logger.error(f"Error downloading migration files: {str(e)}")
        return Response(
            content="Internal server error",
            status_code=500
        )


@dlx_project_handler.error_handling(custom_handler=custom_error_handler)
@router.get("/structure/{repository_id}/", response_model=MigrationStructureResponse)
async def get_migration_structure(
        repository_id: str,
        bms_file_name: str = Query(..., alias="bms_file_name"),
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Get the folder structure of Java migration code for a specific COBOL file.
    
    Args:
        repository_id: ID of the repository
        bms_file_name: Name of the COBOL file
        db: MongoDB database instance
        current_user: Current authenticated user
        
    Returns:
        MigrationStructureResponse: Folder structure of the Java migration code
    """
    try:
        structure_data = await migration_controller.get_migration_structure(
            db, repository_id, bms_file_name
        )
        return MigrationStructureResponse(**structure_data)
    except FileNotFoundError:
        return Response(
            content="Migration structure not found",
            status_code=404
        )
    except Exception as e:
        logger.error(f"Error getting migration structure: {str(e)}")
        return Response(
            content="Internal server error",
            status_code=500
        )


@dlx_project_handler.error_handling(custom_handler=custom_error_handler)
@router.get("/file-content/{repository_id}/", response_model=FileContentResponse)
async def get_migration_file_content(
        repository_id: str,
        bms_file_name: str = Query(..., alias="bms_file_name"),
        file_path: str = Query(..., alias="file_path"),
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Get the content of a Java migration file based on its path.
    
    Args:
        repository_id: ID of the repository
        bms_file_name: Name of the COBOL file
        file_path: Path of the Java file to get content from
        db: MongoDB database instance
        current_user: Current authenticated user
        
    Returns:
        FileContentResponse: Content of the requested file
    """
    try:
        content_data = await migration_controller.get_migration_file_content(
            db, repository_id, bms_file_name, file_path
        )
        return FileContentResponse(**content_data)
    except FileNotFoundError as e:
        return Response(
            content=str(e),
            status_code=404
        )
    except Exception as e:
        logger.error(f"Error getting migration file content: {str(e)}")
        return Response(
            content="Internal server error",
            status_code=500
        )

