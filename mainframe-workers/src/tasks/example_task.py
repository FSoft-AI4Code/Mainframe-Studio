from .base_task import BaseTask
import structlog

logger = structlog.get_logger()

class ExampleTask(BaseTask):
    def validate(self, data: dict) -> bool:
        required_fields = ['message']
        return all(field in data for field in required_fields)
    
    def execute(self, data: dict) -> dict:
        if not self.validate(data):
            raise ValueError("Invalid task data")
            
        logger.info("Executing example task", data=data)
        # Add your task logic here
        return {"status": "success", "message": f"Processed: {data['message']}"} 