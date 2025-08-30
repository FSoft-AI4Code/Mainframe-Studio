import json
from loguru import logger
from config.settings import settings
from utils.rabbitmq_util import get_channel, produce_task
from utils.timeout_util import Timeout
from utils.azure_blob_util import read_blob_file
from .base_task import BaseTask
from typing import Dict, Any
from parsers.wfl_parser import parse_wfl
from controller.reverse_controller import ReverseController

TIME_LIMIT_IN_SECONDS = 300
PARSER_EXCHANGE_NAME = settings.PARSER_EXCHANGE_NAME
GRAPH_ROUTING_KEY = settings.GRAPH_ROUTING_KEY
WFL_TYPE = 'WFL'

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

class WFLParserTask(BaseTask):
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
            blob_name = f"{repository_id}/code/WFL/{name}"
            content = read_blob_file(blob_name)
            if content is None:
                raise FileNotFoundError(f"Cannot read the content of {blob_name}")
            clock = Timeout(TIME_LIMIT_IN_SECONDS)
            with clock:
                reversed_program = parse_wfl(repository_id, content)
            
            if clock.is_timeout:
                error_msg = f"Parsing WFL file {name} takes over {TIME_LIMIT_IN_SECONDS} seconds"
                logger.error(error_msg)
                return {"status": "error", "message": error_msg}
                        
            save_result = self.reverse_controller.save_reverse_engineering(
                name, repository_id, reversed_program, type=WFL_TYPE
            )
            
            if save_result["status"] == "error":
                return save_result

            # Pass job_name to graph task
            job_name = reversed_program.output.get("job_name", name)
            produce_graph_task(repository_id, job_name, WFL_TYPE)
                
            return save_result
                
        except Exception as e:
            error_msg = f"Error processing WFL file: {str(e)}"
            logger.error(error_msg)
            return {"status": "error", "message": error_msg}
