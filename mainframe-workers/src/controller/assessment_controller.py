from loguru import logger
from bson import ObjectId
from schema.assessment import AssessmentUpdate
from database.mongodb import get_database


class AssessmentController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.assessments

    @logger.catch
    def save_assessment(self, repository_id: str, assessment: AssessmentUpdate):
        # try:
        result = self.collection.update_one(
            filter={
                'repository_id': ObjectId(repository_id),
            },
            update={
                '$set': assessment.model_dump()
            },
            upsert=True
        )
        # result = self.collection.update_one(
        #     {"_id": ObjectId(repository_id)}, {"$set": assessment.model_dump()})

        if result.matched_count > 0:
            return {
                "status": "success",
                "message": "Successfully updated reverse engineering result"
            }
        elif result.upserted_id:
            return {
                "status": "success",
                "message": "Successfully inserted reverse engineering result",
            }
        else:
            return {
                "status": "error",
                "message": "Failed to save reverse engineering result"
            }

        # except Exception as e:
        #     logger.error(
        #         "Error saving assessment result", error=str(e))
        #     return {
        #         "status": "error",
        #         "message": f"Error saving assessment result: {str(e)}"
        #     }
