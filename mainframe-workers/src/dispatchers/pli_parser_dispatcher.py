from utils.azure_blob_util import read_blob_csv
import pandas as pd
from utils.rabbitmq_util import get_channel
import json
from loguru import logger
from config.settings import settings

def dispatch_pli_files(repository_id: str):
    """
    Dispatch PLI files for parsing based on the classified CSV file
    
    Args:
        repository_id (str): The repository ID
        
    Returns:
        tuple: A tuple containing (success_count, fail_count)
    """
    blob_name = f"{repository_id}_classified.csv"
    df = read_blob_csv(blob_name)
    pli_files = get_pli_files(df)
    success_count = 0
    fail_count = 0
    
    for pli_file in pli_files:
        try:
            produce_task(repository_id, pli_file['name'])
            success_count += 1
        except Exception as e:
            logger.error(f"Error producing task for PLI file {pli_file['name']}: {str(e)}")
            fail_count += 1
            
    return success_count, fail_count

def get_pli_files(df: pd.DataFrame):
    """
    Filter the DataFrame to get only PLI files
    
    Args:
        df (pd.DataFrame): The DataFrame containing classified files
        
    Returns:
        list: A list of dictionaries containing PLI file information
    """
    pli_rows = df[df["label"] == "PLI"]
    return [{"name": row["name"]} for _, row in pli_rows.iterrows()]

def produce_task(repository_id: str, file_name: str):
    """
    Produce a task for parsing a PLI file
    
    Args:
        repository_id (str): The repository ID
        file_name (str): The name of the PLI file
        
    Returns:
        None
    """
    task_data = {
        "task_type": "parse_pli",
        "data": {
            "name": file_name,
            "repository_id": repository_id,
        }
    }
    
    channel = get_channel()
    channel.basic_publish(
        exchange=settings.PARSER_EXCHANGE_NAME,
        routing_key=settings.PLI_ROUTING_KEY,
        body=json.dumps(task_data)
    )
