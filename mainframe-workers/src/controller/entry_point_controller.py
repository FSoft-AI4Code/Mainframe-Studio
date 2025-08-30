from __future__ import annotations
from enum import Enum
from typing import Any, Dict, List, Optional
from bson import ObjectId
from loguru import logger
from pydantic import BaseModel, computed_field
from controller.node_controller import FileType
from database.mongodb import get_database

class EntryPointCriticality(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    @staticmethod
    def determine_criticality(number_of_files: int) -> EntryPointCriticality:
        if number_of_files < 10:
            return EntryPointCriticality.LOW
        elif number_of_files < 21:
            return EntryPointCriticality.MEDIUM
        else:
            return EntryPointCriticality.HIGH

class EntryPoint(BaseModel):
    id: Optional[str] = None
    repository_id: str
    name: str
    label: FileType
    number_of_files: int
    complexity: int
    line_of_code: int

    @computed_field
    @property
    def criticality(self) -> EntryPointCriticality:
        return EntryPointCriticality.determine_criticality(self.number_of_files)

    class Config:
        use_enum_values = True

    def set_id(self, id: ObjectId):
        self.id = str(id)
    
    @staticmethod
    def from_dict(d: Dict[str, Any]) -> EntryPoint:
        return EntryPoint(
            id=str(d["_id"]),
            name=d["name"],
            label=FileType(d["label"]),
            repository_id=str(d["repository_id"]),
            number_of_lines=d["number_of_lines"],
            complexity=d["complexity"],
            line_of_code=d["line_of_code"]
        )
 
class EntryPointController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.entry_points
    
    def delete_entry_point(self, repository_id: str, name: str, label: str):
        try:
            self.collection.delete_one({"repository_id": ObjectId(repository_id), "name": name, "label": label})
        except Exception as e:
            logger.error("Error getting nodes in group", error=str(e),
                         repository_id=repository_id, name=name, label=label)
            return None
    
    def save_entry_point(self, entry_point: EntryPoint) -> Dict[str, Any]:
        """
        Upsert the given entry point into the entry points collection. 

        Side effect: If this is a new entry point, entry_point.id will be updated

        Args:
            entry_point: The entry_point update data

        Returns:
            Dict[str, Any]: Result of the save operation containing status and message
        """
        try:
            update_data = entry_point.model_dump(exclude=["id"])
            update_data["repository_id"] = ObjectId(
                update_data["repository_id"])
            result = self.collection.update_one(
                filter={
                    'name': entry_point.name,
                    'label': entry_point.label,
                    'repository_id': ObjectId(entry_point.repository_id),
                },
                update={
                    '$set': update_data
                },
                upsert=True
            )

            if result.matched_count > 0:
                return {
                    "status": "success",
                    "message": "Successfully updated entry point"
                }
            elif result.upserted_id:
                entry_point.set_id(result.upserted_id)
                return {
                    "status": "success",
                    "message": "Successfully inserted entry point",
                }
            else:
                return {
                    "status": "error",
                    "message": "Failed to save entry point"
                }

        except Exception as e:
            logger.error("Error saving entry point", error=str(e))
            return {
                "status": "error",
                "message": f"Error saving entry point: {str(e)}"
            }
        
    def get_all_entry_points(self, repository_id: str) -> List[Dict[str, Any]]:
        """
        Get all nodes that belong to a repository from the entry_points collection.
        """
        try:
            return list(self.collection.find({
                "repository_id": ObjectId(repository_id)
            }))
        except Exception as e:
            logger.error("Error getting entry_points", error=str(e),
                         repository_id=repository_id)

    