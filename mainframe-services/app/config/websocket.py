from typing import Dict, AsyncGenerator
from fastapi import FastAPI, WebSocket
from contextlib import asynccontextmanager
from loguru import logger

class WebSocketManager:
    _instance = None
    
    def __init__(self):
        if WebSocketManager._instance is not None:
            raise RuntimeError("Use WebSocketManager.get_instance() instead")
        self.active_connections: Dict[str, WebSocket] = {}
        WebSocketManager._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = WebSocketManager()
        return cls._instance

    async def connect(self, websocket: WebSocket, client_id: str):
        """Connect a client websocket."""
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"Client {client_id} connected. Total connections: {len(self.active_connections)}")

    def disconnect(self, client_id: str):
        """Disconnect a client websocket."""
        if client_id in self.active_connections:
            del self.active_connections[client_id]
            logger.info(f"Client {client_id} disconnected. Total connections: {len(self.active_connections)}")

    async def send_message(self, message: str, client_id: str):
        """Send message to a specific client."""
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(message)

    async def broadcast(self, message: str):
        """Broadcast message to all connected clients."""
        disconnected_clients = []
        for client_id, connection in self.active_connections.items():
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error sending to client {client_id}: {e}")
                disconnected_clients.append(client_id)
        
        # Clean up disconnected clients
        for client_id in disconnected_clients:
            self.disconnect(client_id)

def get_websocket_manager() -> WebSocketManager:
    """Dependency injection for WebSocket manager."""
    return WebSocketManager.get_instance()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    """Lifespan manager for FastAPI application."""
    # Initialize WebSocket Manager
    ws_manager = WebSocketManager.get_instance()
    logger.info("Initializing WebSocket Manager")
    
    yield {
        "ws_manager": ws_manager
    }
    
    # Cleanup on shutdown
    for client_id in list(ws_manager.active_connections.keys()):
        ws_manager.disconnect(client_id)
    logger.info("WebSocket Manager shutdown complete")
