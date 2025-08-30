from .base_task import BaseTask
from typing import Dict, Any
from controller.reverse_controller import ReverseController
from loguru import logger
from llm.statement_summarization import statement_summary

class StatementSummarizationTask(BaseTask):
    def __init__(self):
        self.reverse_controller = ReverseController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate task data has required fields"""
        if not task_data.get('name') or not task_data.get('repository_id'):
            logger.error("No name or repository_id provided in task data")
            return False
        return True

    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute statement summarization task"""
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}
            
        name = task_data.get('name')
        repository_id = task_data.get('repository_id')

        try:
            # Get the parsed program from reverse engineering collection
            program = self.reverse_controller.query_reverse_engineering(
                name, 
                repository_id,
                'COBOL'
            )
            if not program:
                return {
                    "status": "error",
                    "message": f"Program {name} not found in repository {repository_id}"
                }

            # Generate statement summaries
            summary = statement_summary(program.get("statements", []))

            # Save the summary
            save_result = self.reverse_controller.save_statement_summary(
                name,
                repository_id, 
                summary,
                'COBOL'
            )

            if save_result.get("status") == "error":
                return {
                    "status": "error",
                    "message": save_result.get("message", "Error saving summary")
                }

            return {
                "status": "success",
                "message": "Successfully generated and saved statement summary"
            }

        except Exception as e:
            logger.error("Error summarizing COBOL statements", error=str(e))
            return {
                "status": "error", 
                "message": f"Error summarizing COBOL statements: {str(e)}"
            }
