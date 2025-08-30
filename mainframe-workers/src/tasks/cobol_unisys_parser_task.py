import json
from utils.rabbitmq_util import get_channel, produce_task
from .base_task import BaseTask
from typing import Dict, Any
from utils.azure_blob_util import read_blob_file
from utils.timeout_util import Timeout
from parsers.cobol_parser_unisys import parse_cobol_unisys
from controller.reverse_controller import ReverseController
from loguru import logger
from config.settings import settings

TIME_LIMIT_IN_SECONDS = settings.COBOL_PARSER_TIME_LIMIT_IN_SECONDS

PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME
GRAPH_ROUTING_KEY = settings.GRAPH_ROUTING_KEY
COBOL_TYPE = 'COBOL'

def produce_graph_task(repository_id: str, name: str, label: str):
    task_data = {
        "task_type": "parse_graph",
        "data": {
            "repository_id": repository_id,
            "name": name,
            "label": label
        }
    }
    
    channel = get_channel()
    channel.basic_publish(
        exchange=PARSER_EXCHANGE_NAME,
        routing_key=GRAPH_ROUTING_KEY,
        body=json.dumps(task_data)
    )

class CobolUnisysParserTask(BaseTask):
    def __init__(self):
        self.reverse_controller = ReverseController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        if not task_data.get('name') or not task_data.get('repository_id'):
            logger.error("No name or repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}
            
        name = task_data.get('name')
        repository_id = task_data.get('repository_id')
        
        try:
            blob_name = f"{repository_id}/code/COBOL/{name}"
            content = read_blob_file(blob_name)

            if content is None:
                raise FileNotFoundError(f"Cannot read the content of {blob_name}")

            clock = Timeout(TIME_LIMIT_IN_SECONDS)
            with clock:
                reversed_program = parse_cobol_unisys(name, content)
            
            if clock.is_timeout:
                error_msg = f"Parsing COBOL file {name} takes over {TIME_LIMIT_IN_SECONDS} seconds"
                logger.error(error_msg)
                return {
                    "status": "error",
                    "message": error_msg
                }
        
            save_result = self.reverse_controller.save_reverse_engineering(name, repository_id, reversed_program, type=COBOL_TYPE)
            if save_result["status"] == "error":
                return save_result
                
            # Trigger related tasks
            produce_graph_task(repository_id, name, COBOL_TYPE)
            
            # for task_config in [
            #     (settings.COBOL_SUMMARIZATION_ROUTING_KEY, 'summarize_cobol'),
            #     (settings.STATEMENT_SUMMARIZATION_ROUTING_KEY, 'summarize_statements')
            # ]:
            #     produce_task(
            #         routing_key=task_config[0],
            #         exchange=PARSER_EXCHANGE_NAME,
            #         task_type=task_config[1],
            #         data={'repository_id': repository_id, 'name': name}
            #     )
                
            return save_result
                
        except Exception as e:
            error_msg = f"Error processing COBOL file: {str(e)}"
            logger.error(error_msg)
            return {
                "status": "error",
                "message": error_msg
            }
