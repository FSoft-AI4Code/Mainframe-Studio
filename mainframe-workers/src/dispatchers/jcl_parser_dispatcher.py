from utils.azure_blob_util import read_blob_csv, write_blob
import pandas as pd
from utils.rabbitmq_util import get_channel
import json
from loguru import logger
from config.settings import settings

PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME
JCL_ROUTING_KEY = settings.JCL_ROUTING_KEY

def dispatch_jcl_files(repository_id: str):
    blob_name = f"{repository_id}_classified.csv"
    logger.info(f"Reading JCL files from blob {blob_name}")
    df = read_blob_csv(blob_name)
    jcl_files = get_jcl_files(df)
    success_count = 0
    fail_count = 0
    for jcl_file in jcl_files:
        produce_task(repository_id, jcl_file['name'])
    return success_count, fail_count
        

def get_jcl_files(df: pd.DataFrame):
    jcl_rows = df[df["label"] == "JCL"]
    return [{'name': row['name']} for _, row in jcl_rows.iterrows()]

def produce_task(repository_id: str, file_name: str):
    task_data = {
        "task_type": "parse_jcl",
        "data": {
            "name": file_name,
            "repository_id": repository_id,
        }
    }
    
    channel = get_channel()
    channel.basic_publish(
        exchange=PARSER_EXCHANGE_NAME,
        routing_key=JCL_ROUTING_KEY,
        body=json.dumps(task_data)
    )