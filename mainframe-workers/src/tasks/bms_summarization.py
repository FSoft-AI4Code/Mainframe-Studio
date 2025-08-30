from bson import ObjectId

from database.mongodb import get_database
from .base_task import BaseTask
from typing import Dict, Any
from summarization.bms_summarization import bms_summary
from controller.summarization_controller import BmsSummaryController
from utils.azure_blob_util import read_blob_file, get_file_content_from_blob_name
from loguru import logger
import asyncio


class BMSSummarizationTask(BaseTask):
    def __init__(self):
        self.summarization_controller = BmsSummaryController()
        self.db = get_database()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('bms_file_name') or not task_data.get('repository_id'):
            logger.error("No name or repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}

        bms_file_name = task_data.get('bms_file_name')
        cobol_file_name = task_data.get('cobol_file_name')
        repository_id = task_data.get('repository_id')
        path = task_data.get('blob_path')

        try:
            bms_content = get_file_content_from_blob_name(self.db, repository_id, bms_file_name, "BMS")
            cobol_content = get_file_content_from_blob_name(self.db, repository_id, cobol_file_name, "COBOL")

            if bms_content is None or cobol_content is None:
                raise FileNotFoundError(f"Cannot read the content of {bms_file_name} or {cobol_file_name}")

            # Call the async summarization function
            summarized_program = asyncio.run(
                bms_summary(bms_file_name, path, repository_id, bms_content, cobol_content))

            # Save the actual Summarization model directly
            save_result = self.summarization_controller.save_summary(summarized_program)

            if save_result["status"] == "error":
                return {
                    "status": "error",
                    "message": save_result.get("message", "Error saving summarized program")
                }

            # Update status of repo
            self.db.entry_points.update_one(
                {"repository_id": ObjectId(repository_id), "label": "BMS", "name": bms_file_name},
                {"$set": {"status": "summarized"}}
            )

            self.db.reverse_engineering.update_one(
                {"repository_id": ObjectId(repository_id), "type": "BMS", "name": bms_file_name},
                {"$set": {"status": "summarized"}}
            )

            return {
                "status": "success",
                "message": save_result.get("message", "Successfully saved summarized program")
            }

        except Exception as e:
            logger.error(f"Error processing BMS file {e}")
            return {
                "status": "error",
                "message": f"Error processing summary BMS file: {e}"
            }
