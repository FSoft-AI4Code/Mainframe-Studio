from typing import Dict, Any

from loguru import logger

from database.mongodb import get_database
from schema.java_migration import JavaCopybookMigration, JavaBMSMigration


class JavaCopybookMigrationController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.java_copybook_migrations

    def save_summary(self, summary: JavaCopybookMigration) -> Dict[str, Any]:
        """
        Upsert the Java Migration into MongoDB.
        """
        try:
            update_data = summary.model_dump()

            result = self.collection.update_one(
                {
                    "repository_id": update_data["repository_id"],
                    "path": summary.path
                },
                {"$set": update_data},
                upsert=True
            )

            if result.upserted_id:
                return {"status": "success", "message": "Inserted new java migration"}
            elif result.matched_count > 0:
                return {"status": "success", "message": "Updated existing java migration"}
            else:
                return {"status": "error", "message": "Unexpected result saving java migration"}

        except Exception as e:
            logger.error("Error saving Java migration", error=str(e))
            return {"status": "error", "message": str(e)}


class JavaBMSMigrationController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.java_bms_migrations

    def save_summary(self, summary: JavaBMSMigration) -> Dict[str, Any]:
        """
        Upsert the Java Migration into MongoDB.
        """
        try:
            update_data = summary.model_dump()

            result = self.collection.update_one(
                {
                    "repository_id": update_data["repository_id"],
                    "path": summary.path
                },
                {"$set": update_data},
                upsert=True
            )

            if result.upserted_id:
                return {"status": "success", "message": "Inserted new java migration"}
            elif result.matched_count > 0:
                return {"status": "success", "message": "Updated existing java migration"}
            else:
                return {"status": "error", "message": "Unexpected result saving java migration"}

        except Exception as e:
            logger.error("Error saving Java migration", error=str(e))
            return {"status": "error", "message": str(e)}
