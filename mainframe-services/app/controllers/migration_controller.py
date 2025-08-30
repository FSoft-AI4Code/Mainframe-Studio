"""
Migration Controller Module

This module handles the migration of COBOL and BMS files to Java code.
It provides functionality for:
- Publishing migration tasks to RabbitMQ
- Managing migration data in MongoDB
- Downloading and retrieving migration repository structure
- Handling file content retrieval for migrated code
"""

import io
import json
import zipfile

import pika
from bson import ObjectId
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.config.rabbitmq import RabbitHelper
from app.utils.utils import get_blob_path
from app.utils.virtual_storage import VirtualStorage, TemplateCache

# RabbitMQ Configuration Constants
MIGRATION_EXCHANGE_NAME: str = "migration_exchange"
COBOL_MIGRATION_QUEUE_NAME: str = "cobol_java_migration_queue"
BMS_MIGRATION_QUEUE_NAME: str = "bms_java_migration_queue"
COBOL_MIGRATION_ROUTING_KEY: str = "migration.java.cobol"
BMS_MIGRATION_ROUTING_KEY: str = "migration.java.bms"

# Summarization Configuration Constants
BMS_SUMMARIZATION_ROUTING_KEY: str = "summarization.bms"
SUMMARIZATION_EXCHANGE_NAME: str = "summarization_exchange"
BMS_SUMMARIZATION_QUEUE_NAME: str = "bms_summarization_queue"
COBOL_SCREEN_SUMMARIZATION_QUEUE_NAME: str = "cobol_screen_summarization_queue"
COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY: str = "summarization.screen.cobol"

# File Path Constants
CODE_PATH_BASE = "java_template/src/main/java/com/migration/cobol/"
RESOURCE_PATH_BASE = "java_template/src/main/resources/"
TEMPLATE_BASE = "java_template"

# Create an instance of VirtualStorage
virtual_storage = VirtualStorage()

# Initialize template cache
TemplateCache.initialize(TEMPLATE_BASE)


class MigrationPublisher:
    """
    Publisher class for handling RabbitMQ message publishing for migration tasks.
    
    This class is responsible for publishing tasks to RabbitMQ for migration.
    It handles the connection and channel management for publishing messages
    to specific exchanges and queues.
    
    Attributes:
        rabbit_helper (RabbitHelper): Helper instance for RabbitMQ operations
    """

    def __init__(self, exchange_name: str, queue_name: str, routing_key: str):
        """
        Initialize the MigrationPublisher.
        
        Args:
            exchange_name (str): Name of the RabbitMQ exchange
            queue_name (str): Name of the queue to publish to
            routing_key (str): Routing key for message routing
        """
        self.rabbit_helper = RabbitHelper(exchange_name, queue_name,
                                          routing_key, enable_consume=False, dlx_queue=False)

    def publish_task(self, body, exchange: str, routing_key: str):
        """
        Publish a task message to RabbitMQ.
        
        Args:
            body: Message body to publish
            exchange (str): Exchange to publish to
            routing_key (str): Routing key for the message
        """
        self.rabbit_helper.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


async def publish_copybook_migration_task(db: AsyncIOMotorDatabase, repository_id: str, bms_file_name: str,
                                          cobol_file_name: str):
    """
    Publish a task to RabbitMQ to migrate a COBOL copybook.
    
    This function creates and publishes a migration task for converting a COBOL copybook
    to Java code. It includes the necessary metadata and file paths in the message.
    
    Args:
        db (AsyncIOMotorDatabase): MongoDB database instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the associated BMS file
        cobol_file_name (str): Name of the COBOL file to migrate
        
    Returns:
        dict: Status of the operation with success/error message
    """
    try:
        path = await get_blob_path(db, cobol_file_name, repository_id, "COBOL")

        migration_publisher = MigrationPublisher(exchange_name=MIGRATION_EXCHANGE_NAME,
                                                 queue_name=COBOL_MIGRATION_QUEUE_NAME,
                                                 routing_key=COBOL_MIGRATION_ROUTING_KEY)
        data = {
            "repository_id": repository_id,
            "cobol_file_name": cobol_file_name,
            "bms_file_name": bms_file_name,
            "blob_path": path,
        }
        # Create the task message
        message = {
            "task_type": "cobol_java_migration_summary",
            "data": data
        }

        migration_publisher.publish_task(json.dumps(message), exchange=MIGRATION_EXCHANGE_NAME,
                                         routing_key=COBOL_MIGRATION_ROUTING_KEY)

        logger.info(f"Published migration task for {repository_id}/{cobol_file_name}")

        return {"status": "success", "message": f"Task queued for {repository_id}/{cobol_file_name}"}

    except Exception as e:
        logger.error("Failed to publish migration task", error=str(e))
        return {"status": "error", "message": str(e)}


async def get_linked_cobol(db, repository_id: str, bms_file_name: str):
    """
    Retrieves the names of all COBOL node documents linked with a given BMS file.
    
    This function queries the MongoDB database to find all COBOL nodes that are
    linked to a specific BMS file through the 'group' field.
    
    Args:
        db: Motor async database instance
        repository_id (str): Repository ID as a string
        bms_file_name (str): BMS file name to search for in 'group' array
        
    Returns:
        list: List of COBOL node names
        
    Raises:
        Exception: If no matching COBOL nodes are found or if there's a database error
    """
    try:
        repository_id_obj = ObjectId(repository_id)

        cobol_nodes = await db.nodes.find({
            "repository_id": repository_id_obj,
            "label": "COBOL",
            "group": bms_file_name
        }).to_list(length=None)

        if not cobol_nodes:
            msg = f"No COBOL linked with file {bms_file_name}"
            logger.error(msg)
            raise Exception(msg)

        return [node.get("name", "") for node in cobol_nodes]

    except Exception as e:
        logger.error(f"Error getting linked COBOL for {repository_id}/{bms_file_name}: {e}")
        raise


def send_summarization_message(publisher, repository_id, bms_file_name, path):
    """
    Send a BMS summarization message to RabbitMQ.
    
    Args:
        publisher: MigrationPublisher instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the BMS file
        path (str): Path to the BMS file
    """
    data = {
        "repository_id": repository_id,
        "file_name": bms_file_name,
        "blob_path": path,
    }
    # Create the task message
    message = {
        "task_type": "bms_summary",
        "data": data
    }

    publisher.publish_task(json.dumps(message), exchange=SUMMARIZATION_EXCHANGE_NAME,
                           routing_key=BMS_SUMMARIZATION_ROUTING_KEY)


async def send_cobol_summarization_message(publisher, db, repository_id, cobol_file_name):
    """
    Send a COBOL summarization message to RabbitMQ.
    
    Args:
        publisher: MigrationPublisher instance
        db: MongoDB database instance
        repository_id: ID of the repository
        cobol_file_name: Name of the COBOL file
    """
    path = await get_blob_path(db, cobol_file_name, repository_id, "COBOL")
    data = {
        "repository_id": repository_id,
        "file_name": cobol_file_name,
        "blob_path": path,
    }
    # Create the task message
    message = {
        "task_type": "cobol_screen_summary",
        "data": data
    }

    publisher.publish_task(json.dumps(message), exchange=SUMMARIZATION_EXCHANGE_NAME,
                           routing_key=COBOL_SCREEN_SUMMARIZATION_ROUTING_KEY)

    logger.info(f"Published COBOL summarization task for {repository_id}/{cobol_file_name}")


async def publish_bms_migration_task(db: AsyncIOMotorDatabase, repository_id: str, bms_file_name: str):
    """
    Publish a task to RabbitMQ to migrate a BMS screen.
    
    This function creates and publishes a migration task for converting a BMS screen
    to Java code. It handles both the BMS file and its linked COBOL files.
    
    Args:
        db (AsyncIOMotorDatabase): MongoDB database instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the BMS file to migrate
        
    Returns:
        dict: Status of the operation with success/error message
        
    Raises:
        Exception: If there's an error publishing the task or getting linked COBOL files
    """
    try:
        path = await get_blob_path(db, bms_file_name, repository_id, "BMS")

        linked_cobol = await get_linked_cobol(db, repository_id, bms_file_name)

        migration_publisher = MigrationPublisher(exchange_name=MIGRATION_EXCHANGE_NAME,
                                                 queue_name=BMS_MIGRATION_QUEUE_NAME,
                                                 routing_key=BMS_MIGRATION_ROUTING_KEY)

        for cobol_file_name in linked_cobol:
            send_migration_message(migration_publisher, repository_id, bms_file_name, cobol_file_name, path)
            await publish_copybook_migration_task(db, repository_id, bms_file_name, cobol_file_name)

        # Update status of repo
        db.entry_points.update_one(
            {"repository_id": ObjectId(repository_id), "label": "BMS", "name": bms_file_name},
            {"$set": {"status": "migrating"}}
        )

        db.reverse_engineering.update_one(
            {"repository_id": ObjectId(repository_id), "type": "BMS", "name": bms_file_name},
            {"$set": {"status": "migrating"}}
        )

        logger.info(f"Published migration task for {repository_id}/{bms_file_name}")

        return {"status": "success", "message": f"Task queued for {repository_id}/{bms_file_name}"}

    except Exception as e:
        logger.error("Failed to publish migration task", error=str(e))
        return {"status": "error", "message": str(e)}


def send_migration_message(publisher, repository_id, bms_file_name, cobol_file_name, path):
    """
    Send a BMS migration message to RabbitMQ.
    
    Args:
        publisher: MigrationPublisher instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the BMS file
        cobol_file_name (str): Name of the linked COBOL file
        path (str): Path to the BMS file
    """
    data = {
        "repository_id": repository_id,
        "bms_file_name": bms_file_name,
        "cobol_file_name": cobol_file_name,
        "blob_path": path,
    }
    # Create the task message
    migration_message = {
        "task_type": "bms_java_migration_summary",
        "data": data
    }

    publisher.publish_task(json.dumps(migration_message), exchange=MIGRATION_EXCHANGE_NAME,
                           routing_key=BMS_MIGRATION_ROUTING_KEY)


def write_virtual_file(file_detail, path_base: str, subpath: str = ""):
    """
    Write a file to the virtual storage system.
    
    Args:
        file_detail (dict): Dictionary containing file details with 'file_name' and 'file_content'
        path_base (str): Base path where the file should be written
        
    Returns:
        dict: Information about the written file
        
    Raises:
        FileNotFoundError: If the file cannot be written to virtual storage
    """
    controller_file_path = path_base + subpath + file_detail.get("file_name")
    controller_file = virtual_storage.write_file(file_detail.get("file_content"), controller_file_path)
    if not controller_file:
        raise FileNotFoundError("File not found")
    return controller_file


async def download_migration_repo(db: AsyncIOMotorDatabase, repository_id: str, bms_file_name: str):
    """
    Download migration repository data as a zip file.
    
    This function retrieves the migration data for both BMS and COBOL files,
    generates the necessary Java files, and packages them into a zip file
    along with the template structure.
    
    Args:
        db (AsyncIOMotorDatabase): MongoDB database instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the BMS file
        
    Returns:
        bytes: Zip file containing the template structure with generated files
        
    Raises:
        FileNotFoundError: If migration data is not found for either BMS or COBOL files
        Exception: If there's an error during file generation or zip creation
    """
    try:
        cobol_files = await get_linked_cobol(db, repository_id, bms_file_name)
        if not cobol_files:
            raise FileNotFoundError("File not found")

        cobol_file_name = cobol_files[0]
        # Get the cobol path

        cobol_path = await get_blob_path(db, cobol_file_name, repository_id, "COBOL")
        bms_path = await get_blob_path(db, bms_file_name, repository_id, "BMS")

        bms_migration_data = await db.java_bms_migrations.find_one({"path": bms_path,
                                                                    "repository_id": repository_id})

        # Query the java_copybook_migrations collection
        cobol_migration_data = await db.java_copybook_migrations.find_one({
            "path": cobol_path,
            "repository_id": repository_id,
            "linked_cobol": cobol_file_name
        })

        if not cobol_migration_data or not bms_migration_data:
            raise FileNotFoundError("Migration data not found")

        # Store all generated files
        generated_files = []

        # Handle view controller data
        view_controller_data = bms_migration_data.get("controller_java")
        if view_controller_data:
            view_controller_file = write_virtual_file(view_controller_data, CODE_PATH_BASE, "controller/view/")
            generated_files.append(view_controller_file)

        # Handle view data
        view_data = bms_migration_data.get("view_java")
        if view_data:
            view__file = write_virtual_file(view_data, RESOURCE_PATH_BASE, "templates/")
            generated_files.append(view__file)

        # Handle controller data
        controller_data = cobol_migration_data.get("controller_java")
        if controller_data:
            controller_file = write_virtual_file(controller_data, CODE_PATH_BASE)
            generated_files.append(controller_file)

        # Handle DTO data if exists
        dto_data = cobol_migration_data.get("dto_java")
        if dto_data:
            dto_file = write_virtual_file(dto_data, CODE_PATH_BASE)
            generated_files.append(dto_file)

        # Handle service data if exists
        service_data = cobol_migration_data.get("service_java")
        if service_data:
            service_file = write_virtual_file(service_data, CODE_PATH_BASE)
            generated_files.append(service_file)

        # Handle model data if exists
        model_data = cobol_migration_data.get("model_java")
        if model_data:
            model_file = write_virtual_file(model_data, CODE_PATH_BASE)
            generated_files.append(model_file)

        # Handle liquibase data if exists
        liquibase_java = cobol_migration_data.get("liquibase_java")
        if liquibase_java:
            liquibase_file = write_virtual_file(liquibase_java, RESOURCE_PATH_BASE)
            generated_files.append(liquibase_file)

        # Handle repository data if exists
        repository_java = cobol_migration_data.get("repository_java")
        if repository_java:
            repository_file = write_virtual_file(repository_java, CODE_PATH_BASE)
            generated_files.append(repository_file)

        # Create a zip file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Add all generated files to the zip
            for file_info in generated_files:
                file_path = file_info["file_path"]
                zip_file.writestr(file_path, file_info["content"])

            # Add all template files from cache
            template_files = TemplateCache.get_template_files()
            for file_path, content in template_files.items():
                # Skip if the file is already added (generated files)
                if any(file_path == f["file_path"] for f in generated_files):
                    continue
                zip_file.writestr(file_path, content)

        # Reset buffer position to beginning
        zip_buffer.seek(0)
        return zip_buffer.getvalue()

    except Exception as e:
        logger.error(f"Error downloading migration repo: {str(e)}")
        raise


async def get_migration_structure(db: AsyncIOMotorDatabase, repository_id: str, bms_file_name: str) -> dict:
    """
    Get the folder structure of Java migration code for a specific BMS file.
    
    This function retrieves the migration data for a BMS file and its linked COBOL files,
    and constructs a hierarchical folder structure representing the generated Java code.
    
    Args:
        db (AsyncIOMotorDatabase): MongoDB database instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the BMS file
        
    Returns:
        dict: Folder structure of the Java migration code with the following format:
            {
                "repository_id": str,
                "bms_file_name": str,
                "structure": {
                    "name": str,
                    "type": str,
                    "path": str,
                    "children": list
                }
            }
            
    Raises:
        FileNotFoundError: If no migration data is found for the BMS file
        Exception: If there's an error retrieving or processing the migration data
    """
    try:
        bms_path = await get_blob_path(db, bms_file_name, repository_id, "BMS")
        # Get BMS migration data
        bms_migration_data = await db.java_bms_migrations.find_one({
            "repository_id": repository_id,
            "path": bms_path
        })

        if not bms_migration_data:
            raise FileNotFoundError(f"No migration data found for BMS file: {bms_file_name}")

        # Initialize the root structure
        root_structure = {
            "name": "root",
            "type": "directory",
            "path": "/",
            "children": []
        }

        # Add src directory
        src_dir = {
            "name": "src",
            "type": "directory",
            "path": "/src",
            "children": []
        }
        root_structure["children"].append(src_dir)

        # Add main directory under src
        main_dir = {
            "name": "main",
            "type": "directory",
            "path": "/src/main",
            "children": []
        }
        src_dir["children"].append(main_dir)

        # Add java and resources directories under main
        java_dir = {
            "name": "java",
            "type": "directory",
            "path": "/src/main/java",
            "children": []
        }
        resources_dir = {
            "name": "resources",
            "type": "directory",
            "path": "/src/main/resources",
            "children": []
        }
        main_dir["children"].extend([java_dir, resources_dir])

        # Add com directory under java
        com_dir = {
            "name": "com",
            "type": "directory",
            "path": "/src/main/java/com",
            "children": []
        }
        java_dir["children"].append(com_dir)

        # Add migration directory under com
        migration_dir = {
            "name": "migration",
            "type": "directory",
            "path": "/src/main/java/com/migration",
            "children": []
        }
        com_dir["children"].append(migration_dir)

        # Add cobol directory under migration
        cobol_dir = {
            "name": "cobol",
            "type": "directory",
            "path": "/src/main/java/com/migration/cobol",
            "children": []
        }
        migration_dir["children"].append(cobol_dir)

        # Add BMS view files
        if bms_migration_data.get("view_java"):
            view_file = {
                "name": bms_migration_data["view_java"]["file_name"],
                "type": "file",
                "path": f"/src/main/java/com/migration/cobol/{bms_migration_data['view_java']['file_name']}"
            }
            cobol_dir["children"].append(view_file)

        # Add BMS controller files
        if bms_migration_data.get("controller_java"):
            controller_file = {
                "name": bms_migration_data["controller_java"]["file_name"],
                "type": "file",
                "path": f"/src/main/java/com/migration/cobol/{bms_migration_data['controller_java']['file_name']}"
            }
            cobol_dir["children"].append(controller_file)

        # Get linked COBOL files and their migration data
        linked_cobol = await get_linked_cobol(db, repository_id, bms_file_name)
        
        for cobol_file in linked_cobol:
            cobol_migration_data = await db.java_copybook_migrations.find_one({
                "repository_id": repository_id,
                "linked_cobol": cobol_file
            })

            if cobol_migration_data:
                # Add model files
                if cobol_migration_data.get("model_java"):
                    model_file = {
                        "name": cobol_migration_data["model_java"]["file_name"],
                        "type": "file",
                        "path": f"/src/main/java/com/migration/cobol/{cobol_migration_data['model_java']['file_name']}"
                    }
                    cobol_dir["children"].append(model_file)

                # Add DTO files
                if cobol_migration_data.get("dto_java"):
                    dto_file = {
                        "name": cobol_migration_data["dto_java"]["file_name"],
                        "type": "file",
                        "path": f"/src/main/java/com/migration/cobol/{cobol_migration_data['dto_java']['file_name']}"
                    }
                    cobol_dir["children"].append(dto_file)

                # Add service files
                if cobol_migration_data.get("service_java"):
                    service_file = {
                        "name": cobol_migration_data["service_java"]["file_name"],
                        "type": "file",
                        "path": f"/src/main/java/com/migration/cobol/{cobol_migration_data['service_java']['file_name']}"
                    }
                    cobol_dir["children"].append(service_file)

                # Add repository files
                if cobol_migration_data.get("repository_java"):
                    repository_file = {
                        "name": cobol_migration_data["repository_java"]["file_name"],
                        "type": "file",
                        "path": f"/src/main/java/com/migration/cobol/{cobol_migration_data['repository_java']['file_name']}"
                    }
                    cobol_dir["children"].append(repository_file)

                # Add liquibase files to resources directory
                if cobol_migration_data.get("liquibase_java"):
                    liquibase_file = {
                        "name": cobol_migration_data["liquibase_java"]["file_name"],
                        "type": "file",
                        "path": f"/src/main/resources/{cobol_migration_data['liquibase_java']['file_name']}"
                    }
                    resources_dir["children"].append(liquibase_file)

        return {
            "repository_id": repository_id,
            "bms_file_name": bms_file_name,
            "structure": root_structure
        }

    except Exception as e:
        logger.error(f"Error getting migration structure: {str(e)}")
        raise


async def get_migration_file_content(db: AsyncIOMotorDatabase, repository_id: str, bms_file_name: str,
                                     file_path: str) -> dict:
    """
    Get the content of a Java migration file based on its path.
    
    This function retrieves the content of a specific Java file that was generated
    during the migration process. It searches through both BMS and COBOL migration data
    to find the requested file.
    
    Args:
        db (AsyncIOMotorDatabase): MongoDB database instance
        repository_id (str): ID of the repository
        bms_file_name (str): Name of the BMS file
        file_path (str): Path of the Java file to get content from
        
    Returns:
        dict: File content and metadata with the following format:
            {
                "repository_id": str,
                "bms_file_name": str,
                "file_path": str,
                "content": str
            }
            
    Raises:
        FileNotFoundError: If the requested file is not found in the migration data
        Exception: If there's an error retrieving the file content
    """
    try:
        bms_path = await get_blob_path(db, bms_file_name, repository_id, "BMS")
        
        # First check BMS migration data
        bms_migration_data = await db.java_bms_migrations.find_one({
            "repository_id": repository_id,
            "path": bms_path
        })

        if bms_migration_data:
            # Check for view files
            if bms_migration_data.get("view_java") and file_path.endswith(bms_migration_data["view_java"]["file_name"]):
                return {
                    "repository_id": repository_id,
                    "bms_file_name": bms_file_name,
                    "file_path": file_path,
                    "content": bms_migration_data["view_java"]["file_content"]
                }
            
            # Check for controller files
            if bms_migration_data.get("controller_java") and file_path.endswith(bms_migration_data["controller_java"]["file_name"]):
                return {
                    "repository_id": repository_id,
                    "bms_file_name": bms_file_name,
                    "file_path": file_path,
                    "content": bms_migration_data["controller_java"]["file_content"]
                }

        # Get linked COBOL files
        linked_cobol = await get_linked_cobol(db, repository_id, bms_file_name)
        
        # Check each linked COBOL file's migration data
        for cobol_file in linked_cobol:
            cobol_migration_data = await db.java_copybook_migrations.find_one({
                "repository_id": repository_id,
                "linked_cobol": cobol_file
            })

            if cobol_migration_data:
                # Check model files
                if cobol_migration_data.get("model_java") and file_path.endswith(cobol_migration_data["model_java"]["file_name"]):
                    return {
                        "repository_id": repository_id,
                        "bms_file_name": bms_file_name,
                        "file_path": file_path,
                        "content": cobol_migration_data["model_java"]["file_content"]
                    }

                # Check DTO files
                if cobol_migration_data.get("dto_java") and file_path.endswith(cobol_migration_data["dto_java"]["file_name"]):
                    return {
                        "repository_id": repository_id,
                        "bms_file_name": bms_file_name,
                        "file_path": file_path,
                        "content": cobol_migration_data["dto_java"]["file_content"]
                    }

                # Check service files
                if cobol_migration_data.get("service_java") and file_path.endswith(cobol_migration_data["service_java"]["file_name"]):
                    return {
                        "repository_id": repository_id,
                        "bms_file_name": bms_file_name,
                        "file_path": file_path,
                        "content": cobol_migration_data["service_java"]["file_content"]
                    }

                # Check repository files
                if cobol_migration_data.get("repository_java") and file_path.endswith(cobol_migration_data["repository_java"]["file_name"]):
                    return {
                        "repository_id": repository_id,
                        "bms_file_name": bms_file_name,
                        "file_path": file_path,
                        "content": cobol_migration_data["repository_java"]["file_content"]
                    }

                # Check liquibase files
                if cobol_migration_data.get("liquibase_java") and file_path.endswith(cobol_migration_data["liquibase_java"]["file_name"]):
                    return {
                        "repository_id": repository_id,
                        "bms_file_name": bms_file_name,
                        "file_path": file_path,
                        "content": cobol_migration_data["liquibase_java"]["file_content"]
                    }

        raise FileNotFoundError(f"File not found: {file_path}")

    except Exception as e:
        logger.error(f"Error getting migration file content: {str(e)}")
        raise
