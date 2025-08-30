import structlog

from config.settings import settings
from tasks.cobol_unisys_parser_task import CobolUnisysParserTask

from ..base_consumer import BaseConsumer

logger = structlog.get_logger()


class CobolUnisysParserConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(
            settings.QUEUE_CONFIGS["cobol_unisys_tasks"],
            response_queue_config=settings.QUEUE_CONFIGS["cobol_unisys_response_tasks"],
        )
        self.task_factory.register_task("parse_cobol_unisys", CobolUnisysParserTask)

    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)
