from utils.azure_blob_util import read_blob_csv, write_blob
import pandas as pd
from utils.rabbitmq_util import get_channel
import json
from loguru import logger
from config.settings import settings

PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME
BMS_ROUTING_KEY = settings.BMS_ROUTING_KEY

def dispatch_bms_files(repository_id: str):
    blob_name = f"{repository_id}_classified.csv"
    df = read_blob_csv(blob_name)
    bms_files = get_bms_files(df)
    success_count = 0
    fail_count = 0
    for bms_file in bms_files:
        produce_task(repository_id, bms_file['name'])
    return success_count, fail_count
        

def get_bms_files(df: pd.DataFrame):
    bms_rows = df[df['label'] == 'BMS']
    return [{'name': row['name'], 'content': row['content']} for _, row in bms_rows.iterrows()]

def produce_task(repository_id: str, file_name: str):
    task_data = {
        "task_type": "parse_bms",
        "data": {
            "name": file_name,
            "repository_id": repository_id,
        }
    }
    
    channel = get_channel()
    channel.basic_publish(
        exchange=PARSER_EXCHANGE_NAME,
        routing_key=BMS_ROUTING_KEY,
        body=json.dumps(task_data)
    )