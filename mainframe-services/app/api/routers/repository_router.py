from typing import List, Optional

import pandas as pd
from bson import ObjectId
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from fastapi import Query, Path
from fastapi.responses import StreamingResponse
from fastapi import Query
from git import GitCommandError, Repo
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.database import get_database
from app.constants.cobol import FileType
from app.controllers import graph_controller, project_controller, repository_controller, reverse_controller
from app.models.repository import Repository
from app.schemas.common_schema import (
    ErrorResponse,
    PaginationParams,
    ResponseBase
)
from app.schemas.database_crud_schema import DatabaseTableDescriptor
from app.schemas.graph_schema import (
    CreateGraphResponse,
    DeleteGraphResponse,
    EntryPointCriticality,
    GetEntrypointsResponse,
    GetGraphResponse, GetDetailDependencyEntryPoint, EntryPoint, GetStatusEntryPoint,
)
from app.schemas.repository_schema import (
    CreateParsedDataResponse,
    GetRepositoriesResponse,
    GetRepositoryByProjectResponse,
    GetRepositoryResponse,
    RepositoryCreate,
    RepositoryCreateResponse,
    UpdateRepositoryRequest,
    GetFilesByRepositoryResponse,
    GetFileContentResponse,
)
from app.security import auth
from app.worker import queue
from app.constants.cobol import FileType

router = APIRouter()


@router.post("/", response_model=ResponseBase[RepositoryCreateResponse])
async def create_repository(
        repository: RepositoryCreate,
        background_tasks: BackgroundTasks,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    # Check project access first
    await project_controller.check_project_access(
        db, repository.project_id, str(current_user.id)
    )

    logger.info(f"Received repository: {repository}")
    if not repository.url:
        raise HTTPException(status_code=400, detail="Bad Request: Missing URL")

    # Create repository model first
    repository_model = Repository(
        id=ObjectId(),
        name=repository.name,
        description=repository.description,
        url=repository.url,
        project_id=repository.project_id,
        token=repository.token,
        system_type=repository.system_type,
    )
    print(repository_model)
    try:
        # Try to clone the repository first to validate
        logger.info(f"Cloning repository from URL: {repository.url}")
        git_repo = Repo.clone_from(
            repository.url.replace("https://", f"https://{repository.token}@"),
            f"tmp/{repository_model.id}",
        )

        # If clone succeeds, create repository in DB
        repo = await repository_controller.create_repository(
            db=db, repository=repository_model
        )

        # Add background task for processing
        background_tasks.add_task(
            repository_controller.process_repository, db, git_repo, repo
        )

        return ResponseBase(data=repo)

    except GitCommandError as e:
        logger.error(f"Git clone failed: {e}")
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message=f"Repository {repository.url} or token was not valid",
                error_code="INVALID_REPOSITORY",
            ).model_dump(),
        )
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(
            status_code=400,
            detail=f"Bad Request: {str(e)}"
        ) from e


@router.get("/{repository_id}/files", response_model=ResponseBase[GetFilesByRepositoryResponse])
async def read_files_by_repository(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        page_number: Optional[int] = Query(1, alias="page_number"),
        page_limit: Optional[int] = Query(100, alias="page_limit"),
        current_user: auth.User = Depends(auth.get_current_user)
):
    response_data = await repository_controller.get_files_by_repository(db, repository_id, page_number, page_limit)
    return ResponseBase(data=response_data)


@router.get("/{repository_id}/files/{file_type}/{file_name}", response_model=ResponseBase[GetFileContentResponse])
async def read_file_by_blob_path(
        repository_id: str,
        file_type: str,
        file_name: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    response_data = await repository_controller.get_file_by_blob_path(db, repository_id, file_type, file_name)
    return ResponseBase(data=response_data)


@router.get("/{repository_id}", response_model=ResponseBase[GetRepositoryResponse])
async def read_repository(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.check_repository_project_access(
        db, repository_id, str(current_user.id)
    )
    return ResponseBase(data=repository)


@router.get("/", response_model=ResponseBase[GetRepositoriesResponse])
async def read_repositories(
        pagination: PaginationParams = Depends(),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repositories, total = await repository_controller.get_repositories(
        db, user_id=str(current_user.id), skip=pagination.skip, limit=pagination.limit
    )

    return ResponseBase(
        data={
            "repositories": repositories,
            "total": total,
            "skip": pagination.skip,
            "limit": pagination.limit,
        }
    )


@router.get(
    "/project/{project_id}", response_model=ResponseBase[GetRepositoryByProjectResponse]
)
async def read_repository_by_project(
        project_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.get_repository_by_project(
        db, project_id=project_id
    )
    if repository is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Repository not found", error_code="REPOSITORY_NOT_FOUND"
            ).model_dump(),
        )
    return ResponseBase(data=repository)


@router.put("/{repository_id}", response_model=ResponseBase[dict])
async def update_repository(
        repository_id: str,
        repository: UpdateRepositoryRequest,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    # Check project access with owner role
    await repository_controller.check_repository_project_access(
        db, repository_id, str(current_user.id), required_role="owner"
    )
    # Get only the fields that were provided
    update_data = repository.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=400,
            detail=ErrorResponse(
                message="No fields to update", error_code="NO_UPDATES"
            ).model_dump(),
        )

    # Update in database
    result = await repository_controller.update_repository(
        db, repository_id=repository_id, update_data=update_data
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Repository not found", error_code="REPOSITORY_NOT_FOUND"
            ).model_dump(),
        )

    return ResponseBase(data=result)


@router.delete("/{repository_id}", response_model=ResponseBase[DeleteGraphResponse])
async def delete_repository(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    # Check project access with owner role
    await repository_controller.check_repository_project_access(
        db, repository_id, str(current_user.id), required_role="owner"
    )
    """Delete a repository."""
    success = await repository_controller.delete_repository(
        db, repository_id=repository_id
    )
    if not success:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Repository not found", error_code="REPOSITORY_NOT_FOUND"
            ).model_dump(),
        )
    return ResponseBase(
        data=DeleteGraphResponse(
            message=f"Repository {repository_id} successfully deleted"
        )
    )


@router.post(
    "/{repository_id}/parsed_data",
    response_model=ResponseBase[CreateParsedDataResponse],
)
async def create_parsed_data(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.check_repository_project_access(
        db, repository_id, str(current_user.id)
    )
    repository = await repository_controller.get_repository(
        db, repository_id=repository_id
    )
    if repository is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Repository not found", error_code="REPOSITORY_NOT_FOUND"
            ).model_dump(),
        )

    if repository.status in ["classified", "parsed", "assessed"]:
        await queue.enqueue("parse_repo", repo_id=repository_id, timeout=10000)
        return ResponseBase(
            data={
                "id": repository.id,
                "status": repository.status,
                "message": "Parsing initiated",
            }
        )

    raise HTTPException(
        status_code=202,
        detail=ErrorResponse(
            message="Repository is being uploaded, please wait",
            error_code="REPOSITORY_UPLOADING",
        ).model_dump(),
    )


@router.post(
    "/{repository_id}/dependency_graph",
    response_model=ResponseBase[CreateGraphResponse],
)
async def create_graph(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    # Check if the repository exists
    repository = await repository_controller.get_repository(
        db=db, repository_id=repository_id
    )
    if repository is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    graph = await graph_controller.create_graph(db=db, repository_id=repository_id)
    return ResponseBase(data=CreateGraphResponse(graph=graph))


@router.get(
    "/{repository_id}/entrypoints", response_model=ResponseBase[GetEntrypointsResponse]
)
async def get_entrypoints(
        repository_id: str,
        pagination: PaginationParams = Depends(),
        complexity_filter: Optional[int] = Query(None, alias="complexity_filter"),
        loc_filter: Optional[int] = Query(None, alias="loc_filter"),
        type_filter: Optional[FileType] = Query(default=None),
        number_of_files_filter: Optional[int] = Query(None, alias="number_of_files_filter"),
        criticality_filter: Optional[EntryPointCriticality] = Query(default=None),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.get_repository(
        db=db, repository_id=repository_id
    )
    if repository is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    entry_points, total = await graph_controller.get_entrypoints(
        db=db, repository_id=repository_id, skip=pagination.skip, limit=pagination.limit,
        complexity_filter=complexity_filter,
        loc_filter=loc_filter,
        number_of_files_filter=number_of_files_filter,
        criticality_filter=criticality_filter,
        type_filter=type_filter
    )
    return ResponseBase(
        data={
            "entry_points": entry_points,
            "total": total,
            "skip": pagination.skip,
            "limit": pagination.limit,
        }
    )

@router.get("/{repository_id}/crud", response_model=ResponseBase[List[DatabaseTableDescriptor]])
async def get_crud(repository_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    crud = await reverse_controller.get_crud(
        db=db, repository_id=repository_id
    )
    return ResponseBase(data=crud)


@router.get(
    "/{repository_id}/dependency_graph", response_model=ResponseBase[GetGraphResponse]
)
async def get_graph(
        repository_id: str,
        entrypoint_ids: Optional[List[str]] = Query(default=None),
        db: AsyncIOMotorClient = Depends(get_database),
        node_limit: Optional[int] = Query(1000, alias="node_limit"),
        complexity_filter: Optional[int] = Query(None, alias="complexity_filter"),
        loc_filter: Optional[int] = Query(None, alias="loc_filter"),
        nof_filter: Optional[int] = Query(None, alias="nof_filter"),
        criticality_filter: Optional[List[EntryPointCriticality]] = Query(
            default=None, alias="criticality_filter"
        ),
        page_number: Optional[int] = Query(1, alias="page_number"),
        page_limit: Optional[int] = Query(100, alias="page_limit"),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.get_repository(
        db=db, repository_id=repository_id
    )
    if not repository:
        raise HTTPException(status_code=404, detail="Repository not found")

    graph = await graph_controller.get_graph(
        db=db,
        repository_id=repository_id,
        entrypoint_ids=entrypoint_ids,
        node_limit=node_limit,
        complexity_filter=complexity_filter,
        loc_filter=loc_filter,
        nof_filter=nof_filter,
        criticality_filter=criticality_filter,
        page_number=page_number,
        page_limit=page_limit,
    )
    return ResponseBase(data=GetGraphResponse(graph=graph))


@router.get(
    "/{repository_id}/dependency_graph/detail",
    response_model=ResponseBase[GetDetailDependencyEntryPoint]
)
async def get_detail_dependency_entry_point(
        repository_id: str,
        entrypoint_id: str = Query(None, alias="id"),
        refer_id: str = Query(None, alias="refer_id"),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.get_repository(
        db=db, repository_id=repository_id
    )
    if repository is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    result = await graph_controller.get_detail_dependency_entry_point(
        db=db, repository_id=repository_id, entrypoint_id=entrypoint_id, refer_id=refer_id
    )
    return ResponseBase(data=result)


@router.delete(
    "/{repository_id}/dependency_graph",
    response_model=ResponseBase[DeleteGraphResponse],
)
async def delete_graph(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    repository = await repository_controller.get_repository(
        db=db, repository_id=repository_id
    )
    if repository is None:
        raise HTTPException(status_code=404, detail="Repository not found")
    result = await graph_controller.delete_graph(db=db, repository_id=repository_id)
    return ResponseBase(data=DeleteGraphResponse(message=result["message"]))


@router.post("/{repository_id}/reverse_engineering")
async def create_reverse_engineering(
        repository_id: str,
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    db_repository = await repository_controller.get_repository(
        db, repository_id=repository_id
    )
    if db_repository is None:
        raise HTTPException(status_code=404, detail="Repository not found")

    await queue.enqueue("reverse_bmss", repo_id=repository_id, timeout=10000)
    # await queue.enqueue("reverse_jcl", repo_id=repository_id, timeout=10000)
    await queue.enqueue("reverse_cpy", repo_id=repository_id, timeout=10000)

    blob_stream = repository_controller.get_parsed_csv(repository_id)
    df = pd.read_csv(
        blob_stream,
        escapechar="\\",
        encoding="utf-8",
        on_bad_lines="warn",
    )

    for _, row in df.iterrows():
        match row["label"]:
            case "COBOL":
                await queue.enqueue(
                    "reverse_cobol",
                    blob_path=row["path"],
                    parsed_data=row["parsed_data"],
                    timeout=10000,
                )
            case "JCL_IBM":
                await queue.enqueue(
                    "reverse_jcl",
                    blob_path=row["path"],
                    parsed_data=row["parsed_data"],
                    timeout=10000,
                )

    return db_repository


# TODO: Implement the following endpoint. Get all parsed data of repo. From azure storage or mongodb all blobs in repo.
# @router.get("/{repository_id}/parsed_data/")
# async def create_parsed_data(
#     repository_id: str,
#     db: AsyncIOMotorClient = Depends(get_database),
#     current_user: auth.User = Depends(auth.get_current_user)
# ):
#     pass


# TODO: Implement the following endpoint. Get from mongodb the parsed data by blob_id.
# @router.get("/{repository_id}/parsed_data/{blob_id}")
# async def create_parsed_data(
#     repository_id: str,
#     blob_id: str,
#     db: AsyncIOMotorClient = Depends(get_database),
#     current_user: auth.User = Depends(auth.get_current_user)
# ):
#     pass


@router.get(
    "/{repository_id}/source-stats",
    summary="Generate Source Code Statistics Report",
    description="""
    Generate an Excel report containing source code statistics for a repository.
    
    The report includes:
    - Type: Category of source code (COBOL, CPY, BMS, etc.)
    - NOF: Number of Files
    - LOC: Lines of Code
    
    Data is aggregated from the assessments collection in MongoDB.
    
    Returns:
    - Excel file (.xlsx) as a downloadable attachment
    - Filename includes timestamp for uniqueness
    
    Raises:
    - 404: If no assessments are found for the repository
    - 500: For any other server errors
    """,
    response_description="Excel file containing source code statistics"
)
async def generate_source_stats_report(
        repository_id: str = Path(..., description="The ID of the repository to generate the report for"),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user)
):
    """
    Generate a source code statistics report for a given repository.

    Args:
        repository_id (str): The ID of the repository to generate the report for
        db (AsyncIOMotorClient): MongoDB database connection
        current_user (auth.User): Currently authenticated user

    Returns:
        StreamingResponse: Excel file as a downloadable attachment

    Raises:
        HTTPException: If repository_id is invalid or no assessments are found
    """
    # Check repository access
    await repository_controller.check_repository_project_access(
        db, repository_id, str(current_user.id)
    )

    # Generate report using controller
    output, filename = await repository_controller.generate_source_stats_report(db, repository_id)

    # Return the Excel file as a streaming response
    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.get(
    "/{repository_id}/entrypoints/{name}",
    response_model=ResponseBase[GetStatusEntryPoint]
)
async def get_entrypoint_details(
        repository_id: str,
        name: str,
        label: FileType = Query(..., description="Label of the entrypoint"),
        db: AsyncIOMotorClient = Depends(get_database),
        current_user: auth.User = Depends(auth.get_current_user),
):
    """
    Get detailed information about a specific entrypoint by repository_id, name, and label.
    
    Args:
        repository_id: ID of the repository
        name: Name of the entrypoint
        label: Label/type of the entrypoint (e.g. COBOL, JCL_IBM, BMS)
    """
    repository = await repository_controller.get_repository(
        db=db, repository_id=repository_id
    )
    if repository is None:
        raise HTTPException(status_code=404, detail="Repository not found")

    # Find the entrypoint
    entrypoint = await db.entry_points.find_one({
        "repository_id": ObjectId(repository_id),
        "name": name,
        "label": label.value
    })

    if not entrypoint:
        raise HTTPException(
            status_code=404,
            detail=f"Entrypoint with name {name} and label {label.value} not found"
        )

    return ResponseBase(data=GetStatusEntryPoint(
        entry_point=EntryPoint(**entrypoint),
    ))
