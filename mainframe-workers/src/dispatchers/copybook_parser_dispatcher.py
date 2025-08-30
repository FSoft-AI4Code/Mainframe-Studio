import json
from typing import List, Tuple, Dict, Any
from loguru import logger
import pandas as pd
import uuid

from config.settings import settings
from utils.azure_blob_util import read_blob_csv
from utils.rabbitmq_util import get_channel


def dispatch_copybook_files(repository_id: str, system_type: str, job_batches: Dict[str, List[str]], coordinator_id: str):
    """
    Dispatch copybook files for parsing
    
    Args:
        repository_id (str): ID of the repository
        system_type (str): Type of the system (e.g., IBM, UNISYS)
        job_batches (Dict[str, List[str]]): Dictionary of job batches with job IDs and file names
        coordinator_id (str): The ID of the coordinator for this batch of jobs for tracking parsing progress
    """
    total_file_count = sum(len(files) for files in job_batches.values())
    logger.info(f"Dispatching {total_file_count} copybook files for repository {repository_id} with batch size {settings.COPYBOOK_DISPATCHER_BATCH_SIZE}")
    
    for job_id, file_names in job_batches.items():
        produce_copybook_task(repository_id, system_type, file_names, job_id, coordinator_id)
    
    logger.info(f"Dispatched {len(job_batches)} copybook parsing jobs for repository {repository_id} with coordinator ID {coordinator_id}")


def get_copybook_job_batches(repository_id: str, copybook_files: List[Dict[str, Any]], batch_size: int) -> Dict[str, List[str]]:
    """Get job batches for copybook files
    Args:
        repository_id (str): ID of the repository
        copybook_files (List[Dict[str, Any]]): List of copybook files
        batch_size (int): Size of each batch
        
    Returns:
        Dict[str, List[str]]: Dictionary of job batches with job IDs and file names
    """
    
    job_map_list: Dict[str, List[str]] = {}
    for i in range(0, len(copybook_files), batch_size):
        copybook_files_batch = copybook_files[i:i + batch_size]
        file_names: List[str] = [file["name"] for file in copybook_files_batch]
        batch_number = i // batch_size
        job_id = get_copybook_parsing_job_id(repository_id, batch_number)
        job_map_list[job_id] = file_names
    return job_map_list

def get_copybook_parsing_coordinator_id(repository_id: str) -> str:
    """
    Generate a coordinator ID for the copybook parsing task
    
    Args:
        repository_id (str): ID of the repository
        
    Returns:
        str: Generated coordinator ID
    """
    return f"coordinator-copybook-{repository_id}-{uuid.uuid4().hex[:8]}"


def get_copybook_parsing_job_id(repository_id: str, batch_num: int) -> str:
    """
    Generate a job ID for the copybook parsing task
    
    Args:
        repository_id (str): ID of the repository
        batch_num (int): Batch number for the job
        
    Returns:
        str: Generated job ID
    """
    return f"job-copybook-{repository_id}-batch-{batch_num}-{uuid.uuid4().hex[:8]}"


def get_copybook_files(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Get copybook files from the DataFrame
    
    Args:
        df (pd.DataFrame): DataFrame containing file information
        
    Returns:
        List[Dict[str, Any]]: List of copybook files with their names and content
    """
    copybook_rows = df[df["label"] == "COPY"]
    return [{"name": row["name"], "content": row["content"]} for _, row in copybook_rows.iterrows()]

def produce_copybook_task(repository_id: str, system_type: str, file_names: List[str], job_id: str, coordinator_id: str):
    try:
        routing_key = {
            "IBM": settings.COPYBOOK_IBM_ROUTING_KEY,
            "UNISYS": settings.COPYBOOK_UNISYS_ROUTING_KEY,
        }[system_type]
        task_type = {
            "IBM": "parse_copybook_ibm",
            "UNISYS": "parse_copybook_unisys",
        }[system_type]
    except KeyError:
        raise ValueError(f"Invalid system type {system_type}")

    task_data = {
        "task_type": task_type,
        "data": {
            "names": file_names,
            "repository_id": repository_id,
            "job_id": job_id,
            "coordinator_id": coordinator_id,
        }
    }

    channel = get_channel()
    channel.basic_publish(
        exchange=settings.PARSER_EXCHANGE_NAME,
        routing_key=routing_key,
        body=json.dumps(task_data)
    )