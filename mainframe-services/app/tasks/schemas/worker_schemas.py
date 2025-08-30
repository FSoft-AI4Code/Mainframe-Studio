from pydantic import BaseModel, Field
from typing import List

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
            "A list of strings, where each string provides a part of the comprehensive summary detailing the "
            "functionality and purpose of the paragraph. Each element can describe a specific action, process, "
            "or behavior within the paragraph's scope. "
            "Each referenced process is enclosed within [] and linked to its reference name using <>. "
            "For example:\n"
            "- 'Calls the [screen initialization process]<1100-SCREEN-INIT> to clear and prepare the screen for new data.'\n"
            "- 'Calls the [array initialization process]<1200-SCREEN-ARRAY-INIT> to initialize the array fields to be displayed on the screen.'"
        )
    )

    class Config:
        json_schema_extra = {
            "example": {
                "paragraph_name": "1000-SEND-MAP",
                "paragraph_type": "send map",
                "section": "procedure division",
                "details": [
                    {
                        "ref_name": "1100-SCREEN-INIT",
                        "description": "screen initialization process"
                    },
                    {
                        "ref_name": "1200-SCREEN-ARRAY-INIT",
                        "description": "array initialization process"
                    },
                    {
                        "ref_name": "1250-SETUP-ARRAY-ATTRIBS",
                        "description": "array attribute setup process"
                    },
                    {
                        "ref_name": "1300-SETUP-SCREEN-ATTRS",
                        "description": "screen attribute setup process"
                    },
                    {
                        "ref_name": "1400-SETUP-MESSAGE",
                        "description": "message setup process"
                    },
                    {
                        "ref_name": "1500-SEND-SCREEN",
                        "description": "screen sending process"
                    }
                ],
                "paragraph_summary": [
                    "Calls the [screen initialization process]<1100-SCREEN-INIT> to clear and prepare the screen for new data.",
                    "Calls the [array initialization process]<1200-SCREEN-ARRAY-INIT> to initialize the array fields to be displayed on the screen.",
                    "Calls the [array attribute setup process]<1250-SETUP-ARRAY-ATTRIBS> to set up attributes for each array element, like whether the field is protected or not.",
                    "Calls the [screen attribute setup process]<1300-SETUP-SCREEN-ATTRS> to prepare screen attributes, such as positioning and field length.",
                    "Calls the [message setup process]<1400-SETUP-MESSAGE> to check if any error messages need to be displayed and set them up accordingly.",
                    "Calls the [screen sending process]<1500-SEND-SCREEN> to send the screen map to the user, showing the updated data."
                ],
            },
            "example_without_refs": {
                "paragraph_name": "9000-READ-FORWARD",
                "paragraph_type": "read data",
                "section": "procedure division",
                "paragraph_summary": [
                    "Starts browsing through the dataset of cards, beginning with the card number provided.",
                    "Loops through the card data, fetching a screenful of records (up to 7).",
                    "For each record, checks if it should be included or excluded based on the account and card filter settings.",
                    "Populates the screen with the card number, account ID, and card status for each valid record.",
                    "Checks if more records exist to continue the browse. If the maximum screen size is reached, stops fetching records."
                ],
                "details": []
            }
        }