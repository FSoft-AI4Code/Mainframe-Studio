import os
from contextlib import redirect_stdout, redirect_stderr

from pydantic import BaseModel
from antlr4 import CommonTokenStream, InputStream

from ..grammar.ibm_jcl.IBM_JCLLexer import IBM_JCLLexer
from ..grammar.ibm_jcl.IBM_JCLParser import IBM_JCLParser
from ..grammar.ibm_jcl.MyIBM_JCLVisitor import MyIBM_JCLVisitor
from ..grammar.ibm_jcl.jcl_schema import ExecStatement
from ..utils import CodeBlock


class ParsedJCLAntlr(BaseModel):
    VG_JCL: float
    is_vsam: bool
    params_list: list[str]
    dataset_list: list[dict[str, str]]
    exec_statement_list: list[CodeBlock]
    job_statement_list: list[CodeBlock]
    proc_statement_list: list[CodeBlock]
    jcl_lib_statement_list: list[CodeBlock]
    set_statement_list: list[CodeBlock]
    exec_statement_map: dict[str, ExecStatement]


def parse_jcl_antlr(code: str) -> ParsedJCLAntlr:
    """Parse IBM JCL using ANTLR4

    Args:
        code (str): The content of the file

    Returns:
        ParsedJCLAntlr: Parsed JCL
    """
    with open(os.devnull, 'w', encoding='utf-8') as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            stream = CommonTokenStream(IBM_JCLLexer(InputStream(code)))
            stream.fill()
            parser = IBM_JCLParser(stream)
            parser.buildParseTrees = True
            tree = parser.program()

            visitor = MyIBM_JCLVisitor(parser)
            tree.accept(visitor)

    parsed_jcl = ParsedJCLAntlr(
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
    )

    return parsed_jcl
