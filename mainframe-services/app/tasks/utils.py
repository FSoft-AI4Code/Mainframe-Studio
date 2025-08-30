import base64
import datetime
import json
import re
import urllib.parse
import uuid
from typing import Any, Dict, Optional

import pika
import requests
from loguru import logger
from pydantic import BaseModel

from app.config.settings import settings

from .reverse.bms import AnalyzedBMS


def produce_task_mq(event: str, repo_id: str, task_type: str, routing_key: str, system_type: str):
    """
    Produce message to RabbitMQ queue.
    
    Args:
        event: Event type (e.g. 'classified', 'parsed')
        repo_id: Repository ID
        routing_key: Routing key for the message
        task_type: Type of task
    """
    try:
        # Establish connection using the new settings
        connection = pika.BlockingConnection(
            pika.URLParameters(settings.RABBITMQ_URL)
        )
        channel = connection.channel()

        message = {
            "task_type": task_type.lower(),
            "data": {
                "repository_id": repo_id
            }
        }

        # Publish message
        channel.basic_publish(
            exchange=settings.RABBITMQ_EXCHANGE,
            routing_key=routing_key.lower(),
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )

        logger.info(f"Sent {event} event for repo {repo_id} to RabbitMQ")
        
        # Close connection
        connection.close()
        
    except Exception as e:
        logger.error(f"Failed to produce RabbitMQ message: {str(e)}")

class RPCPublisher:
    def __init__(self, response_queue_name: str, response_routing_key: str):
        self.connection = pika.BlockingConnection(
            pika.URLParameters(settings.RABBITMQ_URL))

        self.channel = self.connection.channel()

        self.channel.exchange_declare(
            exchange=settings.RABBITMQ_EXCHANGE,
            exchange_type='topic',  # Changed to topic for more flexible routing
            durable=True
        )
        
        result = self.channel.queue_declare(
            queue=response_queue_name,
            durable=True
        )
        
        self.channel.queue_bind(
            queue=response_queue_name,
            exchange=settings.RABBITMQ_EXCHANGE,
            routing_key=response_routing_key
        )


        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
        
        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        logger.info(f"get messsage with props {props.correlation_id}")
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, routing_key: str, body: str):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=settings.RABBITMQ_EXCHANGE,
            routing_key=routing_key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            ),
            body=body)
        while self.response is None:
            self.connection.process_data_events(time_limit=300)
        return self.response

def produce_rpc_task(task_type: str, 
                     data: Dict[str, Any], 
                     routing_key: str, 
                     response_queue_name: str, 
                     response_routing_key: str):
    try:
        message = {
            "task_type": task_type,
            "data": data
        }
        # Publish message
        return RPCPublisher(response_queue_name=response_queue_name, 
                            response_routing_key=response_routing_key).call(routing_key.lower(), json.dumps(message))
    
    except Exception as e:
        logger.error(f"Failed to produce RabbitMQ message: {str(e)}")

def produce_parse_task_mq(repo_id: str, type: str, file_name: str, system_type: str = "IBM"):
    return produce_rpc_task(
        f"parse_cobol_{system_type.lower()}",
        {"repository_id": repo_id, "name": file_name},
        f"parser.cobol.{system_type.lower()}",
        f"parse_cobol_{system_type.lower()}_response_queue",
        f"parser.cobol.{system_type.lower()}.response",
    )
     
def produce_summarization_task_mq(repo_id: str, type: str, file_name: str):
    return produce_rpc_task(
        "summarize_cobol",
        {
            "repository_id": repo_id,
            "name": file_name
        },
        "cobol.summarization",
        "cobol_summarization_response_queue",
        "cobol.summarization.response"
    )


class CodeBlock(BaseModel):
    content: str
    start_line: int
    end_line: int


def clean_code(input_text):
    lines = input_text.splitlines()
    cleaned_lines = []
    pattern = re.compile(r"^\d+\s*")
    for line in lines:
        new_line = pattern.sub(lambda m: " " * len(m.group(0)), line)
        cleaned_lines.append(new_line)

    # Join the cleaned lines back into a single string
    cleaned_output = "\n".join(cleaned_lines)
    return cleaned_output


def comment_specific_lines(code: str, truncate_col: int=72) -> str:
    # Split the code into lines
    lines = code.splitlines()
    for i, line in enumerate(lines):
        # Remove comments from the line
        if "*>" in line:
            line = line.split("*>")[0].rstrip()

        # Check for @OPTIONS and modify the line accordingly
        if line.strip().startswith("@OPTIONS"):
            line = line[:6] + "*" + line[6:].lstrip()

        # Truncate the line to 72 characters
        if truncate_col != 0:
            lines[i] = line[:72]
            if line.strip().startswith("*"):
                lines[i] = ""

    # Join the lines back into a single string
    return "\n".join(lines)

def trigger_airflow_dag(
    dag_id: str,
    airflow_base_url: str,
    username: str,
    password: str,
    conf: Optional[Dict[str, Any]] = None,
    timeout: int = 30
) -> Dict[str, Any]:
    """
    Trigger an Airflow DAG run via the Airflow REST API.
    
    Args:
        dag_id: The ID of the DAG to trigger
        airflow_base_url: The base URL of the Airflow API (e.g., "http://localhost:8080")
        username: Username for Airflow authentication
        password: Password for Airflow authentication
        conf: Optional configuration parameters to pass to the DAG run
        timeout: Request timeout in seconds
        
    Returns:
        The API response as a dictionary
        
    Raises:
        Exception: If the API call fails
    """
    if conf is None:
        conf = {}
    
    endpoint = urllib.parse.urljoin(airflow_base_url, f"/api/v1/dags/{dag_id}/dagRuns")
    
    utc_now = datetime.datetime.now(tz=datetime.timezone.utc)
    formatted_date = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    payload = {
        "logical_date": formatted_date,
        "conf": conf
    }
    
    base64_auth = base64.b64encode(f"{username}:{password}".encode()).decode()
    
    headers = {
        "Authorization": f"Basic {base64_auth}",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }
    
    logger.info(f"Triggering Airflow DAG: {dag_id}")
    response = requests.post(
        endpoint,
        json=payload,
        headers=headers,
        timeout=timeout
    )
    
    response.raise_for_status()
    result = response.json()
    logger.info(f"Successfully triggered DAG {dag_id}, run ID: {result.get('dag_run_id')}")
    return result

def read_file(file_path: str):
    try:
        with open(file_path, "r", encoding="shift_jis") as f:
            content = clean_code(f.read())
            content = comment_specific_lines(content)
            return content
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = clean_code(f.read())
                content = comment_specific_lines(content)
                return content
        except Exception as e:
            logger.error(
                f"Error reading file {file_path} with UTF-8 encoding: {e}")
    except Exception as e:
        logger.error(f"Error to parse file {file_path} {e}")


def remove_bms_title_line(content: str) -> str:
    content = re.sub(r'^\s*TITLE.*$', '', content,
                     flags=re.MULTILINE).strip()
    return content


def extract_related_pgms(cobols: dict, bmss: list[AnalyzedBMS]):
    outputs = []
    for index, cobol in cobols.items():
        if len(cobol) > 1:
            program_id = cobol.pop("Program_ID", "")

            if program_id:
                for _, screen_access in cobol.items():
                    for bms in bmss:
                        # screen_access["content"].replace("-","_")
                        if bms.file_name in screen_access["content"]:
                            if program_id not in bms.overview.related_pgms:
                                bms.overview.related_pgms.append(program_id)
                            if bms.screen_access == None:
                                bms.screen_access = []
                            bms.screen_access.append(
                                {
                                    "file_name": program_id,
                                    "cmd": screen_access["command"],
                                    "content": screen_access["content"],
                                    "map": screen_access.get("map", "").replace("MAP(", "")[:-1].strip("'"),
                                    "mapset": screen_access.get("mapset", "").replace("MAPSET(", "")[:-1].strip("'"),
                                }
                            )
                        outputs.append(bms)
    return outputs
