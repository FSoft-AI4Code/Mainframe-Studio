from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, Optional, List

from fastapi.exceptions import HTTPException
import numpy as np
from bson import ObjectId
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.constants.cobol import FileType
from app.models.reverse import ReverseEngineering
from app.schemas import reverse_schema
from app.schemas.database_crud_schema import DatabaseTableDescriptor
from app.schemas.reverse_schema import UpdateNodeLabelResponse


async def create_reverse_engineering(db: AsyncIOMotorDatabase, reverse: reverse_schema.ReverseEngineeringCreate):
    reverse_dict = reverse.model_dump()
    reverse_dict["repository_id"] = ObjectId(reverse_dict["repository_id"])
    result = await db.reverse_engineering.insert_one(reverse_dict)
    return await get_reverse_engineering(db, result.inserted_id, reverse.repository_id)


async def get_reverse_engineering(db: AsyncIOMotorDatabase, reverse_id: str, repository_id: Optional[ObjectId] = None):
    reverse = await db.reverse_engineering.find_one({"_id": ObjectId(reverse_id)})
    if reverse:
        # Update repo status
        repo = await db.repositories.find_one({"_id": ObjectId(repository_id)})
        repo["status"] = "reversed"
        await db.repositories.update_one({"_id": ObjectId(repository_id)}, {"$set": repo})
        return ReverseEngineering(**reverse)


async def get_reverse_engineering_by_path(db: AsyncIOMotorDatabase, path: str):
    reverse = await db.reverse_engineering.find_one({"path": path})
    if reverse:
        return ReverseEngineering(**reverse)


async def get_complexity_aggregated_data_of_repository_id(db: AsyncIOMotorDatabase, repository_id: str) -> float:
    pipeline = [
        {
            "$match": {
                "repository_id": ObjectId(repository_id),
                "output.complexity": {"$exists": True}
            }
        },
        {
            "$group": {
                "_id": None,
                "average_complexity": {"$avg": "$output.complexity"},
                "number_of_complexities": {"$sum": 1}
            }
        }
    ]
    result = await db.reverse_engineering.aggregate(pipeline).to_list(length=1)
    return result[0] if result else {"average_complexity": 0.0, "number_of_complexities": 0}


async def get_complexity_distribution(db: AsyncIOMotorDatabase, repository_id: str, type="COBOL") -> dict:
    cursor = db.reverse_engineering.find({
        "repository_id": ObjectId(repository_id),
        "type": type,
        "output.complexity": {"$exists": True}
    })
    documents = await cursor.to_list(length=None)

    # Extract complexity values from documents
    values = [doc["output"]["complexity"] for doc in documents if doc.get("output", {}).get("complexity") is not None]
    if not values:
        return []

    frequencies, bins = np.histogram(values, bins="auto")
    log_frequencies = np.log10(frequencies + 1)  # Adding 1 to avoid log(0)

    # # Build and return the distribution list
    # result = []
    # for i in range(len(frequencies)):
    #     result.append(
    #         reverse_schema.ComplexityDistribution(
    #             bin_start=float(bins[i]),
    #             bin_end=float(bins[i + 1]),
    #             frequency=int(frequencies[i]),
    #             log_frequency=float(log_frequencies[i])
    #         )
    #     )

    return {
        "frequencies": frequencies.tolist(),
        "log_frequencies": log_frequencies.tolist(),
        "bins": bins.tolist(),
    }


async def get_reverse_engineerings(db: AsyncIOMotorDatabase, skip: int = 0, limit: int = 100):
    reverses = await db.reverse_engineering.find().skip(skip).limit(limit).to_list(length=limit)
    return [ReverseEngineering(**reverse) for reverse in reverses]


async def update_reverse_engineering(db: AsyncIOMotorDatabase, reverse_id: str,
                                     reverse_update: reverse_schema.ReverseEngineeringUpdate):
    await db.reverse_engineering.update_one(
        {"_id": ObjectId(reverse_id)},
        {"$set": reverse_update.model_dump()}
    )
    return await get_reverse_engineering(db, reverse_id)


async def delete_reverse_engineering(db: AsyncIOMotorDatabase, reverse_id: str):
    result = await db.reverse_engineering.delete_one({"_id": ObjectId(reverse_id)})
    return result.deleted_count > 0


async def get_reverse_engineering_report(
        db: AsyncIOMotorDatabase,
        repository_id: str,
        type: Optional[str] = None,
        name: Optional[str] = None
) -> Optional[ReverseEngineering]:
    """
    Get reverse engineering reports by repository ID with optional filters.

    Args:
        db: Database connection
        repository_id: ID of the repository
        type: Optional type of reverse engineering report
        name: Optional name of the file

    Returns:
        ReverseEngineering model if found, None otherwise

    Raises:
        ValueError: If type or name parameters are not provided
    """
    try:
        if type is None:
            raise ValueError("type parameter is required")
        if name is None:
            raise ValueError("name parameter is required")

        # Build query with required repository_id and filters
        query = {
            "repository_id": ObjectId(repository_id),
            "type": type,
            "name": name,
            "output": {"$exists": True}
        }

        logger.info(f"Query: {query}")
        reverse = await db.reverse_engineering.find_one(query)
        if reverse:
            return ReverseEngineering(**reverse)
        return None

    except Exception as e:
        logger.error(f"Error getting reverse engineering reports for repository {repository_id}: {str(e)}")
        return None


async def get_crud(db: AsyncIOMotorDatabase, repository_id: str):
    """Retrieve the table_descriptors from the output field of the reverse_engineer collection.

    Args:
        db: AsyncIOMotorDatabase connection
        repository_id: Repository ID

    Returns:
        Table descriptors if found, None otherwise
    """

    try:
        repository_id = ObjectId(repository_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid repository ID: '{repository_id}'")

    pipeline = [
        {
            "$match":
                {
                    "repository_id": ObjectId(repository_id),
                    "output.table_descriptors.1": {"$exists": True}
                }
        },
        {
            "$project": {
                "_id": 0,
                "program_name": "$name",
                "table_descriptors": "$output.table_descriptors"
            }
        }
    ]

    result = await db.reverse_engineering.aggregate(pipeline).to_list()

    table_descriptors = [
        DatabaseTableDescriptor(program_name=record["program_name"], **descriptor) for record in result for descriptor
        in record["table_descriptors"]
    ]

    return table_descriptors


async def list_reverse_engineering_reports(
        db: AsyncIOMotorDatabase,
        repository_id: str,
        type: Optional[FileType] = None
) -> List[reverse_schema.ReverseEngineeringReportResponse]:
    """
    List reverse engineering reports for a repository with optional type filter.
    """
    match_stage = {"repository_id": ObjectId(repository_id)}
    if type:
        match_stage["type"] = type
        match type:
            case FileType.COBOL:
                match_stage["output.exec_flow.edges"] = {"$exists": True, "$ne": []}

    # Use an aggregation pipeline to check if output exists without retrieving its content
    pipeline = [
        {"$match": match_stage},
        {"$project": {
            "status": 1,
            "type": 1,
            "name": 1,
            "is_reversed": {
                "$cond": {
                    "if": {"$ifNull": ["$output", False]},
                    "then": True,
                    "else": False
                }
            }
        }}
    ]

    reports = await db.reverse_engineering.aggregate(pipeline).to_list(length=None)

    if not reports:
        return []

    # Convert to response objects
    return [
        reverse_schema.ReverseEngineeringReportResponse(**report) for report in reports
    ]


def __non_empty_field_conditions(fields):
    for field in fields:
        yield {"$not": {"$in": [f"$output.{field}", [None, "", []]]}}
        yield {"$ne": [{"$type": f"$output.{field}"}, "missing"]}


async def get_file_counts_by_repository(db: AsyncIOMotorDatabase, repository_id: str):
    pipeline = [
        {"$match": {"repository_id": ObjectId(repository_id)}},
        {"$unwind": "$result.assessment"},
        {"$group": {"_id": "$result.assessment.label", "count": {"$sum": 1}}},
        {"$project": {"label": "$_id", "count": 1, "_id": 0}}
    ]
    return await db.assessments.aggregate(pipeline).to_list(length=None)


async def get_reverse_assets_coverage(
        db: AsyncIOMotorDatabase,
        repository_id: str,
) -> Dict[str, Any]:
    """
    Retrieve reverse engineering assets coverage for a given repository
    """
    essential_output_fields = {
        "COBOL": [
            *__non_empty_field_conditions(["statements", "working_storage_variables"]),
            *(
                {
                    "$or": [
                        {"$not": {"$and": list(__non_empty_field_conditions([pair[0]]))}},
                        {"$and": list(__non_empty_field_conditions([pair[1]]))}
                    ]
                } for pair in [("io_files", "variables_flow"), ("paragraph_list", "exec_flow"),
                               ("called_program_list", "subroutines_called")]
            )
        ],
        "COPY": list(__non_empty_field_conditions(["variables_declaration"])),
        "JCL": list(__non_empty_field_conditions(["overview", "step_list"])),
        "BMS": list(__non_empty_field_conditions(["overview", "screen_string"])),
    }
    pipeline = [
        # Filter by repository_id
        {"$match": {"repository_id": ObjectId(repository_id)}},

        # Group by type, count all records and records that have output for each type
        {"$group": {
            "_id": "$type",
            "covered_count": {"$sum": {"$cond": [
                {
                    "$or": [
                        {
                            "$and": [
                                {
                                    "$eq": ["$type", type_]
                                },
                                {
                                    "$ne": [{"$type": "$output"}, "missing"]
                                },
                                {
                                    "$not": {"$in": ["$output", [None, "", []]]}
                                },
                                *conditions
                            ]
                        } for type_, conditions in essential_output_fields.items()
                    ]
                },
                1,
                0
            ]}}
        }}
    ]

    result = await db.reverse_engineering.aggregate(pipeline).to_list()
    assessment_result = await get_file_counts_by_repository(db, repository_id)
    total_files = sum(d['count'] for d in assessment_result)
    total_coverage = sum(d['covered_count'] for d in result)

    by_types = defaultdict(int)

    for d in result:
        label = d['_id']
        by_types[label] = d['covered_count']

    for d in assessment_result:
        if d['label'] == FileType.OTHER.value:
            continue
        label = d['label']
        if label in [FileType.JCL_IBM.value, FileType.JCL_FUJITSU.value]:
            label = FileType.JCL.value

        by_types[label] = by_types[label] / d['count'] * 100

    return {
        "total_coverage": total_coverage / total_files * 100 if total_files > 0 else 0,
        "by_types": [
            {
                "type": key,
                "coverage": value
            } for key, value in by_types.items()
        ]
    }


async def update_label(db, repository_id, file_name, old_label, new_label, comment, description, current_user):
    node = await db.nodes.find_one({"repository_id": ObjectId(repository_id), "name": file_name, "label": old_label.value})
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")
    node_id = node.get("_id")
    # Update the node
    update_data = {
        "label": new_label.value,
        "updated_at": datetime.utcnow(),
        "updated_by": str(current_user.id),  # Convert ObjectId to string
    }
    if comment:
        update_data["comment"] = comment
    if description:
        update_data["description"] = description

    result = await db.nodes.update_one(
        {"_id": node_id},
        {"$set": update_data}
    )
    if result.modified_count == 0:
        raise HTTPException(
            status_code=500,
            detail="Failed to update node label"
        )

    # Update reverse engineer
    reverse_engineer = await db.reverse_engineering.find_one({"repository_id": ObjectId(repository_id), "name": file_name, "type": old_label.value})
    if not reverse_engineer:
        raise HTTPException(status_code=404, detail="Failed to update node label")
    reverse_update_data = {
        "type": new_label.value,
        "updated_at": datetime.utcnow(),
        "updated_by": str(current_user.id),  # Convert ObjectId to string
    }

    await db.reverse_engineering.update_one(
        {"_id": reverse_engineer.get("_id")},
        {"$set": reverse_update_data}
    )

    # Return updated node
    updated_node = await db.nodes.find_one({"_id": node_id})
    if not updated_node:
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve updated node"
        )
    
    # Convert ObjectId to string for repository_id
    updated_node["repository_id"] = str(updated_node["repository_id"])
    return UpdateNodeLabelResponse(**updated_node)
