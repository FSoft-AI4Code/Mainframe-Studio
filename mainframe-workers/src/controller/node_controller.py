from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Set, Union

from bson import ObjectId
from loguru import logger
from pydantic import AfterValidator, BaseModel, BeforeValidator
from typing_extensions import Annotated
import multiprocessing
from database.mongodb import get_database
from classifier.constants import FileType

class NodeStatus(str, Enum):
    """Defines the current status of a node."""

    ALIVE = "ALIVE"
    MISSING = "MISSING"
    DEAD = "DEAD"


def remove_single_quote(node_name: str):
    return node_name.replace("'", "")


class DependencyGraphNode(BaseModel):
    id: Optional[str] = None
    repository_id: str
    name: Annotated[str, AfterValidator(remove_single_quote)]
    label: FileType
    status: NodeStatus
    is_entry_point: bool
    group: Set[str]

    class Config:
        use_enum_values = True

    def set_status(self, status: NodeStatus):
        self.status = status.value

    def set_id(self, id: ObjectId):
        self.id = str(id)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> DependencyGraphNode:
        return DependencyGraphNode(
            id=str(d["_id"]),
            name=d["name"],
            repository_id=str(d["repository_id"]),
            label=FileType[d["label"]],
            status=NodeStatus[d["status"]],
            is_entry_point=d["is_entry_point"],
            group=set(d["group"]),
        )


class NodeController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.nodes

    def query_node(
        self, repository_id: str, name: str, label: str
    ) -> DependencyGraphNode:
        """
        Get a node from the nodes collection.
        """
        try:
            result = self.collection.find_one(
                {"repository_id": ObjectId(repository_id), "name": name, "label": label}
            )
            if result is not None:
                return DependencyGraphNode.from_dict(result)
            return result
        except Exception as e:
            logger.error(
                "Error querying node content",
                error=str(e),
                repository_id=repository_id,
                name=name,
            )
            return None

    def query_node_by_id(self, node_id: str) -> Optional[DependencyGraphNode]:
        """
        Get a node from the nodes collection by its id.
        """
        try:
            result = self.collection.find_one({"_id": ObjectId(node_id)})
            if result is not None:
                return DependencyGraphNode.from_dict(result)
            return None
        except Exception as e:
            logger.error("Error querying node content", error=str(e), node_id=node_id)
            raise

    def get_all_nodes(self, repository_id: str) -> List[Dict[str, Any]]:
        """
        Get all nodes that belong to a repository from the nodes collection.
        """
        try:
            return self.collection.find({"repository_id": ObjectId(repository_id)})
        except Exception as e:
            logger.error(
                "Error getting nodes", error=str(e), repository_id=repository_id
            )
            return None
        
    lock = multiprocessing.Lock()
    def save_node(self, node: DependencyGraphNode) -> Dict[str, Any]:
        """
        Upsert the given node into the nodes collection.

        Side effect: If this is a new node, node.id will be updated

        Args:
            node: The node update data

        Returns:
            Dict[str, Any]: Result of the save operation containing status and message
        """
        try:
            update_data = node.model_dump(exclude=["id"])
            update_data["repository_id"] = ObjectId(update_data["repository_id"])
            update_data["group"] = list(update_data["group"])
            with self.lock:
                result = self.collection.update_one(
                    filter={
                        "name": node.name,
                        "label": node.label,
                        "repository_id": ObjectId(node.repository_id),
                    },
                    update={"$set": update_data},
                    upsert=True,
                )

            if result.matched_count > 0:
                updated_node = self.collection.find_one(
                    {
                        "name": node.name,
                        "label": node.label,
                        "repository_id": ObjectId(node.repository_id),
                    }
                )  
                node.set_id(updated_node["_id"])
                return {"status": "success", "message": "Successfully updated node"}
            elif result.upserted_id:
                node.set_id(result.upserted_id)
                return {
                    "status": "success",
                    "message": "Successfully inserted nodes",
                }
            else:
                return {"status": "error", "message": "Failed to save node"}

        except Exception as e:
            logger.error("Error saving node", error=str(e))
            return {"status": "error", "message": f"Error saving node: {str(e)}"}
