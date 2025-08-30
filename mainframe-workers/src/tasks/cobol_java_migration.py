import asyncio
from typing import Dict, Any

from bson import ObjectId
from loguru import logger

from controller.java_migration_controller import JavaCopybookMigrationController
from database.mongodb import get_database
from java_migration.cobol_java_migration import cobol_java_migration_summary
from utils.azure_blob_util import get_file_content_from_blob_name
from .base_task import BaseTask


def get_related_copybook(db, repository_id, bms_file_name):
    try:
        repository_id_obj = ObjectId(repository_id)
        copy_nodes = db.nodes.find({
            "repository_id": repository_id_obj,
            "label": "COPY",
            "group": bms_file_name
        }).to_list(length=None)

        if not copy_nodes:
            msg = f"No COPYBOOK linked with file {bms_file_name}"
            logger.error(msg)
            raise Exception(msg)

        return [node.get("name", "") for node in copy_nodes]

    except Exception as e:
        logger.error(f"Error getting linked COPY for {repository_id}/{bms_file_name}: {e}")
        raise


def get_copybook_content(db, repository_id, related_copy):
    result = []
    for copy in related_copy:
        try:
            copybook_content = get_file_content_from_blob_name(db, repository_id, copy, "COPYBOOK")
            if copybook_content:
                return result.extend(copybook_content)
        except FileNotFoundError:
            pass
        except Exception as e:
            logger.error(f"Error getting copybook content for {repository_id}/{related_copy}: {e}")
            raise e
    return result


class CobolJavaMigrationTask(BaseTask):
    def __init__(self):
        self.java_migration_controller = JavaCopybookMigrationController()
        self.db = get_database()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('cobol_file_name') or not task_data.get('repository_id'):
            logger.error("No name or repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}

        cobol_file_name = task_data.get('cobol_file_name')
        bms_file_name = task_data.get('bms_file_name')
        repository_id = task_data.get('repository_id')
        path = task_data.get('blob_path')
        related_copy = get_related_copybook(self.db, repository_id, bms_file_name)

        try:
            copybook_content = get_copybook_content(self.db, repository_id, related_copy),

            cobol_content = get_file_content_from_blob_name(self.db, repository_id, cobol_file_name, "COBOL")

            # Call the async Migration function
            migration_program = asyncio.run(
                cobol_java_migration_summary(path, repository_id, cobol_file_name, copybook_content, cobol_content))

            # Save the actual Migration model directly
            save_result = self.java_migration_controller.save_summary(migration_program)

            if save_result["status"] == "error":
                return {
                    "status": "error",
                    "message": save_result.get("message", "Error saving migrated program")
                }

            # Update status of repo
            self.db.entry_points.update_one(
                {"repository_id": ObjectId(repository_id), "label": "BMS", "name": bms_file_name},
                {"$set": {"status": "migrated"}}
            )

            return {
                "status": "success",
                "message": save_result.get("message", "Successfully saved migrated program")
            }

        except Exception as e:
            logger.error("Error processing COBOL file", error=str(e))
            return {
                "status": "error",
                "message": f"Error processing COBOL file: {str(e)}"
            }
