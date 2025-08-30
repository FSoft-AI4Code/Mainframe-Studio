from app.config.database import get_database
from app.controllers import graph_controller
from app.schemas.common_schema import PaginationParams, ResponseBase
from app.schemas.deadcode_schema import DeadTotal, GetDeadcodeResponse
from app.security import auth
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorClient

router = APIRouter()


@router.put("/{repository_id}/files", response_model=ResponseBase[GetDeadcodeResponse])
async def get_deadcode(
    repository_id: str,
    db: AsyncIOMotorClient = Depends(get_database),
    pagination: PaginationParams = Depends(),
    current_user: auth.User = Depends(auth.get_current_user),
):
    data = await graph_controller.get_deadnodes(repository_id, db, pagination.skip, pagination.limit)

    return ResponseBase(data=GetDeadcodeResponse(
        dead_total=DeadTotal(
            dead=data["dead_total"]["dead"], total=data["dead_total"]["total"]),
        complexity_reduction_percentage=data["complexity_reduction_percentage"],
        files=data["files"],
        skip=pagination.skip,
        limit=pagination.limit
    ))
