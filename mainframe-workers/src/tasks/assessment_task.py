import numpy as np
import pandas as pd
from typing import Dict, Any

from loguru import logger

from assessor import count_line
from utils.azure_blob_util import classify_blobs, write_blob_csv
from controller.assessment_controller import AssessmentController
from schema.assessment import AssessmentUpdate

from .base_task import BaseTask


class AssessmentTask(BaseTask):
    def __init__(self):
        self.assessment_controller = AssessmentController()

    def validate(self, task_data: Dict[str, Any]) -> bool:
        """Validate that the required fields are present in task_data"""
        if not task_data.get('repository_id'):
            logger.error("No repository_id provided in task data")
            return False
        return True

    @logger.catch
    def execute(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.validate(task_data):
            return {"status": "error", "message": "Invalid task data"}

        repository_id = task_data.get('repository_id')
        system_type = task_data.get('system_type')

        df = classify_blobs(repository_id, system_type)

        df["result"] = df.apply(
            lambda row: count_line(row["content"], row["label"]), axis=1
        )
        df[["code", "comment"]] = pd.DataFrame(
            df["result"].tolist(), index=df.index)

        write_blob_csv(f"{repository_id}_classified.csv", df)

        df.drop(columns=["result", "content", "encoding"], inplace=True)

        values = df["code"].to_list()

        frequencies, bins = np.histogram(values, bins="auto")
        log_frequencies = np.log10(frequencies + 1)

        self.assessment_controller.save_assessment(
            repository_id=repository_id,
            assessment=AssessmentUpdate(
                result={
                    "assessment": df.to_dict(orient="records"),
                    "code_dist": {
                        "frequencies": frequencies.tolist(),
                        "log_frequencies": log_frequencies.tolist(),
                        "bins": bins.tolist(),
                    },
                },
                status="done",
            )
        )

        logger.info(f"Successfully processed assessment for {repository_id}")

        # except Exception as e:
        #     logger.error("Error processing assessment", error=str(e))
        #     return {
        #         "status": "error",
        #         "message": f"Error processing assessment: {str(e)}"
        #     }
