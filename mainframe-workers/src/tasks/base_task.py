from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseTask(ABC):
    @abstractmethod
    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the task with the given data"""
        pass
    
    @abstractmethod
    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate the task data"""
        pass 