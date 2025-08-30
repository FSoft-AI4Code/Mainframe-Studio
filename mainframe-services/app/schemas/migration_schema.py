from typing import Literal, List, Optional

from pydantic import BaseModel, Field


class FileNode(BaseModel):
    name: str
    type: str  # "file" or "directory"
    path: str
    children: Optional[List['FileNode']] = None


class MigrationStructureResponse(BaseModel):
    repository_id: str
    bms_file_name: str
    structure: FileNode


class FileContentResponse(BaseModel):
    repository_id: str
    bms_file_name: str
    file_path: str
    content: str


class JavaOutputFileModel(BaseModel):
    file_name: str
    file_content: str


class JavaOutputAPIModel(BaseModel):
    api_path: str
    method: Literal["GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]


class JavaCopybookStructure(BaseModel):
    model_java: JavaOutputFileModel
    dto_java: JavaOutputFileModel
    repository_java: JavaOutputFileModel
    service_java: JavaOutputFileModel
    controller_java: JavaOutputFileModel
    liquibase_java: JavaOutputFileModel
    api_java: List[JavaOutputAPIModel]


class JavaBMSStructure(BaseModel):
    view_name: str
    view_java: JavaOutputFileModel
    mapping_apis: List[JavaOutputAPIModel]
    controller_java: JavaOutputFileModel


class JavaCopybookMigration(BaseModel):
    id: str = Field(None, alias="_id")
    repository_id: str = Field(None, description="Repository or project ID")
    linked_cobol: str = Field(None, description="Linked COBOL file name to the COPYBOOK program")
    status: Optional[Literal['running', 'done', 'fail']] = Field(None, description="Processing status")
    path: Optional[str] = Field(None, description="File path to the COPYBOOK program")
    model_java: Optional[JavaOutputFileModel]
    dto_java: Optional[JavaOutputFileModel]
    service_java: Optional[JavaOutputFileModel]
    repository_java: Optional[JavaOutputFileModel]
    controller_java: Optional[JavaOutputFileModel]
    api_java: List[Optional[JavaOutputAPIModel]]
    liquibase_java: Optional[JavaOutputFileModel]


class JavaBMSMigration(BaseModel):
    id: str = Field(None, alias="_id")
    repository_id: str = Field(None, description="Repository or project ID")
    status: Optional[Literal['running', 'done']] = Field(None, description="Processing status")
    path: Optional[str] = Field(None, description="File path to the BMS program")
    view_java: Optional[JavaOutputFileModel]
    controller_java: Optional[JavaOutputFileModel]
    mapping_apis: List[JavaOutputAPIModel]
