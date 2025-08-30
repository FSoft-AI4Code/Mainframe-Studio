from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
import pandas as pd
from io import BytesIO
from datetime import datetime

from app.config.database import get_database
from app.controllers import project_controller
from app.decorators.error_handling import DLXErrorHandler
from app.models.project import Project
from app.schemas.common_schema import ResponseBase, PaginationParams
from app.schemas.project_schema import (
    ProjectCreate,
    ProjectCreateResponse,
    GetProjectResponse,
    GetProjectsResponse,
    UpdateProjectRequest,
    UpdateProjectResponse,
    DeleteProjectResponse
)
from app.security import auth

router = APIRouter()

dlx_project_handler = DLXErrorHandler(
    exchange="dlx_exchange",
    queue_name="dlx_project_queue",
    routing_key="dlq_project_key"
)


def custom_error_handler(exc):
    logger.error(f"Custom project handler - captured exception: {exc}")


@router.post("/", response_model=ResponseBase[ProjectCreateResponse])
@dlx_project_handler.error_handling(custom_handler=custom_error_handler)
async def create_project(
        project: ProjectCreate,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    project_model = Project(
        name=project.name,
        description=project.description,
        user_id=current_user.id
    )
    result = await project_controller.create_project(
        db=db, project=project_model
    )
    # Add project to user's permissions
    await db.users.update_one(
        {"_id": current_user.id},
        {"$push": {"permissions": {"project_id": result.id, "role": "owner"}}}
    )
    return ResponseBase(data=result)


@router.get("/{project_id}", response_model=ResponseBase[GetProjectResponse])
async def read_project(
        project_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    project, _ = await project_controller.check_project_access(db, project_id, str(current_user.id))
    return ResponseBase(data=project)


@router.get("/", response_model=ResponseBase[GetProjectsResponse])
async def read_projects(
        pagination: PaginationParams = Depends(),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    projects, total = await project_controller.get_projects(
        db,
        user_id=str(current_user.id),
        skip=pagination.skip,
        limit=pagination.limit
    )

    return ResponseBase(data={
        "projects": projects,
        "total": total,
        "skip": pagination.skip,
        "limit": pagination.limit
    })


@router.put("/{project_id}", response_model=ResponseBase[UpdateProjectResponse])
async def update_project(
        project_id: str,
        project: UpdateProjectRequest,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    # Check for owner/admin permission
    await project_controller.check_project_access(db, project_id, str(current_user.id), required_role="owner")

    updated_project = await project_controller.update_project(
        db, project_id=project_id, project=project
    )
    return ResponseBase(data=updated_project)


@router.delete("/{project_id}", response_model=ResponseBase[DeleteProjectResponse])
async def delete_project(
        project_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    # Check for owner permission
    await project_controller.check_project_access(db, project_id, str(current_user.id), required_role="owner")

    await project_controller.delete_project(db, project_id=project_id)
    return ResponseBase(
        data=DeleteProjectResponse(
            message=f"Project {project_id} successfully deleted"
        )
    )


@router.get("/{project_id}/repositories/excel")
async def generate_project_repositories_excel(
        project_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    try:
        # Check project access
        await project_controller.check_project_access(db, project_id, str(current_user.id))

        # Fetch repositories data for the specific project
        repositories = await db.repositories.find({"project_id": ObjectId(project_id)}).to_list(length=None)

        if not repositories:
            raise HTTPException(status_code=404, detail="No repositories found for this project")

        # Convert to DataFrame
        df = pd.DataFrame(repositories)

        # Create Excel file in memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Repositories', index=False)

        output.seek(0)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"project_{project_id}_repositories_{timestamp}.xlsx"

        # Return Excel file as downloadable response
        return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={
                "Content-Disposition": f"attachment; filename={filename}"
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
