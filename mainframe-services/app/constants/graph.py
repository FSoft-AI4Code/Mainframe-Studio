from enum import Enum


class RelationshipLabel(str, Enum):
    """Labels to define types of relationships (or edges) between nodes."""

    EXEC_PGM = "EXEC_PGM"
    EXEC_PGM_DATASET = "EXEC_PGM_DATASET"
    EXEC_CICS = "EXEC_CICS"
    STATIC_CALL = "STATIC_CALL"
    STATIC_CALL_WITH_PARAM = "STATIC_CALL_WITH_PARAM"
    DYNAMIC_CALL = "DYNAMIC_CALL"
    DYNAMIC_CALL_WITH_PARAM = "DYNAMIC_CALL_WITH_PARAM"
    HAS_COPYBOOK = "HAS_COPYBOOK"
    HAS_INTERACT = "HAS_INTERACT"
    HAS_CHILD = "HAS_CHILD"
    HAS_PARAGRAPH = "HAS_PARAGRAPH"
    SOURCE = "SOURCE"
    TARGET = "TARGET"
    OWNS = "OWNS"


class NodeStatus(str, Enum):
    """Defines the current status of a node."""

    ALIVE = "ALIVE"
    MISSING = "MISSING"
    DEAD = "DEAD"


NEBULA_SPACE_NAME_PREFIX = "space_"
NEBULA_INDEX_NAME_POSTFIX = "_INDEX"
