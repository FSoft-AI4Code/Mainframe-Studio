from typing import Any, Dict

from loguru import logger
from utils.rabbitmq_util import produce_task
from config.settings import settings

from controller.reverse_controller import ReverseController
from parsers.bat_parser import parse_batch
from utils.azure_blob_util import read_blob_file

from .base_task import BaseTask


class BatchParserTask(BaseTask):
    def __init__(self):
        self.reverse_controller = ReverseController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('repository_id'):
            logger.error("No repository_id provided in task data")
            return False
        if not task_data.get('name'):
            logger.error("No name provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}

        repository_id = task_data.get('repository_id')
        name = task_data.get('name')

        try:
            blob_name = f"{repository_id}/code/BAT/{name}"
            content = read_blob_file(blob_name)
            if content is None:
                raise FileNotFoundError(f"Cannot read the content of {blob_name}")
            reversed_program = parse_batch(content)
            save_result = self.reverse_controller.save_reverse_engineering(
                name, repository_id, reversed_program, type='BAT')
            if save_result["status"] == "error":
                return {
                    "status": "error", 
                    "message": save_result.get("message", "Error saving reversed program")
                }

        except Exception as e:
            logger.error(
                f"Error processing batch file", error=str(e))

            return {
                "status": "error",
                "message": f"Error processing batch file: {str(e)}"
            }
