import pika
from typing import Optional, List
from config.settings import settings, QueueConfig
import structlog

logger = structlog.get_logger()

class RabbitMQConnection:
    def __init__(self, queue_configs: List[QueueConfig]):
        self.connection: Optional[pika.SelectConnection] = None
        self.channel: Optional[pika.Channel] = None
        self.queue_configs = queue_configs
        
    def connect(self) -> None:
        """Establish connection to RabbitMQ server"""
        try:
            credentials = pika.PlainCredentials(
                settings.RABBITMQ_USER,
                settings.RABBITMQ_PASSWORD
            )
            
            parameters = pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                virtual_host=settings.RABBITMQ_VHOST,
                credentials=credentials,
                heartbeat=settings.RABBITMQ_HEARTBEAT
            )
            
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            
            # Declare exchanges and queues for each configuration
            for config in self.queue_configs:
                self.channel.exchange_declare(
                    exchange=config.exchange,
                    exchange_type='topic',  # Changed to topic for more flexible routing
                    durable=True
                )
                
                self.channel.queue_declare(
                    queue=config.name,
                    durable=True
                )
                
                self.channel.queue_bind(
                    queue=config.name,
                    exchange=config.exchange,
                    routing_key=config.routing_key
                )
            
            logger.info("Successfully connected to RabbitMQ")
            
        except Exception as e:
            logger.error("Failed to connect to RabbitMQ", error=str(e))
            raise
            
    def close(self) -> None:
        """Close the connection"""
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            logger.info("RabbitMQ connection closed") 