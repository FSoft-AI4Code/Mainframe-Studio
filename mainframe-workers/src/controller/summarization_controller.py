from typing import Dict, Any, Optional
from bson import ObjectId
from loguru import logger
from schema.summarization import Summarization, CobolLLMScreenSummary, CopybookSummary
from database.mongodb import get_database


class BmsSummaryController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.bms_summaries

    def save_summary(self, summary: Summarization) -> Dict[str, Any]:
        """
        Upsert the BMS summary into MongoDB.
        """
        try:
            update_data = summary.model_dump()
            update_data["id"] = ObjectId(update_data["id"])

            result = self.collection.update_one(
                {
                    "repository_id": update_data["repository_id"],
                    "path": summary.path
                },
                {"$set": update_data},
                upsert=True
            )

            if result.upserted_id:
                return {"status": "success", "message": "Inserted new summary"}
            elif result.matched_count > 0:
                return {"status": "success", "message": "Updated existing summary"}
            else:
                return {"status": "error", "message": "Unexpected result saving summary"}

        except Exception as e:
            logger.error(f"Error saving BMS summary {e}")
            return {"status": "error", "message": str(e)}

class CobolScreenSummaryController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.cobol_screen_summaries

    def save_summary(self, summary: CobolLLMScreenSummary) -> Dict[str, Any]:
        """
        Upsert the Cobol Screen summary into MongoDB.
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
                return {"status": "success", "message": "Inserted new summary"}
            elif result.matched_count > 0:
                return {"status": "success", "message": "Updated existing summary"}
            else:
                return {"status": "error", "message": "Unexpected result saving summary"}

        except Exception as e:
            logger.error("Error saving Cobol Screen Summary", error=str(e))
            return {"status": "error", "message": str(e)}

class CopybookSummaryController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.copybook_summaries

    def save_summary(self, summary: CopybookSummary) -> Dict[str, Any]:
        """
        Upsert the Copybook summary into MongoDB.
        """
        try:
            update_data = summary.model_dump()
            update_data["id"] = ObjectId(update_data["id"])

            result = self.collection.update_one(
                {
                    "repository_id": update_data["repository_id"],
                    "path": summary.path
                },
                {"$set": update_data},
                upsert=True
            )

            if result.upserted_id:
                return {"status": "success", "message": "Inserted new summary"}
            elif result.matched_count > 0:
                return {"status": "success", "message": "Updated existing summary"}
            else:
                return {"status": "error", "message": "Unexpected result saving summary"}

        except Exception as e:
            logger.error("Error saving Copybook Summary", error=str(e))
            return {"status": "error", "message": str(e)}

