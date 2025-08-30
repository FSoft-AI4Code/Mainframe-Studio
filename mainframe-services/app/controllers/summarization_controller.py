import json

import pika
from bson import ObjectId
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.rabbitmq import RabbitHelper
from app.controllers.migration_controller import get_linked_cobol
from app.utils.utils import get_blob_path

BMS_SUMMARIZATION_ROUTING_KEY: str = "summarization.bms"
SUMMARIZATION_EXCHANGE_NAME: str = "summarization_exchange"
BMS_SUMMARIZATION_QUEUE_NAME: str = "bms_summarization_queue"
COBOL_SCREEN_SUMMARIZATION_QUEUE_NAME: str = "cobol_screen_summarization_queue"
COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY: str = "summarization.screen.cobol"


class SummarizationPublisher:
    """
    This class is responsible for publishing tasks to RabbitMQ for BMS screen summarization.
    """

    def __init__(self, exchange_name: str, queue_name: str, routing_key: str):
        self.rabbit_helper = RabbitHelper(exchange_name, queue_name,
                                          routing_key, enable_consume=False, dlx_queue=False)

    def publish_task(self, body, exchange: str, routing_key: str, ):
        self.rabbit_helper.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


async def publish_bms_summarization_task(db: AsyncIOMotorDatabase, repository_id: str, file_name: str):
    """
    Publish a task to RabbitMQ to summarize a BMS screen.
    """
    try:
        path = await get_blob_path(db, file_name, repository_id, "BMS")
        linked_cobol = await get_linked_cobol(db, repository_id, file_name)

        bms_summarization_publisher = SummarizationPublisher(exchange_name=SUMMARIZATION_EXCHANGE_NAME,
                                                             queue_name=BMS_SUMMARIZATION_QUEUE_NAME,
                                                             routing_key=BMS_SUMMARIZATION_ROUTING_KEY)

        for cobol_file_name in linked_cobol:
            send_summary_message(bms_summarization_publisher, repository_id, file_name, cobol_file_name, path)

        logger.info(f"Published BMS summarization task for {repository_id}/{file_name}")

        # Update status of repo
        db.entry_points.update_one(
            {"repository_id": ObjectId(repository_id), "label": "BMS", "name": file_name},
            {"$set": {"status": "summarizing"}}
        )

        db.reverse_engineering.update_one(
            {"repository_id": ObjectId(repository_id), "type": "BMS", "name": file_name},
            {"$set": {"status": "summarizing"}}
        )

        return {"status": "success", "message": f"Task queued for {repository_id}/{file_name}"}

    except Exception as e:
        logger.error(f"Failed to publish BMS summarization task {e}")
        return {"status": "error", "message": str(e)}


def send_summary_message(publisher, repository_id, bms_file_name, cobol_file_name, path):
    data = {
        "repository_id": repository_id,
        "bms_file_name": bms_file_name,
        "cobol_file_name": cobol_file_name,
        "blob_path": path,
    }
    # Create the task message
    message = {
        "task_type": "bms_summary",
        "data": data
    }

    publisher.publish_task(json.dumps(message), exchange=SUMMARIZATION_EXCHANGE_NAME,
                           routing_key=BMS_SUMMARIZATION_ROUTING_KEY)


async def publish_cobol_screen_summarization_task(db: AsyncIOMotorDatabase, repository_id: str, file_name: str):
    """
    Publish a task to RabbitMQ to summarize a COBOL screen.
    """
    try:
        path = await get_blob_path(db, file_name, repository_id, "COBOL")

        cobol_summarization_publisher = SummarizationPublisher(exchange_name=SUMMARIZATION_EXCHANGE_NAME,
                                                               queue_name=COBOL_SCREEN_SUMMARIZATION_QUEUE_NAME,
                                                               routing_key=COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY)

        data = {
            "repository_id": repository_id,
            "file_name": file_name,
            "blob_path": path,
        }
        # Create the task message
        message = {
            "task_type": "cobol_screen_summary",
            "data": data
        }

        cobol_summarization_publisher.publish_task(json.dumps(message), exchange=SUMMARIZATION_EXCHANGE_NAME,
                                                   routing_key=COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY)

        logger.info(f"Published COBOL summarization task for {repository_id}/{file_name}")

        return {"status": "success", "message": f"Task queued for {repository_id}/{file_name}"}

    except Exception as e:
        logger.error("Failed to publish COBOL summarization task", error=str(e))
        return {"status": "error", "message": str(e)}
