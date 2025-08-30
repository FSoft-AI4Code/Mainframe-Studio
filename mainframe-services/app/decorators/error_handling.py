import json
import traceback
import uuid
from functools import wraps
from inspect import iscoroutinefunction

import pika
from bson import ObjectId
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.rabbitmq import RabbitHelper


class ErrorMessageJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, AsyncIOMotorDatabase):
            return str(obj.name)  # Serialize database as its name
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return str(obj)


class DLXErrorHandler:
    def __init__(self, exchange: str, queue_name: str, routing_key: str):
        self.exchange = exchange
        self.routing_key = routing_key
        self.rabbit_helper = RabbitHelper(exchange, queue_name, routing_key, enable_consume=False, dlx_queue=True)

    def error_handling(self, custom_handler=None, re_raise=False):
        def decorator(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    self._handle_exception(e, args, kwargs)
                    if custom_handler:
                        custom_handler(e)
                    if re_raise:
                        raise

            @wraps(func)
            def sync_wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    self._handle_exception(e, args, kwargs)
                    if custom_handler:
                        custom_handler(e)
                    if re_raise:
                        raise

            return async_wrapper if iscoroutinefunction(func) else sync_wrapper

        return decorator

    def _handle_exception(self, exception, args, kwargs):
        """Internal method to handle exception and send to DLX."""
        error_message = {
            "error": str(exception),
            "traceback": traceback.format_exc(),
            "args": args,
            "kwargs": kwargs
        }

        serialized_message = json.dumps(
            error_message,
            cls=ErrorMessageJSONEncoder,
            ensure_ascii=False
        )

        properties = pika.BasicProperties(
            correlation_id=str(uuid.uuid4()),
            content_type='application/json',
            delivery_mode=2  # Persistent message
        )

        try:
            self.rabbit_helper.call(
                exchange=self.exchange,
                routing_key=self.routing_key,
                body=serialized_message,
                properties=properties,
                wait_response=False
            )
            logger.error(f"Error message sent to DLX: {error_message}")
        except Exception as send_error:
            logger.error(f"Failed to send error message to DLX: {send_error}")
