from ..base_consumer import BaseConsumer
from config.settings import settings
from tasks.cobol_summarization_task import CobolSummarizationTask
import structlog

logger = structlog.get_logger()

class CobolSummarizationConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(queue_config=settings.QUEUE_CONFIGS["cobol_summarization"], 
                         response_queue_config=settings.QUEUE_CONFIGS["cobol_summarization_response_tasks"])
        self.task_factory.register_task("summarize_cobol", CobolSummarizationTask)
    
    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)
