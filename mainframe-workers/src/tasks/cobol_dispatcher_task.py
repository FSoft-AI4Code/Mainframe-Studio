from .base_task import BaseTask
from typing import Dict, Any
from dispatchers.cobol_parser_dispatcher import dispatch_cobol_files
from loguru import logger

class CobolDispatcherTask(BaseTask):
    def validate(self, task_data: Dict[str, Any]) -> bool:
        """
        Validate that the required fields are present in task_data
        
        Args:
            task_data (Dict[str, Any]): The task data to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not task_data.get('repository_id'):
            logger.error("No repository_id provided in task data")
            return False
        if not task_data.get('system_type'):
            logger.error("No system_type provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the COBOL dispatcher task
        
        Args:
            task_data (Dict[str, Any]): The task data containing repository_id
            
        Returns:
            Dict[str, Any]: Result of the dispatch operation
        """
        if not self.validate(task_data):
            return {
                "status": "error", 
                "message": "Invalid task data"
            }
            
        repository_id = task_data.get('repository_id')
        system_type = task_data.get('system_type')

        try:
            success_count, fail_count = dispatch_cobol_files(repository_id, system_type)
            return {
                "status": "success",    
                "message": f"Successfully dispatched COBOL files for repository {repository_id}. Success: {success_count}, Fail: {fail_count}"
            }
                
        except Exception as e:
            logger.error("Error dispatching COBOL files", error=str(e))
            return {
                "status": "error",
                "message": f"Error dispatching COBOL files: {str(e)}"
            }
