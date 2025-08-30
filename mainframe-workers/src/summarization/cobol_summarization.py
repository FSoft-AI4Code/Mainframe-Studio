import textwrap
import uuid
from typing import Tuple

from loguru import logger
from pydantic import UUID4

from config.llm_client import get_llm
from schema.core_schema import PyObjectId
from schema.summarization import CobolLLMSummary, CobolLLMScreenSummary


def build_llm_prompt_for_cobol_analysis(cobol_source: str) -> str:
    """
    Generate a single prompt string for LLM to analyze COBOL program logic and screen flow.

    Args:
        cobol_source (str): Full content of the COBOL source code.

    Returns:
        str: Full prompt string to send to the LLM.
    """
    prompt = textwrap.dedent(f"""
        You are an expert in COBOL programming and legacy systems modernization.
        Analyze the given COBOL source code, identify screen flows (UI navigation),
        logic branches, data interactions (including DB2 or CICS calls),
        and user inputs/outputs.

        Your task is to summarize:
        1. Screen navigation flow (what screen shows up under what conditions).
        2. Execution logic per status (TX-PROGRAM-STATUS, PF Keys).
        3. User interaction flow (input, validation, display).
        4. Key database interactions (SQL and cursors).
        5. Mappings between UI fields and data variables.
        6. Based on COBOL logic (e.g., PERFORM sections, EIBAID, IF logic, CICS verbs like READ, REWRITE, DELETE), infer possible user or system operations.
        7. Group COPYBOOKs that together represent a single business entity (e.g., Customer, Order, Product).
        8. For each item in copybook_groups, suggest a Java-style model name (e.g., ModelName1, ModelName2), and explain what the model represents.
        9. For each model, suggest a list of REST API endpoints to be generated.
           - Each endpoint should include: HTTP method (GET, POST, PUT, DELETE), path, and purpose (e.g., "create new customer", "update order", "delete product", "inquire status").



        Output in markdown format with sections for:
        - Screen Flow
        - Logic Flow
        - User Input/Validation
        - Database Access
        - UI ↔ Logic Mapping
        - copybook_groups:
              ModelName1: <You have to define the Java-style model name base on the entity>
                copybooks: [COPY1, COPY2]
                description: <explanation>
                apis:
                  - method: GET
                    path: /modelname1/
                    action: inquiry
                  - method: POST
                    path: /modelname1
                    action: create
              ModelName2:
              ...

        Here is the COBOL source code for analysis:

        ```cobol
        {cobol_source}
        ```
    """)

    return prompt


async def process_summary_cobol_file(
        path: str,
        repository_id: str,
        content: str,
        structured_llm
) -> Tuple[str, CobolLLMScreenSummary]:
    try:
        prompt = build_llm_prompt_for_cobol_analysis(cobol_source=content)
        output = await structured_llm.ainvoke(prompt)

        logger.info(f'================= COBOL Summarization ===================')
        logger.debug(output)

        return path, CobolLLMScreenSummary(
            _id=uuid.uuid4().hex,
            repository_id=repository_id,
            status="done",
            path=path,
            program_id=output.program_id,
            trans_id=output.trans_id,
            screen_nodes=output.screen_nodes,
            logic_flow=output.logic_flow,
            user_interaction=output.user_interaction,
            database_access=output.database_access,
            ui_to_logic_mapping=output.ui_to_logic_mapping,
            copybook_groups=output.copybook_groups,
        )

    except Exception as e:
        logger.error(f"Error processing BMS screen at {path}: {e}")
        return path, CobolLLMScreenSummary(
            repository_id=repository_id,
            status="done",
            path=path,
            program_id="",
            trans_id="",
            screen_nodes=[],
            logic_flow=[],
            user_interaction=None,
            database_access=None,
            ui_to_logic_mapping=None,
            copybook_groups=None,
        )


@logger.catch
async def cobol_screen_summary(path: str, repository_id: str, content: str) -> CobolLLMScreenSummary:
    """
    Process a single COBOL screen map asynchronously and return a structured MongoDB-compatible document.
    """
    try:
        llm = get_llm(model_type="assistant")
        structured_llm = llm.with_structured_output(CobolLLMSummary)
        _, result = await process_summary_cobol_file(path, repository_id, content, structured_llm)
        logger.info(f'cobol_screen_summary: {result}')
        return result

    except Exception as e:
        logger.error(f"Error summarizing COBOL screen: {e}")
        return CobolLLMScreenSummary(
            repository_id=repository_id,
            status="done",
            path=path,
            program_id="",
            trans_id="",
            screen_nodes=[],
            logic_flow=[],
            user_interaction=None,
            database_access=None,
            ui_to_logic_mapping=None,
            copybook_groups=None,
        )
