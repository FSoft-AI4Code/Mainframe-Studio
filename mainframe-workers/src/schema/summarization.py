from datetime import datetime
from typing import Dict, Literal
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from schema.core_schema import PyObjectId


class MigrationAPI(BaseModel):
    method: Optional[Literal['GET', 'POST', 'PUT', 'DELETE']] = Field(None, description="HTTP Methods")
    path: Optional[str]
    actions: Optional[str]


class MigrationModel(BaseModel):
    linked_cobol: Optional[str]
    copybooks: Optional[List[str]]
    description: Optional[str] = Field(None, description="Brief purpose of the model")
    apis: Optional[List[MigrationAPI]]


class Summarization(BaseModel):
    id: PyObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str = Field(..., alias="name")
    repository_id: Optional[str] = Field(None, description="Repository or project ID")
    status: Optional[Literal['running', 'done']] = Field(None, description="Processing status")
    path: Optional[str] = Field(None, description="File path to the BMS screen")
    short_description: Optional[str] = Field(None, description="Brief purpose of the screen")
    parameters: Optional[Dict[str, str]] = Field(default_factory=dict)
    linked_cobol: Optional[List[str]] = Field(default_factory=list)
    actions: Optional[List[str]] = Field(default_factory=list)
    copybook_groups: Optional[Dict[str, MigrationModel]] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }



class SummarizationLLM(BaseModel):
    short_description: Optional[str]
    parameters: Optional[Dict[str, str]]
    linked_cobol: Optional[List[str]]
    actions: Optional[List[str]]
    copybook_groups: Optional[Dict[str, MigrationModel]]


class ScreenTransition(BaseModel):
    event: str  # e.g., "PF6 pressed", "TX-PROGRAM-STATUS=1"
    to_screen: str
    condition: Optional[str]  # Optional extra condition


class ScreenNode(BaseModel):
    screen_id: str  # Unique ID for screen node, e.g., "ADS557A"
    title: Optional[str]  # Human-readable label
    description: Optional[str]
    type: str  # e.g., "form", "detail", "list", "summary"
    entry_conditions: List[str]  # e.g., ["TX-PROGRAM-STATUS=0"]
    transitions: List[ScreenTransition]


class LogicFlow(BaseModel):
    status: str  # E.g., TX-PROGRAM-STATUS
    condition: str
    actions: List[str]


class UserInputField(BaseModel):
    field_name: str
    type: str
    validations: List[str]
    mapped_variable: Optional[str]


class UserInteraction(BaseModel):
    fields: List[UserInputField]
    messages: List[str]


class SQLQuery(BaseModel):
    type: str  # SELECT, INSERT, etc.
    table: str
    description: str
    where_clause: Optional[str]


class DatabaseAccess(BaseModel):
    queries: List[SQLQuery]


class FieldMapping(BaseModel):
    ui_field: str
    cobol_variable: str
    usage_context: str  # where/when it's used


class UIToLogicMapping(BaseModel):
    mappings: List[FieldMapping]


class CobolLLMSummary(BaseModel):
    program_id: str
    trans_id: str
    screen_nodes: List[ScreenNode]  # For graph-based rendering
    logic_flow: List[LogicFlow]
    user_interaction: UserInteraction
    database_access: DatabaseAccess
    ui_to_logic_mapping: UIToLogicMapping
    copybook_groups: Optional[Dict[str, MigrationModel]]


class CobolLLMScreenSummary(BaseModel):
    id: str = Field(None, alias="_id")
    repository_id: Optional[str] = Field(None, description="Repository or project ID")
    status: Optional[Literal['running', 'done']] = Field(None, description="Processing status")
    path: Optional[str] = Field(None, description="File path to the COBOL program")
    program_id: Optional[str] = Field(None, description="COBOL PROGRAM-ID")
    trans_id: Optional[str] = Field(None, description="CICS transaction ID (TRANSID)")

    screen_nodes: List[ScreenNode] = Field(default_factory=list, description="Screens and transitions")
    logic_flow: List[LogicFlow] = Field(default_factory=list, description="Execution logic branches")
    user_interaction: Optional[UserInteraction] = Field(None, description="Input fields and messages")
    database_access: Optional[DatabaseAccess] = Field(None, description="SQL queries and access logic")
    ui_to_logic_mapping: Optional[UIToLogicMapping] = Field(None, description="UI ↔ COBOL data variable mappings")
    copybook_groups: Optional[Dict[str, MigrationModel]] = Field(default_factory=dict)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __init__(
            self,
            _id: str = None,
            repository_id: Optional[str] = None,
            status: Optional[Literal['running', 'done']] = None,
            path: Optional[str] = None,
            program_id: Optional[str] = None,
            trans_id: Optional[str] = None,
            screen_nodes: Optional[List[ScreenNode]] = None,
            logic_flow: Optional[List[LogicFlow]] = None,
            user_interaction: Optional[UserInteraction] = None,
            database_access: Optional[DatabaseAccess] = None,
            ui_to_logic_mapping: Optional[UIToLogicMapping] = None,
            copybook_groups: Optional[Dict[str, MigrationModel]] = None,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None,
    ):
        super().__init__(
            _id=_id,
            repository_id=repository_id,
            status=status,
            path=path,
            program_id=program_id,
            trans_id=trans_id,
            screen_nodes=screen_nodes or [],
            logic_flow=logic_flow or [],
            user_interaction=user_interaction,
            database_access=database_access,
            ui_to_logic_mapping=ui_to_logic_mapping,
            copybook_groups=copybook_groups,
            created_at=created_at or datetime.utcnow(),
            updated_at=updated_at or datetime.utcnow(),
        )

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }


class CopybookField(BaseModel):
    name: str
    type: str
    level: int
    description: Optional[str]
    occurs: Optional[int]
    redefines: Optional[str]
    usage: Optional[str]
    picture: Optional[str]


class CopybookGroup(BaseModel):
    name: str
    level: int
    description: Optional[str]
    fields: List[CopybookField]
    groups: List['CopybookGroup']


class CopybookSummary(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    repository_id: Optional[str] = Field(None, description="Repository or project ID")
    status: Optional[Literal['running', 'done']] = Field(None, description="Processing status")
    path: Optional[str] = Field(None, description="File path to the copybook")
    short_description: Optional[str] = Field(None, description="Brief purpose of the copybook")
    fields: List[CopybookField] = Field(default_factory=list)
    groups: List[CopybookGroup] = Field(default_factory=list)
    record_length: Optional[int] = Field(None, description="Total record length in bytes")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }
