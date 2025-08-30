from ..base_consumer import BaseConsumer
from config.settings import settings
from tasks.bms_modernization_task import BMSModernizationTask
import structlog

logger = structlog.get_logger()

class BMSModernizationConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["bms_modernization"],
                            response_queue_config=settings.QUEUE_CONFIGS["bms_modernization_response"])
        self.task_factory.register_task("modernize_bms", BMSModernizationTask)
    
    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing modernization message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)
