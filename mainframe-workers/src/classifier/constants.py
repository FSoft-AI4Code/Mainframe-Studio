from enum import Enum


class FileType(str, Enum):
    """Enumeration of file types for mainframe migration."""

    COBOL = "COBOL"
    PLI = "PLI"
    CSD = "CSD"
    DB = "DB"
    COPY = "COPY"
    PROC = "PROC"
    JCL = "JCL"
    JCL_IBM = "JCL_IBM"
    JCL_FUJITSU = "JCL_FUJITSU"
    SQL = "SQL"
    BMS = "BMS"
    OTHER = "OTHER"
    UTILITY = "UTILITY"
    LDL = "LDL"
    DASDL = "DASDL"
    WFL = "WFL"
    CLIST = "CLIST"
    PANEL = "PANEL"
    REPORT = "REPORT"


class SystemType(str, Enum):
    """Enumeration of mainframe system types."""

    IBM = "IBM"
    UNISYS = "UNISYS"
    DNP = "DNP"
    FUJITSU = "FUJITSU"
