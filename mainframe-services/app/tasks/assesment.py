# coding: utf-8
import io
import re
import time

import numpy as np
import pandas as pd
from azure.storage.blob import BlobServiceClient
from bson import ObjectId
from loguru import logger

from app.config.database import get_database
from app.config.settings import settings


async def extract_assessment(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    t0 = time.time()
    logger.info(f"Assesst content from {repo_id}")
    db = await get_database()
    repo = await db.repositories.find_one({"_id": ObjectId(repo_id)})
    # TODO: check if assessment not found -> create new one
    assessment = await db.assessments.find_one({"_id": ObjectId(repo_id)})

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    blob_client = container_client.get_blob_client(f"{repo_id}_classified.csv")
    blob_metadata = blob_client.get_blob_properties().metadata
    encoding = blob_metadata["encoding"]
    blob_data = blob_client.download_blob().readall()
    blob_stream = io.BytesIO(blob_data)
    df = pd.read_csv(
        blob_stream,
        escapechar="\\",
        encoding=encoding,
        on_bad_lines="warn",
    )

    df["result"] = df.apply(
        lambda row: count_line(row["content"], row["label"]), axis=1
    )
    df[["code", "comment"]] = pd.DataFrame(df["result"].tolist(), index=df.index)
    df.drop(columns=["result", "content", "encoding"], inplace=True)

    values = df["code"].to_list()
    frequencies, bins = np.histogram(values, bins="auto")
    log_frequencies = np.log10(frequencies + 1)  # Adding 1 to avoid log(0)

    assessment["result"] = {
        "assessment": df.to_dict(orient="records"),
        "code_dist": {
            "frequencies": frequencies.tolist(),
            "log_frequencies": log_frequencies.tolist(),
            "bins": bins.tolist(),
        },
    }
    assessment["status"] = "done"

    await db.assessments.update_one({"_id": ObjectId(repo_id)}, {"$set": assessment})

    repo["status"] = "assessed"
    repo["is_assessed"] = True
    await db.repositories.update_one({"_id": ObjectId(repo_id)}, {"$set": repo})
    logger.info(f"Assesst repo {repo_id} successfully - Time: {str(time.time() - t0)}")


def count_line(code: str, label: str):

    match label:
        case "COBOL" | "COPY" | "DB":
            count = fast_analyze_cobol(code)
        case "JCL":
            count = fast_analyze_jcl_ibm(code)
        case "BMS":
            count = fast_analyze_bms(code)
        case _:
            count = len(code.split("\n")), 0

    return count


def fast_analyze_cobol(code: str):

    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = 0
    code_with_comment_lines = 0
    for line in lines:
        if len(line) > 7 and line[6] == "*":
            comment_lines += 1

        # check *> not in string
        split = line.split("'")

        for i in range(0, len(split), 2):
            if "*>" in split[i]:
                comment_lines += 1

                if re.search(r"[A-Za-z0-9]", line[: line.find("*>")]):
                    code_with_comment_lines += 1

    loc = total_lines - empty_lines - comment_lines + code_with_comment_lines

    # print(parse_file_output['statsMap'])

    return [loc, comment_lines]


def fast_analyze_jcl_ibm(code: str):
    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^/{1,2}\*", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_bms(code: str):
    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^\s*\*", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_jcl_fujitsu(code: str):
    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"^\\\*", code, re.MULTILINE))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_pli(code: str):
    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_lines = len(re.findall(r"/\*.*\*/", code))

    loc = total_lines - empty_lines - comment_lines

    return [loc, comment_lines]


def fast_analyze_csd(code: str):
    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    loc = total_lines - empty_lines

    return [loc, 0]


def fast_analyze_sql(code: str):
    lines = code.split("\n")
    total_lines = len(lines)
    empty_lines = len(re.findall(r"^\s*$", code, re.MULTILINE))

    comment_blocks = re.findall(r"/\*[\s\S]*\*/", code)
    comment_line_count = 0

    for line in comment_blocks:
        comment_line_count += len(line.splitlines())

    comment_blocks_lines = [
        line for block in comment_blocks for line in block.splitlines()
    ]

    for line in lines:
        if re.search(r"^\s*--", line) and line not in comment_blocks_lines:
            comment_line_count += 1
    loc = total_lines - empty_lines - comment_line_count

    # for line in lines:
    #     if line in_comm
    #     split = line.split("'")

    #     # check -- not in string
    #     for i in range(0, len(split), 2):
    #         if "--" in split[i]:
    #             comment_lines += 1
    #             break

    # loc = total_lines - empty_lines - comment_lines

    # return loc, comment_line_count
    return [loc, comment_line_count]
