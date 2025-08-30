"""
Redis client module for centralized Redis connection management.
This module provides a singleton Redis client that can be reused across the application.
"""
import redis
from redis.exceptions import ConnectionError, AuthenticationError
from loguru import logger
from config.settings import settings


def get_redis_client():
    """
    Get the Redis client instance.
    
    Returns:
        redis.Redis: A Redis client instance
    """
    return RedisClient.get_instance()


class RedisClient:
    """
    Singleton Redis client for reuse across the application.
    Provides centralized connection management and error handling.
    """
    _instance = None
    
    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of the Redis client.
        
        Returns:
            redis.Redis: The Redis client instance
        """
        if cls._instance is None:
            cls._instance = cls._create_client()
        return cls._instance
    
    @classmethod
    def _create_client(cls):
        """
        Create a new Redis client with proper configuration.
        
        Returns:
            redis.Redis: A new Redis client instance
        """
        # Connect to Redis - only include password if it's actually set
        redis_args = {
            "host": settings.REDIS_HOST,
            "port": settings.REDIS_PORT,
            "db": settings.REDIS_DB,
            "decode_responses": True
        }
        
        # Only add password if it's not None or empty
        if settings.REDIS_PASSWORD:
            redis_args["password"] = settings.REDIS_PASSWORD
        
        try:
            client = redis.Redis(**redis_args)
            # Test the connection
            client.ping()
            logger.info(f"Successfully connected to Redis at {settings.REDIS_HOST}:{settings.REDIS_PORT}")
            return client
        except AuthenticationError as e:
            # Handle the more specific exception first
            logger.error(f"Redis authentication error: {e}")
            raise
        except ConnectionError as e:
            # Handle the more general exception after
            logger.error(f"Redis connection error: {e}")
            raise
    
    @classmethod
    def reset_instance(cls):
        """
        Reset the singleton instance.
        Useful for testing or when connection parameters change.
        """
        if cls._instance is not None:
            try:
                cls._instance.close()
            except:
                pass
            cls._instance = None