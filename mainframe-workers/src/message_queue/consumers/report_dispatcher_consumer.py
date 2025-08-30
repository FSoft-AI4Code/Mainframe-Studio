from ..base_consumer import BaseConsumer
from config.settings import settings
from tasks.report_dispatcher_task import ReportDispatcherTask
import structlog

logger = structlog.get_logger()

class ReportDispatcherConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["report_dispatcher"])
        self.task_factory.register_task("dispatch_report", ReportDispatcherTask)
    
    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data)
