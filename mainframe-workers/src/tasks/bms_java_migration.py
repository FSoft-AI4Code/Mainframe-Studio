import asyncio
from typing import Dict, Any

from bson import ObjectId
from loguru import logger

from controller.java_migration_controller import JavaBMSMigrationController
from database.mongodb import get_database
from java_migration.cobol_java_migration import bms_java_migration_summary
from utils.azure_blob_util import get_file_content_from_blob_name, read_blob_file
from .base_task import BaseTask


def get_copybook_summary_linked_cobol(db, repository_id, cobol_file_name, bms_file_name):
    bms_summary = db.bms_summaries.find_one({
        "repository_id": repository_id,
        "name": bms_file_name
    })

    if not bms_summary:
        raise FileNotFoundError(f"BMS summary for {bms_file_name} not found in repository {repository_id}")

    for k, v in bms_summary.get("copybook_groups", {}).items():
        if v.get("linked_cobol") == cobol_file_name:
            return k, v

    raise FileNotFoundError(f"BMS summary for {bms_file_name} not found")


class BMSJavaMigrationTask(BaseTask):
    def __init__(self):
        self.java_migration_controller = JavaBMSMigrationController()
        self.db = get_database()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('bms_file_name') or not task_data.get('repository_id'):
            logger.error("No bms_file_name or repository_id provided in task data")
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

            model_name, cobol_summary = get_copybook_summary_linked_cobol(self.db, repository_id, cobol_file_name, bms_file_name)

            # Call the async Migration function
            migration_program = asyncio.run(
                bms_java_migration_summary(path, repository_id, cobol_content, bms_content, model_name, cobol_summary))

            # Save the actual Migration model directly
            save_result = self.java_migration_controller.save_summary(migration_program)

            if save_result["status"] == "error":
                return {
                    "status": "error",
                    "message": save_result.get("message", "Error saving migration program")
                }

            # Update status of repo
            self.db.entry_points.update_one(
                {"repository_id": ObjectId(repository_id), "label": "BMS", "name": bms_file_name},
                {"$set": {"status": "migrated"}}
            )

            self.db.reverse_engineering.update_one(
                {"repository_id": ObjectId(repository_id), "type": "BMS", "name": bms_file_name},
                {"$set": {"status": "migrated"}}
            )

            return {
                "status": "success",
                "message": save_result.get("message", "Successfully saved migration program")
            }

        except Exception as e:
            logger.error(f"Error processing migration BMS file {e}")
            raise e


def get_linked_api_path(db, repository_id, cobol_file_name):
    java_copybook_migration = db.java_copybook_migrations.find(
        {"repository_id": repository_id,
         "linked_cobol": cobol_file_name}
    ).to_list(length=1)

    if not java_copybook_migration:
        raise FileNotFoundError
    api_path = java_copybook_migration[0].get("api_java")
    return api_path
