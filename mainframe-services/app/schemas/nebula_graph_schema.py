import uuid
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from bson import ObjectId
from loguru import logger
from pydantic import BaseModel, Field

from app.constants.cobol import FileType
from app.constants.graph import NEBULA_INDEX_NAME_POSTFIX, RelationshipLabel
from app.schemas.common_schema import PyObjectId


class BaseNode(BaseModel, ABC):
    """Represents a node with a unique ID, name, and group associations."""

    id: PyObjectId = Field(
        default_factory=PyObjectId,
        alias="_id",
        description="Unique identifier for the node",
    )
    name: str = Field(..., description="Name of the node")
    group: List[str] = Field(
        default_factory=list, description="List of groups the node belongs to"
    )
    status: str = Field(
        ..., description="Status of the node, can be ALIVE, MISSING, DEAD"
    )

    @staticmethod
    @abstractmethod
    def properties() -> Dict[str, str]:
        """Define vertex-specific properties with Nebula data types."""
        return {"id": "string", "name": "string", "group": "string", "status": "string"}

    @classmethod
    @abstractmethod
    def node_description(cls) -> str:
        """Define the description for chatbot to understand the node"""

    @classmethod
    @abstractmethod
    def tag(cls) -> FileType:
        """Returns the Nebula Graph tag name associated with this class."""

    @classmethod
    def create_vertex_statement(cls) -> str:
        """Generate a CREATE TAG statement with comments for each property using class methods."""
        vertex_name = cls.tag().value
        properties_with_comments = []

        # Retrieve properties and descriptions from the class
        for name, field in cls.model_fields.items():
            nebula_type = cls.properties().get(
                name, "string"
            )  # Default to 'string' if not found in properties
            description = field.description  # Directly access description from Field
            comment = f"COMMENT '{description}'" if description else ""
            properties_with_comments.append(f"{name} {nebula_type} {comment}")

        # Retrieve node description from the class
        properties_str = ",\n    ".join(properties_with_comments)
        node_description = cls.node_description()
        return f"CREATE TAG IF NOT EXISTS {vertex_name} (\n    {properties_str}\n) COMMENT = '{node_description}';"

    @classmethod
    def create_tag_index_statement(cls) -> str:
        """Generate a CREATE TAG INDEX statement"""
        vertex_name = cls.tag().value
        index_name = f"{vertex_name}{NEBULA_INDEX_NAME_POSTFIX}"
        return f"CREATE TAG INDEX IF NOT EXISTS {index_name} ON {vertex_name}();"

    @classmethod
    def rebuild_index_statement(cls) -> str:
        """Generate a REBUILD TAG INDEX statement"""
        vertex_name = cls.tag().value
        index_name = f"{vertex_name}{NEBULA_INDEX_NAME_POSTFIX}"
        return f"REBUILD TAG INDEX {index_name};"

    def insert_vertex_statement(self) -> str:
        """Generate INSERT VERTEX statement using instance values."""
        vertex_name = self.tag().value
        properties = self.properties()
        property_keys = [name for name in properties.keys() if name != "id"]

        # Construct values string using instance attributes
        values_str = ", ".join(
            [
                (
                    f'"{getattr(self, name)}"'
                    if nebula_type == "string"
                    else str(getattr(self, name))
                )
                for name, nebula_type in properties.items()
                if name != "id"  # Skip the 'id' property
            ]
        )
        return f'INSERT VERTEX {vertex_name}({", ".join(property_keys)}) VALUES "{self.id}":({values_str});'

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, BaseNode):
            return self.id == other.id
        return False

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True


class CobolNode(BaseNode):
    @staticmethod
    def properties():
        return super(CobolNode, CobolNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the COBOL program in the mainframe repository."

    @classmethod
    def tag(cls) -> FileType:
        return FileType.COBOL


class CopyNode(BaseNode):
    @staticmethod
    def properties():
        return super(CopyNode, CopyNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the copybook in the mainframe repository."

    @classmethod
    def tag(cls) -> FileType:
        return FileType.COPY


class BmsNode(BaseNode):
    @staticmethod
    def properties():
        return super(BmsNode, BmsNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the BMS (Basic Mapping Support) file in the mainframe repository."

    @classmethod
    def tag(cls) -> FileType:
        return FileType.BMS


class JclIbmNode(BaseNode):
    @staticmethod
    def properties():
        return super(JclIbmNode, JclIbmNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the JCL (Job Control Language) file in the mainframe repository used in IBM mainframe operating system."

    @classmethod
    def tag(cls) -> FileType:
        return FileType.JCL_IBM


class OtherNode(BaseNode):
    @staticmethod
    def properties():
        return super(OtherNode, OtherNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the other files in the repository."

    @classmethod
    def tag(cls) -> FileType:
        return FileType.OTHER


class BaseEdge(BaseModel, ABC):
    """Represents an edge with source and target vertices."""

    source: PyObjectId = Field(..., description="Source vertex ID")
    target: PyObjectId = Field(..., description="Target vertex ID")
    rank: Optional[int] = Field(default=0, description="Rank of the edge")

    @staticmethod
    @abstractmethod
    def properties() -> Dict[str, str]:
        """Define edge-specific properties with Nebula data types."""
        return {"source": "string", "target": "string"}

    @classmethod
    @abstractmethod
    def edge_description(cls) -> str:
        """Define the description for chatbot to understand the relationships of different types of nodes."""

    @classmethod
    @abstractmethod
    def tag(cls) -> RelationshipLabel:
        """Returns the Nebula Graph edge type associated with this class."""

    @classmethod
    def create_edge_statement(cls) -> str:
        """Generate a CREATE EDGE statement with comments for each property using class methods."""
        edge_name = cls.tag().value
        properties_with_comments = []

        # Retrieve properties and descriptions from model_fields
        properties = cls.properties()  # Call properties as a static method
        for name, field in cls.model_fields.items():
            nebula_type = properties.get(
                name, "string"
            )  # Default to 'string' if not found in properties
            description = field.description
            if not description:
                raise ValueError(
                    f"Description for field '{name}' is missing. Please add a description for LLM to understand the schema."
                )
            comment = f"COMMENT '{description}'"
            properties_with_comments.append(f"{name} {nebula_type} {comment}")

        # Retrieve edge description from the class
        properties_str = ",\n    ".join(properties_with_comments)
        edge_description = cls.edge_description()
        return f"CREATE EDGE IF NOT EXISTS {edge_name} (\n    {properties_str}\n) COMMENT = '{edge_description}';"

    @classmethod
    def create_edge_index_statement(cls) -> str:
        """Generate a CREATE EDGE INDEX statement"""
        edge_name = cls.tag().value
        index_name = f"{edge_name}{NEBULA_INDEX_NAME_POSTFIX}"
        return f"CREATE EDGE INDEX IF NOT EXISTS {index_name} ON {edge_name}();"

    @classmethod
    def rebuild_index_statement(cls) -> str:
        """Generate a REBUILD EDGE INDEX statement"""
        edge_name = cls.tag().value
        index_name = f"{edge_name}{NEBULA_INDEX_NAME_POSTFIX}"
        return f"REBUILD EDGE INDEX {index_name};"

    def insert_edge_statement(self) -> str:
        """Generate an INSERT EDGE statement using instance values."""
        edge_name = self.tag().value
        properties = self.properties()

        ignore_props = ["id", "source", "target", "rank"]
        property_keys = [name for name in properties.keys() if name not in ignore_props]

        # Construct values string using instance attributes
        values = []

        for name, nebula_type in properties.items():
            if name in ignore_props:
                continue

            if nebula_type == "string":
                value = getattr(self, name)
                if value is None:
                    values.append("null")
                else:
                    values.append(f"'{value}'")
            else:
                values.append(str(getattr(self, name)))

        values_str = ", ".join(values)
        return f'INSERT EDGE {edge_name}({", ".join(property_keys)}) VALUES "{self.source}" -> "{self.target}"@{self.rank}:({values_str});'

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        from_attributes = True


class ExecPgm(BaseEdge):
    step_name: str = Field(
        ..., description="The step name which passes dataset to the COBOL program"
    )
    dataset_name: Optional[str] = Field(
        ...,
        description="The name of the dataset used as input for the COBOL program, can be null",
    )

    @classmethod
    def edge_description(cls):
        return "Represents relationship between JCL_IBM and COBOL, the JCL_IBM executes the COBOL file with a dataset. If a program is executed with many datasets, it will have multiple edges. The number of steps in a JCL is equal to the number of unique step names."

    @staticmethod
    def properties() -> Dict[str, str]:
        base_properties = super(ExecPgm, ExecPgm).properties()
        base_properties.update({"step_name": "string", "dataset_name": "string"})
        return base_properties

    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.EXEC_PGM


class StaticCall(BaseEdge):
    procedure: str = Field(
        ..., description="Name of the procedure which contains the Call statement"
    )

    param: Optional[str] = Field(
        ...,
        description="The parameter used for calling the program, can be null",
    )

    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.STATIC_CALL

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between COBOL and COBOL, the program statically calls other program with a param. If a program is called with many params, it will have multiple edges."

    @staticmethod
    def properties():
        base_properties = super(StaticCall, StaticCall).properties()
        base_properties.update({"procedure": "string", "param": "string"})
        return base_properties


class DynamicCall(BaseEdge):
    procedure: str = Field(
        ..., description="Name of the procedure which contains the Call statement"
    )

    param: Optional[str] = Field(
        ..., description="The parameter used for calling the program, can be null."
    )

    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.DYNAMIC_CALL

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between COBOL and COBOL, the program dynamically calls other program with a param. If a program is called with many params, it will have multiple edges."

    @staticmethod
    def properties():
        base_properties = super(DynamicCall, DynamicCall).properties()
        base_properties.update({"procedure": "string", "param": "string"})

        return base_properties


class HasCopybook(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.HAS_COPYBOOK

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between COBOL and COPY or COPY and COPY, the program uses a copybook or a copybook uses another copybook"

    @staticmethod
    def properties():
        base_properties = super(HasCopybook, HasCopybook).properties()

        return base_properties


class HasInteract(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.HAS_INTERACT

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between BMS and COBOL, the BMS files interact with the COBOL program"

    @staticmethod
    def properties():
        return super(HasInteract, HasInteract).properties()


class UtilityNode(BaseNode):
    @staticmethod
    def properties():
        return super(UtilityNode, UtilityNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the utility files in the mainframe repository."

    @classmethod
    def tag(cls) -> FileType:
        return FileType.UTILITY


class ParagraphNode(BaseModel):
    id: PyObjectId

    name: str = Field(description="Name of the paragraph")

    @staticmethod
    def properties() -> Dict[str, str]:
        """Define vertex-specific properties with Nebula data types."""
        return {"name": "string"}

    @classmethod
    def node_description(cls):
        return "Represents the paragraph in COBOL program"

    @classmethod
    def tag(cls) -> str:
        return "PARAGRAPH"

    @classmethod
    def create_vertex_statement(cls) -> str:
        """Generate a CREATE TAG statement with comments for each property using class methods."""
        properties_with_comments = []

        # Retrieve properties and descriptions from the class
        for name, field in cls.model_fields.items():
            nebula_type = cls.properties().get(
                name, "string"
            )  # Default to 'string' if not found in properties
            description = field.description  # Directly access description from Field
            comment = f"COMMENT '{description}'" if description else ""
            properties_with_comments.append(f"{name} {nebula_type} {comment}")

        # Retrieve node description from the class
        properties_str = ",\n    ".join(properties_with_comments)
        node_description = cls.node_description()
        return f"CREATE TAG IF NOT EXISTS {cls.tag()} (\n    {properties_str}\n) COMMENT = '{node_description}';"

    @classmethod
    def create_tag_index_statement(cls) -> str:
        """Generate a CREATE TAG INDEX statement"""
        return f"CREATE TAG INDEX IF NOT EXISTS {cls.tag()}_INDEX ON {cls.tag()}();"

    @classmethod
    def rebuild_index_statement(cls) -> str:
        """Generate a REBUILD TAG INDEX statement"""
        return "REBUILD TAG INDEX PARAGRAPH_INDEX;"

    def insert_vertex_statement(self) -> str:
        """Generate INSERT VERTEX statement using instance values."""
        vertex_name = self.tag()
        properties = self.properties()
        property_keys = [name for name in properties.keys() if name != "id"]

        # Construct values string using instance attributes
        values_str = ", ".join(
            [
                (
                    f'"{getattr(self, name)}"'
                    if nebula_type == "string"
                    else str(getattr(self, name))
                )
                for name, nebula_type in properties.items()
                if name != "id"  # Skip the 'id' property
            ]
        )
        return f'INSERT VERTEX {vertex_name}({", ".join(property_keys)}) VALUES "{self.id}":({values_str});'


class IdentifierNode(BaseModel):
    id: PyObjectId

    name: str = Field(description="Name of the COBOL identifier")

    level: str = Field(description="Level of the COBOL identifier")

    picture: Optional[str] = Field(description="Picture clause of the identifier")

    default_value: Optional[str] = Field(description="Default value of the identifier")

    @staticmethod
    def properties() -> Dict[str, str]:
        """Define vertex-specific properties with Nebula data types."""
        return {
            "name": "string",
            "level": "string",
            "picture": "string",
            "default_value": "string",
        }

    @classmethod
    def node_description(cls):
        return "Represents the identifier in COBOL program"

    @classmethod
    def tag(cls) -> str:
        return "IDENTIFIER"

    @classmethod
    def create_vertex_statement(cls) -> str:
        """Generate a CREATE TAG statement with comments for each property using class methods."""
        properties_with_comments = []

        # Retrieve properties and descriptions from the class
        for name, field in cls.model_fields.items():
            nebula_type = cls.properties().get(
                name, "string"
            )  # Default to 'string' if not found in properties
            description = field.description  # Directly access description from Field
            comment = f"COMMENT '{description}'" if description else ""
            properties_with_comments.append(f"{name} {nebula_type} {comment}")

        # Retrieve node description from the class
        properties_str = ",\n    ".join(properties_with_comments)
        node_description = cls.node_description()
        return f"CREATE TAG IF NOT EXISTS {cls.tag()} (\n    {properties_str}\n) COMMENT = '{node_description}';"

    @classmethod
    def create_tag_index_statement(cls) -> str:
        """Generate a CREATE TAG INDEX statement"""
        return f"CREATE TAG INDEX IF NOT EXISTS {cls.tag()}_INDEX ON {cls.tag()}();"

    @classmethod
    def rebuild_index_statement(cls) -> str:
        """Generate a REBUILD TAG INDEX statement"""
        return f"REBUILD TAG INDEX {cls.tag()}_INDEX;"

    def insert_vertex_statement(self) -> str:
        """Generate INSERT VERTEX statement using instance values."""
        vertex_name = self.tag()
        properties = self.properties()
        property_keys = [name for name in properties.keys() if name != "id"]

        # Construct values string using instance attributes
        values = []

        for name, nebula_type in properties.items():
            if name == "id":
                continue

            value = str(getattr(self, name))
            if nebula_type == "string":
                escaped_value = value.replace('"', r"\"").replace("\n", " ")
                escaped_value = f'"{escaped_value}"'
                values.append(escaped_value)
            else:
                values.append(value)

        values_str = ", ".join(values)

        return f'INSERT VERTEX {vertex_name}({", ".join(property_keys)}) VALUES "{self.id}":({values_str});'


class LiteralNode(BaseModel):
    id: PyObjectId

    name: str = Field(description="The name of the literal")

    @staticmethod
    def properties() -> Dict[str, str]:
        """Define vertex-specific properties with Nebula data types."""
        return {"name": "string"}

    @classmethod
    def node_description(cls):
        return "Represents the literal in COBOL program"

    @classmethod
    def tag(cls) -> str:
        return "LITERAL"

    @classmethod
    def create_vertex_statement(cls) -> str:
        """Generate a CREATE TAG statement with comments for each property using class methods."""
        properties_with_comments = []

        # Retrieve properties and descriptions from the class
        for name, field in cls.model_fields.items():
            nebula_type = cls.properties().get(
                name, "string"
            )  # Default to 'string' if not found in properties
            description = field.description  # Directly access description from Field
            comment = f"COMMENT '{description}'" if description else ""
            properties_with_comments.append(f"{name} {nebula_type} {comment}")

        # Retrieve node description from the class
        properties_str = ",\n    ".join(properties_with_comments)
        node_description = cls.node_description()
        return f"CREATE TAG IF NOT EXISTS {cls.tag()} (\n    {properties_str}\n) COMMENT = '{node_description}';"

    @classmethod
    def create_tag_index_statement(cls) -> str:
        """Generate a CREATE TAG INDEX statement"""
        return f"CREATE TAG INDEX IF NOT EXISTS {cls.tag()}_INDEX ON {cls.tag()}();"

    @classmethod
    def rebuild_index_statement(cls) -> str:
        """Generate a REBUILD TAG INDEX statement"""
        return f"REBUILD TAG INDEX {cls.tag()}_INDEX;"

    def insert_vertex_statement(self) -> str:
        """Generate INSERT VERTEX statement using instance values."""
        vertex_name = self.tag()
        properties = self.properties()
        property_keys = [name for name in properties.keys() if name != "id"]

        # Construct values string using instance attributes
        values_str = ", ".join(
            [
                (
                    f'"{getattr(self, name)}"'
                    if nebula_type == "string"
                    else str(getattr(self, name))
                )
                for name, nebula_type in properties.items()
                if name != "id"  # Skip the 'id' property
            ]
        )
        return f'INSERT VERTEX {vertex_name}({", ".join(property_keys)}) VALUES "{self.id}":({values_str});'


class BaseStatementNode(BaseModel, ABC):
    id: PyObjectId

    start_line: int = Field(description="Start line of the statement")

    stop_line: int = Field(description="End line of the statement")

    code_content: str = Field(description="Code content of the statement")

    @staticmethod
    @abstractmethod
    def properties() -> Dict[str, str]:
        """Define vertex-specific properties with Nebula data types."""
        return {
            "id": "string",
            "start_line": "int",
            "stop_line": "int",
            "code_content": "string",
        }

    @classmethod
    @abstractmethod
    def node_description(cls) -> str:
        """Define the description for chatbot to understand the node"""

    @classmethod
    @abstractmethod
    def tag(cls) -> str:
        """Returns the Nebula Graph tag name associated with this class."""

    @classmethod
    def create_vertex_statement(cls) -> str:
        """Generate a CREATE TAG statement with comments for each property using class methods."""
        vertex_name = cls.tag()
        properties_with_comments = []

        # Retrieve properties and descriptions from the class
        for name, field in cls.model_fields.items():
            nebula_type = cls.properties().get(
                name, "string"
            )  # Default to 'string' if not found in properties
            description = field.description  # Directly access description from Field
            comment = f"COMMENT '{description}'" if description else ""
            properties_with_comments.append(f"{name} {nebula_type} {comment}")

        # Retrieve node description from the class
        properties_str = ",\n    ".join(properties_with_comments)
        node_description = cls.node_description()
        return f"CREATE TAG IF NOT EXISTS {vertex_name} (\n    {properties_str}\n) COMMENT = '{node_description}';"

    @classmethod
    def create_tag_index_statement(cls) -> str:
        """Generate a CREATE TAG INDEX statement"""
        vertex_name = cls.tag()
        index_name = f"{vertex_name}{NEBULA_INDEX_NAME_POSTFIX}"
        return f"CREATE TAG INDEX IF NOT EXISTS {index_name} ON {vertex_name}();"

    def insert_vertex_statement(self) -> str:
        """Generate INSERT VERTEX statement using instance values."""
        vertex_name = self.tag()
        properties = self.properties()
        property_keys = [name for name in properties.keys() if name != "id"]

        # Construct values string using instance attributes
        values_str = ", ".join(
            [
                (
                    f'"{getattr(self, name)}"'
                    if nebula_type == "string"
                    else str(getattr(self, name))
                )
                for name, nebula_type in properties.items()
                if name != "id"  # Skip the 'id' property
            ]
        )
        return f'INSERT VERTEX {vertex_name}({", ".join(property_keys)}) VALUES "{self.id}":({values_str});'

    @classmethod
    def rebuild_index_statement(cls) -> str:
        """Generate a REBUILD EDGE INDEX statement"""
        tag_name = cls.tag()
        index_name = f"{tag_name}{NEBULA_INDEX_NAME_POSTFIX}"
        return f"REBUILD TAG INDEX {index_name};"


class SetStatementNode(BaseStatementNode):
    @staticmethod
    def properties():
        return super(SetStatementNode, SetStatementNode).properties()

    @classmethod
    def node_description(cls):
        return "Represents the SET statement in COBOL program"

    @classmethod
    def tag(cls) -> str:
        return "SET_STATEMENT"


class HasChild(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.HAS_CHILD

    @classmethod
    def edge_description(cls):
        return "Represent the relationship between COBOL variables. The parent variable has a child variable."

    @staticmethod
    def properties():
        base_properties = super(HasChild, HasChild).properties()

        return base_properties


class HasParagraph(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.HAS_PARAGRAPH

    @classmethod
    def edge_description(cls):
        return "Represent the relationship between paragraph and COBOL file. The COBOL file has a paragraph."

    @staticmethod
    def properties():
        base_properties = super(HasParagraph, HasParagraph).properties()

        return base_properties


class Source(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.SOURCE

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between source variable and COBOL statement"

    @staticmethod
    def properties():
        base_properties = super(Source, Source).properties()

        return base_properties


class Target(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.TARGET

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between COBOL statement and target variable, the direction is from statement to variable or value node"

    @staticmethod
    def properties():
        base_properties = super(Target, Target).properties()

        return base_properties


class Owns(BaseEdge):
    @classmethod
    def tag(cls) -> RelationshipLabel:
        return RelationshipLabel.OWNS

    @classmethod
    def edge_description(cls):
        return "Represents the relationship between the COBOL paragraph and COBOL statement. The paragraph owns the statement."

    @staticmethod
    def properties():
        base_properties = super(Owns, Owns).properties()

        return base_properties
