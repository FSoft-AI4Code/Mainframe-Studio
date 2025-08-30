import json
from abc import ABC, abstractmethod
from traceback import print_exc

import pika
import structlog
from loguru import logger
from pika import spec
from pika.channel import Channel

from config.settings import QueueConfig, settings
from tasks.task_factory import TaskFactory

from .connection import RabbitMQConnection

logger = structlog.get_logger()


class BaseConsumer(ABC):
    def __init__(
        self, queue_config: QueueConfig, response_queue_config: QueueConfig = None
    ):
        self.queue_config = queue_config
        queue_configs = [queue_config]
        if response_queue_config is not None:
            self.response_queue_config = response_queue_config
            queue_configs.append(response_queue_config)
        self.connection = RabbitMQConnection(queue_configs)
        self.task_factory = TaskFactory()

    @abstractmethod
    def process_message(self, task_type: str, task_data: dict) -> dict:
        """Process the message according to consumer type"""
        pass

    def callback(
        self,
        ch: Channel,
        method: spec.Basic.Deliver,
        properties: spec.BasicProperties,
        body: bytes,
    ) -> None:
        try:
            message = json.loads(body)
            task_type = message.get("task_type")
            task_data = message.get("data", {})

            result = self.process_message(task_type, task_data)

            if result.get("requeue", False):

                # Headers are initialized in requeue_message
                if not properties.headers:
                    properties.headers = {}

                retry_count = properties.headers.get(settings.RETRY_COUNT_HEADER, 0)
                retry_count += 1

                logger.warning(
                    "Task will be requeued after error",
                    error=result.get("message"),
                    retry_count=retry_count,
                    task_type=task_type,
                    delay_seconds=self.queue_config.requeue_delay_time_in_seconds,
                )

                # Cannot use basic_nack with requeue=True, it cannot track number of retries and does not have delay mechanism
                # Instead, publish to a delay queue with a TTL and DLX
                self.requeue_message(
                    ch,
                    method,
                    properties,
                    body,
                    retry_count,
                    "Task needs to be requeued",
                    delay_seconds=self.queue_config.requeue_delay_time_in_seconds,
                )

                return

            logger.info(
                "Task executed successfully", task_type=task_type, result=result
            )

            if (
                properties.reply_to is not None
                and properties.correlation_id is not None
            ):
                ch.basic_publish(
                    exchange=self.response_queue_config.exchange,
                    routing_key=self.response_queue_config.routing_key,
                    properties=pika.BasicProperties(
                        correlation_id=properties.correlation_id, delivery_mode=2
                    ),
                    body=json.dumps(result),
                )

            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            logger.error("Error processing message", error=str(e), message=body)
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def requeue_message(
        self,
        ch: Channel,
        method: spec.Basic.Deliver,
        properties: spec.BasicProperties,
        body: bytes,
        retry_count: int,
        error_info: str,
        delay_seconds: int = 1,
    ) -> None:
        """
        Requeue a message with a configurable delay using RabbitMQ's dead letter exchange pattern.

        This method implements a delayed retry mechanism:
        1. The original message is acknowledged (removed from the queue)
        2. A copy with updated retry information is placed in a temporary delay queue
        3. The delay queue has a message TTL and dead letter configuration
        4. When the TTL expires, RabbitMQ automatically moves the message to the original queue

        Args:
            ch: The RabbitMQ channel object
            method: Details about the delivery including the delivery tag
            properties: Message properties including headers and correlation ID
            body: The message body as bytes
            retry_count: The incremented retry count to store in message headers
            error_info: Information about the error that caused the requeue
            delay_seconds: How long to delay before reprocessing (in seconds), defaults to 1

        Note:
            This method creates a delay queue with format "{original_queue}.delay" with:
            - A TTL equal to delay_seconds * 1000 (milliseconds)
            - A dead letter exchange pointing to the original exchange
            - A dead letter routing key pointing to the original queue

        Warning:
            If the delay queue already exists with different TTL, this will cause
            a PRECONDITION_FAILED error. For different delays, use unique queue names.
        """
        # First ack the original message
        ch.basic_ack(delivery_tag=method.delivery_tag)

        # Update headers with retry count
        headers = properties.headers.copy() if properties.headers else {}
        headers[settings.RETRY_COUNT_HEADER] = retry_count
        headers[settings.LAST_ERROR_HEADER] = error_info
        headers[settings.ORIGINAL_ROUTING_KEY_HEADER] = self.queue_config.routing_key

        # Declare a delay queue for requeued messages
        delay_queue_name = f"{self.queue_config.name}{settings.DELAY_QUEUE_SUFFIX}.{self.queue_config.requeue_delay_time_in_seconds}"
        arguments = {
            settings.TTL_HEADER: delay_seconds * 1000,  # TTL in milliseconds
            settings.DLX_HEADER: self.queue_config.exchange,
            settings.DLX_ROUTING_KEY_HEADER: self.queue_config.routing_key,
        }
        ch.queue_declare(queue=delay_queue_name, durable=True, arguments=arguments)

        # Publish to the delay queue instead of original queue
        ch.basic_publish(
            exchange="",  # Use default exchange
            routing_key=delay_queue_name,  # Route directly to delay queue
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id,
                headers=headers,
                delivery_mode=2,  # persistent
            ),
            body=body,
        )

        logger.info(
            "Message requeued with delay",
            retry_count=retry_count,
            delay_seconds=delay_seconds,
            error=error_info,
        )

    def start_consuming(self) -> None:
        try:
            self.connection.connect()
            self.connection.channel.basic_qos(
                prefetch_count=settings.WORKER_PREFETCH_COUNT
            )

            self.connection.channel.basic_consume(
                queue=self.queue_config.name, on_message_callback=self.callback
            )

            logger.info(f"Started consuming messages for {self.queue_config.name}")

            self.connection.channel.start_consuming()

        except KeyboardInterrupt:
            self.connection.channel.stop_consuming()
            self.connection.close()
        except Exception as e:
            print_exc()
            logger.error("Error in consumer", error=str(e))
            raise
