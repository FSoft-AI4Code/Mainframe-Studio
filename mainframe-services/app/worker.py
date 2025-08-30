import io

import pandas as pd
import psutil
from azure.storage.blob import BlobServiceClient
from bson import ObjectId
from loguru import logger
from saq import Queue
from saq.job import Status

from app.config.database import get_database
from app.config.settings import settings
from app.constants.cobol import SystemType
from app.tasks import (
    classify_repo,
    extract_assessment,
    extract_complexity,
    parse_repo,
    read_content,
    reverse_bmss,
    reverse_cobol,
    reverse_cpy,
    reverse_jcl,
    trigger_create_graph,
    trigger_init_nebula,
)

logger.add("worker.log")


class MainframeQueue(Queue):
    async def enqueue(self, job_or_func, **kwargs):
        default_kwargs = {"ttl": -1, "timeout": 10000}
        default_kwargs.update(kwargs)
        return await super().enqueue(job_or_func, **default_kwargs)


queue = MainframeQueue.from_url(settings.REDIS_URL)


async def before_process(ctx):
    # Inject database connection into context
    ctx["db"] = await get_database()
    if ctx["job"].function in ["reverse_cobol", "reverse_jcl"]:
        pass
    else:
        logger.info(ctx)


async def after_process(ctx):
    if ctx["job"].status == Status.COMPLETE:
        match ctx["job"].function:
            case "read_content":
                await queue.enqueue(
                    "classify_repo", repo_id=ctx["job"].kwargs["repo_id"], timeout=10000
                )
            case "classify_repo":
                await queue.enqueue(
                    "extract_assessment",
                    repo_id=ctx["job"].kwargs["repo_id"],
                    timeout=10000,
                )
            case "parse_repo":  # TODO: seprate pipeline
                await queue.enqueue(
                    "trigger_create_graph",
                    repo_id=ctx["job"].kwargs["repo_id"],
                    timeout=10000,
                )
                await queue.enqueue(
                    "extract_complexity",
                    repo_id=ctx["job"].kwargs["repo_id"],
                    timeout=10000,
                )
                # for each cbl and jcl
                await trigger_reverse_engineering(ctx["job"].kwargs["repo_id"])
            case "trigger_create_graph":
                await queue.enqueue(
                    "trigger_init_nebula",
                    repo_id=ctx["job"].kwargs["repo_id"],
                    timeout=10000,
                )
    else:
        logger.error(ctx)


async def trigger_reverse_engineering(
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    db = await get_database()
    repo = await db.repositories.find_one({"_id": ObjectId(repo_id)})
    system_type = SystemType[repo.get("system_type", "IBM")]

    # Skip reverse engineering for Unisys, DNP systems
    # TODO: Add support for Unisys, DNP
    if system_type == SystemType.UNISYS or system_type == SystemType.DNP:
        logger.warning(
            f"Skip reverse engineering for {system_type.value} system {repo_id}"
        )
        return

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(f"{repo_id}_parsed.csv")
    blob_data = blob_client.download_blob().readall()
    encoding = blob_client.get_blob_properties().metadata["encoding"]
    blob_stream = io.BytesIO(blob_data)
    df = pd.read_csv(
        blob_stream,
        escapechar="\\",
        encoding=encoding,
        on_bad_lines="warn",
    )

    jobs = [
        await queue.enqueue("reverse_bmss", repo_id=repo_id, timeout=10000),
        await queue.enqueue("reverse_cpy", repo_id=repo_id, timeout=10000),
    ]
    for _, row in df.iterrows():
        match row["label"]:
            case "COBOL":
                job = await queue.enqueue(
                    "reverse_cobol",
                    blob_path=row["path"],
                    parsed_data=row["parsed_data"],
                    timeout=10000,
                )
                jobs.append(job)
            case "JCL_IBM":
                job = await queue.enqueue(
                    "reverse_jcl",
                    blob_path=row["path"],
                    parsed_data=row["parsed_data"],
                    timeout=10000,
                )
                jobs.append(job)
            case _:
                continue

    # Wait for all jobs to complete or fail
    for job in jobs:
        try:
            await job.refresh(until_complete=0)
        except Exception as e:
            logger.error(job.info())

    repo["is_reversed"] = True
    await db.repositories.update_one({"_id": ObjectId(repo_id)}, {"$set": repo})
    logger.info(f"Reverse engineering completed for {repo_id}")


settings = {
    "queue": queue,
    "functions": [
        read_content,
        classify_repo,
        parse_repo,
        reverse_cobol,
        reverse_bmss,
        reverse_jcl,
        reverse_cpy,
        extract_assessment,
        extract_complexity,
        trigger_create_graph,
        trigger_init_nebula,
    ],
    "concurrency": psutil.cpu_count(logical=False),
    "before_process": before_process,
    "after_process": after_process,
}
