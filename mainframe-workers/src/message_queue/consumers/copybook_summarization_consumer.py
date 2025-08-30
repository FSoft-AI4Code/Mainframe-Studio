from typing import Dict, Any
from loguru import logger
from message_queue.base_consumer import BaseConsumer
from tasks.copybook_summarization_task import CopybookSummarizationTask

class CopybookSummarizationConsumer(BaseConsumer):
    def __init__(self):
        super().__init__()
        self.task = CopybookSummarizationTask()
        self.queue_name = "copybook_summarization"

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a copybook summarization message.
        
        Args:
            message: Dictionary containing:
                - repository_id: str
                - path: str (path to copybook file)
                - content: str (copybook content)
        
        Returns:
            Dict containing status and result
        """
        try:
            logger.info(f"Processing copybook summarization for {message.get('path')}")
            result = self.task.execute(message)
            return result
        except Exception as e:
            logger.error(f"Error processing copybook summarization message: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            } 