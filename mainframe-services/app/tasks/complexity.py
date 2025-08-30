# coding: utf-8
import ast
import io
import time

import pandas as pd
from azure.storage.blob import BlobServiceClient
from bson import ObjectId
from loguru import logger

from app.config.database import get_database
from app.config.settings import settings
from app.constants.cobol import SystemType
from app.controllers.complexity_controller import create_complexity
from app.schemas.complexity_schema import ComplexityCreate


async def extract_complexity(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    t0 = time.time()
    logger.info(f"Extract complexity content from {repo_id}")
    db = await get_database()
    repo = await db.repositories.find_one({"_id": ObjectId(repo_id)})
    system_type = SystemType[repo.get("system_type", "IBM")]

    # Skip reverse engineering for Unisys, DNP systems
    # TODO: Add support for Unisys, DNP systems
    if system_type == SystemType.UNISYS or system_type == SystemType.DNP:
        logger.warning(
            f"Skip extracting complexity for {system_type.value} system {repo_id}"
        )
        return

    complexity = await db.complexities.find_one({"_id": ObjectId(repo_id)})
    if not complexity:
        complexity = {
            "_id": ObjectId(repo_id),
            "repository_id": ObjectId(repo_id),
        }

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(f"{repo_id}_parsed.csv")
    encoding = blob_client.get_blob_properties().metadata["encoding"]
    blob_data = blob_client.download_blob().readall()
    blob_stream = io.BytesIO(blob_data)
    df = pd.read_csv(
        blob_stream,
        escapechar="\\",
        encoding=encoding,
        on_bad_lines="warn",
    )
    df["complexity"] = df.apply(
        lambda x: get_complexity(x["label"], x["parsed_data"]), axis=1
    )
    df["complexity_category"] = df.apply(
        lambda x: add_complexity_cat(x["complexity"]), axis=1
    )
    df.drop(columns=["content", "encoding", "parsed_data"], inplace=True)

    complexity["result"] = {"complexity": df.to_dict(orient="records")}
    complexity["status"] = "done"

    await db.complexities.update_one(
        {"_id": ObjectId(repo_id)}, {"$set": complexity}, upsert=True
    )
    logger.info(
        f"Extract complexity repo {repo_id} successfully - Time: {str(time.time() - t0)}"
    )


def get_complexity(label, parsed_data):

    try:
        if type(parsed_data) == str:
            parsed_data = ast.literal_eval(parsed_data)
        match label:
            case "COBOL":
                return parsed_data["statsMap"]["VG"] + 1
            case "JCL_IBM":
                return parsed_data["VG_JCL"] + 1
            case "COPY":
                return parsed_data["statsMap"]["VG"] + 1
            case _:
                return 1
    except Exception as e:
        logger.error(e)
        return 1


def add_complexity_cat(complexity):
    if complexity < 100:
        return "Simple"
    if complexity >= 100 and complexity < 500:
        return "Medium"
    if complexity >= 500 and complexity < 1000:
        return "Complex"
    if complexity >= 1000:
        return "Very complex"
