from .base_task import BaseTask
from typing import Dict, Any
from summarization.cobol_summarization import cobol_screen_summary
from controller.summarization_controller import CobolScreenSummaryController
from utils.azure_blob_util import read_blob_file
from loguru import logger
import asyncio


class CobolScreenSummarizationTask(BaseTask):
    def __init__(self):
        self.summarization_controller = CobolScreenSummaryController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('file_name') or not task_data.get('repository_id'):
            logger.error("No name or repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}

        file_name = task_data.get('file_name')
        repository_id = task_data.get('repository_id')
        path = task_data.get('blob_path')

        try:
            blob_name = f"{repository_id}/code/COBOL/{file_name}"
            content = read_blob_file(path)
            if content is None:
                raise FileNotFoundError(f"Cannot read the content of {blob_name}")

            # Call the async summarization function
            summarized_program = asyncio.run(cobol_screen_summary(blob_name, repository_id, content))

            # Save the actual Summarization model directly
            save_result = self.summarization_controller.save_summary(summarized_program)

            if save_result["status"] == "error":
                return {
                    "status": "error",
                    "message": save_result.get("message", "Error saving summarized program")
                }

            return {
                "status": "success",
                "message": save_result.get("message", "Successfully saved summarized program")
            }

        except Exception as e:
            logger.error("Error processing COBOL file", error=str(e))
            return {
                "status": "error",
                "message": f"Error processing COBOL file: {str(e)}"
            }
