from typing import Any, Dict, List

import pymongo
from bson import ObjectId
from bson.errors import InvalidId
from loguru import logger
from pymongo.errors import BulkWriteError

from database.mongodb import get_database
from schema.dataset_assignment import JclDatasetAssignment


class DatasetAssignmentController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.dataset_assignments

    def save_dataset_assignments(
        self, dataset_assignments: List[JclDatasetAssignment]
    ) -> Dict[str, Any]:
        """
        Save multiple dataset assignments using MongoDB bulk write operations.

        This method performs a non-transactional bulk write to efficiently save
        multiple dataset assignments. Each assignment is saved with an upsert
        operation (update if exists, insert if not).

        Args:
            dataset_assignments: List of dataset assignments to save

        Returns:
            Dictionary with operation results including status and counts
        """
        if not dataset_assignments:
            return {"status": "success", "message": "No dataset assignments to save"}

        try:
            # Create bulk write operations
            operations = []
            invalid_ids = []

            for assignment in dataset_assignments:
                try:
                    repository_obj_id = ObjectId(assignment.repository_id)
                except (TypeError, InvalidId) as e:
                    invalid_ids.append((assignment.repository_id, str(e)))
                    continue

                # Convert model to dict for MongoDB
                assignment_dict = assignment.model_dump()
                assignment_dict["repository_id"] = repository_obj_id

                # Create upsert operation
                operations.append(
                    pymongo.UpdateOne(
                        filter={
                            "jcl_name": assignment.jcl_name,
                            "exec_program_id": assignment.exec_program_id,
                            "ddname": assignment.ddname,
                            "dataset_name": assignment.dataset_name,
                            "repository_id": repository_obj_id,
                        },
                        update={"$set": assignment_dict},
                        upsert=True,
                    )
                )

            # Should not insert if there is any invalid repository ID, this will cause missing data
            if invalid_ids:
                invalid_id_string = ", ".join([str(t) for t in invalid_ids])
                error_msg = f"Cannot insert dataset assignments with invalid repository IDs: {invalid_id_string}"
                logger.error(error_msg)
                return {
                    "status": "error",
                    "message": error_msg,
                    "invalid_ids": invalid_ids,
                }

            # Execute bulk write without transactions
            result = self.collection.bulk_write(operations)

            # Log results
            jcl_name = (
                dataset_assignments[0].jcl_name if dataset_assignments else "unknown"
            )
            logger.info(
                f"Dataset assignments of JCL file {jcl_name} saved: {result.upserted_count} inserted, "
                f"{result.modified_count} updated"
            )

            return {
                "status": "success",
                "message": f"Successfully saved {len(dataset_assignments)} dataset assignments",
                "inserted": result.upserted_count,
                "updated": result.modified_count,
            }

        except BulkWriteError as bwe:
            # Handle bulk write errors with details
            logger.error(f"Bulk write error: {str(bwe)}")
            return {
                "status": "error",
                "message": f"Error saving dataset assignments: {str(bwe)}",
                "details": bwe.details,
            }
        except Exception as e:
            # Handle any other exceptions
            logger.error(f"Error saving dataset assignments: {str(e)}")
            return {
                "status": "error",
                "message": f"Error saving dataset assignments: {str(e)}",
            }

    def query_dataset_assignments(
        self, repository_id: str, jcl_name: str
    ) -> List[JclDatasetAssignment]:
        """
        Query dataset assignments for a JCL file in a repository.

        Args:
            repository_id: ID of the repository
            jcl_name: Name of the JCL file

        Returns:
            List of dataset assignments for the JCL file
        """
        query = {
            "repository_id": ObjectId(repository_id),
            "jcl_name": jcl_name,
        }

        # Query dataset assignments
        dataset_assignments = self.collection.find(query)

        # Convert MongoDB documents to model objects
        assignments = []
        for assignment in dataset_assignments:
            assignments.append(JclDatasetAssignment(**assignment))

        return assignments
