from ..base_consumer import BaseConsumer
from config.settings import settings
from tasks.copybook_unisys_parser_task import CopybookUnisysParserTask
import structlog

logger = structlog.get_logger()

class CopybookUnisysParserConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["copybook_unisys_tasks"])
        self.task_factory.register_task("parse_copybook_unisys", CopybookUnisysParserTask)
    
    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)