import json
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    WebSocket,
    WebSocketDisconnect,
    status,
)
from loguru import logger

from app.config.database import get_database
from app.config.websocket import get_websocket_manager
from app.controllers import chat_controller
from app.schemas.common_schema import ResponseBase, ErrorResponse
from app.schemas.chat_schema import (
    ChatCreate,
    ChatCreateResponse,
    MessageCreate,
    MessageConfig,
    WSMessageRequest,
    WSMessageResponse,
    WSErrorResponse,
    GetChatResponse,
)
from app.security import auth
from app.models.chat import Chat

router = APIRouter()


@router.post("/", response_model=ResponseBase[ChatCreateResponse])
async def create_chat(
    chat: ChatCreate,
    db=Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user),
):
    """Create a new chat."""
    # Convert ChatCreate schema to Chat model
    chat_model = Chat(
        project_id=chat.project_id,
        messages=chat.messages
    )
    
    chat_id = await chat_controller.create_chat(db=db, chat=chat_model)
    
    return ResponseBase(data=ChatCreateResponse(id=chat_id))


@router.get("/project/{project_id}", response_model=ResponseBase[GetChatResponse])
async def read_chat_by_project(
    project_id: str,
    db=Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    """Get the chat instance associated with a specific project."""
    chat = await chat_controller.get_chat_by_project(db, project_id)
    if chat is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Chat not found for this project",
                error_code="CHAT_NOT_FOUND"
            ).model_dump()
        )
    logger.info(f"Chat found: {chat}")
    return ResponseBase(data=chat)


@router.get("/{chat_id}", response_model=ResponseBase[GetChatResponse])
async def read_chat(
    chat_id: str,
    db=Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user)
):
    chat = await chat_controller.get_chat(db, chat_id)
    if chat is None:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Chat not found",
                error_code="CHAT_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(data=chat)


@router.websocket("/ws/{chat_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    chat_id: str,
    db=Depends(get_database),
    ws_manager=Depends(get_websocket_manager),
):
    try:
        # Authenticate user
        current_user = await auth.get_current_user_ws(websocket, db)

        # Accept connection and add to manager
        await ws_manager.connect(websocket, chat_id)

        try:
            while True:
                data = await websocket.receive_text()
                message_data = WSMessageRequest(**json.loads(data))
                message = MessageCreate(
                    repository_id=message_data.repository_id,
                    content=message_data.content,
                    sender=message_data.sender,
                    config=message_data.config or MessageConfig()
                )
 
                async for response in chat_controller.chat(db, chat_id, message):
                    await ws_manager.send_message(
                        WSMessageResponse(data=response).model_dump_json(), 
                        chat_id
                    )

        except WebSocketDisconnect:
            logger.info(f"Client disconnected: {chat_id}")
            ws_manager.disconnect(chat_id)
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            await ws_manager.send_message(
                WSErrorResponse(
                    message=str(e),
                    error_code="MESSAGE_PROCESSING_ERROR"
                ).model_dump_json(), 
                chat_id
            )
            ws_manager.disconnect(chat_id)

    except HTTPException as he:
        logger.error(f"Authentication error: {he.detail}")
        await websocket.send_json(
            WSErrorResponse(
                message="Authentication failed",
                error_code="AUTH_ERROR",
                details=he.detail
            ).model_dump()
        )


@router.delete("/{chat_id}", response_model=ResponseBase[bool])
async def delete_chat(
    chat_id: str,
    db=Depends(get_database),
    current_user: auth.User = Depends(auth.get_current_user),
):
    success = await chat_controller.delete_chat(db, chat_id=chat_id)
    if not success:
        raise HTTPException(
            status_code=404,
            detail=ErrorResponse(
                message="Chat not found",
                error_code="CHAT_NOT_FOUND"
            ).model_dump()
        )
    return ResponseBase(
        data=success,
        message="Chat successfully deleted"
    )
