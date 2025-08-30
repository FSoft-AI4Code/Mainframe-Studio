from typing import List, Optional

from pydantic import BaseModel


class JclDatasetAccessOperation(BaseModel):
    """
    Represents how a specific COBOL program accesses a dataset defined in JCL.

    This class captures the relationship between an individual program and
    a dataset, including how the program accesses the dataset (read, write, etc.).

    Attributes:
        open_by_program_id: The ID of the program that opens the dataset
        open_mode: The mode of access (e.g., INPUT, OUTPUT, I-O)
    """

    open_by_program_id: str
    open_mode: str


class JclDatasetAssignment(BaseModel):
    """
    Maps a dataset defined in JCL to its usage patterns across programs.

    This class represents how a dataset declared in a JCL DD statement is accessed
    throughout the program call hierarchy, capturing all programs that interact
    with the dataset and their access modes. It serves as a comprehensive record
    of dataset references and access patterns for dependency analysis and data lineage.

    Attributes:
        repository_id: The ID of the repository containing this dataset assignment
        step: The name of the JCL step in which this dataset is defined
        jcl_name: The name of the JCL file where this dataset is defined
        exec_program_id: The ID of the program specified in the EXEC statement that uses this dataset
        dataset_name: The physical name of the dataset being accessed (DSN)
        ddname: The DD name that identifies this dataset within the JCL
        access_operations: List of operations showing how different programs access this dataset,
                          including access modes (READ, WRITE, etc.) and the programs performing them
        dataset_type: The type of dataset
    """

    repository_id: str
    step: str
    jcl_name: str
    exec_program_id: str
    dataset_name: str
    ddname: str
    access_operations: List[JclDatasetAccessOperation] = []
    dataset_type: str
