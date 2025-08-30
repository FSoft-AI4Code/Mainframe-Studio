# coding: utf-8
import ast
import io
import re
import time
import unicodedata
from app.config.database import get_database
import charset_normalizer
import numpy as np
import pandas as pd
from azure.storage.blob import BlobServiceClient
from azure.core.pipeline.transport import RequestsTransport
import urllib3
from bson import ObjectId
from langchain.schema import HumanMessage, SystemMessage
from loguru import logger
from pandarallel import pandarallel
from tqdm.auto import tqdm
import concurrent.futures
from pymongo import UpdateOne

from app.config.constants import IBM_MAINFRAME_UTILITIES
from app.config.settings import settings
from app.constants.cobol import SystemType
from app.schemas.reverse_schema import ReverseEngineeringStatus

from .classifier import RuleBasedTextClassifierBySystem
from .parser import Parser
from .reverse.bms import  parse_bms
from .reverse.cobol import (
    CopybookDependency,
    parse_cobol_antlr,
    parse_cobol_dnp,
    parse_cobol_unisys,
)
from .reverse.copy import COPY_TEMPLATE
from .reverse.jcl import parse_jcl_antlr
from multiprocessing import Pool
from functools import partial
from .utils import (
    clean_code,
    comment_specific_lines,
    remove_bms_title_line,
    trigger_airflow_dag
)

parser = Parser(
    cache_path="tmp",
    cobol_parser_path="koopa.jar",
    jcl_parser_path="jcl_parser.jar",
)

def get_blob_service_client(connection_string: str):
    # Configure connection pooling
    transport = RequestsTransport(
        connection_pool_size=30,
        connection_timeout=30,
        read_timeout=30,
        retries=3
    )
    
    return BlobServiceClient.from_connection_string(
        conn_str=connection_string,
        transport=transport
    )

def parse_ibm(content, encoding, label, copy_map, dependency_map):
    try:
        match label:
            case "COBOL":
                output = parser.parse_cobol(
                    code=content, encoding=encoding, copy_map=copy_map
                )
                output.update(
                    parse_cobol_antlr(
                        code=content, dependency_map=dependency_map
                    ).model_dump()
                )
                return output
            case "JCL_IBM":
                return parse_jcl_antlr(content).model_dump()
            case "COPY":
                output = parser.parse_copy(code=content, encoding=encoding, copy_map={})
                output.update(
                    parse_cobol_antlr(
                        code=COPY_TEMPLATE.format(content), dependency_map={}
                    ).model_dump()
                )
                return output
            case "BMS":
                return parse_bms(remove_bms_title_line(content))
            case _:
                return {}
    except Exception as e:
        logger.error(e)
        return {}


def parse_unisys(content, encoding, label, copy_map, dependency_map):
    try:
        match label:
            case "COBOL":
                return parse_cobol_unisys(content, dependency_map).model_dump()
            case "COPY":
                return parse_cobol_unisys(
                    COPY_TEMPLATE.format(content), {}
                ).model_dump()
            case _:
                return {}
    except Exception as e:
        logger.error(e)
        return {}


def parse_dnp(content, encoding, label, copy_map, dependency_map):
    try:
        match label:
            case "COBOL":
                return parse_cobol_dnp(content, dependency_map).model_dump()
            case "COPY":
                return parse_cobol_dnp(COPY_TEMPLATE.format(content), {}).model_dump()
            case _:
                return {}
    except Exception as e:
        logger.error(e)
        return {}


async def parse_repo(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    logger.info(f"Parsing content from {repo_id}")
    db = ctx["db"]  # Get injected database connection
    repo = await db.repositories.find_one({"_id": ObjectId(repo_id)})
    system_type = SystemType(repo["system_type"])

    pandarallel.initialize(progress_bar=True)

    logger.info(f"Parsing content from {repo_id}")

    blob_service_client = get_blob_service_client(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(f"{repo_id}_classified.csv")
    blob_data = blob_client.download_blob().readall()
    blob_metadata = blob_client.get_blob_properties()
    encoding = blob_metadata.metadata["encoding"]

    blob_stream = io.BytesIO(blob_data)

    df = pd.read_csv(
        blob_stream,
        escapechar="\\",
        encoding=encoding,
        on_bad_lines="warn",
    )

    t0 = time.time()
    copy_df = df[df["label"] == "COPY"].copy()

    if not copy_df.empty:
        match system_type:
            case SystemType.IBM:
                copy_df["dependency"] = copy_df.apply(
                    lambda row: CopybookDependency(
                        parsed_data=parse_cobol_antlr(
                            COPY_TEMPLATE.format(row["content"]), {}
                        ).model_copy(update={"program_id": row["name"]}),
                        code_content=row["content"],
                    ),
                    axis=1,
                )
            case SystemType.UNISYS:
                copy_df["dependency"] = copy_df.apply(
                    lambda row: CopybookDependency(
                        parsed_data=parse_cobol_unisys(
                            COPY_TEMPLATE.format(row["content"]), {}
                        ).model_copy(update={"program_id": row["name"]}),
                        code_content=row["content"],
                    ),
                    axis=1,
                )
            case SystemType.DNP:
                copy_df["dependency"] = copy_df.apply(
                    lambda row: CopybookDependency(
                        parsed_data=parse_cobol_dnp(
                            COPY_TEMPLATE.format(row["content"]), {}
                        ).model_copy(update={"program_id": row["name"]}),
                        code_content=row["content"],
                    ),
                    axis=1,
                )
    else:
        copy_df["dependency"] = None

    copy_df.set_index("name", inplace=True)
    # Remove extension from copybook names
    copy_df.index = copy_df.index.str.split(".").str[0]

    df = df[df["label"] != "OTHER"]
    # Shuffle to avoid one chunk being more expensive than the others in pandas parallel apply
    df = df.sample(frac=1)

    match system_type:
        case SystemType.IBM:
            df["parsed_data"] = df.parallel_apply(
                lambda row: parse_ibm(
                    row["content"],
                    row["encoding"],
                    row["label"],
                    copy_map=copy_df["content"].to_dict(),
                    dependency_map=copy_df["dependency"].to_dict(),
                ),
                axis=1,
            )
        case SystemType.UNISYS:
            df["parsed_data"] = df.parallel_apply(
                lambda row: parse_unisys(
                    row["content"],
                    row["encoding"],
                    row["label"],
                    copy_map=copy_df["content"].to_dict(),
                    dependency_map=copy_df["dependency"].to_dict(),
                ),
                axis=1,
            )
        case SystemType.DNP:
            df["parsed_data"] = df.parallel_apply(
                lambda row: parse_dnp(
                    row["content"],
                    row["encoding"],
                    row["label"],
                    copy_map=copy_df["content"].to_dict(),
                    dependency_map=copy_df["dependency"].to_dict(),
                ),
                axis=1,
            )
    t1 = time.time()

    csv_string = df.to_csv(
        index=False, escapechar="\\", doublequote=True, encoding=encoding
    )
    csv_bytes = csv_string.encode(encoding)

    # Upload the bytes object to Azure Blob Storage
    blob_client = container_client.get_blob_client(blob=f"{repo_id}_parsed.csv")
    blob_client.upload_blob(csv_bytes, overwrite=True)

    blob_metadata = blob_client.get_blob_properties().metadata
    blob_metadata.update({"encoding": encoding})
    blob_client.set_blob_metadata(metadata=blob_metadata)

    repo["status"] = "parsed"
    await db.repositories.update_one({"_id": ObjectId(repo_id)}, {"$set": repo})
    logger.info(
        f"Uploaded the parsed dataframe CSV file to Azure Blob Storage: {repo_id}_parsed.csv - Time: {str(t1 - t0)}"
    )

async def process_duplicate_files(repository_id: str, df: pd.DataFrame):
    df_duplicated = df[df.duplicated(subset=["name", "label"], keep=False)]
    db = await get_database()
    if db is None:
        logger.error("Cannot connect to database to store duplicate files")
        return

    duplicate_dict = {}
    for _, row in df_duplicated.iterrows():
        name = row["name"]
        label = row["label"]
        content = row["content"]
        path = row["path"]
        key = (name, label)
        if key not in duplicate_dict:
            duplicate_dict[key] = []
        duplicate_dict[key].append({"repository_id": ObjectId(repository_id), "content": content, "encoding": row["encoding"], "path": path, "same_content_with": []})
        
    for key, values in duplicate_dict.items():
        name, label = key
        
        for i in range(len(values)):
            for j in range(len(values)):
                if i != j and values[i]["content"] == values[j]["content"]:
                    values[i]["same_content_with"].append(values[j]["path"])
            
    duplicate_list = []
    for key, values in duplicate_dict.items():
        name, label = key
        for value in values:
            value["name"] = name
            value["label"] = label
            del value["content"]
            duplicate_list.append(value)
    
    operations = []
    for value in duplicate_list:
        filter_query = {
            "repository_id": value["repository_id"],
            "name": value["name"],
            "label": value["label"],
            "path": value["path"]
        }
        update_doc = {"$set": value}
        operations.append(UpdateOne(filter_query, update_doc, upsert=True))
    if operations:
        await db.duplicate_files.bulk_write(operations)

def classify_by_system_type(content: str, encoding: str, system_type: SystemType):
    try:
        classifier = RuleBasedTextClassifierBySystem()
        return classifier.detect(code=content, encoding=encoding, system_type=system_type)
    except Exception as e:
        logger.error(f"Error classifying content: {e} | Encoding: {encoding} | System Type: {system_type}", exc_info=True, stack_info=True)
        return None

async def classify_repo(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    logger.info(f"Classifying content from {repo_id}")
    db = ctx["db"]  # Get injected database connection
    repo = await db.repositories.find_one({"_id": ObjectId(repo_id)})
    system_type = SystemType(repo["system_type"])
    logger.info(f"Classifying with system type: {system_type.value}")

    blob_service_client = get_blob_service_client(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(f"{repo_id}.csv")
    blob_data = blob_client.download_blob().readall()
    blob_metadata = blob_client.get_blob_properties()
    encoding = blob_metadata.metadata["encoding"]

    blob_stream = io.BytesIO(blob_data)

    df = pd.read_csv(
        blob_stream,
        escapechar="\\",
        encoding=encoding,
        on_bad_lines="warn",
    )
    t0 = time.time()
    # Drop rows with NaN in 'content' or 'encoding'. Reset the index after dropping rows.
    df = df.dropna(subset=["content", "encoding"])
    df = df.reset_index(drop=True)
    logger.info(f"Classifying {len(df)} files")
    tqdm.pandas()
    df["label"] = df.progress_apply(
        lambda row: classify_by_system_type(
            row["content"], row["encoding"], system_type
        ),
        axis=1,
    )
    await process_duplicate_files(repo_id, df)
    t1 = time.time()

    csv_string = df.to_csv(
        index=False, escapechar="\\", doublequote=True, encoding=encoding
    )
    csv_bytes = csv_string.encode(encoding)

    # Upload the bytes object to Azure Blob Storage
    blob_client = container_client.get_blob_client(blob=f"{repo_id}_classified.csv")
    blob_client.upload_blob(csv_bytes, overwrite=True)

    blob_metadata = blob_client.get_blob_properties().metadata
    blob_metadata.update({"encoding": encoding})
    blob_client.set_blob_metadata(metadata=blob_metadata)
    logger.info("Uploaded the classified dataframe CSV file to Azure Blob Storage")

    def process_file(row):
        try:
            label = row["label"].value
            path = row["path"]
            file_name = row["name"]

            # This is a async operation but we are using it in a sync way
            # therefore the condition always return a Future object which make
            # the condition always True
            # if not db.reverse_engineering.find_one(
            #     filter={
            #         "repository_id": ObjectId(repo_id),
            #         "name": file_name,
            #         "type": label,
            #     }
            # ):

            # Workaroud is to upsert the document whether it exists or not
            classify_status = ReverseEngineeringStatus.CLASSIFIED if label is not None else ReverseEngineeringStatus.CLASSIFIED_ERROR
            db.reverse_engineering.update_one(
                filter={
                    "repository_id": ObjectId(repo_id),
                    "name": file_name,
                    "type": label,
                },
                update={
                    "$set": {
                        "name": file_name,
                        "path": path,
                        "type": label,
                        "repository_id": ObjectId(repo_id),
                        "status": classify_status,
                    }
                },
                upsert=True,
            )

            with get_blob_service_client(connection_string) as blob_service_client:
                container_client = blob_service_client.get_container_client(container_name)
                # Get source blob content
                source_blob_client = container_client.get_blob_client(blob=path)
                source_blob_data = source_blob_client.download_blob().readall()
                encoding = charset_normalizer.detect(source_blob_data)['encoding']
                
                # Upload to new standardized path
                target_blob_client = container_client.get_blob_client(blob=f"{repo_id}/code/{label}/{file_name}")
                target_blob_client.upload_blob(source_blob_data, overwrite=True)
                
                # Set encoding metadata
                blob_metadata = target_blob_client.get_blob_properties().metadata
                blob_metadata.update({"encoding": encoding})
                target_blob_client.set_blob_metadata(metadata=blob_metadata)
                return True
        except Exception as e:
            logger.error(f"Error processing file {path}: {str(e)}")
            return False

    # Convert DataFrame to list of dictionaries
    rows = df.to_dict('records')
    
    # Use concurrent.futures with tqdm
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        results = list(tqdm(
            executor.map(process_file, rows),
            total=len(rows),
            desc="Processing files"
        ))

    repo["status"] = "classified"
    await db.repositories.update_one({"_id": ObjectId(repo_id)}, {"$set": repo})
    trigger_airflow_dag(
        dag_id="reverse_repo",
        airflow_base_url=settings.AIRFLOW_BASE_URL,
        username=settings.AIRFLOW_USERNAME,
        password=settings.AIRFLOW_PASSWORD,
        conf={"repository_id": repo_id}
    )
    logger.info(
        f"Uploaded the classified dataframe CSV file to Azure Blob Storage: {repo_id}_classified.csv - Time: {str(t1-t0)}"
    )


def read_blob(blob_data: bytes):
    file_content = charset_normalizer.from_bytes(
        blob_data,
        cp_isolation=[
            "utf-8",
            "shift_jis",
        ],
    ).best()

    if file_content is None:
        file_content = charset_normalizer.from_bytes(blob_data).best()

        if file_content is None:
            return None, None

    return str(file_content), file_content.encoding


async def read_content(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):

    logger.info(f"Reading content from {container_name}")
    db = ctx["db"]  # Get injected database connection
    # TODO: check status repo if done
    blob_service_client = get_blob_service_client(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blobs = container_client.list_blobs(name_starts_with=repo_id)

    outputs = []
    # Download each blob
    repo_encoding = "utf-16"  # encoding for the whole blob
    for blob in blobs:
        # TODO: remove after seprate azure container for csv files
        if blob.name.endswith(".csv") or "/code/" in blob.name:
            continue
        blob_client = container_client.get_blob_client(blob)
        blob_data = blob_client.download_blob().readall()
        blob_content, encoding = read_blob(blob_data)
        if blob_content is None or encoding is None:
            logger.error(f"Cannot read file {blob.name} - Repo: {repo_id}")
        else:
            blob_name = blob.name.split("/")[-1]
            blob_name_without_extension = blob_name.split(".")[0]
            outputs.append(
                {
                    "name": blob_name_without_extension,
                    "path": blob.name,
                    "content": blob_content,
                    "encoding": encoding,
                }
            )
            # TODO: create parsed_data document for each blob

    logger.info(f"Downloaded all blobs from {repo_id}")

    df = pd.DataFrame(outputs)
    csv_string = df.to_csv(
        index=False, escapechar="\\", doublequote=True, encoding=repo_encoding
    )
    csv_bytes = csv_string.encode(repo_encoding)

    # Upload the bytes object to Azure Blob Storage
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=f"{repo_id}.csv"
    )
    blob_client.upload_blob(csv_bytes, overwrite=True)

    blob_metadata = blob_client.get_blob_properties().metadata
    blob_metadata.update({"encoding": repo_encoding})
    blob_client.set_blob_metadata(metadata=blob_metadata)

    # Update repo status
    repo = await db.repositories.find_one({"_id": ObjectId(repo_id)})
    repo["status"] = "readed"
    await db.repositories.update_one({"_id": ObjectId(repo_id)}, {"$set": repo})
    logger.info(f"Uploaded the dataframe CSV file to Azure Blob Storage: {repo_id}.csv")
