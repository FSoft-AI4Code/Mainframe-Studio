from ..base_consumer import BaseConsumer
from config.settings import settings
import structlog

logger = structlog.get_logger()

class NotificationConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["notification_tasks"])
    
    def process_message(self, task_type: str, task_data: dict) -> dict:
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data) 