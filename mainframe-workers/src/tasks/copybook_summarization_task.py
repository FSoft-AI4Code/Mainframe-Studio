from typing import Dict, Any
from loguru import logger
from tasks.base_task import BaseTask
from controller.summarization_controller import CopybookSummaryController
from schema.summarization import CopybookSummary
from summarization.copybook_summarization import CopybookSummarizer

class CopybookSummarizationTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.controller = CopybookSummaryController()
        self.summarizer = CopybookSummarizer()

    def execute(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the copybook summarization task.
        
        Args:
            data: Dictionary containing:
                - repository_id: str
                - path: str (path to copybook file)
                - content: str (copybook content)
        
        Returns:
            Dict containing status and result
        """
        try:
            # Create initial summary with running status
            summary = CopybookSummary(
                repository_id=data["repository_id"],
                status="running",
                path=data["path"]
            )
            self.controller.save_summary(summary)

            # Process the copybook content
            result = self.summarizer.summarize(data["content"])
            
            # Update summary with results
            summary.status = "done"
            summary.short_description = result.get("short_description")
            summary.fields = result.get("fields", [])
            summary.groups = result.get("groups", [])
            summary.record_length = result.get("record_length")
            
            # Save final summary
            save_result = self.controller.save_summary(summary)
            
            if save_result["status"] == "success":
                return {
                    "status": "success",
                    "message": "Copybook summarization completed successfully",
                    "data": summary.model_dump()
                }
            else:
                return {
                    "status": "error",
                    "message": f"Error saving summary: {save_result['message']}"
                }

        except Exception as e:
            logger.error(f"Error in copybook summarization task: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            } 