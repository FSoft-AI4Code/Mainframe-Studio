import ast
import asyncio
import io
import os
import re
import time
import traceback
from typing import Any, Dict, Set, Tuple
import azure.core
import networkx as nx
import pandas as pd
import pymongo
import asyncio
from app.config.constants import IBM_MAINFRAME_UTILITIES
from azure.storage.blob import BlobServiceClient
from bson import ObjectId
from fastapi import Depends, HTTPException
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.config.database import get_database
from app.config.settings import settings
from app.constants.graph import NodeStatus
from app.controllers.reverse_controller import (
    get_complexity_aggregated_data_of_repository_id,
    get_reverse_engineering_report,
)
from app.models.graph import EdgeModel, EntryPointModel, NodeModel
from app.schemas.deadcode_schema import FileForDeadCode
from app.schemas.graph_schema import *


# --------------------------
# Helper Functions
# --------------------------


def detect_entry_points(
    graph: nx.DiGraph, labels: Optional[Set[str]] = None
) -> List[Dict]:
    """
    Detects entry points in the graph. Entry points are nodes with no incoming edges and specific labels.
    """
    if labels is None:
        labels = {"JCL", "BMS"}
    return [
        {"id": node, **data}
        for node, data in graph.nodes(data=True)
        if graph.in_degree(node) == 0 and data.get("label") in labels
    ]


def assign_groups(graph: nx.DiGraph, entry_points: List[Dict]) -> Dict[str, Set[str]]:
    """
    Assigns group labels to nodes based on all entry points they are reachable from.
    This ensures that nodes can belong to multiple groups if they are reachable from multiple entry points.
    """
    node_to_groups = {node: set() for node in graph.nodes()}
    for entry in entry_points:
        entry_id = entry["id"]
        entry_name = entry["name"]
        # Use descendants to get all nodes reachable from the entry point
        reachable_nodes = nx.descendants(graph, entry_id) | {entry_id}
        for node in reachable_nodes:
            node_to_groups[node].add(entry_name)
    return node_to_groups


def build_graph_data(graph: nx.DiGraph, entry_points: List[Dict]) -> Dict:
    """
    Builds a structured graph data dictionary from the NetworkX graph and entry points.
    """
    node_to_groups = assign_groups(graph, entry_points)
    graph_data = {"nodes": [], "edges": []}

    entrypoint_ids = {entry["id"] for entry in entry_points}

    # Add nodes with 'group' and 'is_entry_point' attributes
    for node, data in graph.nodes(data=True):
        groups = sorted(node_to_groups[node])
        graph_data["nodes"].append(
            {
                "id": node,
                "label": data.get("label", ""),
                "name": data.get("name", ""),
                "status": data.get("status", ""),
                "group": groups,
                "is_entry_point": node in entrypoint_ids,
            }
        )

    # Add edges with 'group' attribute and assign group based on source node's groups
    for u, v, attrs in graph.edges(data=True):
        source_groups = node_to_groups.get(u, set())
        edge_group = list(
            source_groups
        )  # Assign edge to the same groups as the source node
        edge_data = {
            "source": u,
            "target": v,
            "type": attrs.get("label", ""),
            "group": edge_group,  # Added group attribute
            "properties": {
                k: v for k, v in attrs.items() if k not in {"source", "target", "type"}
            },
        }
        graph_data["edges"].append(edge_data)
    return graph_data


def fetch_parsed_data(repository_id: str) -> List[Dict]:
    """
    Fetches and returns parsed data from Azure Blob Storage.
    Includes robust error handling and validation for blob operations.
    """
    try:
        # Initialize Azure Blob Service Client
        connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
        if not connection_string:
            raise ValueError("Azure Storage connection string is not configured")

        container_name = settings.AZURE_STORAGE_CONTAINER_NAME
        if not container_name:
            raise ValueError("Azure Storage container name is not configured")

        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )
        container_client = blob_service_client.get_container_client(container_name)

        # Validate container exists
        if not container_client.exists():
            raise HTTPException(
                status_code=404, detail=f"Container '{container_name}' not found"
            )

        # Get blob client and check if blob exists
        blob_name = f"{repository_id}_parsed.csv"
        blob_client = container_client.get_blob_client(blob_name)
        encoding = blob_client.get_blob_properties().metadata["encoding"]

        if not blob_client.exists():
            raise HTTPException(
                status_code=404, detail=f"Parsed data file '{blob_name}' not found"
            )

        # Download blob with retry logic
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                # Download the blob
                blob_data = blob_client.download_blob()
                blob_content = blob_data.readall()

                # Convert to DataFrame
                blob_stream = io.BytesIO(blob_content)
                df = pd.read_csv(
                    blob_stream,
                    escapechar="\\",
                    encoding=encoding,
                    on_bad_lines="warn",
                )

                # Convert parsed_data column from string to dict
                if "parsed_data" not in df.columns:
                    raise ValueError("CSV file does not contain 'parsed_data' column")

                df["parsed_data"] = df["parsed_data"].apply(
                    lambda x: ast.literal_eval(x) if pd.notna(x) else {}
                )

                logger.info(
                    f"Successfully fetched and parsed data for repository {repository_id}"
                )
                return df.to_dict(orient="records")

            except Exception as e:
                retry_count += 1
                if retry_count == max_retries:
                    traceback.print_exc()
                    logger.error(
                        f"Failed to download blob after {max_retries} attempts: {str(e)}"
                    )
                    raise
                logger.warning(
                    f"Retry {retry_count}/{max_retries} after error: {str(e)}"
                )
                time.sleep(1)

    except ValueError as ve:
        logger.error(f"Configuration error: {str(ve)}")
        raise HTTPException(status_code=500, detail=f"Configuration error: {str(ve)}")

    except azure.core.exceptions.ResourceNotFoundError as rnf:
        logger.error(f"Azure resource not found: {str(rnf)}")
        raise HTTPException(
            status_code=404, detail=f"Azure resource not found: {str(rnf)}"
        )

    except azure.core.exceptions.AzureError as ae:
        logger.error(f"Azure service error: {str(ae)}")
        raise HTTPException(status_code=500, detail=f"Azure service error: {str(ae)}")

    except Exception as e:
        logger.error(f"Unexpected error fetching parsed data: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error fetching parsed data: {str(e)}"
        )


# --------------------------
# Graph Extraction Functions
# --------------------------


def extract_graph(
    parsed_output: List[Dict],
) -> Tuple[
    Dict[Tuple[str, str], Dict],
    Dict[Tuple[Tuple[str, str], Tuple[str, str], str], Dict],
]:
    """
    Extracts raw graph nodes and edges from the parsed_output format.
    Returns dictionaries of node data and edge data without applying models.
    """
    node_dict: Dict[Tuple[str, str], Dict] = {}
    edge_dict: Dict[Tuple[Tuple[str, str], Tuple[str, str], str], Dict] = {}

    # Create a set of existing files (file_name, label) in the repository
    existing_files = set()
    for file_entry in parsed_output:
        file_name = parse_program_name(file_entry.get("name")).upper()
        file_label = file_entry.get("label", "UNKNOWN")
        existing_files.add((file_name, file_label))

    for file_entry in parsed_output:
        file_name = parse_program_name(file_entry.get("name")).upper()
        file_label = file_entry.get("label", "UNKNOWN")
        source_key = (file_name, file_label)

        add_node(
            node_dict=node_dict,
            key=source_key,
            name=file_name,
            label=file_label,
            status=NodeStatus.ALIVE.value,
            is_entry_point=False,
        )

        parsed_data = file_entry.get("parsed_data", {})

        if file_label == FileType.COBOL.value:
            process_cobol_file(
                parsed_data, source_key, node_dict, edge_dict, existing_files
            )
        elif file_label == FileType.JCL_IBM.value:
            process_jcl_file(
                parsed_data, source_key, node_dict, edge_dict, existing_files
            )

    return node_dict, edge_dict


def add_node(
    node_dict: Dict[Tuple[str, str], Dict],
    key: Tuple[str, str],
    name: str,
    label: str,
    status: str,
    is_entry_point: bool,
):
    """
    Adds a node to the node_dict if it doesn't already exist.
    """
    if key not in node_dict:
        node_dict[key] = {
            "name": name,
            "label": label,
            "group": [],
            "status": status,
            "is_entry_point": is_entry_point,
        }


def add_edge(
    edge_dict: Dict[Tuple[Tuple[str, str], Tuple[str, str], str], Dict],
    source_key: Tuple[str, str],
    target_key: Tuple[str, str],
    label: str,
    properties: Dict,
):
    """
    Adds an edge to the edge_dict. If the edge already exists, it updates the properties.
    """
    edge_key = (source_key, target_key, label)
    if edge_key not in edge_dict:
        edge_dict[edge_key] = {
            "source": source_key,
            "target": target_key,
            "label": label,
            "properties": properties,
        }
    else:
        # Merge properties based on the relationship type
        if label == RelationshipLabel.STATIC_CALL.value:
            edge_dict[edge_key]["properties"]["calls"].extend(
                properties.get("calls", [])
            )
        elif label == RelationshipLabel.EXEC_PGM.value:
            edge_dict[edge_key]["properties"]["steps"].extend(
                properties.get("steps", [])
            )
        # Add more conditions if other relationship types require property aggregation


def process_cobol_file(
    parsed_data: Dict,
    source_key: Tuple[str, str],
    node_dict: Dict[Tuple[str, str], Dict],
    edge_dict: Dict[Tuple[Tuple[str, str], Tuple[str, str], str], Dict],
    existing_files: Set[Tuple[str, str]],
):
    """
    Processes COBOL file entries to extract static calls, copybook relationships, and CICS interactions.
    """
    # Process Static Calls
    call_params = extract_static_calls(parsed_data)
    for program_name, params in call_params.items():
        cleaned_program_name = parse_program_name(program_name)
        label = (
            "UTILITY"
            if cleaned_program_name in IBM_MAINFRAME_UTILITIES
            else FileType.COBOL.value
        )
        called_program_key = (cleaned_program_name, label)

        # Determine the status based on whether the program exists
        status = (
            NodeStatus.ALIVE.value
            if called_program_key in existing_files
            else NodeStatus.MISSING.value
        )

        if called_program_key not in node_dict:
            add_node(
                node_dict=node_dict,
                key=called_program_key,
                name=cleaned_program_name,
                label=label,
                status=status,
                is_entry_point=False,
            )

        add_edge(
            edge_dict=edge_dict,
            source_key=source_key,
            target_key=called_program_key,
            label=RelationshipLabel.STATIC_CALL.value,
            properties={"calls": params},
        )

    # Process Copybook Relationships
    copy_loc_map = parsed_data.get("copyLocFileMap", {})
    for copybook_id in copy_loc_map.values():
        cleaned_copybook_id = parse_program_name(copybook_id)  # Parse copybook name
        label = (
            "UTILITY"
            if cleaned_copybook_id in IBM_MAINFRAME_UTILITIES
            else FileType.COPY.value
        )
        copybook_key = (cleaned_copybook_id, label)

        status = (
            NodeStatus.ALIVE.value
            if copybook_key in existing_files
            else NodeStatus.MISSING.value
        )

        if copybook_key not in node_dict:
            add_node(
                node_dict=node_dict,
                key=copybook_key,
                name=cleaned_copybook_id,
                label=label,
                status=status,
                is_entry_point=False,
            )

        add_edge(
            edge_dict=edge_dict,
            source_key=source_key,
            target_key=copybook_key,
            label=RelationshipLabel.HAS_COPYBOOK.value,
            properties={},
        )

    # Process CICS Interactions
    cics_map = parsed_data.get("cics_map", {})
    for mapset_info in cics_map.values():
        if "mapset" in mapset_info:
            mapset_id = extract_mapset_id(mapset_info["mapset"])
            if mapset_id:
                bms_key = (mapset_id, "BMS")

                status = (
                    NodeStatus.ALIVE.value
                    if bms_key in existing_files
                    else NodeStatus.MISSING.value
                )

                if bms_key not in node_dict:
                    add_node(
                        node_dict=node_dict,
                        key=bms_key,
                        name=mapset_id,
                        label=FileType.BMS.value,
                        status=status,
                        is_entry_point=False,
                    )

                add_edge(
                    edge_dict=edge_dict,
                    source_key=bms_key,
                    target_key=source_key,
                    label=RelationshipLabel.HAS_INTERACT.value,
                    properties={},
                )


def extract_static_calls(parsed_data: Dict) -> Dict[str, List[Dict]]:
    """
    Extracts static call relationships from parsed_data.
    Returns empty dict if no calls found or description is empty.
    """
    call_params = {}
    for value in parsed_data.get("startSectionMap", {}).values():
        if value.get("Calls"):
            description = value.get("Description", None)
            # Skip if description is None or empty array
            if not description:
                continue

            if isinstance(description, list):
                # Skip if array has only 1 or 0 elements
                if len(description) <= 1:
                    continue

                for statement_list in description[1:]:
                    for statement in statement_list:
                        if "callStatement" in statement:
                            temp_entry = {
                                "paragraph": value.get("Section_name", ""),
                                "identifier": [],
                            }
                            program_name = None
                            for identifier in statement:
                                if "programName####" in identifier:
                                    parts = identifier.split("####")
                                    if len(parts) == 2:
                                        _, program_name = parts
                                        temp_entry["programName"] = program_name
                                elif "identifier####" in identifier:
                                    parts = identifier.split("####")
                                    if len(parts) == 2:
                                        _, val = parts
                                        temp_entry["identifier"].append(val)

                            if program_name:
                                call_params.setdefault(program_name, []).append(
                                    temp_entry
                                )
    return call_params


def parse_program_name(program_name: str) -> str:
    """
    Cleans the program name by removing quotes and file extensions.
    """
    # Remove quotes
    program_name = re.sub(r"['\"]", "", program_name)
    # Remove file extension
    program_name = os.path.splitext(program_name)[0]
    return program_name


def extract_mapset_id(mapset_str: str) -> str:
    """
    Extracts the mapset ID from a mapset string using regex.
    """
    match_obj = re.search(r"MAPSET\('(.+?)'\)", mapset_str)
    if match_obj:
        return match_obj.group(1)
    return ""


def process_jcl_file(
    parsed_data: Dict,
    source_key: Tuple[str, str],
    node_dict: Dict[Tuple[str, str], Dict],
    edge_dict: Dict[Tuple[Tuple[str, str], Tuple[str, str], str], Dict],
    existing_files: Set[Tuple[str, str]],
):
    """
    Processes JCL_IBM file entries to extract execution steps.
    """
    exec_statement_map = parsed_data.get("exec_statement_map", {})
    for step_info in exec_statement_map.values():
        pgm = step_info.get("parameters_map", {}).get("PGM")
        if pgm:
            step_properties = extract_jcl_step_properties(step_info)
            label = (
                "UTILITY" if pgm in IBM_MAINFRAME_UTILITIES else FileType.COBOL.value
            )
            pgm_key = (pgm, label)

            status = (
                NodeStatus.ALIVE.value
                if pgm_key in existing_files
                else NodeStatus.MISSING.value
            )

            if pgm_key not in node_dict:
                add_node(
                    node_dict=node_dict,
                    key=pgm_key,
                    name=pgm,
                    label=label,
                    status=status,
                    is_entry_point=False,
                )

            add_edge(
                edge_dict=edge_dict,
                source_key=source_key,
                target_key=pgm_key,
                label=RelationshipLabel.EXEC_PGM.value,
                properties={"steps": [step_properties]},
            )


def extract_jcl_step_properties(step_info: Dict) -> Dict:
    """
    Extracts and structures properties from a JCL step.
    """
    step_name = step_info.get("step_name", "")
    code = step_info.get("code", {})
    statements = step_info.get("statements", [])

    return {
        "step_name": step_name,
        "code": {
            "content": code.get("content"),
            "start_line": code.get("start_line"),
            "end_line": code.get("end_line"),
        },
        "statements": [
            {
                "ddname": stmt.get("ddname"),
                "parameters_map": stmt.get("parameters_map"),
                "dataset_map_list": stmt.get("dataset_map_list"),
                "logic": stmt.get("logic"),
            }
            for stmt in statements
        ],
    }


# --------------------------
# Node and Edge Model Functions
# --------------------------


def convert_to_node_models(
    node_dict: Dict[Tuple[str, str], Dict], repository_id: str
) -> List[NodeModel]:
    """
    Converts raw node data to NodeModel instances.
    """
    nodes = []
    for key, data in node_dict.items():
        node = NodeModel(
            id=PyObjectId(),
            name=data["name"],
            label=data["label"],
            group=data["group"],
            status=NodeStatus[data["status"]],
            repository_id=PyObjectId(repository_id),
            is_entry_point=data.get("is_entry_point", False),
        )
        nodes.append(node)
    return nodes


def convert_to_edge_models(
    edge_dict: Dict[Tuple[ObjectId, ObjectId, RelationshipLabel], Dict],
    node_lookup: Dict[Tuple[str, str], NodeModel],
    repository_id: str,
) -> List[EdgeModel]:
    """
    Converts raw edge data to EdgeModel instances.
    """
    edges = []
    for key, data in edge_dict.items():
        source_key = data["source"]
        target_key = data["target"]
        source_node = node_lookup.get(source_key)
        target_node = node_lookup.get(target_key)
        if not source_node or not target_node:
            continue  # Skip edges with missing nodes

        edge = EdgeModel(
            id=PyObjectId(),
            source=source_node.id,
            target=target_node.id,
            label=data["label"],
            properties=data["properties"],
            repository_id=PyObjectId(repository_id),
        )
        edges.append(edge)
    return edges


# --------------------------
# Main Graph Creation and Retrieval Functions
# --------------------------

from app.schemas.graph_schema import Edge, GetDependenciesGraph


async def create_graph(
    repository_id: str, db: AsyncIOMotorClient = Depends(get_database)
) -> GetDependenciesGraph:
    """
    Main function to create a graph structure from parsed data and return the graph data.
    """
    parsed_output = fetch_parsed_data(repository_id)
    node_dict, edge_dict = extract_graph(parsed_output)

    # Create NetworkX graph
    graph = nx.DiGraph()

    # Add nodes to the graph
    for node_key, node in node_dict.items():
        graph.add_node(
            node_key,
            name=node["name"],
            label=node["label"],
            group=node["group"],
            status=node["status"],
        )

    # Add edges to the graph
    for edge_key, edge in edge_dict.items():
        source_key = edge["source"]
        target_key = edge["target"]
        graph.add_edge(
            source_key, target_key, label=edge["label"], **edge["properties"]
        )

    # Detect entry points and build graph data
    entry_points = detect_entry_points(graph)
    graph_data = build_graph_data(graph, entry_points)
    nodes = graph_data["nodes"]
    edges = graph_data["edges"]

    # Build mappings for nodes
    node_key_map = {}  # Map from (name, label) to node data
    node_id_to_key = {}  # Map from node 'id' to (name, label)
    for node in nodes:
        node_key = (node["name"], node["label"])
        node_key_map[node_key] = node
        node_id_to_key[node["id"]] = node_key

    # Prepare bulk operations for nodes
    node_bulk_ops = []
    repository_id_obj = ObjectId(repository_id)
    for node_key, node_data in node_key_map.items():
        node_bulk_ops.append(
            pymongo.UpdateOne(
                {
                    "name": node_data["name"],
                    "label": node_data["label"],
                    "repository_id": repository_id_obj,
                },
                {
                    "$set": {
                        "name": node_data["name"],
                        "label": node_data["label"],
                        "group": node_data["group"],
                        "status": NodeStatus[node_data["status"]],
                        "repository_id": repository_id_obj,
                        "is_entry_point": node_data.get("is_entry_point", False),
                    }
                },
                upsert=True,
            )
        )

    # Execute bulk operations for nodes
    if node_bulk_ops:
        await db.nodes.bulk_write(node_bulk_ops)

    # Query existing nodes to get their IDs
    existing_nodes_cursor = db.nodes.find({"repository_id": repository_id_obj})
    existing_nodes = await existing_nodes_cursor.to_list(length=10000)
    existing_node_ids = {
        (node["name"], node["label"]): node["_id"] for node in existing_nodes
    }

    # Prepare bulk operations for edges
    edge_bulk_ops = []
    for edge in edges:
        source_node_key = node_id_to_key.get(edge["source"])
        target_node_key = node_id_to_key.get(edge["target"])
        if not source_node_key or not target_node_key:
            continue  # Skip if nodes are missing

        source_id = existing_node_ids.get(source_node_key)
        target_id = existing_node_ids.get(target_node_key)
        if source_id and target_id:
            edge_bulk_ops.append(
                pymongo.UpdateOne(
                    {
                        "source": source_id,
                        "target": target_id,
                        "repository_id": repository_id_obj,
                    },
                    {
                        "$set": {
                            "source": source_id,
                            "target": target_id,
                            "type": edge.get("type", ""),
                            "group": edge.get("group", []),
                            "properties": edge.get("properties", {}),
                            "repository_id": repository_id_obj,
                        }
                    },
                    upsert=True,
                )
            )

    # Execute bulk operations for edges
    if edge_bulk_ops:
        await db.edges.bulk_write(edge_bulk_ops)

    return await get_graph(repository_id, db=db, entrypoint_ids=None)


async def validate_paging_and_filters(
    page_number: int, page_limit: int, node_limit: int
):
    """Validate input filters and pagination parameters."""
    if page_number < 1:
        raise HTTPException(
            status_code=400, detail="Page number must be greater than 0"
        )
    if page_limit < 1:
        raise HTTPException(status_code=400, detail="Page limit must be greater than 0")
    if node_limit < 1:
        raise HTTPException(status_code=400, detail="Node limit must be greater than 0")


async def build_entrypoint_query(
    repository_id: str,
    complexity_filter: Optional[int],
    loc_filter: Optional[int],
    nof_filter: Optional[int],
    criticality_filter,
    entrypoint_ids: Optional[List[str]],
) -> dict:
    """Build the query for filtering entry points."""
    repository_id_obj = ObjectId(repository_id)

    query = {
        "repository_id": repository_id_obj,
    }

    if complexity_filter:
        query["complexity"] = {"$lte": complexity_filter}

    if loc_filter:
        query["line_of_code"] = {"$lte": loc_filter}

    if nof_filter:
        query["number_of_files"] = {"$lte": nof_filter}

    if criticality_filter:
        query["criticality"] = {"$in": criticality_filter}

    if entrypoint_ids:
        try:
            name_filter = [ObjectId(id) for id in entrypoint_ids]
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid entrypoint_ids format")
        if not name_filter:
            raise HTTPException(
                status_code=404,
                detail="No matching entry points found for provided IDs",
            )
        query["_id"] = {"$in": name_filter}

    return query


async def fetch_entrypoints_with_pagination(
    db: AsyncIOMotorClient, query: dict, page_number: int, page_limit: int
) -> Tuple[List[dict], int]:
    """Fetch entry points with pagination and return total count."""
    total_entries = await db.entry_points.count_documents(query)

    if total_entries == 0:
        raise HTTPException(
            status_code=404,
            detail="No matching entry points found for the given filters",
        )

    skip = (page_number - 1) * page_limit
    if skip >= total_entries:
        raise HTTPException(
            status_code=404, detail="Page number exceeds available data"
        )

    entry_points_cursor = db.entry_points.find(query).skip(skip).limit(page_limit)
    entry_points = await entry_points_cursor.to_list(length=page_limit)

    return entry_points, total_entries


async def fetch_entrypoints_with_nodes(
    db: AsyncIOMotorClient, query: dict, page_number: int, page_limit: int
) -> List[dict]:
    """Fetch entry points and join with nodes using aggregation, applying pagination."""
    skip = (page_number - 1) * page_limit

    pipeline = [
        {"$match": query},  # Apply filters
        {
            "$lookup": {
                "from": "nodes",
                "let": {"repo_id": "$repository_id", "entry_name": "$name"},
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {
                                "$and": [
                                    {"$eq": ["$repository_id", "$$repo_id"]},
                                    {"$eq": ["$name", "$$entry_name"]},
                                    {"$eq": ["$is_entry_point", True]},
                                ]
                            }
                        }
                    }
                ],
                "as": "matched_nodes",
            }
        },
        {
            "$unwind": {"path": "$matched_nodes", "preserveNullAndEmptyArrays": True}
        },  # Avoid errors if no match
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "label": 1,
                "repository_id": 1,
                "number_of_files": 1,
                "complexity": 1,
                "line_of_code": 1,
                "criticality": 1,
                "refer_id": "$matched_nodes._id",
            }
        },
        {"$skip": skip},  # Apply pagination offset
        {"$limit": page_limit},  # Limit per page
    ]

    entry_points_cursor = db.entry_points.aggregate(pipeline)
    entry_points = await entry_points_cursor.to_list(length=page_limit)

    return entry_points


async def calculate_filter_graph_data(
    repository_id: str,
    node_limit: int,
    complexity_filter: Optional[int],
    loc_filter: Optional[int],
    nof_filter: Optional[int],
    criticality_filter,
    entrypoint_ids: Optional[List[str]] = None,
    db: AsyncIOMotorClient = Depends(get_database),
    page_number: Optional[int] = 1,
    page_limit: Optional[int] = 100,
) -> Tuple[List[dict], List[str], int, int]:
    """Calculate node limit and return entry point IDs within the limit, with pagination."""

    # Validate input
    await validate_paging_and_filters(page_number, page_limit, node_limit)

    # Build query
    query = await build_entrypoint_query(
        repository_id,
        complexity_filter,
        loc_filter,
        nof_filter,
        criticality_filter,
        entrypoint_ids,
    )

    # Fetch paginated entry points with nodes using aggregation
    entry_points = await fetch_entrypoints_with_nodes(
        db, query, page_number, page_limit
    )

    # Calculate node limit and filter entry points
    temp_node_limit = 0
    entry_point_name_filter = []

    for entry in entry_points:
        number_of_files = entry.get("number_of_files", 0)

        # Check if adding this entry would exceed the node limit
        if temp_node_limit + number_of_files > node_limit:
            break

        temp_node_limit += number_of_files
        entry_point_name_filter.append(entry["name"])

    total_entries = len(entry_points)

    return entry_points, entry_point_name_filter, total_entries


def validate_object_id(id_str: Optional[str], field_name: str) -> ObjectId:
    if not id_str:
        logger.error(f"Missing required field: {field_name}")
        raise ValueError(f"Missing required field: {field_name}")
    try:
        return ObjectId(id_str)
    except Exception as e:
        logger.exception(f"Invalid ObjectId for field '{field_name}': {id_str}")
        raise ValueError(f"Invalid ObjectId for field '{field_name}': {id_str}") from e


async def get_child_node_ids(
        db, repository_id_str: str, source_node_id_str: str
) -> List[dict]:
    repository_id = validate_object_id(repository_id_str, "repository_id")
    source_node_id = validate_object_id(source_node_id_str, "source_node_id")

    pipeline = [
        {
            "$match": {
                "repository_id": repository_id,
                "source": source_node_id,
                "type": {"$ne": "EXEC_CICS"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "target": 1
            }
        }
    ]
    try:
        results = await db.edges.aggregate(pipeline).to_list(length=None)
        logger.info(f"Retrieved {len(results)} child node IDs.")
        return results
    except Exception as e:
        logger.exception("Failed to aggregate child node IDs.")
        return []


async def get_child_node_detail(
        db, repository_id: str, source_node_id: str
) -> List[dict]:
    try:
        list_sub_nodes = await get_child_node_ids(db, repository_id, source_node_id)
        target_ids = [item["target"] for item in list_sub_nodes if "target" in item]

        if not target_ids:
            return []

        node_filter = {"_id": {"$in": target_ids}}
        results = await get_node_extend_data(db=db, node_filter=node_filter, node_limit=len(target_ids))
        logger.info(f"Retrieved {len(results)} sub-nodes for source {source_node_id}.")
        return results
    except Exception as e:
        logger.exception("Failed to get child node detail.")
        return []


async def process_child_node(
        db, repository_id: str, target_id: ObjectId
) -> dict:
    try:
        child_node_data = await get_node_extend_data(db, {"_id": target_id}, 1)
        if not child_node_data or not isinstance(child_node_data, list):
            logger.warning(f"No node data found for target ID {target_id}")
            return {}

        sub_node_data = await get_child_node_detail(db, repository_id, str(target_id))
        child_node_data[0]['sub_nodes'] = sub_node_data
        return child_node_data[0]
    except Exception as e:
        logger.exception(f"Failed to process child node {target_id}")
        return {}


async def get_detail_dependency_entry_point(
        db,
        repository_id: Optional[str] = None,
        entrypoint_id: Optional[str] = None,
        refer_id: Optional[str] = None
) -> GetDetailDependencyEntryPoint:
    repo_obj_id = validate_object_id(repository_id, "repository_id")
    entry_obj_id = validate_object_id(entrypoint_id, "entrypoint_id")
    refer_obj_id = validate_object_id(refer_id, "refer_id")

    try:
        entrypoint_data = await db.entry_points.find_one({"_id": entry_obj_id})
        if not entrypoint_data:
            logger.error(f"Entrypoint with ID {entrypoint_id} not found.")
            raise ValueError(f"Entrypoint with ID {entrypoint_id} not found.")

        child_node_ids = await get_child_node_ids(db, str(repo_obj_id), str(refer_obj_id))
        tasks = [
            process_child_node(db, str(repo_obj_id), child_id["target"])
            for child_id in child_node_ids if "target" in child_id
        ]
        child_nodes = await asyncio.gather(*tasks)

        logger.info(f"Retrieved detail dependency for entrypoint {entrypoint_id}")
        return GetDetailDependencyEntryPoint(
            parent_entry_point=entrypoint_data,
            child_nodes=child_nodes
        )
    except Exception as e:
        logger.exception("Failed to retrieve dependency entry point.")
        raise e


async def get_graph(
    repository_id: str,
    db: AsyncIOMotorClient = Depends(get_database),
    entrypoint_ids: Optional[List[str]] = None,
    node_limit: Optional[int] = 1000,
    complexity_filter: Optional[int] = None,
    nof_filter: Optional[int] = None,
    criticality_filter: Optional[List[EntryPointCriticality]] = None,
    loc_filter: Optional[int] = None,
    page_number: Optional[int] = 1,
    page_limit: Optional[int] = 100,
) -> GetDependenciesGraph:
    """Retrieve graph data and filter nodes and edges based on entry points with pagination."""
    repository_id_obj = ObjectId(repository_id)

    entry_points, entry_point_filter_name, total_entries = (
        await calculate_filter_graph_data(
            repository_id,
            node_limit,
            complexity_filter,
            loc_filter,
            nof_filter,
            criticality_filter,
            entrypoint_ids,
            db,
            page_number,
            page_limit,
        )
    )

    if entrypoint_ids and not entry_point_filter_name:
        raise HTTPException(
            status_code=404, detail="No matching entry point names found."
        )

    if entry_points:
        node_filter = {
            "$and": [
                {"group": {"$in": entry_point_filter_name}},
                {"repository_id": repository_id_obj},
            ]
        }

        total_entry_points = total_entries
    else:
        node_filter = {"repository_id": repository_id_obj}
        total_entry_points = 0
    nodes, total_nodes = await asyncio.gather(
        get_node_extend_data(db, node_filter, node_limit),
        db.nodes.count_documents(node_filter),
    )
    node_ids = [node["_id"] for node in nodes]

    edges_filter = (
        {"repository_id": repository_id_obj}
        if not node_ids
        else {"source": {"$in": node_ids}, "target": {"$in": node_ids}}
    )

    edge_limit = node_limit * (node_limit - 1)  # for directed graph without self-loops
    edges, total_edges = await asyncio.gather(
        db.edges.find(edges_filter).limit(edge_limit).to_list(None),
        db.edges.count_documents(edges_filter),
    )

    return GetDependenciesGraph(
        total_entry_points=total_entry_points,
        repository_id=PyObjectId(repository_id),
        nodes=[ExtendNode(**node) for node in nodes],
        edges=[Edge(**edge) for edge in edges],
        entry_points=entry_points,
        page=page_number,
        page_size=page_limit,
        total=total_nodes + total_edges,
    )


async def get_node_extend_data(
    db: AsyncIOMotorClient, node_filter: Dict[str, Any], node_limit: int
) -> List[Dict[str, Any]]:
    pipeline = [
        {"$match": node_filter},  # Apply filter to select nodes
        {
            "$lookup": {
                "from": "reverse_engineering",
                "let": {
                    "name": "$name",
                    "label": "$label",  # label in nodes
                    "repository_id": "$repository_id",
                },
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {
                                "$and": [
                                    {"$eq": ["$name", "$$name"]},
                                    {
                                        "$eq": ["$type", "$$label"]
                                    },  # type in reverse_engineering
                                    {"$eq": ["$repository_id", "$$repository_id"]},
                                ]
                            }
                        }
                    },
                    {"$project": {"_id": 0, "output": 1}},  # Only keep output field
                ],
                "as": "reverse_engineering_data",
            }
        },
        {
            "$addFields": {
                "reverse_output": {
                    "$arrayElemAt": ["$reverse_engineering_data", 0]  # Get first match
                }
            }
        },
        {
            "$addFields": {
                "line_of_code": {
                    "$ifNull": [
                        "$reverse_output.output.line_of_code",
                        1,
                    ]  # Default to 1 if None
                },
                "complexity": {
                    "$ifNull": [
                        "$reverse_output.output.complexity",
                        1,
                    ]  # Default to 1 if None
                },
            }
        },
        {
            "$project": {
                "reverse_engineering_data": 0,  # Remove lookup data
                "reverse_output": 0,  # Remove extracted field
            }
        },
        {"$limit": node_limit},  # Limit the number of nodes returned
    ]

    nodes = await db.nodes.aggregate(pipeline).to_list(None)
    return nodes  # Return the enriched nodes


async def delete_graph(
    repository_id: str, db: AsyncIOMotorClient = Depends(get_database)
) -> Dict:
    """
    Removes the graph data for a specific repository.
    """
    # Check if the graph exists
    repository_id_obj = ObjectId(repository_id)
    existing_nodes = await db.nodes.find_one({"repository_id": repository_id_obj})
    existing_edges = await db.edges.find_one({"repository_id": repository_id_obj})
    if not existing_nodes:
        return {
            "status": "error",
            "message": "Graph not found for the repository.",
        }
    if not existing_edges:
        return {
            "status": "error",
            "message": "Graph not found for the repository.",
        }
    await db.nodes.delete_many({"repository_id": repository_id_obj})
    await db.edges.delete_many({"repository_id": repository_id_obj})
    return {"status": "success", "message": "Graph data removed."}


async def get_entrypoints(
    repository_id: str,
    db: AsyncIOMotorClient = Depends(get_database),
    complexity_filter: Optional[int] = 0,
    loc_filter: Optional[int] = 0,
    number_of_files_filter: Optional[int] = 1,
    criticality_filter: Optional[EntryPointCriticality] = None,
    type_filter: Optional[FileType] = None,
    skip: int = 0,
    limit: int = 100,
) -> Tuple[List[EntryPointModel], int]:
    """
    Retrieves entry points for a specific repository.
    """
    query = {
        "repository_id": ObjectId(repository_id),
    }

    if complexity_filter:
        query["complexity"] = {"$lte": complexity_filter}

    if loc_filter:
        query["line_of_code"] = {"$lte": loc_filter}

    if number_of_files_filter:
        query["number_of_files"] = {"$lte": number_of_files_filter}

    if criticality_filter:
        query["criticality"] = criticality_filter.value

    if type_filter:
        query["label"] = type_filter.value

    total_entry_points = await db.entry_points.count_documents(query)
    entry_points = (
        await db.entry_points.find(query).sort("_id").skip(skip).limit(limit).to_list()
    )
    return [
        EntryPointModel(**entry_point_data) for entry_point_data in entry_points
    ], total_entry_points


async def get_deadnodes(
    repository_id: str,
    db: AsyncIOMotorClient = Depends(get_database),
    skip: int = 0,
    limit: int = 100,
) -> Dict[str, Any]:
    """
    Retrieves entry points for a specific repository.
    """
    repository_id_obj = ObjectId(repository_id)

    total_nodes = await db.nodes.count_documents(
        {
            "repository_id": repository_id_obj,
            "status": {"$ne": NodeStatus.MISSING.value},
        }
    )
    total_dead = await db.nodes.count_documents(
        {"repository_id": repository_id_obj, "status": NodeStatus.DEAD.value}
    )

    list_of_deadnodes = [
        (node["name"], node["label"])
        for node in (
            await db.nodes.find(
                {"repository_id": repository_id_obj, "status": NodeStatus.DEAD.value}
            )
            .sort("_id")
            .to_list()
        )
    ]

    complexity_reduction = 0

    files: List[FileForDeadCode] = []
    for dead_node_name, dead_node_label in list_of_deadnodes:
        rv = await get_reverse_engineering_report(
            db, repository_id, dead_node_label, dead_node_name
        )
        if rv is None:
            files.append(
                FileForDeadCode(
                    file_name=dead_node_name,
                    type=dead_node_label,
                    lines_of_code=0,
                    complexity=0,
                )
            )
            continue

        complexity = 0
        lines_of_code = 0
        if isinstance(rv.output, dict):
            complexity = rv.output.get("complexity", 0)
            complexity_reduction += complexity
            lines_of_code = rv.output.get("line_of_code", 0)
        files.append(
            FileForDeadCode(
                file_name=dead_node_name,
                type=dead_node_label,
                lines_of_code=lines_of_code,
                complexity=complexity,
            )
        )

    files.sort(key=lambda x: x.complexity, reverse=True)
    files = files[skip : skip + limit]

    complexity_data = await get_complexity_aggregated_data_of_repository_id(
        db, repository_id
    )
    total_complexity = (
        complexity_data["average_complexity"]
        * complexity_data["number_of_complexities"]
    )

    complexity_reduction_percentage = (
        complexity_reduction / max(1, total_complexity) * 100
    )

    return {
        "dead_total": {"dead": total_dead, "total": total_nodes},
        "complexity_reduction_percentage": complexity_reduction_percentage,
        "files": files,
    }
