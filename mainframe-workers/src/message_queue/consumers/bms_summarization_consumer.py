from ..base_consumer import BaseConsumer
from config.settings import settings
from tasks.bms_summarization import BMSSummarizationTask
import structlog

logger = structlog.get_logger()


class BMSSummarizationConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["bms_summarization"])
        self.task_factory.register_task("bms_summary", BMSSummarizationTask)

    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)