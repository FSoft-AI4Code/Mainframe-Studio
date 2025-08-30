from datetime import datetime
from http.client import HTTPException
from typing import List, Tuple, Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from app.schemas.utility_schema import UtilityCreate, UtilityUpdate, UtilityInDB
from app.config.constants import IBM_MAINFRAME_UTILITIES


async def process_nodes_to_utilities(db: AsyncIOMotorClient, repository_id: str) -> int:
    """
    Process nodes with label 'UTILITY' and insert them into utilities collection
    Returns the number of utilities created
    """
    # Find all nodes with label 'UTILITY' for the given repository
    nodes = await db.nodes.find({
        "repository_id": ObjectId(repository_id),
        "label": "UTILITY"
    }).to_list(length=None)

    created_count = 0
    for node in nodes:
        # Check if utility already exists
        existing = await db.utilities.find_one({
            "node_id": str(node["_id"]),
            "name": node.get("name", ""),
            "repository_id": ObjectId(repository_id)
        })

        if not existing:
            # Determine category based on utility name
            category = "Other"
            if node.get("name") in IBM_MAINFRAME_UTILITIES:
                if node.get("name") in ["IDCAMS", "IEBCOMPR", "IEBCOPY", "IEBDG", "IEBEDIT", "IEBGENER", "IEBIMAGE",
                                        "IEBISAM", "IEBPTPCH", "IEBUPDTE"]:
                    category = "Dataset Utilities"
                elif node.get("name") in ["IEFBR14"]:
                    category = "Scheduler Utilities"
                elif node.get("name") in ["ICKDSF", "IEHDASDR", "IEHINITT", "IEHLIST", "IEHMOVE", "IEHPROGM", "HEWL",
                                          "IEWL", "IGYCOMP", "EDCMPROC", "ASMA90"]:
                    category = "System Utilities"
                elif node.get("name") in ["SORT", "IGYCRCTL", "DFSMS"]:
                    category = "Supporting Programs"

            utility = UtilityCreate(
                name=node.get("name", ""),
                category=category,
                node_id=str(node["_id"]),
                repository_id=ObjectId(repository_id)
            )

            await db.utilities.insert_one(utility.model_dump(by_alias=True))
            created_count += 1

    return created_count


async def create_utility(db, repository_id, file_name, label, category_name, comment, description) -> UtilityInDB:
    """Create a new utility"""

    node = await db.nodes.find_one({"repository_id": ObjectId(repository_id), "name": file_name, "label": label})
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    node_id = node.get("_id")
    # Create a new utility with the provided parameters
    utility = UtilityCreate(
        name=file_name,
        category=category_name,
        repository_id=ObjectId(repository_id),
        node_id=node_id,
        description=description if description else "",
        comment=comment if comment else ""  # Use empty string if comment is None
    )

    # Insert the utility into the database
    utility_dict = utility.model_dump(by_alias=True)
    result = await db.utilities.insert_one(utility_dict)

    # Fetch and return the created utility
    created_utility = await db.utilities.find_one({"_id": result.inserted_id})

    # Update node label to UTL
    db.nodes.update_one(
        {"_id": ObjectId(node_id)},
        {"$set": {"label": "UTILITY"}}
    )
    return UtilityInDB(**created_utility)


async def get_utility(db: AsyncIOMotorClient, utility_id: str) -> Optional[UtilityInDB]:
    """Get a utility by ID"""
    utility = await db.utilities.find_one({"_id": ObjectId(utility_id)})
    return UtilityInDB(**utility) if utility else None


async def get_utilities(
        db: AsyncIOMotorClient,
        repository_id: str,
        skip: int = 0,
        limit: int = 10
) -> Tuple[List[UtilityInDB], int]:
    """Get utilities for a repository with pagination"""
    query = {"repository_id": repository_id}
    total = await db.utilities.count_documents(query)
    utilities = await db.utilities.find(query).skip(skip).limit(limit).to_list(length=limit)
    return [UtilityInDB(**utility) for utility in utilities], total


async def update_utility(
        db: AsyncIOMotorClient,
        utility_id: str,
        utility: UtilityUpdate
) -> Optional[UtilityInDB]:
    """Update a utility"""
    update_data = utility.model_dump(exclude_unset=True)
    if update_data:
        update_data["updated_at"] = datetime.utcnow()
        await db.utilities.update_one(
            {"_id": ObjectId(utility_id)},
            {"$set": update_data}
        )
    updated_utility = await db.utilities.find_one({"_id": ObjectId(utility_id)})
    return UtilityInDB(**updated_utility) if updated_utility else None


async def delete_utility(db: AsyncIOMotorClient, utility_id: str) -> bool:
    """Delete a utility"""
    result = await db.utilities.delete_one({"_id": ObjectId(utility_id)})
    return result.deleted_count > 0


async def get_category_by_project(db, repository_id):
    """
    Get the distribution of utility categories for a given repository
    Returns a dictionary with category counts
    """
    pipeline = [
        {
            "$match": {
                "repository_id": repository_id
            }
        },
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1}
            }
        }
    ]

    result = await db.utilities.aggregate(pipeline).to_list(length=None)
    category_distribution = {doc["_id"]: doc["count"] for doc in result}

    # Ensure all categories are present in the result
    all_categories = ["Dataset Utilities", "Scheduler Utilities", "System Utilities", "Supporting Programs", "Other"]
    for category in all_categories:
        if category not in category_distribution:
            category_distribution[category] = 0

    return category_distribution
