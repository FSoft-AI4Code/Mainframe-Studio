import sys
from datetime import timedelta
from typing import Optional

from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param
from airflow.utils.trigger_rule import TriggerRule
from loguru import logger

sys.path.append("./src")

from config.settings import settings
from controller.dataset_assignment_controller import \
    DatasetAssignmentController
from controller.edge_controller import EdgeController
from controller.node_controller import NodeController
from controller.reverse_controller import ReverseController
from parsers.bms_parser import parse_bms as _parse_bms
from parsers.cobol_parser_ibm import parse_cobol_ibm
from parsers.cobol_parser_ibm import \
    parse_screen_access as _parse_screen_access
from parsers.copybook_parser_ibm import parse_copybook_ibm
from parsers.jcl_dataset_assignment import JclDatasetAssignmentExtractor
from parsers.jcl_parser import parse_jcl as _parse_jcl
from parsers.pli_parser import parse_pli as _parse_pli
from schema.dataset_assignment import JclDatasetAssignment
from schema.reverse_engineering import (ReverseEngineeringStatus,
                                        ReverseEngineeringUpdate)
from tasks.graph_task import GraphTask
from utils.azure_blob_util import read_blob_csv, read_blob_file

with DAG(
    dag_id="reverse_repo",
    schedule=None,  # Manual trigger only since we have required params
    params={
        "repository_id": Param(
            type="string",
            description="Repository ID to process"
        ),
    },
    default_args={
        "execution_timeout": timedelta(seconds=settings.REVERSE_REPO_EXECUTION_TIMEOUT),
    }
) as dag:
    """
    DAG for reverse engineering mainframe repositories by parsing COBOL and copybooks.
    
    Parameters:
    - repository_id: Repository ID to process
    """
    
    @task.python()
    def get_files(**context):
        """Get files to process for the repository.
        """
        repository_id = context["params"]["repository_id"]
        dag.log.info(f"Getting files for repository {repository_id}")
        df = read_blob_csv(f"{repository_id}_classified.csv")
        
        if df is None:
            raise RuntimeError(f"Blob file {repository_id}_classified.csv not found")
        
        # return the file name and label records
        df = df[["name", "label"]]
        return df.to_dict("records")
    
    @task.python()
    def filter_by_label(files: list[dict], label: str) -> list[dict]:
        return [f for f in files if f["label"] == label]
    
    @task.python()
    def parse_copybook(file: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        name = file["name"]
        blob_name = f"{repository_id}/code/COPY/{name}"
        content = read_blob_file(blob_name)
        result = parse_copybook_ibm(name, content)
        return result.model_dump()
    
    @task.python(trigger_rule=TriggerRule.ALL_DONE)
    def parse_cobol(file: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        name = file["name"]
        blob_name = f"{repository_id}/code/COBOL/{name}"
        content = read_blob_file(blob_name)
        result = parse_cobol_ibm(repository_id, name, content)
        return result.model_dump()
    
    @task.python()
    def parse_screen_access(file: dict, **context) -> Optional[dict]:
        repository_id = context["params"]["repository_id"]
        name = file["name"]
        blob_name = f"{repository_id}/code/COBOL/{name}"
        content = read_blob_file(blob_name)
        if content is None:
            raise RuntimeError(f"Content is None for {name}")
        screen_name = _parse_screen_access(content, cache_dir=settings.KOOPA_CACHE_DIR)
        
        if screen_name:
            parsed_screen_access = {
                "screen": screen_name,
                "name": file["name"],
                "type": "BMS",
            }
            return parsed_screen_access
        return None
    
    @task.python()
    def map_screen_access(parsed_screen_access: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        reverse_controller = ReverseController()
        result = reverse_controller.map_screen_access(parsed_screen_access["screen"], parsed_screen_access["name"], repository_id)
        return result
    
    @task.python()
    def parse_jcl(file: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        name = file["name"]
        blob_name = f"{repository_id}/code/JCL/{name}"
        content = read_blob_file(blob_name)
        result = _parse_jcl(name, content)
        return result.model_dump()
    
    @task.python()
    def parse_bms(file: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        name = file["name"]
        blob_name = f"{repository_id}/code/BMS/{name}"
        content = read_blob_file(blob_name)
        result = _parse_bms(name, content)
        return result.model_dump()
    
    @task.python()
    def parse_pli(file: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        name = file["name"]
        blob_name = f"{repository_id}/code/PLI/{name}"
        content = read_blob_file(blob_name)
        result = _parse_pli(name, content)
        return result.model_dump()
    
    @task.python(trigger_rule=TriggerRule.ALL_DONE)
    def save_reverse_engineering(parsed_data: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        reverse_controller = ReverseController()
        reverse_engineering_update = ReverseEngineeringUpdate(**parsed_data)
        save_result = reverse_controller.save_reverse_engineering(
            parsed_data["name"], repository_id, reverse_engineering_update, type=parsed_data["type"]
        )
        return save_result
    
    @task.python(trigger_rule=TriggerRule.ALL_DONE)
    def generate_graph(parsed_data: dict, **context) -> dict:
        repository_id = context["params"]["repository_id"]
        graph_task = GraphTask()
        data = {
            "repository_id": repository_id,
            "name": parsed_data["name"],
            "label": parsed_data["type"],
        }
        if parsed_data.get("screen"):
            data["program"] = parsed_data["screen"]
        result = graph_task.execute(data)
        return result
    
    @task.python(trigger_rule=TriggerRule.ALL_DONE)
    def extract_dataset_assignment(jcl_file: dict, **context) -> dict:
        reverse_controller = ReverseController()
        node_controller = NodeController()
        edge_controller = EdgeController()
        jcl_dataset_assignment_extractor = JclDatasetAssignmentExtractor(
            reverse_controller, node_controller, edge_controller
        )
        
        jcl_name = jcl_file["name"]
        repository_id = context["params"]["repository_id"]
        dataset_assignment_models = jcl_dataset_assignment_extractor.extract_jcl_datasets(jcl_name, repository_id)
        dataset_assignments = [dataset_assignment.model_dump() for dataset_assignment in dataset_assignment_models]
        return {
            "dataset_assignments": dataset_assignments,
            "jcl_name": jcl_name
        }
    
    @task.python(trigger_rule=TriggerRule.ALL_DONE)
    def save_dataset_assignments(dataset_assignment_data: dict, **context) -> dict:
        dataset_assignments = dataset_assignment_data["dataset_assignments"]
        jcl_name = dataset_assignment_data["jcl_name"]
        repository_id = context["params"]["repository_id"]
        
        reverse_controller = ReverseController()
        reverse_controller.save_reverse_engineering(
            jcl_name,
            repository_id,
            ReverseEngineeringUpdate(status=ReverseEngineeringStatus.EXTRACTED_DATASET_ASSIGNMENT),
            type="JCL"
        )
        
        if len(dataset_assignments) == 0:
            return
        
        dataset_assignment_controller = DatasetAssignmentController()
        dataset_assignment_models = [JclDatasetAssignment(**dataset_assignment) for dataset_assignment in dataset_assignments]
        save_result = dataset_assignment_controller.save_dataset_assignments(dataset_assignment_models)
        
        return save_result
    
    files = get_files()
    
    filter_copy = filter_by_label.override(task_id="filter_copy")
    filter_jcl = filter_by_label.override(task_id="filter_jcl")
    filter_bms = filter_by_label.override(task_id="filter_bms")
    filter_pli = filter_by_label.override(task_id="filter_pli")
    filter_cobol = filter_by_label.override(task_id="filter_cobol")
    
    copy_files = filter_copy(files, "COPY")
    jcl_files = filter_jcl(files, "JCL")
    bms_files = filter_bms(files, "BMS")
    pli_files = filter_pli(files, "PLI")
    cobol_files = filter_cobol(files, "COBOL")
    
    # JCL flow
    parsed_jcl = parse_jcl.expand(file=jcl_files)
    saved_reverse_engineering_jcl = save_reverse_engineering.expand(parsed_data=parsed_jcl)
    graph_task_jcl = generate_graph.expand(parsed_data=parsed_jcl)
    
    saved_reverse_engineering_jcl >> graph_task_jcl
    
    # BMS flow
    parsed_bms = parse_bms.expand(file=bms_files)
    saved_reverse_engineering_bms = save_reverse_engineering.expand(parsed_data=parsed_bms)
    graph_task_bms = generate_graph.expand(parsed_data=parsed_bms)
    saved_reverse_engineering_bms >> graph_task_bms
    
    # PLI flow
    parsed_pli = parse_pli.expand(file=pli_files)
    saved_reverse_engineering_pli = save_reverse_engineering.expand(parsed_data=parsed_pli)
    graph_task_pli = generate_graph.expand(parsed_data=parsed_pli)
    saved_reverse_engineering_pli >> graph_task_pli
    
    # COBOL flow
    parsed_cobol = parse_cobol.expand(file=cobol_files)
    
    parsed_screen_access = parse_screen_access.expand(file=cobol_files)
    mapped_screen_access = map_screen_access.expand(parsed_screen_access=parsed_screen_access)
    graph_task_screen = generate_graph.expand(parsed_data=parsed_screen_access)
    mapped_screen_access >> graph_task_screen
    
    saved_reverse_engineering_cobol = save_reverse_engineering.expand(parsed_data=parsed_cobol)
    graph_task_cobol = generate_graph.expand(parsed_data=parsed_cobol)
    saved_reverse_engineering_cobol >> graph_task_cobol
    
    # COPYBOOK flow
    parsed_copy = parse_copybook.expand(file=copy_files)
    saved_reverse_engineering_copy = save_reverse_engineering.expand(parsed_data=parsed_copy)
    graph_task_copy = generate_graph.expand(parsed_data=parsed_copy)
    
    saved_reverse_engineering_copy >> graph_task_copy >> parsed_cobol
    
    # Dataset
    extracted_dataset_assignment = extract_dataset_assignment.expand(jcl_file=jcl_files)
    saved_dataset_assignments = save_dataset_assignments.expand(dataset_assignment_data=extracted_dataset_assignment)
    graph_task_jcl >> extracted_dataset_assignment
    graph_task_cobol >> extracted_dataset_assignment
    extracted_dataset_assignment >> saved_dataset_assignments
