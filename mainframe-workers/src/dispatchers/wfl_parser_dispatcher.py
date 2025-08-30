from utils.azure_blob_util import read_blob_csv, write_blob
import pandas as pd
from utils.rabbitmq_util import get_channel
import json
from loguru import logger
from config.settings import settings

PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME
WFL_ROUTING_KEY = settings.WFL_ROUTING_KEY

def dispatch_wfl_files(repository_id: str):
    blob_name = f"{repository_id}_classified.csv"
    df = read_blob_csv(blob_name)
    wfl_files = get_wfl_files(df)
    success_count = 0
    fail_count = 0
    for wfl_file in wfl_files:
        produce_task(repository_id, wfl_file['name'])
    return success_count, fail_count
        

def get_wfl_files(df: pd.DataFrame):
    wfl_rows = df[df['label'] == 'WFL']
    return [{'name': row['name']} for _, row in wfl_rows.iterrows()]

def produce_task(repository_id: str, file_name: str):
    task_data = {
        "task_type": "parse_wfl",
        "data": {
            "name": file_name,
            "repository_id": repository_id,
        }
    }
    
    channel = get_channel()
    channel.basic_publish(
        exchange=PARSER_EXCHANGE_NAME,
        routing_key=WFL_ROUTING_KEY,
        body=json.dumps(task_data)
    )