from utils.azure_blob_util import read_blob_csv
import pandas as pd
from utils.rabbitmq_util import get_channel
import json
from loguru import logger
from config.settings import settings
from classifier.constants import FileType

def dispatch_clist_files(repository_id: str):
    """
    Dispatch CLIST files for parsing based on the classified CSV file
    
    Args:
        repository_id (str): The repository ID
        
    Returns:
        tuple: A tuple containing (success_count, fail_count)
    """
    blob_name = f"{repository_id}_classified.csv"
    df = read_blob_csv(blob_name)
    clist_files = get_clist_files(df)
    success_count = 0
    fail_count = 0
    
    for clist_file in clist_files:
        try:
            produce_task(repository_id, clist_file['name'])
            success_count += 1
        except Exception as e:
            logger.error(f"Error producing task for CLIST file {clist_file['name']}: {str(e)}")
            fail_count += 1
            
    return success_count, fail_count

def get_clist_files(df: pd.DataFrame):
    """
    Filter the DataFrame to get only CLIST files
    
    Args:
        df (pd.DataFrame): The DataFrame containing classified files
        
    Returns:
        list: A list of dictionaries containing CLIST file information
    """
    clist_rows = df[df["label"] == FileType.CLIST]
    return [{"name": row["name"]} for _, row in clist_rows.iterrows()]

def produce_task(repository_id: str, file_name: str):
    """
    Produce a task for parsing a CLIST file
    
    Args:
        repository_id (str): The repository ID
        file_name (str): The name of the CLIST file
        
    Returns:
        None
    """
    task_data = {
        "task_type": "parse_clist",
        "data": {
            "name": file_name,
            "repository_id": repository_id,
        }
    }
    
    channel = get_channel()
    channel.basic_publish(
        exchange=settings.PARSER_EXCHANGE_NAME,
        routing_key=settings.CLIST_ROUTING_KEY,
        body=json.dumps(task_data)
    )
