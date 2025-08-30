from utils.azure_blob_util import read_blob_csv, write_blob
import pandas as pd
from utils.rabbitmq_util import get_channel
import json
from loguru import logger
from config.settings import settings

PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME

def dispatch_cobol_files(repository_id: str, system_type: str):
    blob_name = f"{repository_id}_classified.csv"
    df = read_blob_csv(blob_name)
    cobol_files = get_cobol_files(df)
    success_count = 0
    fail_count = 0
    for cobol_file in cobol_files:
        produce_task(repository_id, system_type, cobol_file['name'])
    return success_count, fail_count

def get_cobol_files(df: pd.DataFrame):
    cobol_rows = df[df['label'] == 'COBOL']
    return [{'name': row['name']} for _, row in cobol_rows.iterrows()]

def produce_task(repository_id: str, system_type: str, file_name: str):
    try:
        routing_key = {
            "UNISYS": settings.COBOL_UNISYS_ROUTING_KEY,
            "DNP": settings.COBOL_DNP_ROUTING_KEY
        }[system_type]
        task_type = {
            "UNISYS": "parse_cobol_unisys",
            "DNP": "parse_cobol_dnp"
        }[system_type]
    except KeyError:
        raise ValueError(f"Invalid system type {system_type}")
    task_data = {
        "task_type": task_type,
        "data": {
            "name": file_name,
            "repository_id": repository_id,
        }
    }
    channel = get_channel()
    channel.basic_publish(
        exchange=settings.PARSER_EXCHANGE_NAME,
        routing_key=routing_key,
        body=json.dumps(task_data)
    )


