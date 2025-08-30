import traceback
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
from dotenv import load_dotenv
import os
import sys
from pydantic import BaseModel
from typing import List, Optional, Dict, Any, Generator
from antlr4 import CommonTokenStream, InputStream
from grammar.dnp.DNPLexer import DNPLexer
from grammar.dnp.DNPParser import DNPParser
from grammar.dnp.DNPVisitorImp import DNPVisitorImp
from grammar.dnp.dnp_cobol_schemas import DNPStatementFactory
from grammar.common.base_cobol_schemas import Statement, Comment

import json
import uuid
import subprocess
from loguru import logger
import re
from typing import Union
import math
import itertools
from pymongo import MongoClient

def parse_cobol_koopa(parse_func: str, code: str, encoding: str = "utf-8", last_depth: str = "200"):
    try:
        # Get cache path and koopa parser path from settings
        cache_path = "tmp"
        cobol_parser = "koopa.jar"

        # Write code to a temporary file
        tmp_code_file = f"{uuid.uuid4().hex}.cbl"
        tmp_parsed_file = f"{uuid.uuid4().hex}.json"
        tmp_code_file_path = os.path.join(cache_path, tmp_code_file)
        tmp_parsed_file_path = os.path.join(cache_path, tmp_parsed_file)

        with open(tmp_code_file_path, "w", encoding=encoding) as f:
            f.write(code)

        subprocess.call(
            [
                "java",
                "-classpath",
                cobol_parser,
                f"koopa.examples.basic.{parse_func}",
                tmp_code_file_path,
                tmp_parsed_file_path,
                last_depth,
                cache_path,
            ],
            stdout=subprocess.DEVNULL
        )

        with open(tmp_parsed_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Format the data
        formatted_data = format_koopa_data(data)

        # Clean up temporary files
        os.remove(tmp_code_file_path)
        os.remove(tmp_parsed_file_path)

        return formatted_data

    except Exception as e:
        logger.error("Koopa parsing failed", error=str(e), code_file=tmp_code_file_path, parsed_file=tmp_parsed_file_path)
        raise


def format_koopa_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format the Koopa parser output data by replacing spaces with underscores in keys.
    Handles nested dictionaries and lists recursively.
    """
    formatted_data = {}
    for key, value in data.items():
        formatted_key = key.replace(" ", "_")
        if isinstance(value, dict):
            formatted_data[formatted_key] = format_koopa_data(value)
        elif isinstance(value, list):
            formatted_list = []
            for item in value:
                if isinstance(item, dict):
                    formatted_list.append(format_koopa_data(item))
                else:
                    formatted_list.append(item)
            formatted_data[formatted_key] = formatted_list
        else:
            formatted_data[formatted_key] = value
    return formatted_data

def extract_copy_filenames(lines: List[str]) -> Dict[str, Union[str, int]]:
    """Find COPY statements in the COBOL file lines and extract filenames with their line numbers."""
    return {
        line_number: re.search(r"^\s+COPY\s+([^\s]+)", line).group(1).split(".")[0]
        for line_number, line in enumerate(lines)
        if re.match(r"^\s+COPY\s+.*\.", line) and not line.lstrip().startswith("*")
    }


def query_copy_content(filename: str) -> str:
    mongo_uri = f"mongodb://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DB_NAME')}?authSource=admin"
    client = MongoClient(mongo_uri)
    db = client.mainframe
    collection = db.reverse_engineering
    result = collection.find_one({"name": filename})
    if result:
        return result.get("content", "")
    else:
        return None

def handle_replacing_copy(copy_line: str, copy_content: str) -> str:
    if "REPLACING" not in copy_line:
        return copy_content
    
    copy_content_lines = copy_content.split("\n")
    match = re.search(
        r"REPLACING\s+(==\s+)?([^\s]+)(\s+==)?\s+BY\s+(==\s+)?([^\s]+)(\s+==)?",
        copy_line,
    )
    if match:
        source, target = match.group(2).replace("==", ""), match.group(5).strip(".").replace("==", "")
        copy_content_lines = [
            line.replace(source, target) for line in copy_content_lines
        ]
    return "\n".join(copy_content_lines)

def read_blob_file(blob_name: str):
    try:
        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blob_name = f"677dd79199b0284a3a8b5abc/{blob_name}"
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob()
        encoding = blob_client.get_blob_properties().metadata.get("encoding", "CP932")
        return blob_data.content_as_text(encoding=encoding)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    
def read_blob_csv():
    # Get Azure Storage details from environment variables
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
    blob_name = "677dd79199b0284a3a8b5abc_classified.csv"
    
    # Validate environment variables
    if not all([connection_string, container_name, blob_name]):
        raise ValueError("Missing required environment variables. Please check your .env file.")
    
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        blob_client = container_client.get_blob_client(blob_name)
        encoding = blob_client.get_blob_properties().metadata["encoding"]
        blob_data = blob_client.download_blob()
        df = pd.read_csv(io.BytesIO(blob_data.readall()),
                    escapechar="\\",
                    encoding=encoding,
                    on_bad_lines="warn",
                )
        return df
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def calculate_cobol_variable_length(
    pic: str, compression_format: Optional[str] = None
) -> int:
    pic = pic.upper()
    symbol_list = ["9", "X", "A", "P", "Z"]
    regex_extract_length = re.compile(r"\((.*?)\)")

    # sum all the numbers inside brackets
    length_list = re.findall(regex_extract_length, pic)
    length = sum(list(map(int, length_list)))

    # sum the number of symbols which are not before "("
    for element in pic.split(")"):
        if "(" not in element:
            element = element.upper()

            for symbol in symbol_list:
                length += element.count(symbol)

    if compression_format is None:
        return length

    compression_format = compression_format.upper()
    # recalculate length with compression format
    is_half_int = math.ceil(length / 2) == math.floor(length / 2)

    is_binary_compression_format = (
        "COMP" in compression_format or "BINARY" in compression_format
    )

    is_bcd_compressed_format = (
        "COMP-3" in compression_format or "PACKED-DECIMAL" in compression_format
    )

    if is_bcd_compressed_format:
        length = math.ceil(length / 2) + \
            1 if is_half_int else math.ceil(length / 2)
    elif is_binary_compression_format:
        if length <= 4:
            length = 2
        elif length <= 9:
            length = 4
        elif length <= 18:
            length = 8

    return length

def handle_analysis_map(analysis_map: Dict[str, Any]) -> Dict[str, Any]:
    data_map_list = analysis_map["dataMapList"]
    io_map_list = analysis_map["ioMapList"]
    linkage_map_list = analysis_map["linkageMapList"]

    for i, data_map in enumerate(data_map_list):
        if "pic" not in data_map:
            continue

        pic = data_map["pic"]
        compression_format: Optional[str] = data_map.get("data_type")

        length = calculate_cobol_variable_length(
            pic=pic, compression_format=compression_format
        )

        data_map_list[i]["num_digits"] = str(length)

    if len(io_map_list) > 0 and isinstance(io_map_list[0], list):
        io_map_list = list(itertools.chain(*io_map_list))

    for io_map in io_map_list:
        if "pic" not in io_map:
            continue

        pic = io_map["pic"]
        compression_format = io_map.get("data_type")

        length = calculate_cobol_variable_length(
            pic=pic, compression_format=compression_format
        )

        io_map["num_digits"] = str(length)

    for linkage_map in linkage_map_list:
        if "num_digits" not in linkage_map:
            continue

        pic = linkage_map["pic"]
        compression_format = linkage_map.get("data_type")

        length = calculate_cobol_variable_length(
            pic=pic, compression_format=compression_format
        )

        linkage_map["num_digits"] = str(length)

class CopyGraphItem(BaseModel):
    index: int
    program_id: str
    program_type: str
    program_name: str
    call_type: str
    notes: str
    locations: str = ""

class CopyGraph(BaseModel):
    programs: List[CopyGraphItem]
    details: List[str]

class ReferencesSubCommand(BaseModel):
    command: str
    explain: str

class IOParamsDefTable(BaseModel):
    item_name: str = None
    cobol_level: str = None
    cobol_dtype: str = None
    length: str = None
    access_mode: str = None
    dtype: str = None
    default_value: str = None
    remarks: str = None

class IOParamsDef(BaseModel):
    input_table: Optional[List[IOParamsDefTable]] = None
    input_note: str = ""
    output_table: Optional[List[IOParamsDefTable]] = None
    output_note: str = ""

class IOItem(BaseModel):
    index: int
    item_name: str = ""
    physical_name: str = ""
    type: str = ""
    crud_op: str = ""
    access_mode: str = ""
    notes: str = ""

class OverviewProgram(BaseModel):
    programe_name: str
    io_files: List
    db_accesses: List
    copy_files: List
    call_files: List
    summarization: Optional[str] = ""
    io_table: List[IOItem]

def get_io_desc(ioMapList, linkageMapList):
    in_descs = []
    out_descs = []
    levels = []
    for ioMaps in ioMapList:
        for io in ioMaps:
            level = int(io["level"])
            if not level in levels:
                levels.append(level)
    for io in linkageMapList:
        level = int(io["level"])
        if not level in levels:
            levels.append(level)
    levels.sort()
    levelMap = {}
    for i in range(len(levels)):
        levelMap[levels[i]] = i

    for ioMaps in ioMapList:
        for io in ioMaps:
            desc = {}
            level = int(io["level"])
            space = levelMap[level] * "   "
            if "label name" in io:
                desc["Item name"] = space + io["label name"]
            else:
                desc["Item name"] = ""
            if "level" in io:
                desc["Cobol level"] = io["level"]
            else:
                desc["Cobol level"] = ""
            if "property" in io:
                desc["Cobol data type"] = io["property"]
            else:
                desc["Cobol data type"] = ""
            if "num digits" in io:
                desc["Length"] = io["num digits"].replace("V", "")
            else:
                desc["Length"] = ""

            if "type" in io:
                desc["Access mode"] = io["type"]
            else:
                desc["Access mode"] = ""
            dtype = ""
            if "property" in io:
                dtype = "Int"
                if io["property"] == "X":
                    dtype = "String"
            desc["Data type"] = dtype

            default_value = ""
            if "default value" in io:
                default_value = io["default value"]
            desc["Default value"] = default_value

            if level == 1:
                desc["Remarks"] = "Java DTO class equivalence"
            else:
                desc["Remarks"] = "Java " + dtype + " data type equivalence"

            # TODO: Fix key error "type"
            io_type = io.get("type", "")
            if io_type == "INPUT" or io_type == "I-O":
                in_descs.append(
                    IOParamsDefTable(
                        item_name=desc["Item name"],
                        cobol_level=desc["Cobol level"],
                        cobol_dtype=desc["Cobol data type"],
                        length=desc["Length"],
                        access_mode=desc["Access mode"],
                        dtype=desc["Data type"],
                        default_value=desc["Default value"],
                        remarks=desc["Remarks"],
                    )
                )
            if io_type == "OUTPUT" or io_type == "I-O" or io_type == "EXTEND":
                out_descs.append(
                    IOParamsDefTable(
                        item_name=desc["Item name"],
                        cobol_level=desc["Cobol level"],
                        cobol_dtype=desc["Cobol data type"],
                        length=desc["Length"],
                        access_mode=desc["Access mode"],
                        dtype=desc["Data type"],
                        default_value=desc["Default value"],
                        remarks=desc["Remarks"],
                    )
                )

    for io in linkageMapList:
        desc = {}
        level = int(io["level"])
        space = levelMap[level] * "   "
        if "label_name" in io:
            desc["Item name"] = space + io["label_name"]
        else:
            desc["Item name"] = ""
        if "level" in io:
            desc["Cobol level"] = io["level"]
        else:
            desc["Cobol level"] = ""
        if "property" in io:
            desc["Cobol data type"] = io["property"]
        else:
            desc["Cobol data type"] = ""
        if "num_digits" in io:
            desc["Length"] = io["num_digits"].replace("V", "")
        else:
            desc["Length"] = ""

        if "type" in io:
            desc["Access mode"] = io["type"]
        else:
            desc["Access mode"] = ""

        dtype = "String" if io.get("property") == "X" else "Int" if io.get("property") else ""
        desc["Data type"] = dtype

        desc["Default value"] = io.get("default value", "")
        desc["Remarks"] = "Java DTO class equivalence" if level == 1 else "Java " + dtype + " data type equivalence"

        # TODO: Fix key error "type"
        io_type = io.get("type", "")
        if io_type == "INPUT" or io_type == "I-O":
            in_descs.append(
                IOParamsDefTable(
                    item_name=desc["Item name"],
                    cobol_level=desc["Cobol level"],
                    cobol_dtype=desc["Cobol data type"],
                    length=desc["Length"],
                    access_mode=desc["Access mode"],
                    dtype=desc["Data type"],
                    default_value=desc["Default value"],
                    remarks=desc["Remarks"],
                )
            )
        if io_type == "OUTPUT" or io_type == "I-O" or io_type == "EXTEND":
            out_descs.append(
                IOParamsDefTable(
                    item_name=desc["Item name"],
                    cobol_level=desc["Cobol level"],
                    cobol_dtype=desc["Cobol data type"],
                    length=desc["Length"],
                    access_mode=desc["Access mode"],
                    dtype=desc["Data type"],
                    default_value=desc["Default value"],
                    remarks=desc["Remarks"],
                )
            )

    return in_descs, out_descs

class AnalyzedProgram:
    io_section: Optional[str] = ""
    overview: Optional[OverviewProgram] = None
    io_params_def: Optional[IOParamsDef] = None
    # process_logic: Optional[List] = []
    process_logic: Optional[str] = ""
    copy_graph: Optional[CopyGraph] = None
    references: Optional[List[ReferencesSubCommand]] = []
    meta: Optional[Dict] = None

    def __init__(self, blob: Dict):
        self.parsed_data = blob

        for _, section in blob["startSectionMap"].items():
            if "iosection" in section["Name"].strip().lower():
                self.io_section = section["Code_content"]

    def __extract_io_files(self):
        index = 1
        io_table = []
        for file_name, object in self.parsed_data["analysisMap"][
            "ioObjectList"
        ].items():
            file_name_splits = file_name.split(".")
            if len(file_name_splits) > 1:
                item_name = file_name_splits[-1]
            else:
                item_name = file_name

            if "JCL_Name" in object.keys():

                physical_name = object["JCL_Name"]

                io_table.append(
                    IOItem(
                        index=index,
                        item_name=item_name,
                        physical_name=physical_name,
                        notes="",
                    )
                )
            else:
                physical_name = file_name

                io_table.append(
                    IOItem(
                        index=index,
                        item_name=item_name,
                        physical_name=physical_name,
                        type=object["type"],
                        crud_op=object["crud_operation"],
                        access_mode=object["access_mode"],
                        notes="",
                    )
                )
        return io_table

    def __extract_copy_graph_items(
        self
    ):  # TODO: Check program name
        copy_graph_items = []
        for index, call_file in enumerate(self.parsed_data["callLocFileMap"].values()):
            copy_graph_items.append(
                CopyGraphItem(
                    index=index,
                    program_id=call_file.split("::")[0].replace("'", ""),
                    program_type="Cobol",
                    program_name=call_file.split("::")[0].replace(
                        "'", ""
                    ),  # Check in list program name
                    call_type=(
                        "Dynamic call"
                        if call_file.split("::")[1] == "dynamic"
                        else "Static Call"
                    ),
                    notes="",
                )
            )
        for index, copy_file in enumerate(self.parsed_data["copyLocFileMap"].values()):
            copy_graph_items.append(
                CopyGraphItem(
                    index=index,
                    program_id=copy_file,
                    program_type="Copy",
                    program_name=copy_file,
                    call_type="Static Call",
                    notes="",
                )
            )
        for index, sql_file in enumerate(self.parsed_data["sqlLocFileMap"].values()):
            note = "SQL file"
            # TODO: config is_involve_SQLCA -> SQL Communication area -> SQLCA
            copy_graph_items.append(
                CopyGraphItem(
                    index=index,
                    program_id=sql_file,
                    program_type="Copy/SQL",
                    program_name=sql_file,
                    call_type="Static Call",
                    notes=note,
                )
            )
        return copy_graph_items

    def extract_overview(self):
        self.overview = OverviewProgram(
            programe_name=self.parsed_data["analysisMap"]["ProgramID"],
            io_files=[],
            db_accesses=self.parsed_data["analysisMap"]["sqlActionList"].keys(),
            copy_files=list(self.parsed_data["copyLocFileMap"].values()),
            call_files=list(self.parsed_data["callLocFileMap"].values()),
            io_table=self.__extract_io_files(),
        )
        return self.overview

    def extract_io_params_def(self):
        # for io_map in self.analysisMap['ioMapList']:
        # for _ in self.analysisMap['linkageMapList']:
        # TODO: ioMapList and linkageMapList return empty list
        # https://dev.azure.com/azurefsoft062/COBOL-migration/_git/research_cobol?path=/GenTemplates_2.py&version=GBmaster&line=2164&lineEnd=2277&lineStartColumn=5&lineEndColumn=35&lineStyle=plain&_a=contents
        in_desc, out_desc = get_io_desc(
            self.parsed_data["analysisMap"]["ioMapList"],
            self.parsed_data["analysisMap"]["linkageMapList"],
        )
        self.io_params_def = IOParamsDef(
            input_table=in_desc,
            output_table=out_desc,
        )
        return self.io_params_def

    def extact_copy_graph(self):
        # https://dev.azure.com/azurefsoft062/COBOL-migration/_git/research_cobol?path=/GenTemplates_2.py&version=GBmaster&line=2055&lineEnd=2082&lineStartColumn=5&lineEndColumn=30&lineStyle=plain&_a=contents
        # TODO: copy_graph and details
        self.copy_graph = CopyGraph(
            programs=self.__extract_copy_graph_items(), details=[""]
        )
        return self.copy_graph

    def extract_all(self):
        self.extract_overview()
        self.extract_io_params_def()
        self.extact_copy_graph()

class ReverseEngineeringUpdate(BaseModel):
    status: str
    output: Optional[dict] = None
    type: Optional[str] = None

def preprocess_dnp(code):
    code = code.replace("\u001E", "<RS>")  # change the token

    code = re.sub(r"^.{6}", "      ", code, flags=re.MULTILINE)
    code = re.sub(r"^.{6}\/", "      *", code, flags=re.MULTILINE)
    code = re.sub(r"^\s{7}\*", "      **", code, flags=re.MULTILINE)
    code = re.sub(r"\*>.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^\s*\\.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"\d{6}[A-Za-z]{2}", "        ", code, flags=re.MULTILINE)

    # Remove empty line, keep only 72 characters
    code = "\n".join([line for line in code.splitlines() if line.strip()])
    code = code.replace("<RS>", "\u001E")  # restore token

    return code

def get_io_files(file_control_list, file_description_list) -> List[Dict[str, str]]:
    """
    Format IO files information from file control entries
    
    Args:
        file_control_list: List of file control entries from parser
        
    Returns:
        List[Dict[str, str]]: List of formatted IO file information
    """
    io_files = []

    copybooks_dict = {
        file_description.file_name: file_description.copybooks for file_description in file_description_list
    }

    for file_control in file_control_list:
        copybooks = copybooks_dict.get(file_control.file_name, [])
        copybooks = [copybook.model_dump() for copybook in copybooks]
        io_file = {
            "name": file_control.assignment_name,
            "access_mode": file_control.access_mode,
            "copybooks": copybooks
        }
        io_files.append(io_file)
    
    return io_files

def map_picture_clause(picture_clause):
        if picture_clause is None:
            return None
        elif "X" in picture_clause:
            return "X"
        elif "A" in picture_clause:
            return "A"
        elif "9" in picture_clause or "S9" in picture_clause:
            return "9"
        elif "N" in picture_clause:
            return "N"
        else:
            return None

def extract_cobol_comment(
    lexer: Union[DNPLexer], stream: CommonTokenStream
) -> List[Comment]:
    symbolic_names = lexer.symbolicNames
    tokens = stream.tokens
    comment_list = []
    for token in tokens:
        token_name = (
            symbolic_names[token.type]
            if token.type < len(symbolic_names)
            else "UNKNOWN"
        )

        if token_name in [
            "COMMENTLINE",
            "COMMENTLINE2",
            "COMMENTLINE_2",
            "COMMENTLINE_3",
            "COMMENTLINE_4",
        ]:
            # ignore comment line with only "*"
            processed_content = token.text.replace("*", "").strip()
            if processed_content:
                content = token.text

                # remove first 6 characters for comment line
                # ignore for inline comment
                if not content.startswith("*>"):
                    content = content[5:]

                content = content.strip()

                comment_list.append(
                    Comment(
                        content=content,
                        line_number=token.line,
                    )
                )
    return comment_list

def get_subroutines_called(statements, comments) -> List[Dict[str, str]]:
    subroutines_called = []
    for statement in iterate_statements(statements):
        if statement.tag == "CallStatement":
            subroutine_name = statement.call_identifiers[0] if statement.call_identifiers else statement.call_literal
            business_name = next(
                (comment.content for comment in sorted(comments, key=lambda x: x.line_number, reverse=True)
                 if comment.line_number < statement.start_line), 
                None
            )
            
            subroutines_called.append({
                "name": subroutine_name,
                "business_name": business_name
            })
    return subroutines_called

def get_working_storage_variables(variable_list) -> List[Dict[str, str]]:
    working_storage_variables = []
    working_storage_list = variable_list.working_storage
    for variable in working_storage_list:
        variable = {
            "level": variable.level,
            "name": variable.name,
            "data_type": map_picture_clause(variable.picture_clause) if variable.picture_clause else "",
            "length": f"{variable.picture_clause}{f" {variable.compression_format}" if variable.compression_format else ''}",
            "default_value": variable.default_value if variable.default_value else "",
            "remarks": variable.redefine if variable.redefine else variable.occur if variable.occur else "",
        }
        working_storage_variables.append(variable)
    return working_storage_variables

def query_copybook(copybook_name, repository_id) -> Dict[str, str]:
    try:
        mongo_uri = f"mongodb://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DB_NAME')}?authSource=admin"
        client = MongoClient(mongo_uri)
        db = client.mainframe
        collection = db.reverse_engineering

        result = collection.find_one({
            'name': copybook_name,
            'repository_id': repository_id,
            'type': 'COPY'
        })

        if result and result.get('output'):
            return result['output']
        else:
            logger.error(f"No copybook found for {copybook_name}")
            return {}

    except Exception as e:
        logger.error(f"Error querying copybook: {str(e)}")
        return {}
    
def get_variables_flow(io_files, working_storage_variables, statements) -> List[Dict[str, str]]:
    variables_flow = []
    for io_file in io_files:
        if io_file.get("access_mode") == "OUTPUT":
            for copybook in io_file.get("copybooks"):
                copybook_data = query_copybook(copybook.get("copybook_name"), "677dd79199b0284a3a8b5abc")
                
                variables_declaration = copybook_data.get("variables_declaration")
                for declaration in variables_declaration:
                    # Get all replacements where declaration name contains the replaceable text
                    replaceable = ""
                    replacement = ""
                    matching_replacements = [
                        (rule.get("replaceable").replace("=", ""), rule.get("replacement").replace("=", "")) 
                        for rule in copybook.get("replacing") 
                        if rule.get("replaceable").replace("=", "") in declaration.get("name", "")
                    ]
                    # Use the first matching replacement if any found
                    if matching_replacements:
                        replaceable, replacement = matching_replacements[0]
                    name = declaration.get("name").replace(replaceable, replacement)
                    src_variable = next((statement.move_from for statement in iterate_statements(statements) \
                                         if statement.tag == "MoveStatement" and \
                                            statement.move_to == name), None)
                    src_data_type = None
                    src_length = None
                    if src_variable:
                        src_var = next((var for var in working_storage_variables 
                                      if var["name"] == src_variable), None)
                        src_data_type = src_var["data_type"] if src_var else None
                        src_length = src_var["length"] if src_var else None
                        
                    
                    variable = {
                        "name": name,
                        "data_type": declaration.get("data_type"),
                        "length": declaration.get("length"),
                        "src_variable": src_variable,
                        "src_data_type": src_data_type,
                        "src_length": src_length
                    }
                    variables_flow.append(variable)
    return variables_flow

def iterate_statements(statements) -> Generator[Statement, None, None]:
    for statement in statements:
        yield statement
        for _, attr_value in statement.__dict__.items():
            if isinstance(attr_value, list) and attr_value and isinstance(attr_value[0], Statement):
                for nested_statement in iterate_statements(attr_value):
                    yield nested_statement

def parse_cobol_antlr(code: str) -> Optional[Dict]:
    try:
        code = preprocess_dnp(code)
        code = "\n".join(code.splitlines())
        stream = CommonTokenStream(DNPLexer(InputStream(code)))
        stream.fill()
        lexer = DNPLexer(InputStream(code))
        parser = DNPParser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        visitor = DNPVisitorImp(parser)
        tree.accept(visitor)
        statements = [DNPStatementFactory.from_dict(statement) for statement in visitor.statements]
        # Use the extracted get_io_files function
        io_files = get_io_files(visitor.file_control_list, visitor.file_description_list)
        working_storage_variables = get_working_storage_variables(visitor.variable_list)
        comments = extract_cobol_comment(lexer, stream)
        identification_division = next((division for division in visitor.division_list if division.division_name == "IDENTIFICATION DIVISION"), None)
        description = "\n".join([comment.content for comment in comments if comment.line_number < identification_division.start_line]) if identification_division else ""
        subroutines_called = get_subroutines_called(statements, comments)
        variables_flow = get_variables_flow(io_files, working_storage_variables, statements)
        parsed_program = {
            "program_id": visitor.program_id,
            "io_files": io_files,
            "description": description,
            "working_storage_variables": working_storage_variables,
            "subroutines_called": subroutines_called,
            "variables_flow": variables_flow,
        }
        # logger.info(parsed_program)
        return parsed_program
    except Exception as e:
        exception = sys.exc_info()
        logger.error(f"Error parsing COBOL code: {e}")
        logger.opt(exception=exception).info("Logging exception traceback")
        return None
    
def save_parsed_program(name: str, repository_id: str, parsed_program: Dict[str, Any], type: str) -> Dict[str, Any]:
    """
    Save parsed program result to database using upsert operation
    
    Args:
        name (str): The name of the program
        repository_id (str): The repository ID
        parsed_program (Dict[str, Any]): The parsed program data
        type (str): The type of program
        
    Returns:
        Dict[str, Any]: Result of the save operation containing status and message
    """
    try:
        mongo_uri = f"mongodb://{os.getenv('MONGODB_USER')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DB_NAME')}?authSource=admin"
        client = MongoClient(mongo_uri)
        db = client.mainframe
        collection = db.reverse_engineering

        result = collection.update_one(
            filter={
                'name': name,
                'repository_id': repository_id,
                'type': type
            },
            update={
                '$set': {
                    'status': 'done',
                    'output': parsed_program
                }
            },
            upsert=True
        )
        
        if result.matched_count > 0:
            return {
                "status": "success", 
                "message": "Successfully updated parsed program"
            }
        elif result.upserted_id:
            return {
                "status": "success",
                "message": "Successfully inserted parsed program"
            }
        else:
            return {
                "status": "error",
                "message": "Failed to save parsed program"
            }

    except Exception as e:
        logger.error("Error saving parsed program", error=str(e))
        logger.error(traceback.format_exc())
        return {
            "status": "error",
            "message": f"Error saving parsed program: {str(e)}"
        }

def parse_cobol():
    try:
        df = read_blob_csv()
        cobol_df = df[df['label'] == 'COBOL'].copy()
        # Print the 'content' field and parse it
        if 'content' in cobol_df.columns:
            for _, row in cobol_df.iterrows():
                print(row['name'])
                content = read_blob_file(f"code/COBOL/{row['name']}")
                parsed_program = parse_cobol_antlr(
                        code=content
                    )
                
                save_parsed_program(row['name'], "677dd79199b0284a3a8b5abc", parsed_program, 'COBOL')
        else:
            print("The 'content' field does not exist in the DataFrame.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Traceback:")
        traceback.print_exc()

if __name__ == "__main__":
    
    # Load environment variables
    load_dotenv()
    parse_cobol()