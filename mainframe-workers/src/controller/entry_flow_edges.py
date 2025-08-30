from enum import Enum
from typing import Any, Dict, List, Optional

from bson import ObjectId
from loguru import logger
from pydantic import BaseModel, Field

from database.mongodb import get_database
from .edge_controller import RelationshipLabel


class EntryFlowEdge(BaseModel):
    id: Optional[str] = None
    repository_id: str
    source: str
    target: str
    type_: RelationshipLabel = Field(alias="type")
    properties: Optional[Dict[str, Any]] = None

    def set_id(self, id: ObjectId):
        self.id = str(id)

    class Config:
        use_enum_values = True


class EntryFlowEdgeController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.entry_flow_edges
    def query_edge(
        self, repository_id: str, source: str, target: str, type_: str
    ) -> Dict[str, Any]:
        """
        Get an edge from the edges collection.
        """
        try:
            return self.collection.find_one(
                {
                    "repository_id": repository_id,
                    "source": source,
                    "target": target,
                    "type": type_,
                }
            )
        except Exception as e:
            logger.error(
                "Error querying edge content",
                error=str(e),
                repository_id=repository_id,
                source=source,
                target=target,
                type_=type_,
            )
            return None

    def query_outgoing_edges(
        self, source_id: str, edge_type: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """
        Get all outgoing edges from a node in the edges collection.
        """
        query = {"source": ObjectId(source_id)}
        if edge_type:
            query["type"] = {"$in": edge_type}

        try:
            return list(self.collection.find(query))
        except Exception as e:
            logger.error(
                "Error querying outgoing edges",
                error=str(e),
                source_id=source_id,
                edge_type=edge_type,
            )
            raise

    def get_all_edges(self, repository_id: str) -> List[Dict[str, Any]]:
        """
        Get all edges that belong to a repository in the edges collection.
        """
        try:
            return list(
                self.collection.find({"repository_id": ObjectId(repository_id)})
            )
        except Exception as e:
            logger.error(
                "Error getting edges", error=str(e), repository_id=repository_id
            )
            return None

    def save_edge(self, edge: EntryFlowEdge) -> Dict[str, Any]:
        """
        Upsert the given edge into the edges collection.

        Side effect: If this is a new edge, edge.id will be updated

        Args:
            edge: The edge update data

        Returns:
            Dict[str, Any]: Result of the save operation containing status and message
        """
        try:
            update_data = edge.model_dump(by_alias=True, exclude=["id"])
            for id_field in ["repository_id", "source", "target"]:
                update_data[id_field] = ObjectId(update_data[id_field])

            result = self.collection.update_one(
                filter={
                    "repository_id": ObjectId(edge.repository_id),
                    "source": ObjectId(edge.source),
                    "target": ObjectId(edge.target),
                    "type": edge.type_,
                },
                update={"$set": update_data},
                upsert=True,
            )

            if result.matched_count > 0:
                return {"status": "success", "message": "Successfully updated edge"}
            elif result.upserted_id:
                edge.set_id(result.upserted_id)
                return {
                    "status": "success",
                    "message": "Successfully inserted edges",
                }
            else:
                return {"status": "error", "message": "Failed to save edge"}

        except Exception as e:
            logger.error("Error saving edge", error=str(e))
            return {"status": "error", "message": f"Error saving edge: {str(e)}"}
