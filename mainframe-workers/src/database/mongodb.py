from pymongo import MongoClient
import structlog
from config.settings import settings

logger = structlog.get_logger()

_db = None

def get_database():
    """
    Returns a database instance, creating a new connection if one doesn't exist.
    Uses settings for configuration with authentication.
    """
    global _db
    if _db is not None:
        return _db

    try:
        # Get MongoDB connection details from settings
        mongo_host = settings.MONGODB_HOST
        mongo_port = settings.MONGODB_PORT
        mongo_user = settings.MONGODB_USER
        mongo_password = settings.MONGODB_PASSWORD
        db_name = settings.MONGODB_DB_NAME

        # Construct connection URL with authentication
        if mongo_user and mongo_password:
            mongo_url = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{db_name}?authSource=admin"
        else:
            logger.warning("MongoDB credentials not provided, attempting connection without authentication")
            mongo_url = f"mongodb://{mongo_host}:{mongo_port}/{db_name}"

        # Create client and connect to database
        client = MongoClient(mongo_url)
        _db = client[db_name]
        
        # Test connection
        client.admin.command('ping')
        logger.info("Successfully connected to MongoDB", database=db_name)
        
        return _db

    except Exception as e:
        logger.error("Failed to connect to MongoDB", error=str(e))
        raise 