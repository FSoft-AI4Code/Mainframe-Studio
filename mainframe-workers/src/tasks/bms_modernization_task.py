from .base_task import BaseTask
from typing import Dict, Any
from utils.azure_blob_util import write_blob
from controller.reverse_controller import ReverseController
from modernization.bms_modernization import modernize_bms
import structlog
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
from config.settings import settings

logger = structlog.get_logger()

class BMSModernizationTask(BaseTask):
    def __init__(self):
        self.reverse_controller = ReverseController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('name') or not task_data.get('repository_id'):
            logger.error("No name or repository_id provided in task data")
            return False
        return True
        
    def check_blob_exists(self, blob_name: str, container_name: str = "$web") -> bool:
        """Check if a blob already exists in the specified container"""
        try:
            connection_string = settings.AZURE_STORAGE_CONNECTION_STRING
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            container_client = blob_service_client.get_container_client(container_name)
            blob_client = container_client.get_blob_client(blob_name)
            
            # Check if blob exists by trying to get its properties
            blob_client.get_blob_properties()
            return True
        except ResourceNotFoundError:
            return False
        except Exception as e:
            logger.error(f"Error checking if blob exists: {str(e)}")
            return False

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}
            
        name = task_data.get('name')
        repository_id = task_data.get('repository_id')
        
        # Define target blob name
        blob_name = f"{repository_id}/modernization/{name}.html"
        
        # Check if the modernized BMS already exists
        if self.check_blob_exists(blob_name, container_name="$web"):
            logger.info(f"Modernized BMS '{name}' already exists, skipping modernization")
            return {
                "status": "success",
                "message": f"Modernized BMS '{name}' already exists",
                "skip": True
            }

        try:
            bms_data = self.reverse_controller.query_reverse_engineering(name, repository_id, "BMS")
            if not bms_data:
                error_msg = f"No BMS data found for {name}"
                logger.error(error_msg)
                return {"status": "error", "message": error_msg}
            else:
                screen_string = bms_data.get("screen_string")
                modernized_screen = modernize_bms(screen_string)
                # Extract the html code from the output inside the ```html ... ``` block
                html_code = modernized_screen.content.split("```html")[1].split("```")[0]
                modernized_screen = html_code.strip()
                
                # Upload directly to blob storage
                upload_success = write_blob(blob_name, modernized_screen, 
                                          container_name="$web", 
                                          content_type="text/html")
                
                if not upload_success:
                    return {
                        "status": "error",
                        "message": "Failed to upload modernized BMS to blob storage"
                    }
                
                return {
                    "status": "success",
                    "message": f"Successfully modernized and uploaded BMS '{name}' to blob storage",
                }
                
        except Exception as e:
            logger.error("Error modernizing BMS file", error=str(e))
            return {
                "status": "error",
                "message": f"Error modernizing BMS file: {str(e)}"
            }
