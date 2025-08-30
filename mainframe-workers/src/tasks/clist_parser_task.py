from loguru import logger
from config.settings import settings
from utils.timeout_util import Timeout
from utils.azure_blob_util import read_blob_file
from .base_task import BaseTask
from typing import Dict, Any
from parsers.clist_parser import parse_clist
from controller.reverse_controller import ReverseController
from classifier.constants import FileType

class ClistParserTask(BaseTask):
    TASK_TYPE = "parse_clist"

    def __init__(self):
        self.reverse_controller = ReverseController()
    
    def validate(self, task_data: Dict[str, Any]) -> bool:
        if not task_data.get("name") or not task_data.get("repository_id"):
            logger.error("No name or repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}
            
        name = task_data.get("name")
        repository_id = task_data.get("repository_id")

        try:
            blob_name = f"{repository_id}/code/CLIST/{name}"
            content = read_blob_file(blob_name)

            if content is None:
                raise FileNotFoundError(f"Cannot read the content of {blob_name}")
            
            reversed_program = parse_clist(content)
            
            save_result = self.reverse_controller.save_reverse_engineering(
                name, repository_id, reversed_program, type=FileType.CLIST
            )

            return save_result
        except Exception as e:
            error_msg = f"Error processing CLIST file: {str(e)}"
            logger.error(error_msg)
            return {"status": "error", "message": error_msg}
