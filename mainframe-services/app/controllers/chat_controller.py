import uuid
from datetime import datetime
from typing import Any, AsyncGenerator, Dict, List, Optional, Set

from bson import ObjectId
from fastapi import HTTPException
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.messages.ai import AIMessage
from langchain_core.messages.tool import ToolMessage
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.agents.graph import graph
from app.config.nebula import get_nebula_client
from app.constants.graph import NEBULA_SPACE_NAME_PREFIX, RelationshipLabel
from app.controllers.graph_controller import fetch_parsed_data
from app.models.chat import Chat, Message
from app.schemas import chat_schema, nebula_graph_schema


async def create_chat(db: AsyncIOMotorDatabase, chat: Chat) -> str:
    """
    Create a new chat session.

    Args:
        db: Database connection
        chat: Chat model instance

    Returns:
        Inserted chat ID as string

    Raises:
        HTTPException: If chat creation fails
    """
    try:
        # Convert to dict and handle ObjectId
        chat_dict = {
            "project_id": ObjectId(chat.project_id),
            "messages": [msg.model_dump() for msg in chat.messages],
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }

        # Insert into database
        result = await db.chats.insert_one(chat_dict)

        # Return the inserted ID as string
        return str(result.inserted_id)

    except Exception as e:
        logger.error(f"Error creating chat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create chat: {str(e)}")


async def get_chat(db: AsyncIOMotorDatabase, chat_id: str):
    chat = await db.chats.find_one({"_id": ObjectId(chat_id)})
    if chat:
        return Chat(**chat)


async def get_chat_by_project(
    db: AsyncIOMotorDatabase, project_id: str
) -> Optional[Chat]:
    """
    Get a chat by project ID.

    Args:
        db: Database connection
        project_id: Project ID to find chat for

    Returns:
        Chat model if found, None otherwise
    """
    try:
        chat_dict = await db.chats.find_one({"project_id": ObjectId(project_id)})
        if not chat_dict:
            return None

        # Convert messages to Message models
        messages = [Message(**msg) for msg in chat_dict.get("messages", [])]

        # Create and return Chat model
        return Chat(
            id=chat_dict["_id"],
            project_id=chat_dict["project_id"],
            messages=messages,
            created_at=chat_dict.get("created_at", datetime.utcnow()),
            updated_at=chat_dict.get("updated_at", datetime.utcnow()),
        )

    except Exception as e:
        logger.error(f"Error getting chat for project {project_id}: {str(e)}")
        return None


async def chat(
    db: AsyncIOMotorDatabase,
    chat_id: str,
    message: chat_schema.MessageCreate,
) -> AsyncGenerator[str, None]:
    """
    Process chat messages and stream AI responses.

    Args:
        db: Database connection
        chat_id: ID of the chat session
        message: User's message

    Yields:
        AI response content as it's generated
    """
    try:
        # Get chat session
        chat = await get_chat_session(db, chat_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Chat not found")

        # Prepare messages and config
        messages = prepare_chat_messages(chat.messages, message)
        config = prepare_graph_config(
            message.repository_id,
            message.config.is_assessed,
            message.config.is_reversed,
        )
        # Stream responses
        async for response in stream_ai_responses(messages, config):
            yield response

        # Save chat history
        await save_chat_history(db, chat_id, message, response)

    except IndexError as e:
        logger.error(f"Index error in chat processing: {str(e)}")
        raise HTTPException(
            status_code=500, detail="No valid repository found for processing"
        )
    except Exception as e:
        logger.error(f"Error in chat processing: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Chat processing error: {str(e)}")


async def get_chat_session(db: AsyncIOMotorDatabase, chat_id: str) -> Chat:
    """Get and validate chat session."""
    chat = await get_chat(db, chat_id=chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat


async def get_repository_config(db: AsyncIOMotorDatabase, project_id: str) -> Dict:
    """Get repository configuration for the project."""
    repository = await get_repositories_by_project(db, project_id)
    return repository[0] if isinstance(repository, list) else repository


def prepare_chat_messages(
    chat_messages: List, new_message: chat_schema.MessageCreate
) -> List:
    """Prepare messages for the graph processing."""
    try:
        # Ensure chat_messages is not None
        messages = chat_messages or []

        # Create new message
        user_message = chat_schema.Message(
            content=new_message.content, sender=new_message.sender
        )

        # Combine existing messages with new message
        messages = list(messages) + [user_message]

        # Format messages for graph processing
        return [(message.sender, message.content) for message in messages]

    except Exception as e:
        logger.error(f"Error preparing chat messages: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to prepare chat messages: {str(e)}"
        )


def prepare_graph_config(
    repository_id: str, is_assessed: bool, is_reversed: bool
) -> Dict:
    """Prepare configuration for graph processing."""

    return {
        "configurable": {
            "thread_id": str(uuid.uuid4()),
            "repository_id": repository_id,
            "is_assessed": is_assessed,
            "is_reversed": is_reversed,
        }
    }


async def stream_ai_responses(
    messages: List, config: Dict
) -> AsyncGenerator[str, None]:
    """Stream AI responses from the graph."""
    try:
        async for event in graph.astream(
            {"messages": messages}, config, stream_mode="values"
        ):
            messages = event.get("messages", [])
            if messages and (isinstance(messages[-1], (AIMessage, ToolMessage))):
                yield messages[-1].content
    except Exception as e:
        logger.error(f"Error streaming AI responses: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to stream AI responses: {str(e)}"
        )


async def save_chat_history(
    db: AsyncIOMotorDatabase,
    chat_id: str,
    user_message: chat_schema.MessageCreate,
    ai_content: str,
):
    """Save the chat history to database."""
    try:
        messages_to_save = [
            chat_schema.Message(
                content=user_message.content, sender=user_message.sender
            ).model_dump(),
            chat_schema.Message(content=ai_content, sender="assistant").model_dump(),
        ]

        await db.chats.update_one(
            {"_id": ObjectId(chat_id)},
            {
                "$push": {"messages": {"$each": messages_to_save}},
                "$set": {"updated_at": messages_to_save[0]["timestamp"]},
            },
        )
    except Exception as e:
        logger.error(f"Error saving chat history: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to save chat history: {str(e)}"
        )


async def delete_chat(db: AsyncIOMotorDatabase, chat_id: str):
    result = await db.chats.delete_one({"_id": ObjectId(chat_id)})
    return result.deleted_count > 0


def create_exec_pgm_edges(
    source: str,
    target: str,
    props: Dict[str, Any],
    rank_map: dict[tuple[str, str], int],
) -> List[nebula_graph_schema.ExecPgm]:
    edges = []
    steps = props.get("steps", [])

    for step in steps:
        # Ensure step_name is always present
        step_name = step.get("step_name", "")
        statements = step.get("statements", [])

        if not statements:
            rank_map[(source, target)] = rank_map.get((source, target), 0) + 1
            edges.append(
                nebula_graph_schema.ExecPgm(
                    source=source,
                    target=target,
                    step_name=step_name,
                    dataset_name=None,
                    rank=rank_map.get((source, target), 0),
                )
            )

        for statement in statements:
            dataset_map_list = statement.get("dataset_map_list", [])
            if not dataset_map_list:
                rank_map[(source, target)] = rank_map.get((source, target), 0) + 1
                edges.append(
                    nebula_graph_schema.ExecPgm(
                        source=source,
                        target=target,
                        step_name=step_name,
                        dataset_name=None,
                        rank=rank_map.get((source, target), 0),
                    )
                )

            for dataset in dataset_map_list:
                rank_map[(source, target)] = rank_map.get((source, target), 0) + 1
                edges.append(
                    nebula_graph_schema.ExecPgm(
                        source=source,
                        target=target,
                        step_name=step_name,
                        dataset_name=dataset.get("dataset_name", ""),
                        rank=rank_map.get((source, target), 0),
                    )
                )
    return edges


def create_call_edges(
    source: str,
    target: str,
    props: Dict[str, Any],
    edge_class: type[nebula_graph_schema.StaticCall | nebula_graph_schema.DynamicCall],
    rank_map: dict[tuple[str, str], int],
) -> List[Any]:
    edges = []
    for call in props.get("calls", []):
        params = call.get("identifier", [])
        procedure = call.get("paragraph")

        if not params:
            rank_map[(source, target)] = rank_map.get((source, target), 0) + 1
            edges.append(
                edge_class(
                    source=source,
                    target=target,
                    procedure=procedure,
                    param=None,
                    rank=rank_map.get((source, target), 0),
                )
            )
            continue

        edges.extend(
            [
                edge_class(
                    source=source, target=target, procedure=procedure, param=param
                )
                for param in params
            ]
        )
    return edges


async def init_nebula(db: AsyncIOMotorDatabase, repository_id: str) -> None:
    nebula_client = get_nebula_client(f"{NEBULA_SPACE_NAME_PREFIX}{repository_id}")
    logger.info(f"Initializing Nebula graph for repository {repository_id}")

    try:
        # Define node schema factory
        node_schema_factory = {
            "COBOL": nebula_graph_schema.CobolNode,
            "COPY": nebula_graph_schema.CopyNode,
            "JCL_IBM": nebula_graph_schema.JclIbmNode,
            "BMS": nebula_graph_schema.BmsNode,
            "OTHER": nebula_graph_schema.OtherNode,
            "UTILITY": nebula_graph_schema.UtilityNode,
        }

        # Process nodes
        nebula_nodes: Set[Any] = set()
        async for node in db.nodes.find({"repository_id": ObjectId(repository_id)}):
            if node_schema := node_schema_factory.get(node["label"]):
                try:
                    nebula_nodes.add(
                        node_schema(
                            id=str(node["_id"]),
                            name=node.get("name", ""),
                            group=node.get("group", ""),
                            status=node.get("status", ""),
                        )
                    )
                except Exception as e:
                    logger.error(f"Error creating node schema: {str(e)}")

        # Process edges
        edge_type_counts: Dict[str, int] = {label: 0 for label in RelationshipLabel}
        nebula_edges: List[Any] = []
        rank_map: dict[tuple[str, str], int] = {}

        async for edge in db.edges.find({"repository_id": ObjectId(repository_id)}):
            edge_type = edge.get("type")
            source = str(edge.get("source"))
            target = str(edge.get("target"))
            props = edge.get("properties", {})

            try:
                match edge_type:
                    case RelationshipLabel.EXEC_PGM.value:
                        new_edges = create_exec_pgm_edges(
                            source, target, props, rank_map
                        )
                        nebula_edges.extend(new_edges)
                        edge_type_counts["EXEC_PGM"] += len(new_edges)

                    case RelationshipLabel.STATIC_CALL.value:
                        new_edges = create_call_edges(
                            source,
                            target,
                            props,
                            nebula_graph_schema.StaticCall,
                            rank_map,
                        )
                        nebula_edges.extend(new_edges)
                        edge_type_counts["STATIC_CALL"] += len(new_edges)

                    case RelationshipLabel.DYNAMIC_CALL.value:
                        new_edges = create_call_edges(
                            source,
                            target,
                            props,
                            nebula_graph_schema.DynamicCall,
                            rank_map,
                        )
                        nebula_edges.extend(new_edges)
                        edge_type_counts["DYNAMIC_CALL"] += len(new_edges)

                    case RelationshipLabel.HAS_COPYBOOK.value:
                        nebula_edges.append(
                            nebula_graph_schema.HasCopybook(
                                source=source, target=target
                            )
                        )
                        edge_type_counts["HAS_COPYBOOK"] += 1

                    case RelationshipLabel.HAS_INTERACT.value:
                        nebula_edges.append(
                            nebula_graph_schema.HasInteract(
                                source=source, target=target
                            )
                        )
                        edge_type_counts["HAS_INTERACT"] += 1

                    case _:
                        logger.warning(f"Unknown edge type: {edge_type}")

            except Exception as e:
                logger.error(f"Error processing edge: {str(e)}")

        nebula_node_list = list(nebula_nodes)

        statement_nodes, statement_edges = load_statements(
            repository_id, nebula_node_list
        )

        nebula_node_list.extend(statement_nodes)
        nebula_edges.extend(statement_edges)

        # Insert data in batches
        logger.info(
            f"Inserting {len(nebula_node_list)} nodes and {len(nebula_edges)} edges"
        )
        logger.info(f"Edge counts by type: {edge_type_counts}")

        nebula_client.insert_node_batch(nebula_node_list)
        nebula_client.insert_edge_batch(nebula_edges)
        logger.info("Successfully inserted all nodes and edges")

    except Exception as e:
        logger.error(f"Error in init_nebula: {str(e)}")
        raise
    finally:
        nebula_client.close()
    return {
        "message": f"Successfully initialized Nebula graph for repository {repository_id}"
    }


def find_variable_node_by_name(nodes, name):
    for node in nodes:
        if (
            isinstance(
                node,
                (nebula_graph_schema.IdentifierNode, nebula_graph_schema.LiteralNode),
            )
            and node.name == name
        ):
            return node
    return None


def load_statements(repository_id: str, file_nodes: List[nebula_graph_schema.BaseNode]):
    parsed_data = fetch_parsed_data(repository_id)

    nodes = []
    edges = []

    for parsed_data_file in parsed_data:
        if parsed_data_file["label"] != "COBOL":
            continue

        file_name = parsed_data_file["name"]

        file_node = None

        for node in file_nodes:
            if node.name == file_name:
                file_node = node
                break

        if not file_node:
            logger.warning(f"File node not found for file {file_name}")
            continue

        parsed_data_file = parsed_data_file.get("parsed_data", {})

        if not parsed_data_file:
            logger.warning(f"File {file_name} has no parsed data")
            continue

        statements = parsed_data_file["statements"]
        variables = parsed_data_file["variable_list"]
        paragraphs = parsed_data_file["paragraph_list"]

        for i, paragraph in enumerate(paragraphs):
            paragraph_node = nebula_graph_schema.ParagraphNode(
                id=str(ObjectId()),
                name=paragraph["paragraph_name"],
            )
            nodes.append(paragraph_node)
            edges.append(
                nebula_graph_schema.HasParagraph(
                    source=file_node.id, target=paragraph_node.id
                )
            )

        parent_stack = []

        for i, variable in enumerate(variables):
            name = variable["name"]
            id = str(ObjectId())
            variable["id"] = id
            level = variable["level"]

            variable_node = nebula_graph_schema.IdentifierNode(
                id=id,
                name=variable["name"],
                level=variable["level"],
                picture=variable["picture_clause"],
                default_value=variable["default_value"],
            )
            nodes.append(variable_node)

            if level == "01" or level == "77":
                # Clear parent stack for new hierarchy
                parent_stack = []
                parent_stack.append(variable)
                continue

            if level > parent_stack[-1]["level"]:
                edges.append(
                    nebula_graph_schema.HasChild(
                        source=parent_stack[-1]["id"],
                        target=id,
                    )
                )
                parent_stack.append(variable)

            else:
                if len(parent_stack) > 0 and parent_stack[0]["level"] > level:
                    logger.warning(
                        f"Variable: '{variable}' of file '{file_name}' has no parent"
                    )
                    continue

                while parent_stack[-1]["level"] >= level:
                    parent_stack.pop()
                edges.append(
                    nebula_graph_schema.HasChild(
                        source=parent_stack[-1]["id"],
                        target=id,
                    )
                )
                parent_stack.append(variable)

        for statement_dict in statements:
            statement_dict["id"] = str(ObjectId())
            tag = statement_dict["tag"]

            if tag == "SetStatement":
                statement = nebula_graph_schema.SetStatementNode(
                    id=statement_dict["id"],
                    start_line=statement_dict["start_line"],
                    stop_line=statement_dict["stop_line"],
                    code_content=statement_dict["raw"],
                )
                nodes.append(statement)

                set_to_statement = statement_dict.get("setToStatement", None)
                if set_to_statement is None:
                    logger.warning(f"Set statement has no setToStatement")
                    logger.warning(f"Statement: {statement_dict} of file {file_name}")
                    continue
                for set_to in set_to_statement:
                    if set_to["identifier_2"]:
                        existing_variable_node = find_variable_node_by_name(
                            nodes, set_to["identifier_2"]
                        )

                        if not existing_variable_node:
                            new_variable_id = str(ObjectId())
                            nodes.append(
                                nebula_graph_schema.IdentifierNode(
                                    id=new_variable_id,
                                    name=set_to["identifier_2"],
                                    level="",
                                    picture=None,
                                    default_value=None,
                                )
                            )

                            edges.append(
                                nebula_graph_schema.Target(
                                    source=statement.id,
                                    target=new_variable_id,
                                )
                            )
                        else:
                            edges.append(
                                nebula_graph_schema.Target(
                                    source=statement.id,
                                    target=existing_variable_node.id,
                                )
                            )

                    if set_to["literal_2"]:
                        existing_variable_node = find_variable_node_by_name(
                            nodes, set_to["literal_2"]
                        )

                        if not existing_variable_node:
                            new_variable_id = str(ObjectId())

                            nodes.append(
                                nebula_graph_schema.IdentifierNode(
                                    id=new_variable_id,
                                    name=set_to["literal_2"],
                                    level="",
                                    picture=None,
                                    default_value=None,
                                )
                            )

                            edges.append(
                                nebula_graph_schema.Target(
                                    source=statement.id,
                                    target=new_variable_id,
                                )
                            )
                        else:
                            edges.append(
                                nebula_graph_schema.Target(
                                    source=statement.id,
                                    target=existing_variable_node.id,
                                )
                            )

                    for identifier_1 in set_to["identifier_1"]:
                        existing_variable_node = find_variable_node_by_name(
                            variables, identifier_1
                        )

                        if not existing_variable_node:
                            new_variable_id = str(ObjectId())

                            nodes.append(
                                nebula_graph_schema.IdentifierNode(
                                    id=new_variable_id,
                                    name=identifier_1,
                                    level="",
                                    picture=None,
                                    default_value=None,
                                )
                            )

                            edges.append(
                                nebula_graph_schema.Source(
                                    source=new_variable_id,
                                    target=statement.id,
                                )
                            )
                        else:
                            edges.append(
                                nebula_graph_schema.Source(
                                    source=existing_variable_node.id,
                                    target=statement.id,
                                )
                            )

    return nodes, edges


async def delete_nebula(repository_id: str):
    client = get_nebula_client(f"{NEBULA_SPACE_NAME_PREFIX}{repository_id}")
    client.delete_space()
    return {
        "message": f"Successfully deleted Nebula space for repository {repository_id}"
    }
