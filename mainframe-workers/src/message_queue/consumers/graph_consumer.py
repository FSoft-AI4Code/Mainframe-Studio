import structlog

from config.settings import settings
from tasks.graph_task import GraphTask

from ..base_consumer import BaseConsumer

logger = structlog.get_logger()


class GraphConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["graph_tasks"])
        self.task_factory.register_task("parse_graph", GraphTask)

    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message",
                    task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)
