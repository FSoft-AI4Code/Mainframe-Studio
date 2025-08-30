from config.settings import settings
from utils.rabbitmq_util import produce_dispatch_task, produce_graph_task, produce_task
from .base_task import BaseTask
from typing import Dict, Any
from utils.azure_blob_util import read_blob_file, read_blob_csv
from parsers.copybook_parser_dnp import parse_copybook_dnp
from controller.reverse_controller import ReverseController
from loguru import logger


class CopybookDNPParserTask(BaseTask):
    def __init__(self):
        self.reverse_controller = ReverseController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        if not task_data.get('repository_id'):
            logger.error("No repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}
            
        repository_id = task_data.get('repository_id')
        results = []
        
        try:
            blob_name = f"{repository_id}_classified.csv"
            df = read_blob_csv(blob_name)
            copybook_df = df[df['label'] == 'COPY'].copy()
            for _, row in copybook_df.iterrows():
                try:
                    name = row['name']
                    content_path = f"{repository_id}/code/COPY/{name}"
                    content = read_blob_file(content_path)
                    
                    parsed_copybook = parse_copybook_dnp(content)
                    if parsed_copybook:
                        save_result = self.reverse_controller.save_reverse_engineering(
                            name, repository_id, parsed_copybook, 'COPY'
                        )
                        results.append({
                            "name": name,
                            "status": save_result["status"],
                            "message": save_result.get("message", "Successfully saved reversed copybook")
                        })
                        produce_graph_task(repository_id, name, "COPY")
                    else:
                        results.append({
                            "name": name,
                            "status": "error",
                            "message": f"Failed to parse copybook {name}"
                        })
                except Exception as e:
                    logger.error(f"Error processing copybook {name}: {str(e)}")
                    results.append({
                        "name": name,
                        "status": "error",
                        "message": f"Error processing copybook: {str(e)}"
                    })

            successful = sum(1 for r in results if r["status"] == "success")
            failed = sum(1 for r in results if r["status"] == "error")

            produce_dispatch_task("DNP", repository_id)
            
            return {
                "status": "completed",
                "message": f"Processed {len(results)} copybooks: {successful} successful, {failed} failed",
            }
                
        except Exception as e:
            logger.error("Error processing DNP copybooks", error=str(e))
            return {
                "status": "error",
                "message": f"Error processing DNP copybooks: {str(e)}"
            }