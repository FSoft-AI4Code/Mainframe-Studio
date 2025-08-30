from typing import Callable
import pika
import json
from config.settings import settings
from .connection import RabbitMQConnection
from tasks.task_factory import TaskFactory
import structlog

logger = structlog.get_logger()

class Consumer:
    def __init__(self):
        self.connection = RabbitMQConnection()
        self.task_factory = TaskFactory()
        
    def callback(self, ch: pika.Channel, method: pika.spec.Basic.Deliver,
                properties: pika.spec.BasicProperties, body: bytes) -> None:
        try:
            message = json.loads(body)
            task_type = message.get('task_type')
            task_data = message.get('data', {})
            
            task = self.task_factory.create_task(task_type)
            result = task.execute(task_data)
            
            logger.info("Task executed successfully",
                       task_type=task_type,
                       result=result)
            
            ch.basic_ack(delivery_tag=method.delivery_tag)
            
        except Exception as e:
            logger.error("Error processing message",
                        error=str(e),
                        message=body)
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    
    def start_consuming(self) -> None:
        """Start consuming messages from the queue"""
        try:
            self.connection.connect()
            self.connection.channel.basic_qos(
                prefetch_count=settings.WORKER_PREFETCH_COUNT
            )
            
            self.connection.channel.basic_consume(
                queue=settings.QUEUE_NAME,
                on_message_callback=self.callback
            )
            
            logger.info("Started consuming messages",
                       queue=settings.QUEUE_NAME)
            
            self.connection.channel.start_consuming()
            
        except KeyboardInterrupt:
            self.connection.channel.stop_consuming()
            self.connection.close()
        except Exception as e:
            logger.error("Error in consumer", error=str(e))
            raise 