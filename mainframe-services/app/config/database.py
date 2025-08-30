from motor.motor_asyncio import AsyncIOMotorClient
from loguru import logger
from app.config.settings import settings

# Create MongoDB client with full configuration
client = AsyncIOMotorClient(
    settings.MONGO_URI,
    serverSelectionTimeoutMS=5000
)

# Get database instance
database = client[settings.MONGO_DATABASE]


async def get_database():
    """
    Get database connection with connection verification.
    
    Returns:
        AsyncIOMotorDatabase if connection successful, None otherwise
    """
    try:
        # Verify connection is alive
        await client.server_info()
        return database
    except Exception as e:
        logger.error(f"Unable to connect to MongoDB server: {e}")
        logger.debug(f"Connection details: {settings.MONGO_HOST}:{settings.MONGO_PORT}")
        return None


async def close_database_connection():
    """Close database connection."""
    try:
        client.close()
        logger.info("MongoDB connection closed")
    except Exception as e:
        logger.error(f"Error closing MongoDB connection: {e}")
