from enum import Enum
from typing import List
from pydantic import BaseModel

class DatabaseOperation(str, Enum):
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class DatabaseTableDescriptor(BaseModel):
    """
    Database table descriptor containing information about the table used in the COBOL program.
    """

    program_name: str
    database_name: str
    table_name: str
    invoke_names: List[str]
    operations: List[DatabaseOperation]
