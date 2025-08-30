from typing import Dict, Any, Tuple, List
from loguru import logger
from config.llm_client import get_llm
from schema.summarization import Summarization, SummarizationLLM

INSTRUCTION = """You are a COBOL BMS and CICS expert.

You will be given the full content of a BMS screen map (and optionally COBOL logic and COPYBOOK content). Your task is to analyze the actual content and extract real information, avoiding placeholder or example data.

Your output should include:

1. short_description: A concise explanation of what the screen is used for, based **only on field names, labels, and layout**.
2. parameters: A dictionary where each key is a real field name from the map, and the value includes:
   - type: input/output
   - length
   - any validation or formatting rules
3. linked_cobol: List the actual COBOL program names that call or are called by this screen (from PERFORMs, LINK, XCTL, RETURN, etc.).
4. actions: List real user actions supported on this screen, like PF keys, buttons, line commands, or any UI-based trigger. Do not invent.
5. operations: Based on the actual COBOL logic (EIBAID, IF, PERFORM, CICS READ/WRITE/DELETE), infer what the user or system can do.
6. copybook_groups: Group COPYBOOKs that are used together to represent a business entity (e.g., Customer, Account). 
   - Use real COPYBOOK names
   - Suggest a Java-style model name
   - Describe what the group represents based on COPYBOOK content
   - Link actual COBOL programs that use those COPYBOOKs
   - For each group, suggest real REST API endpoints:
     - method
     - path
     - purpose (e.g., create, read, update, delete)

IMPORTANT:
- Only use field names, COPYBOOKs, and program names that appear in the provided BMS and COBOL content.
- Do not use placeholders like PROGRAM1, COPY1, Model1, etc.
- Do not hallucinate or invent data.
- Output must be plain structured text. No Markdown or formatting.

Input:
BMS Code
{BMS_CODE}
COBOL Code
{COBOL_CODE}
"""


async def process_bms_screen(file_name: str, path: str, repository_id: str, bms_content: str, cobol_content: str,
                             structured_llm: SummarizationLLM) -> Tuple[str, Summarization]:
    try:
        prompt = INSTRUCTION.format(BMS_CODE=bms_content, COBOL_CODE=cobol_content)
        output = await structured_llm.ainvoke(prompt)
        logger.info(f'================= BMS Summarization ===================')
        logger.debug(output)
        return path, Summarization(
            name=file_name,
            repository_id=repository_id,
            status="done",
            path=path,
            short_description=output.short_description,
            parameters=output.parameters,
            linked_cobol=output.linked_cobol,
            actions=output.actions,
            copybook_groups=output.copybook_groups
        )


    except Exception as e:
        logger.error(f"Error processing BMS screen at {path}: {e}")
        return path, Summarization(
            name=file_name,
            repository_id=repository_id,
            status="done",
            path=path,
            short_description="Error during summarization",
            parameters={},
            linked_cobol=[],
            actions=[],
            copybook_groups={}
        )


@logger.catch
async def bms_summary(file_name: str, path: str, repository_id: str, bms_content: str,
                      cobol_content: str) -> Summarization:
    """
    Process a single BMS screen map asynchronously and store the summarization to MongoDB.
    """
    try:
        llm = get_llm(model_type="assistant")
        structured_llm = llm.with_structured_output(SummarizationLLM)
        _, result = await process_bms_screen(file_name, path, repository_id, bms_content, cobol_content, structured_llm)
        return result

    except Exception as e:
        logger.error(f"Error summarizing BMS screen: {e}")
        return Summarization(
            name=file_name,
            repository_id=repository_id,
            status="done",
            path=path,
            short_description="Error during summarization",
            parameters={},
            linked_cobol=[],
            actions=[],
            copybook_groups={}
        )


JAVA_PROMPT = """
You are an expert in COBOL BMS and Java. Given a BMS screen definition, generate the following:

1. A Java `Model` class with fields representing input/output screen fields.
   - Map each field to a reasonable Java type (`String`, `int`, `LocalDate`, etc.).
   - Use proper Java naming conventions (camelCase).
   - Add comments for length and any validation.
   - Add `@JsonProperty` annotations for JSON serialization/deserialization.
   - Add `@Data` or `@Getter/@Setter` annotations for getters/setters.
   - Add validation function for each field if exist.

2. A Java `Controller` class with a stub method to handle screen interactions.
   - Include an endpoint with `@PostMapping` or `@GetMapping`.
   - Use the model class as input/output (DTO).
   - Assume it's part of a Spring Boot app.

Format your response with:
---MODEL---
<Java model class here>
---CONTROLLER---
<Java controller class here>

{CODE}
"""


async def generate_java_from_bms(name: str, content: str) -> dict:
    try:
        llm = get_llm(model_type="assistant")
        structured_llm = llm.with_text_output()

        prompt = JAVA_PROMPT.format(CODE=content)
        response = await structured_llm.ainvoke(prompt)
        response = response.strip()

        model_code = ""
        controller_code = ""

        if "---MODEL---" in response and "---CONTROLLER---" in response:
            parts = response.split("---CONTROLLER---")
            model_code = parts[0].replace("---MODEL---", "").strip()
            controller_code = parts[1].strip()
        else:
            raise ValueError("Invalid response format from LLM")

        return {
            "status": "success",
            "model": model_code,
            "controller": controller_code,
            "raw": response
        }

    except Exception as e:
        logger.error("Failed to generate Java code from BMS", error=str(e))
        return {
            "status": "error",
            "message": str(e)
        }
