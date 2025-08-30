import json
from fastapi import APIRouter, Depends, HTTPException

from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.settings import settings
from app.config.database import get_database
from app.constants.cobol import FileType
from app.controllers import reverse_controller
from app.controllers.assessment_controller import get_assessments_by_repository
from app.schemas.common_schema import ErrorResponse, ResponseBase
from app.schemas.inference_schema import SummarizationRequest, SummarizationResponse, ModernizationRequest, ModernizationResponse
from app.security import auth
from app.tasks.utils import produce_rpc_task, produce_summarization_task_mq


router = APIRouter()

@router.post("/summarizations", response_model=ResponseBase[SummarizationResponse])
async def create_summarization(
    request: SummarizationRequest,
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    if request.type == FileType.COBOL.value:
        reverse = await reverse_controller.get_reverse_engineering_report(
            db, 
            repository_id=request.repository_id,
            type=request.type,
            name=request.name
        )
        if reverse is None:
            raise HTTPException(
                status_code=406,
                detail=ErrorResponse(
                    message="Reverse report need to be generated for this file first.",
                    error_code="REVERSE_REPORTS_NOT_FOUND"
                )
            )
        
        produce_summarization_task_mq(request.repository_id, request.type, request.name)
        
        reverse = await reverse_controller.get_reverse_engineering_report(
            db, 
            repository_id=request.repository_id,
            type=request.type,
            name=request.name
        )

        summarization = (reverse.model_dump()
                         .get("output", {})
                         .get("processing_logic", {})
                         .get("paragraph_level", {}))

        return ResponseBase(data=SummarizationResponse(
            summarization=summarization
        ))
    else:
        raise HTTPException(
            status_code=406,
            detail=ErrorResponse(
                message="Getting summarization for this file type is not supported.",
                error_code="SUMMARIZATION_NOT_SUPPORTED"
            ).model_dump()
        )
    
@router.post("/modernization", response_model=ResponseBase[ModernizationResponse])
async def modernize(
    request: ModernizationRequest,
    db: AsyncIOMotorDatabase = Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    if request.type != FileType.BMS:
        return ErrorResponse(
            message="Getting modernization for this file type is not supported.",
            error_code="MODERNIZATION_NOT_SUPPORTED"
        ).model_dump()
    else:
        response = produce_rpc_task(
            "modernize_bms",
            {
                "repository_id": request.repository_id,
                "name": request.name
            },
            "modernize.bms",
            "bms_modernization_response_queue",
            "modernize.bms.response"
        )        
        response = json.loads(response.decode('utf-8'))
        if response.get("status") != "success":
            raise HTTPException(status_code=400, detail=response.get("message", "Modernization failed"))
        else:
            return ResponseBase(
                success=True,
                message="Modernization request sent successfully.",
                data=ModernizationResponse(
                    url=f"{settings.AZURE_WEB_DEPLOYMENT_URL}/{request.repository_id}/modernization/{request.name}.html"
                )
            )