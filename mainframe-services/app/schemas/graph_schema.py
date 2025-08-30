from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from app.constants.cobol import FileType
from app.constants.graph import RelationshipLabel
from app.schemas.common_schema import PyObjectId


class NodeStatus(str, Enum):
    """Defines the current status of a node."""
    ALIVE = "ALIVE"
    MISSING = "MISSING"
    DEAD = "DEAD"


class Node(BaseModel):
    """Represents a node with a unique ID, name, and group associations."""
    id: PyObjectId = Field(alias="_id")
    name: str
    label: FileType
    group: Optional[List[str]] = []
    status: NodeStatus
    is_entry_point: bool = False


class NodeDetailData(BaseModel):
    name: str
    label: FileType
    complexity: Optional[int]
    line_of_code: Optional[int]
    group: Optional[List[str]] = []
    status: NodeStatus
    is_entry_point: bool = False


class SubNodeData(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str
    label: FileType
    complexity: Optional[int]
    line_of_code: Optional[int]
    group: Optional[List[str]] = []
    status: NodeStatus
    is_entry_point: bool = False


class ExtendNode(BaseModel):
    """Represents a node with a unique ID, name, and group associations."""
    id: PyObjectId = Field(alias="_id")
    name: str
    label: FileType
    complexity: Optional[int]
    line_of_code: Optional[int]
    group: Optional[List[str]] = []
    status: NodeStatus
    is_entry_point: bool = False
    sub_nodes: Optional[List[SubNodeData]] = []


class EntryPointCriticality(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class EntryPoint(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str
    label: Optional[FileType] = None
    number_of_files: int
    complexity: int
    line_of_code: int
    criticality: EntryPointCriticality
    status: str = "init"


class EntryPointExtend(EntryPoint):
    refer_id: Optional[PyObjectId] = None


class Edge(BaseModel):
    """Represents an edge (or relationship) between two nodes with associated properties."""
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    source: PyObjectId
    target: PyObjectId
    type: RelationshipLabel
    group: List[str] = []
    properties: dict


class Graph(BaseModel):
    """Represents a graph with nodes and edges."""
    repository_id: PyObjectId
    nodes: List[Node]
    edges: List[Edge]
    entry_points: List[Node]


class GetDependenciesGraph(BaseModel):
    total_entry_points: int
    total: int
    page: int
    page_size: int
    repository_id: PyObjectId
    nodes: List[ExtendNode]
    edges: List[Edge]
    entry_points: List[EntryPointExtend]


class GetDetailDependencyEntryPoint(BaseModel):
    parent_entry_point: EntryPoint
    child_nodes: List[ExtendNode]

class GetStatusEntryPoint(BaseModel):
    entry_point: EntryPoint


class CreateGraphResponse(BaseModel):
    graph: GetDependenciesGraph


class GetGraphResponse(BaseModel):
    graph: GetDependenciesGraph


class DeleteGraphResponse(BaseModel):
    message: str


class GetEntrypointsResponse(BaseModel):
    entry_points: List[EntryPoint]
    total: int
    limit: int
    skip: int
