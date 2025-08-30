from __future__ import annotations

import os
import re
from contextlib import redirect_stderr, redirect_stdout
from typing import Dict, List, Optional

from antlr4 import CommonTokenStream, InputStream
from langchain.schema import HumanMessage, SystemMessage
from loguru import logger
from pydantic import BaseModel, SerializeAsAny

from app.tasks.config.constants import INSTRUCTION
from app.tasks.grammar.dnp.dnp_cobol_schemas import DNPStatementFactory
from app.tasks.grammar.dnp.DNPLexer import DNPLexer
from app.tasks.grammar.dnp.DNPParser import DNPParser
from app.tasks.grammar.dnp.DNPVisitorImp import DNPVisitorImp
from app.tasks.grammar.ibm_cobol.ibm_cobol_schemas import IBMStatementFactory
from app.tasks.grammar.unisys_cobol.cobol_unisys_schemas import UnisysStatementFactory
from app.tasks.grammar.unisys_cobol.CobolUnisysLexer import CobolUnisysLexer
from app.tasks.grammar.unisys_cobol.CobolUnisysParser import CobolUnisysParser
from app.tasks.grammar.unisys_cobol.DaikyoUnisysCobolVistor import (
    DaikyoUnisysCobolVistor,
)
from app.tasks.schemas.worker_schemas import ParagraphOutput

from ..grammar.common.base_cobol_schemas import (
    CobolVariable,
    FileControlEntry,
    FileDescriptionEntry,
    ImportedCopybook,
    Statement,
)
from ..grammar.ibm_cobol.Cobol85Lexer import Cobol85Lexer
from ..grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from ..grammar.ibm_cobol.MyCobol85Visitor import MyCobol85Visitor, Paragraph


class CopybookDependency(BaseModel):
    parsed_data: ParsedProgramAntlr
    code_content: str


class ParsedProgramAntlr(BaseModel):
    program_id: str
    copybook_list: list[ImportedCopybook]
    file_control_list: list[FileControlEntry]
    file_description_list: list[FileDescriptionEntry]
    variable_list: SerializeAsAny[list[CobolVariable]]
    copybook_dependencies: list[CopybookDependency]
    paragraph_list: list[Paragraph]
    statements: SerializeAsAny[list[Statement]]


def parse_cobol_antlr(
    code: str, dependency_map: dict[str, CopybookDependency]
) -> ParsedProgramAntlr:
    """Parse COBOL program using ANTLR4

    Args:
        code (str): The COBOL code
        dependency_map dict[str, CopybookDependency]: The dependency dictionary with keys are the file ID, values are dependency.
    Returns:
        ParsedProgramAntlr: Parsed COBOL code
    """
    try:
        with open(os.devnull, "w", encoding="utf-8") as devnull:
            with redirect_stdout(devnull), redirect_stderr(devnull):
                code = "\n".join(code.splitlines())
                stream = CommonTokenStream(Cobol85Lexer(InputStream(code)))
                stream.fill()

                parser = Cobol85Parser(stream)
                parser.buildParseTrees = True
                tree = parser.startRule()

                visitor = MyCobol85Visitor(parser)
                tree.accept(visitor)

        statements_dict = visitor.statements

        statements = []
        for statement_dict in statements_dict:
            statement = IBMStatementFactory.from_dict(statement_dict)
            statements.append(statement)

        imported_copybooks = [
            copybook.copybook_name for copybook in visitor.copybook_list
        ]

        dependency_list = [
            dependency
            for file_id, dependency in dependency_map.items()
            if file_id in imported_copybooks
        ]

        parsed_program = ParsedProgramAntlr(
            program_id=visitor.program_id,
            copybook_list=visitor.copybook_list,
            file_control_list=visitor.file_control_list,
            file_description_list=visitor.file_description_list,
            variable_list=visitor.variable_list,
            copybook_dependencies=dependency_list,
            statements=statements,
            paragraph_list=visitor.paragraph_list,
        )

        return parsed_program
    except Exception as e:
        logger.error(f"Error parsing COBOL code: {e}")
        # raise e
        return parsed_program


def preprocess_cobol_unisys(code: str) -> str:
    L = 72  # lenght of COBOL Unisys terminal
    i = 0
    # Regex to detect the line number at the beginning of each line (e.g., 000100)
    # Find position of line start with
    code = code.replace("\u001E", "<RS>")  # change the token
    lines = code.splitlines()
    pattern = re.compile(
        r"^.{7}IDENTIFICATION\s*DIVISION.|^.{7}ID\s*DIVISION.|^.{8}IDENTIFICATION\s*DIVISION.|^.{8}ID\s*DIVISION."
    )

    for i, line in enumerate(lines):
        if pattern.search(line):
            break
        if i > 100:
            break
    if i <= 100:
        # Delete all file before
        code = "\n".join(lines[i:])

    # Store unwanted characters after the code line
    pattern = re.compile(
        r"^\d{6}$|^\d{2}/\d{2}/\d{2}$|^[^\s]{8}$|^[^\s]{7}$|^\d{6}\s[A-Z]$"
    )
    extracted_numbers = set()
    for line in lines:
        if len(line) >= 70:
            candidate = line[L:80].strip()
            if pattern.match(candidate):
                extracted_numbers.add(candidate)

    code = re.sub(r"^.{6}", "      ", code, flags=re.MULTILINE)
    code = re.sub(r"^.{6}\/", "      *", code, flags=re.MULTILINE)
    code = re.sub(r"^\s{7}\*", "      **", code, flags=re.MULTILINE)
    code = re.sub(r"\*>.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^\s*\\.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"\d{6}[A-Za-z]{2}", "        ", code, flags=re.MULTILINE)

    # Remove unwanted characters
    for num in extracted_numbers:
        code = code.replace(num, "")

    # Remove empty line, keep only 72 characters
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    code = code.replace("<RS>", "\u001E")  # restore token

    return code


def parse_cobol_unisys(
    code: str, dependency_map: dict[str, CopybookDependency]
) -> ParsedProgramAntlr:
    """Parse COBOL program using ANTLR4

    Args:
        code (str): The COBOL code
        dependency_map dict[str, CopybookDependency]: The dependency dictionary with keys are the file ID, values are dependency.
    Returns:
        ParsedProgramAntlr: Parsed COBOL code
    """
    try:
        with open(os.devnull, "w", encoding="utf-8") as devnull:
            with redirect_stdout(devnull), redirect_stderr(devnull):
                code = "\n".join(code.splitlines())
                clean_code = preprocess_cobol_unisys(code)
                stream = CommonTokenStream(CobolUnisysLexer(InputStream(clean_code)))
                stream.fill()

                parser = CobolUnisysParser(stream)
                parser.buildParseTrees = True
                tree = parser.startRule()

                visitor = DaikyoUnisysCobolVistor(parser)
                tree.accept(visitor)

        statements_dict = visitor.statements

        statements = []
        for statement_dict in statements_dict:
            statement = UnisysStatementFactory.from_dict(statement_dict)
            statements.append(statement)

        imported_copybooks = [
            copybook.copybook_name for copybook in visitor.copybook_list
        ]

        dependency_list = [
            dependency
            for file_id, dependency in dependency_map.items()
            if file_id in imported_copybooks
        ]

        parsed_program = ParsedProgramAntlr(
            program_id=visitor.program_id,
            copybook_list=visitor.copybook_list,
            file_control_list=visitor.file_control_list,
            file_description_list=visitor.file_description_list,
            variable_list=visitor.variable_list,
            copybook_dependencies=dependency_list,
            statements=statements,
            paragraph_list=visitor.paragraph_list,
        )

        return parsed_program
    except Exception as e:
        logger.error(f"Error parsing COBOL code: {e}")
        # raise e
        return parsed_program


def preprocess_dnp(code):
    L = 72  # lenght of COBOL terminal
    i = 0
    # Regex to detect the line number at the beginning of each line (e.g., 000100)
    # Find position of line start with
    code = code.replace("\u001E", "<RS>")  # change the token
    lines = code.splitlines()
    pattern = re.compile(
        r"^.{7}IDENTIFICATION\s*DIVISION.|^.{7}ID\s*DIVISION.|^.{8}IDENTIFICATION\s*DIVISION.|^.{8}ID\s*DIVISION."
    )

    for i, line in enumerate(lines):
        if pattern.search(line):
            break
        if i > 100:
            break
    if i <= 100:
        # Delete all file before
        code = "\n".join(lines[i:])

    # Store unwanted characters after the code line
    # pattern = re.compile(r"^\d{6}$|^\d{2}/\d{2}/\d{2}$|^[^\s]{8}$|^[^\s]{7}$|^\d{6}\s[A-Z]$")
    # extracted_numbers = set()
    # for line in lines:
    #     if len(line) >= 70:
    #         candidate = line[L:80].strip()
    #         if pattern.match(candidate):
    #             extracted_numbers.add(candidate)

    code = re.sub(r"^.{6}", "      ", code, flags=re.MULTILINE)
    code = re.sub(r"^.{6}\/", "      *", code, flags=re.MULTILINE)
    code = re.sub(r"^\s{7}\*", "      **", code, flags=re.MULTILINE)
    code = re.sub(r"\*>.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"^\s*\\.*$", "", code, flags=re.MULTILINE)
    code = re.sub(r"\d{6}[A-Za-z]{2}", "        ", code, flags=re.MULTILINE)

    # Remove unwanted characters
    # for num in extracted_numbers:
    #     code = code.replace(num, "")

    # Remove empty line, keep only 72 characters
    code = "\n".join([line for line in code.splitlines() if line.strip()])
    code = code.replace("<RS>", "\u001E")  # restore token

    return code


def parse_cobol_dnp(code: str, dependency_map: dict[str, CopybookDependency]):
    """Parse COBOL program using ANTLR4 for DNP system

    Args:
        code (str): The COBOL code
        dependency_map dict[str, CopybookDependency]: The dependency dictionary with keys are the file ID, values are dependency.
    """
    code = "\n".join(code.splitlines())
    clean_code = preprocess_dnp(code)
    with open(os.devnull, "w", encoding="utf-8") as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            stream = CommonTokenStream(DNPLexer(InputStream(clean_code)))
            stream.fill()

            parser = DNPParser(stream)
            parser.buildParseTrees = True
            tree = parser.startRule()

            visitor = DNPVisitorImp(parser)
            tree.accept(visitor)

    statements_dict = visitor.statements

    statements = []
    for statement_dict in statements_dict:
        statement = DNPStatementFactory.from_dict(statement_dict)
        statements.append(statement)

    imported_copybooks = [copybook.copybook_name for copybook in visitor.copybook_list]

    dependency_list = [
        dependency
        for file_id, dependency in dependency_map.items()
        if file_id in imported_copybooks
    ]

    parsed_program = ParsedProgramAntlr(
        program_id=visitor.program_id,
        copybook_list=visitor.copybook_list,
        file_control_list=visitor.file_control_list,
        file_description_list=visitor.file_description_list,
        variable_list=visitor.variable_list,
        copybook_dependencies=dependency_list,
        statements=statements,
        paragraph_list=visitor.paragraph_list,
    )

    return parsed_program


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
    summarization: str
    io_table: List[IOItem]


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


class CopyGraphItem(BaseModel):
    index: int
    program_id: str
    program_type: str
    program_name: str
    call_type: str
    notes: str
    locations: str = ""


class ReferencesSubCommand(BaseModel):
    command: str
    explain: str


class ReferencesCommand(ReferencesSubCommand):
    subcommands: List[ReferencesSubCommand]


class CopyGraph(BaseModel):
    programs: List[CopyGraphItem]
    details: List[str]


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
            # print(io)
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

        dtype = (
            "String"
            if io.get("property") == "X"
            else "Int" if io.get("property") else ""
        )
        desc["Data type"] = dtype

        desc["Default value"] = io.get("default value", "")
        desc["Remarks"] = (
            "Java DTO class equivalence"
            if level == 1
            else "Java " + dtype + " data type equivalence"
        )

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

    def __summarize_procedure_div(self, llm):
        messages = [
            SystemMessage(
                content="Act as a COBOL expert. Your task is to provide a short, clear, and logical summary of the main flow of COBOL code sections. You will be given either a section of COBOL source code or a set of summaries. Based on the input, please produce a concise and logical summary that clearly indicates the function of the COBOL code, including specific table names if applicable."
            ),
            HumanMessage(
                content=self.parsed_data["divisionContentMap"]["procedureDivision"]
            ),
        ]
        response = llm.invoke(messages)
        return response.content

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
        self, list_program_name=None
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

    def extract_overview(self, llm):
        self.overview = OverviewProgram(
            programe_name=self.parsed_data["analysisMap"]["ProgramID"],
            io_files=[],
            db_accesses=self.parsed_data["analysisMap"]["sqlActionList"].keys(),
            copy_files=list(self.parsed_data["copyLocFileMap"].values()),
            call_files=list(self.parsed_data["callLocFileMap"].values()),
            summarization=self.__summarize_procedure_div(llm),
            # summarization="",
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

    def extract_process_logic(self, llm):
        """Extract and analyze the logic of each paragraph in the COBOL program.

        Args:
            llm: Language model with structured output capability

        Returns:
            dict: Analyzed paragraph logic with metadata
        """
        process_logic = {"paragraph_level": {}}
        structured_llm = llm.with_structured_output(ParagraphOutput)

        # Process each paragraph
        for paragraph in self.parsed_data["paragraph_list"]:
            paragraph_name = paragraph["paragraph_name"]
            paragraph_code = paragraph["paragraph_code"]

            # Analyze paragraph logic using LLM
            prompt = INSTRUCTION.format(CODE=paragraph_code)
            output = structured_llm.invoke(prompt)

            # Build paragraph metadata
            process_logic["paragraph_level"][paragraph_name] = {
                "paragraph_name": paragraph_name,
                "section": paragraph["section"],
                "paragraph_code": paragraph_code,
                "paragraph_lines": paragraph["paragraph_lines"],
                "ref_paragraphs": paragraph["ref_paragraphs"],
                "paragraph_logic": output.paragraph_summary,
            }

        self.process_logic = process_logic
        return process_logic

    def extract_statement_logic(self, llm):
        process_logic_explained = {}
        structed_llm = llm.with_structured_output(ParagraphOutput)
        self.process_logic = self.parsed_data["statements"]
        for statement in self.process_logic:
            key = statement["statement_name"]
            value = statement["statement_code"]
            prompt = INSTRUCTION.format(CODE=value)
            output = structed_llm.invoke(prompt)
            process_logic_explained[key] = output.paragraph_summary
        self.process_logic = process_logic_explained
        return self.process_logic

    def extact_copy_graph(self):
        # https://dev.azure.com/azurefsoft062/COBOL-migration/_git/research_cobol?path=/GenTemplates_2.py&version=GBmaster&line=2055&lineEnd=2082&lineStartColumn=5&lineEndColumn=30&lineStyle=plain&_a=contents
        # TODO: copy_graph and details
        self.copy_graph = CopyGraph(
            programs=self.__extract_copy_graph_items(), details=[""]
        )
        return self.copy_graph

    def extract_all(self, llm):
        self.extract_overview(llm)
        self.extract_io_params_def()
        self.extract_process_logic(llm)
        self.extact_copy_graph()
