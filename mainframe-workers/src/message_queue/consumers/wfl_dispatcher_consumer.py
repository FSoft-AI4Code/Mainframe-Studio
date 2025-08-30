from ..base_consumer import BaseConsumer
from config.settings import settings
from tasks.wfl_dispatcher_task import WFLDispatcherTask
import structlog

logger = structlog.get_logger()

class WFLDispatcherConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(settings.QUEUE_CONFIGS["wfl_dispatcher"])
        self.task_factory.register_task("dispatch_wfl", WFLDispatcherTask)
    
    def process_message(self, task_type: str, task_data: dict) -> dict:
        logger.info("Processing message", task_type=task_type, task_data=task_data)
        task = self.task_factory.create_task(task_type)
        return task.execute(task_data) 