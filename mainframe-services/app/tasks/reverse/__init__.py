# coding: utf-8
import ast
import io
import re
import time

import pandas as pd
from azure.storage.blob import BlobServiceClient
from bson import ObjectId
from langchain.schema import HumanMessage, SystemMessage
from loguru import logger

from app.config.constants import IBM_MAINFRAME_UTILITIES
from app.config.database import get_database
from app.config.llm_client import get_llm
from app.config.settings import settings
from app.controllers.reverse_controller import (
    get_reverse_engineering_by_path,
    update_reverse_engineering,
)
from app.schemas.reverse_schema import ReverseEngineeringUpdate

from ..reverse.bms import AnalyzedBMS
from ..reverse.cobol import AnalyzedProgram
from ..utils import extract_related_pgms


async def reverse_cobol(ctx, *, blob_path: str, parsed_data: str):
    t0 = time.time()
    logger.info(f"Reverse engineering content from {blob_path}")
    db = await get_database()
    reverse = await get_reverse_engineering_by_path(db, blob_path)

    if reverse is None:
        logger.error(f"Reverse engineering task not found for {blob_path}")
        raise Exception(f"Reverse engineering task not found for {blob_path}")

    llm = get_llm()

    parsed_data_dict = ast.literal_eval(parsed_data)
    program = AnalyzedProgram(parsed_data_dict)
    program.extract_all(llm)

    reverse_update_payload = ReverseEngineeringUpdate(
        status="done",
        output={
            "label": "COBOL",
            "overview": program.overview.model_dump(),
            "io_params_def": program.io_params_def.model_dump(),
            "process_logic": program.process_logic,
            "copy_graph": program.copy_graph.model_dump(),
        },
        type="COBOL",
    )

    await update_reverse_engineering(db, reverse.id, reverse_update_payload)
    logger.info(
        f"Reverse engineering COBOL task completed for {blob_path} - Time: {str(time.time() - t0)}"
    )


async def reverse_bmss(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    t0 = time.time()
    logger.info(f"Reverse engineering bms content for {repo_id}")
    db = await get_database()
    # reverse = await get_reverse_engineering_by_path(db, blob_path)

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

    bmss_df = df[df["label"] == "BMS"]
    cobols_df = df[df["label"] == "COBOL"]

    cobols = {}
    for _, row in cobols_df.iterrows():
        try:
            parsed_data = ast.literal_eval(row["parsed_data"])
            cobols[row["name"]] = parsed_data.get("cics_map", [])
        except Exception as e:
            logger.error(f"Error processing COBOL file {row['name']}: {str(e)}")
            cobols[row["name"]] = []

    bmss = []
    for _, row in bmss_df.iterrows():
        bms = AnalyzedBMS(
            file_name=row["name"],
            path=row["path"],
            definitions=ast.literal_eval(row["parsed_data"]),
        )
        bms.extract_data()
        bmss.append(bms)

    outputs = extract_related_pgms(cobols, bmss)

    for out in outputs:
        reverse = await get_reverse_engineering_by_path(db, out.path)
        if reverse is None:
            logger.error(f"Reverse engineering task not found for {out.path}")

        reverse_update_payload = ReverseEngineeringUpdate(
            status="done",
            output={
                "label": "BMS",
                "overview": out.overview.model_dump(),
                "data": [item.model_dump() for item in out.data] if out.data else [],
                "screen_string": out.screen_string,
            },
            type="BMS",
        )

        await update_reverse_engineering(db, reverse.id, reverse_update_payload)
    logger.info(
        f"Reverse engineering task BMS completed for {repo_id} - - Time: {str(time.time() - t0)}"
    )


async def reverse_cpy(
    ctx,
    *,
    repo_id: str,
    container_name: str = settings.AZURE_STORAGE_CONTAINER_NAME,
    connection_string: str = settings.AZURE_STORAGE_CONNECTION_STRING,
):
    t0 = time.time()
    logger.info(f"Reverse engineering cpy content for {repo_id}")
    db = await get_database()
    # reverse = await get_reverse_engineering_by_path(db, blob_path)

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

    cpy_df = df[df["label"] == "COPY"]

    def map_picture_clause(picture_clause):
        if picture_clause is None:
            return None
        if "X" in picture_clause or "A" in picture_clause:
            return "char"
        elif "9" in picture_clause or "S9" in picture_clause:
            return "numeric"
        else:
            return None

    for _, row in cpy_df.iterrows():
        reverse = await get_reverse_engineering_by_path(db, row["path"])
        if reverse is None:
            logger.error(f"Reverse engineering task not found for {row['path']}")

        reverse_update_payload = ReverseEngineeringUpdate(
            status="done",
            output={
                "variables": [
                    {
                        **variable,
                        "data_type": map_picture_clause(variable["picture_clause"]),
                    }
                    for variable in ast.literal_eval(row["parsed_data"])[
                        "variable_list"
                    ]
                ]
            },
            type="COPY",
        )

        await update_reverse_engineering(db, reverse.id, reverse_update_payload)

    logger.info(
        f"Reverse engineering task COPYBOOK completed for {repo_id} - - Time: {str(time.time() - t0)}"
    )


async def reverse_jcl(ctx, *, blob_path: str, parsed_data: str):
    t0 = time.time()
    logger.info(f"Reverse engineering content from {blob_path}")
    llm = get_llm()
    db = await get_database()

    reverse = await get_reverse_engineering_by_path(db, blob_path)
    if reverse is None:
        logger.error(f"Reverse engineering task not found for {blob_path}")

    parsed_data_dict = ast.literal_eval(parsed_data)

    try:
        job_statement = parsed_data_dict["job_statement_list"][0]["content"]

        patterns = {
            "class": re.compile(r"CLASS=([A-Z])"),
            "msgclass": re.compile(r"MSGCLASS=([A-Z])"),
            "notify": re.compile(r"NOTIFY=(&SYSUID)"),
            "time": re.compile(r"TIME=([0-9]+)"),
        }

        # Extract values
        extracted_values = {}
        for key, pattern in patterns.items():
            match = pattern.search(job_statement)
            extracted_values[key] = match.group(1) if match else None

        overview = {
            "job_name": reverse.name,
            "class": extracted_values["class"],
            "msgclass": extracted_values["msgclass"],
            "notify": extracted_values["notify"],
            "time": extracted_values["time"],
        }
    except Exception as e:
        logger.error(f"Reverse JCL with no job statement {reverse.name} - {e}")
        overview = {
            "job_name": reverse.name,
            "class": None,
            "msgclass": None,
            "notify": None,
            "time": None,
        }

    exec_statement_map = parsed_data_dict["exec_statement_map"]
    steps = []
    for step_name, exec_statement in exec_statement_map.items():
        program_executed = exec_statement["parameters_map"].get("PGM")
        description = IBM_MAINFRAME_UTILITIES.get(program_executed)

        # dd_statements = []
        io_statements = []
        for statement in exec_statement["statements"]:
            # dd_statement = f"{statement['ddname']} DD "
            # for param, value in statement["parameters_map"].items():
            #     dd_statement += f"{param}={value},"
            # dd_statements.append(dd_statement)

            for ds in statement["dataset_map_list"]:
                io_statements.append(f"{statement['ddname']}: {ds['dd_statement']}\n")
        if len(io_statements) > 0:
            messages = [
                SystemMessage(
                    content="Act as a COBOL expert. Your task to is summarize to give best property of JCL IBM. Output should be short and clear in one line."
                ),
                HumanMessage(
                    content=f"Step name: {step_name}\nProgram executed: {program_executed}\nDescription of program: {description}\nDD Statement: {exec_statement['statements']}\nInput and output files: {io_statements}\n"
                ),
            ]
            # TODO: queue for each jcl file because of using llm
            property = llm.invoke(messages).content
        else:
            property = None

        steps.append(
            {
                "step_name": step_name,
                "program_executed": program_executed,
                "description": description,
                "dd_statement": exec_statement["statements"],
                "io_statements": io_statements,
                "property": property,
            }
        )

    messages = [
        SystemMessage(
            content="Act as a COBOL expert. Your task to is summarize to give best property of JCL IBM. Output should be short and clear in one line."
        ),
        HumanMessage(
            content=f"Overview of JCL IBM job: {str(overview)}\nSteps: {str(steps)}\n"
        ),
    ]
    overview["description"] = llm.invoke(messages).content

    reverse_update_payload = ReverseEngineeringUpdate(
        status="done", output={"overview": overview, "step_list": steps}, type="JCL_IBM"
    )

    await update_reverse_engineering(db, reverse.id, reverse_update_payload)
    logger.info(
        f"Reverse engineering task JCL completed for {blob_path} - Time: {str(time.time() - t0)}"
    )
