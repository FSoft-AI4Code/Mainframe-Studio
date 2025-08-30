from fastapi import APIRouter, Depends
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.database import get_database
from app.controllers import summarization_controller
from app.decorators.error_handling import DLXErrorHandler
from app.schemas.common_schema import ResponseBase
from app.schemas.summarization_schema import (
    Summarization
)
from app.security import auth

router = APIRouter()

dlx_project_handler = DLXErrorHandler(
    exchange="dlx_exchange",
    queue_name="dlx_summarization_queue",
    routing_key="dlq_summarization_key"
)


def custom_error_handler(exc):
    logger.error(f"Custom project handler - captured exception: {exc}")


@dlx_project_handler.error_handling(custom_handler=custom_error_handler)
@router.post("/bms/{repository_id}/files/{file_name}", response_model=ResponseBase[Summarization])
async def summarization_bms_file(
        repository_id: str,
        file_name: str,
        db: AsyncIOMotorDatabase = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    response_data = await summarization_controller.publish_bms_summarization_task(db, repository_id, file_name)
    return ResponseBase(data=None)
