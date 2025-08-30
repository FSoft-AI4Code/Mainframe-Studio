import structlog

from config.settings import settings
from tasks.bat_parser_task import BatchParserTask

from ..base_consumer import BaseConsumer

logger = structlog.get_logger()


class BatchParserConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["bat_tasks"])
        self.task_factory.register_task("parse_bat", BatchParserTask)

    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message",
                    task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)
