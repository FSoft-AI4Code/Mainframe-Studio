from typing import Dict, Any, List, Tuple
from pydantic import BaseModel, Field
from loguru import logger
from config.llm_client import get_llm
import concurrent.futures


INSTRUCTION = """Analyze the provided code snippet and generate a structured JSON output that represents its logic and functionality.

Focus on:
- Summarizing the overall purpose and key actions performed in the code.
- Highlighting important conditions, their outcomes, and any significant operations.
- Avoiding excessive details or line-by-line explanations; instead, group related actions logically, prioritize the actions that actually change state or have external effects.
- Combine related actions into a single concise statement where possible. For IF-ELSE conditions, omit branches with no significant action (e.g., CONTINUE) and focus only on the branch that performs meaningful actions.
- For example:
    "- When seeing this code:\n"
    "    IF CONDITION-A\n"
    "        CONTINUE\n"
    "    ELSE\n"
    "        MOVE 'VALUE' TO FIELD-B\n"
    "        PERFORM PROCESS-C\n"
    "    END-IF.\n"
    "  The summary should be: 'Moves VALUE to FIELD-B and calls the [process C]<PROCESS-C> when CONDITION-A is false.'\n"

- Ensuring the summary is concise, clear.

Code snippet:
{CODE}
"""

class RefParagraph(BaseModel):
    """
    Represents a referenced paragraph with its name and description.
    The description matches the text within [] in the paragraph summary.
    """
    ref_name: str = Field(
        ...,
        description="The unique identifier or name of the referenced paragraph (e.g., '1100-SCREEN-INIT')."
    )
    description: str = Field(
        ...,
        description=(
            "A brief description of the referenced paragraph's purpose or functionality. "
            "This description matches the text within [] in the paragraph summary. "
            "For example, for [screen initialization process]<1100-SCREEN-INIT>, the description would be 'screen initialization process'."
        )
    )
class ParagraphOutput(BaseModel):
    """
    Represents the structured output of a paragraph, including its metadata and detailed descriptions.
    """
    paragraph_name: str = Field(
        ...,
        description="The unique name or identifier of the paragraph (e.g., '1000-SEND-MAP')."
    )
    paragraph_type: str = Field(
        ...,
        description=(
            "The type or category of the paragraph, indicating its primary function "
            "(e.g., 'send map', 'read data')."
        )
    )
    section: str = Field(
        ...,
        description=(
            "The section within the codebase where the paragraph is defined "
            "(e.g., 'procedure division')."
        )
    )
    details: List[RefParagraph] = Field(
        default_factory=list,
        description=(
            "A list of referenced paragraphs that are invoked or utilized within this paragraph. "
            "Each referenced paragraph includes its name and a description that exactly matches the text within [] in the paragraph summary. "
            "This list can be empty if there are no references."
        )
    )
    paragraph_summary: List[str] = Field(
        ...,
        description=(
        "A list of strings, where each string provides a concise summary of the functionality and purpose of the code snippet. "
        "Each element should group related actions or conditions into a single logical explanation where possible, avoiding detailed explanations of each line. "
        "Focus only on the key outcomes or actions that change program state or have external effects. Avoid explaining trivial operations or branches that do not change the program state "
        "For IF-ELSE blocks where one branch has no significant action (like CONTINUE), only describe the meaningful branch. "
        "For example:\n"
        "- When seeing this code:\n"
        "    IF CONDITION-A\n"
        "        CONTINUE\n"
        "    ELSE\n"
        "        MOVE 'VALUE' TO FIELD-B\n"
        "        PERFORM PROCESS-C\n"
        "    END-IF.\n"
        "  The summary should be: 'Moves VALUE to FIELD-B and calls the [process C]<PROCESS-C> when CONDITION-A is false.'\n"
        "Always use simple, direct language focusing on what the code actually accomplishes."
        "Each referenced process or function should be enclosed within [] and linked to its reference name using <>."
        "For example:\n"
        "- 'Calls the [initialization process]<INIT-FUNCTION> to set up the environment.'\n"
        "- 'Executes the [error handling routine]<ERROR-HANDLER> to manage unexpected conditions.'"
        )
    )

def process_paragraph(paragraph: Dict[str, Any], structured_llm) -> Tuple[str, Dict[str, Any]]:
    try:
        paragraph_name = paragraph["paragraph_name"]
        paragraph_code = paragraph["paragraph_code"]
        prompt = INSTRUCTION.format(CODE=paragraph_code)
        output = structured_llm.invoke(prompt)
        return paragraph_name, {
            "paragraph_name": paragraph_name,
            "section": paragraph.get("section"),
            "paragraph_code": paragraph_code,
            "paragraph_lines": paragraph["paragraph_lines"],
            "paragraph_logic": output.paragraph_summary,
        }
    except Exception as e:
        logger.error(f"Error processing paragraph {paragraph_name}: {e}")
        return paragraph_name, None

@logger.catch
def cobol_summary(paragraph_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    try:
        llm = get_llm(model_type="assistant")
        structured_llm = llm.with_structured_output(ParagraphOutput)
        results = {}

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = {
                executor.submit(process_paragraph, paragraph, structured_llm): paragraph
                for paragraph in paragraph_list
            }
            
            for future in concurrent.futures.as_completed(futures):
                paragraph_name, result = future.result()
                if result:
                    results[paragraph_name] = result

        return results

    except Exception as e:
        logger.error(f"Error processing COBOL file: {str(e)}")
        return {
            "status": "error",
            "message": f"Error processing COBOL file: {str(e)}"
        }
