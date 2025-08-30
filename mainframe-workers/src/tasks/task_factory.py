from typing import Dict, Type
from .base_task import BaseTask
import structlog

logger = structlog.get_logger()

class TaskFactory:
    def __init__(self):
        self._tasks: Dict[str, Type[BaseTask]] = {}
    
    def register_task(self, task_type: str, task_class: Type[BaseTask]) -> None:
        """Register a task class for a specific task type"""
        self._tasks[task_type] = task_class
        logger.info(f"Registered task type: {task_type}")
    
    def create_task(self, task_type: str) -> BaseTask:
        """Create a task instance based on task type"""
        task_class = self._tasks.get(task_type)
        if task_class is None:
            raise ValueError(f"Unknown task type: {task_type}")
        
        return task_class() 