import subprocess
from contextlib import asynccontextmanager
from fastapi import BackgroundTasks, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.routers import (
    assessment_router,
    auth_router,
    chat_router,
    complexity_router,
    dataset_assignment_router,
    deadcode_router,
    duplicate_file_router,
    inference_router,
    project_router,
    repository_router,
    reverse_router,
    user_router,
    summarization_router,
    migration_router,
    utility_router,
)
from app.config.nebula import get_nebula_connection
from app.config.database import get_database
from app.config.websocket import WebSocketManager
from app.config.settings import settings
from app.utils.queue import background_queue

logger.add("loguru.log")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Combined lifespan manager for both Nebula Graph connection and WebSocket manager.
    """
    # Initialize MongoDB connection
    db = await get_database()
    db.users.create_index({"permissions.project_id": 1})
    db.projects.create_index({"_id": 1})
    logger.info("MongoDB connection initialized.")
    # Initialize Nebula Graph connection
    # nebula_connection = get_nebula_connection()
    logger.info("Nebula connection pool initialized.")

    # Initialize WebSocket Manager
    ws_manager = WebSocketManager.get_instance()
    logger.info("WebSocket Manager initialized.")

    try:
        yield {
            # "nebula_connection": nebula_connection,
            "ws_manager": ws_manager
        }
    finally:
        # Cleanup on shutdown

        # Close Nebula connection
        # nebula_connection.close()
        logger.info("Nebula connection pool closed.")

        # Cleanup WebSocket connections
        for client_id in list(ws_manager.active_connections.keys()):
            ws_manager.disconnect(client_id)
        logger.info("WebSocket Manager shutdown complete.")


app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(project_router.router, prefix="/projects", tags=["Projects"])
app.include_router(
    repository_router.router, prefix="/repositories", tags=["Repositories"]
)
app.include_router(
    assessment_router.router, prefix="/assessments", tags=["Assessments"]
)
app.include_router(
    complexity_router.router, prefix="/complexities", tags=["Complexities"]
)
app.include_router(
    reverse_router.router, prefix="/reverse", tags=["Reverse Engineering"]
)
app.include_router(chat_router.router, prefix="/chat", tags=["Chat"])
app.include_router(deadcode_router.router, prefix="/deadcode", tags=["Deadcode"])
app.include_router(summarization_router.router, prefix="/summarization", tags=["Summarization"])
app.include_router(migration_router.router, prefix="/migration", tags=["Migration"])
app.include_router(inference_router.router, prefix="/inference", tags=["Inferences"])
app.include_router(duplicate_file_router.router, prefix="/duplicate-files", tags=["Duplicate Files"])

app.include_router(
    dataset_assignment_router.router, prefix="/datasets", tags=["Dataset Assignments"]
)
app.include_router(utility_router.router, prefix="/utilities", tags=["Utilities"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}


@app.on_event("startup")
async def startup_event():
    # You can add any startup logic here
    pass


@app.on_event("shutdown")
async def shutdown_event():
    # You can add any shutdown logic here
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
