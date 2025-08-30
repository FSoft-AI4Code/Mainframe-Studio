from enum import Enum


class FileType(str, Enum):
    """Enumeration of file types for mainframe migration."""

    COBOL = "COBOL"
    PLI = "PLI"
    PLI_COPY = "PLI_COPY"
    CSD = "CSD"
    CICS = "CICS"
    DB = "DB"
    COPY = "COPY"
    JCL = "JCL"
    PROC = "PROC"
    JCL_IBM = "JCL_IBM"
    JCL_FUJITSU = "JCL_FUJITSU"
    SQL = "SQL"
    BMS = "BMS"
    OTHER = "OTHER"
    UTILITY = "UTILITY"
    LDL = "LDL"
    WFL = "WFL"
    DASDL = "DASDL"
    PANEL = "PANEL"
    EASY = "EASY"
    ASM = "ASM"
    DDL = "DDL"
    REPORT = "REPORT"
    A_AUTO = "A_AUTO"
    CLIST = "CLIST"


class SystemType(str, Enum):
    """Enumeration of mainframe system types."""

    IBM = "IBM"
    UNISYS = "UNISYS"
    DNP = "DNP"
    FUJITSU = "FUJITSU"
