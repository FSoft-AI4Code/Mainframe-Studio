import ast
import os
import re
import time
from contextlib import redirect_stderr, redirect_stdout
from typing import Any

from antlr4 import CommonTokenStream, InputStream
from loguru import logger
from pydantic import BaseModel, SerializeAsAny

from assessor.assessor import count_line
from parsers.grammar.common.base_cobol_schemas import CodeBlock
from parsers.grammar.ibm_jcl.IBM_JCLLexer import IBM_JCLLexer
from parsers.grammar.ibm_jcl.IBM_JCLParser import IBM_JCLParser
from parsers.grammar.ibm_jcl.jcl_schema import ExecStatement, JclStatement
from parsers.grammar.ibm_jcl.MyIBM_JCLVisitor import MyIBM_JCLVisitor
from schema.reverse_engineering import ReverseEngineeringStatus, ReverseEngineeringUpdate


class ParsedJCLAntlr(BaseModel):
    job: str
    VG_JCL: float
    is_vsam: bool
    params_list: list[str]
    dataset_list: list[dict[str, Any]]
    exec_statement_list: list[CodeBlock]
    job_statement_list: list[CodeBlock]
    proc_statement_list: list[CodeBlock]
    jcl_lib_statement_list: list[CodeBlock]
    set_statement_list: list[CodeBlock]
    exec_statement_map: dict[str, ExecStatement]
    statement_list: SerializeAsAny[list[JclStatement]]

    def __init__(self, **kwargs):
        # deserialize statement_list and exec_statement_map to appropriate objects

        for index in range(len(kwargs["statement_list"])):
            current_statement = kwargs["statement_list"][index]
            if isinstance(current_statement, dict):
                statement_tag = current_statement["tag"]
                for name, subclass in JclStatement.subclass_registry().items():
                    registry_tag = subclass.model_fields["tag"].default
                    if statement_tag == registry_tag:
                        current_statement = subclass(**current_statement)
                        break
                kwargs["statement_list"][index] = current_statement

        for key, value in list(kwargs["exec_statement_map"].items()):
            if isinstance(value, dict):
                kwargs["exec_statement_map"][key] = ExecStatement(**value)

        super().__init__(**kwargs)


def reverse_jcl(name, parsed_data, line_of_code):

    try:
        job_statement = parsed_data["job_statement_list"][0]["content"]

        patterns = {
            "class": re.compile(r"CLASS=([A-Z])"),
            "msgclass": re.compile(r"MSGCLASS=([A-Z])"),
            "notify": re.compile(r"NOTIFY=(&SYSUID)"),
            "time": re.compile(r"TIME=([0-9]+)"),
        }

        # Extract values
        extracted_values = {}
        for key, pattern in patterns.items():
            match = pattern.search(job_statement)
            extracted_values[key] = match.group(1) if match else None

        overview = {
            "job_name": name,
            "class": extracted_values["class"],
            "msgclass": extracted_values["msgclass"],
            "notify": extracted_values["notify"],
            "time": extracted_values["time"],
        }
    except Exception as e:
        logger.error(f"Reverse JCL with no job statement {name} - {e}")
        overview = {
            "job_name": name,
            "class": None,
            "msgclass": None,
            "notify": None,
            "time": None,
        }

    exec_statement_map = parsed_data["exec_statement_map"]
    steps = []
    for step_name, exec_statement in exec_statement_map.items():
        program_executed = exec_statement["parameters_map"].get("PGM")

        # dd_statements = []
        io_statements = []
        for statement in exec_statement["statements"]:
            # dd_statement = f"{statement['ddname']} DD "
            # for param, value in statement["parameters_map"].items():
            #     dd_statement += f"{param}={value},"
            # dd_statements.append(dd_statement)

            if statement["tag"] != "DdStatement":
                continue

            for ds in statement["dataset_map_list"]:
                io_statements.append(f"{statement['ddname']}: {ds['dd_statement']}\n")

        steps.append(
            {
                "step_name": step_name,
                "program_executed": program_executed,
                "dd_statement": exec_statement["statements"],
                "io_statements": io_statements,
            }
        )
    return {
        **parsed_data,
        "overview": overview,
        "step_list": steps,
        "line_of_code": line_of_code,
    }
def extract_dd_main_part(jcl_line):
    # Updated regex to handle DD name (e.g., SORTIN) with leading spaces and trailing comments
    match = re.match(r"^\s*//\s*([A-Z0-9]*)\s+DD\s+([^\n]+?)(?:\s+.*)?$", jcl_line.strip())
    
    if match:
        # Combine the DD name and the parameters to form the main part
        return f"//{match.group(1)}   DD {match.group(2).strip()}"
    else:
        return None  # No match found, return None
def extract_continue_main_part(jcl_line):
    match = re.match(r"^\s*//\s+([^\n]+?)(?:\s+.*)?$", jcl_line.strip())
    if match:
        return f"//        {match.group(1)}"

def preprocess_jcl(code: str) -> str:
    # Pattern matches everything from <== to end of line

    code = code.replace("\u001E", "<RS>") #change the token
    pattern = r'\s*<==.*$'
    L = 72
    code = "\n".join([line[:L] for line in code.splitlines() if line.strip()])
    lines = code.splitlines()
    for i, line in enumerate(lines):
        if "//" in line:
            break
        if i > 100:
            break
    if i <= 100:
    # Delete all file before
        code = "\n".join(lines[i:])
    # Process line by line and remove inline comments
    cleaned_lines = []
    for line in code.splitlines():
        cleaned_line = re.sub(pattern, '', line)
        cleaned_lines.append(cleaned_line)
    code = '\n'.join(cleaned_lines)
    code = "\n".join([line.rstrip() for line in code.splitlines() if line.strip()])
    code = code.replace("=(,","=(").replace("=(,","=(").replace("=(,","=(").replace("=(,","=(").replace("=(,","=(").replace("=(,","=(").replace("=(,","=(").replace("=(,","=(").replace("*************","")
    pattern = r',\n//\s+BLKSIZE='
    code = re.sub(pattern, ',BLKSIZE=', code)
    code = '\n'.join([line for line in code.splitlines() if not line == "//"])
    code = code.replace("", "")
    # Process DD without any parameters
    pattern = r"^//[^ \t\r\n/=,()*]*[ \t]+DD$"
    code = re.sub(pattern,"",code,flags=re.MULTILINE)
    code = '\n'.join([line.rstrip() for line in code.splitlines() if not line == "//" and not line == "////" and not line == "///" and not line == "/////" and line])
    lines = code.splitlines()
    for i,line in enumerate(lines):
        if " DD " in line:
            lines[i] = extract_dd_main_part(line) if extract_dd_main_part(line) else line
        elif line.startswith("//") and ("SPACE=" in line or "VOL=" in line or "DCB=" in line or "UNIT=" in line or "DISP=" in line or "LABEL=" in line) and " EXEC " not in line:
            lines[i] = extract_continue_main_part(line) if extract_continue_main_part(line) else line
        elif " EXEC " in line:
            lines[i] = re.sub(r"\s+[0-9]{2}/[0-9]{2}/[0-9]{2}$","", lines[i])
    code = '\n'.join(lines)
    code = code.replace("<RS>","\u001E") #restore token
    return code

def parse_jcl_antlr(code: str) -> ParsedJCLAntlr:
    """Parse IBM JCL using ANTLR4

    Args:
        code (str): The content of the file

    Returns:
        ParsedJCLAntlr: Parsed JCL
    """
    with open(os.devnull, "w", encoding="utf-8") as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            code = preprocess_jcl(code)
            stream = CommonTokenStream(IBM_JCLLexer(InputStream(code)))
            stream.fill()
            parser = IBM_JCLParser(stream)
            parser.buildParseTrees = True
            tree = parser.startRule()

            visitor = MyIBM_JCLVisitor(parser)
            tree.accept(visitor)

    parsed_jcl = ParsedJCLAntlr(
        job=visitor.job,
        VG_JCL=visitor.num_conditions,
        params_list=visitor.params_list,
        is_vsam=visitor.is_vsam,
        dataset_list=visitor.dataset_list,
        exec_statement_list=visitor.exec_statement_list,
        job_statement_list=visitor.job_statement_list,
        proc_statement_list=visitor.proc_statement_list,
        jcl_lib_statement_list=visitor.jcl_lib_statement_list,
        set_statement_list=visitor.set_statement_list,
        exec_statement_map=visitor.exec_statement_map,
        statement_list=visitor.statement_list,
    )

    return parsed_jcl


def parse_jcl(name: str, code: str) -> ReverseEngineeringUpdate:
    """Parse IBM JCL using ANTLR4

    Args:
        name (str): The name of the JCL file
        code (str): The content of the file

    Returns:
        ReverseEngineeringUpdate: Parsed JCL with status
    """
    try:
        parsed_jcl = parse_jcl_antlr(code)
        reversed_jcl = reverse_jcl(
            name, parsed_jcl.model_dump(), count_line(code, "JCL")[0]
        )
        return ReverseEngineeringUpdate(
            name=name,
            output=reversed_jcl, 
            type="JCL", 
            status=ReverseEngineeringStatus.PARSED
        )
    except Exception as e:
        logger.error(f"Error parsing JCL {name}: {e}", exc_info=True, stack_info=True)
        return ReverseEngineeringUpdate(
            name=name,
            type="JCL",
            status=ReverseEngineeringStatus.PARSED_ERROR
        )
