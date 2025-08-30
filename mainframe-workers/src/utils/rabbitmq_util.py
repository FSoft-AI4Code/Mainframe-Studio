import json
import pika
from typing import Any, Dict, Optional
from loguru import logger
from config.settings import settings

# RabbitMQ connection parameters from settings
RABBITMQ_HOST = settings.RABBITMQ_HOST
RABBITMQ_PORT = settings.RABBITMQ_PORT
RABBITMQ_USER = settings.RABBITMQ_USER
RABBITMQ_PASSWORD = settings.RABBITMQ_PASSWORD
RABBITMQ_VHOST = settings.RABBITMQ_VHOST

PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME
COBOL_DISPATCHER_ROUTING_KEY = settings.COBOL_DISPATCHER_ROUTING_KEY
GRAPH_ROUTING_KEY = settings.GRAPH_ROUTING_KEY

_connection: Optional[pika.BlockingConnection] = None
_channel: Optional[pika.channel.Channel] = None

def get_connection() -> pika.BlockingConnection:
    """
    Get or create a RabbitMQ connection
    """
    global _connection
    
    try:
        if _connection is None or _connection.is_closed:
            credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
            parameters = pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=RABBITMQ_PORT,
                virtual_host=RABBITMQ_VHOST,
                credentials=credentials
            )
            _connection = pika.BlockingConnection(parameters)
            logger.info("Created new RabbitMQ connection")
    except Exception as e:
        logger.error(f"Failed to create RabbitMQ connection: {str(e)}")
        raise

    return _connection

def get_channel(exchange_name: str = None, 
                exchange_type: str = "direct",
                queue_name: str = None,
                routing_key: str = None,
                durable: bool = True) -> pika.channel.Channel:
    """
    Get or create a RabbitMQ channel with optional exchange and queue declarations
    
    Args:
        exchange_name (str, optional): Name of the exchange to declare
        exchange_type (str, optional): Type of exchange (direct, fanout, topic, headers)
        queue_name (str, optional): Name of the queue to declare
        routing_key (str, optional): Routing key for binding queue to exchange
        durable (bool, optional): Whether the exchange and queue should be durable
        
    Returns:
        pika.channel.Channel: The RabbitMQ channel
    """
    global _channel
    
    try:
        if _channel is None or _channel.is_closed:
            connection = get_connection()
            _channel = connection.channel()
            logger.info("Created new RabbitMQ channel")
            
        # Declare exchange if specified
        if exchange_name:
            _channel.exchange_declare(
                exchange=exchange_name,
                exchange_type=exchange_type,
                durable=durable
            )
            logger.info(f"Declared exchange: {exchange_name}")
            
        # Declare queue and bind if specified
        if queue_name:
            _channel.queue_declare(queue=queue_name, durable=durable)
            logger.info(f"Declared queue: {queue_name}")
            
            # Bind queue to exchange if both are specified
            if exchange_name and routing_key:
                _channel.queue_bind(
                    exchange=exchange_name,
                    queue=queue_name,
                    routing_key=routing_key
                )
                logger.info(f"Bound queue {queue_name} to exchange {exchange_name} with routing key {routing_key}")
            
    except Exception as e:
        logger.error(f"Failed to create RabbitMQ channel: {str(e)}")
        raise

    return _channel

def close_connection():
    """
    Close the RabbitMQ connection if it exists
    """
    global _connection, _channel
    
    try:
        if _channel is not None and not _channel.is_closed:
            _channel.close()
            _channel = None
            
        if _connection is not None and not _connection.is_closed:
            _connection.close()
            _connection = None
            
        logger.info("Closed RabbitMQ connection and channel")
    except Exception as e:
        logger.error(f"Error closing RabbitMQ connection: {str(e)}") 


def produce_task(routing_key: str, exchange: str, task_type: str, data: Dict[str, Any]):
    task_data = {
        "task_type": task_type,
        "data": data
    }
    channel = get_channel()
    channel.basic_publish(
        exchange=exchange,
        routing_key=routing_key,
        body=json.dumps(task_data)
    )


def produce_dispatch_task(system_type: str, repository_id: str):
    produce_task(COBOL_DISPATCHER_ROUTING_KEY, PARSER_EXCHANGE_NAME, "dispatch_cobol", {
        "system_type": system_type,
        "repository_id": repository_id,
    })


def produce_graph_task(repository_id: str, name: str, label: str):
    produce_task(
        GRAPH_ROUTING_KEY,
        PARSER_EXCHANGE_NAME,
        "parse_graph",
        {"repository_id": repository_id, "name": name, "label": label},
    )
