import os
import re
from math import floor
from xml.etree import ElementTree

import sqlglot
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_ibm_cobol_lexer import IBMCOBOLLexer, IBMCOBOLStyle

from app.constants.cobol import FileType, SystemType


def cobol_to_html(cobol, encoding="cp1252"):
    """A utility function that converts the COBOL code to HTML by using a lexer.

    Args:
        cobol (str): COBOL code
        encoding (str, optional): Encoding of the code. Defaults to 'cp1252'

    Returns:
        str: Highlighted COBOL code in HTML format
    """

    return highlight(
        cobol,
        IBMCOBOLLexer(encoding=encoding),
        HtmlFormatter(style=IBMCOBOLStyle, full=True),
    )


class RuleBasedTextClassifier:
    """A rule-based code classifier."""

    def __init__(self):
        pass

    def detect_cobol(self, code: str) -> bool:
        """Detect whether the code is COBOL program

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a COBOL program, False otherwise
        """

        lines = code.splitlines()

        found_procedure_division = False
        found_screen_section = False

        for line in lines:
            line = line.strip()

            if re.search(
                r"(\s*procedure\s+division\s*)\.?", line, re.IGNORECASE
            ) and not line.startswith("*"):
                found_procedure_division = True

            if re.match(
                r"^([0-9]*)?(\s*screen\s+section\s*)\.", line, re.IGNORECASE
            ) and not line.startswith("*"):
                found_screen_section = True

        if found_procedure_division and not found_screen_section:
            return True

        return False

    def detect_screen(self, code: str) -> bool:
        """Detect whether the code is COBOL screen program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a COBOL screen program, False otherwise
        """
        lines = code.splitlines()

        found_procedure_division = False
        found_screen_section = False

        for line in lines:
            line = line.strip()

            if found_procedure_division and found_screen_section:
                return True

            # DFHM files do not have procedure division and screen section
            if not found_procedure_division and not found_screen_section:
                if re.match(
                    r"^([A-Za-z]+[0-9]*){1}\s+DFHM\w{2}\s+(\w+=.+,?)+",
                    line,
                    re.IGNORECASE,
                ):
                    return True

            if (
                not found_procedure_division
                and re.search(r"(\s*procedure\s+division\s*)\.?", line, re.IGNORECASE)
                and not line.startswith("*")
            ):
                found_procedure_division = True

            if (
                not found_screen_section
                and re.search(
                    r"^([0-9]*)?(\s*screen\s+section\s*)\.", line, re.IGNORECASE
                )
                and not line.startswith("*")
            ):
                found_screen_section = True
        else:
            return False

    def detect_jcl_ibm(self, code: str) -> bool:
        """Detect whether the code is JCL code used on IBM mainframe.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is JCL code used on IBM mainframe, False otherwise
        """
        lines = code.splitlines()

        ibm_regex = r"//\w*\s+(JOB|SET|DD|EXEC|JCLLIB|INCLUDE|STEPLIB|PROC)\s+.+"

        for line in lines:
            line = line.strip()
            if re.match(ibm_regex, line):
                return True
        else:
            return False

    def detect_jcl_fujitsu(self, code: str) -> bool:
        """Detect whether the code is JCL code used on Fujitsu mainframe.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is JCL code used on Fujitsu mainframe, False otherwise
        """
        lines = code.splitlines()

        fujitsu_regex = r"\\\w*\s+(FD|EX|PARA|)\s+(([a-zA-Z0-9]+)(=[a-zA-Z0-9]+)?(,)?)+"

        for line in lines:
            line = line.strip()
            if re.match(fujitsu_regex, line):
                return True
        else:
            return False

    def detect_copy(self, code: str, code_encoding: str) -> bool:
        """Detect whether the code is a COBOL copybook.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a copybook, False otherwise
        """
        lines = code.splitlines()
        not_comments = []

        # filter comments
        for line in lines:
            if "*" not in line:
                line = line.replace("\t", " ")
                not_comments.append(line)

        content = "\n".join(not_comments)

        html = cobol_to_html(content, encoding=code_encoding)
        html = BeautifulSoup(html, "html.parser")

        err_element = html.find("span", {"class": "err"})

        return True if not err_element else False

    def detect_sql(self, code: str) -> bool:
        """Detect whether the code is pure SQL.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is SQL, False otherwise
        """
        try:
            # TODO parser does not throw exception when transpiling non-sql code
            sqlglot.transpile(code)
            return True

        except Exception as e:
            return False

    def detect_db(self, code: str) -> bool:
        """Detect whether the code is the database code. The database code includes the SQL table declarations and the corresponding COBOL variable declarations.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is the database code, False otherwise
        """
        lines = code.splitlines()

        for line in lines:
            if re.search(
                r"exec sql declare\s+\w+(.\w+)*\s+table", line, re.IGNORECASE
            ) and not line.startswith("*"):
                return True
        else:
            return False

    def detect_bms(self, code: str) -> bool:
        """Detect whether the code is a COBOL BMS (Basic Mapping Support) program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a COBOL BMS program, False otherwise
        """
        lines = code.splitlines()
        found_bms_section = False
        for line in lines:
            line = line.strip()
            if re.search(r"\s*DFHMSD", line, re.IGNORECASE):
                found_bms_section = True
            if found_bms_section and re.search(r"\s*DFHMDI", line, re.IGNORECASE):
                return True
        return False

    def detect_pli(self, code: str) -> bool:
        """Detect whether the code is PL/I code.
        Args:
            code (str): The code to be classified
        Returns:
            bool: True if the code is PL/I code, False otherwise
        """
        preprocessed_code = re.sub(
            r"(\s+)$", "", code, flags=re.MULTILINE | re.IGNORECASE
        )  # remove trailing space
        preprocessed_code = re.sub(
            r"(\d+)$", "", preprocessed_code, flags=re.MULTILINE | re.IGNORECASE
        )  # remove trailing line number
        preprocessed_code = re.sub(
            r"\/\*([\s\S]+?)\*\/", "", preprocessed_code, flags=re.IGNORECASE
        )  # remove comments

        pli_variable_declaration_regex = r"DCL\s+\d+\s+[A-Za-z0-9\_\@]+"
        pli_procedure_regex = r"([A-Za-z0-9\_]+)[\s\n]*:[\s\n]*PROC[\s\n]*([^;]+?);"
        if re.search(
            pli_variable_declaration_regex, preprocessed_code, flags=re.IGNORECASE
        ):
            return True

        if re.search(
            pli_procedure_regex,
            preprocessed_code,
            flags=re.IGNORECASE,
        ):
            return True

        return False

    def detect_csd(self, code: str) -> bool:
        """Detect whether the code is a CICS System Definition (CSD) file.
        Args:
            code (str): The code to be classified
        Returns:
            bool: True if the code is a CSD file, False otherwise
        """
        define_properties = [
            "FILE",
            "GROUP",
            "RLSACCESS",
            "READINTEG",
            "DSNSHARING",
            "STRINGS",
            "STATUS",
            "OPENTIME",
            "DISPOSITION",
            "DATABUFFERS",
            "INDEXBUFFERS",
            "TABLE",
            "MAXNUMRECS",
            "UPDATEMODEL",
            "LOAD",
            "RECORDFORMAT",
            "ADD",
            "BROWSE",
            "DELETE",
            "READ",
            "UPDATE",
            "JOURNAL",
            "JNLREAD",
            "JNLSYNCREAD",
            "JNLUPDATE",
            "JNLADD",
            "JNLSYNCWRITE",
            "RECOVERY",
            "FWDRECOVLOG",
            "BACKUPTYPE",
            "DEFINETIME",
            "CHANGETIME",
            "CHANGEUSRID",
            "CHANGEAGENT",
            "CHANGEAGREL",
        ]

        delete_keywords = [
            "FILE",
            "MAPSET",
            "GROUP",
            "PROGRAM",
            "TRANSACTION",
            "LIBRARY",
            "TDQUEUE",
        ]

        define_regex = re.compile(
            rf"DEFINE\s+(({'|'.join([keyword for keyword in define_properties])})\s*(\([A-Z0-9\.]+\))\s*)+"
        )

        delete_regex = re.compile(
            rf"DELETE\s+(({'|'.join([keyword for keyword in delete_keywords])})\s*(\([A-Z0-9\.]+\))\s*)+"
        )

        if define_regex.search(code, re.IGNORECASE) or delete_regex.search(
            code, re.IGNORECASE
        ):
            return True

        return False

    def detect(self, code: str, code_encoding: str) -> str:
        """Classify the code to supported types.

        Args:
            code (str): The code to be classified
            code_encoding (str): The encoding of the code

        Returns:
            str: The type of classified code.
        """
        if len(code.strip()) == 0:
            return "OTHER"

        is_bms = self.detect_bms(code)
        if is_bms:
            return "BMS"

        is_pli = self.detect_pli(code)
        if is_pli:
            return "PLI"

        is_jcl_ibm = self.detect_jcl_ibm(code)
        if is_jcl_ibm:
            return "JCL_IBM"

        is_jcl_fujitsu = self.detect_jcl_fujitsu(code)
        if is_jcl_fujitsu:
            return "JCL_FUJITSU"

        is_csd = self.detect_csd(code)
        if is_csd:
            return "CSD"

        is_screen = self.detect_screen(code)
        if is_screen:
            return "SCREEN"

        is_cobol = self.detect_cobol(code)
        if is_cobol:
            return "COBOL"

        is_copy = self.detect_copy(code, code_encoding)
        if is_copy:
            is_db = self.detect_db(code)

            if is_db:
                return "DB"

            return "COPY"

        is_sql = self.detect_sql(code)
        if is_sql:
            return "SQL"

        return "OTHER"


class RuleBasedTextClassifierBySystem:
    """A rule-based code classifier based on the mainframe system type."""

    def __init__(self):
        """Initialize the classifier and load COBOL verbs."""
        # Load COBOL verbs from file
        self.cobol_verbs = set()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        verbs_file = os.path.join(project_root, "cobol_verbs.txt")

        try:
            with open(verbs_file, "r", encoding="utf-8") as f:
                self.cobol_verbs = {line.strip() for line in f if line.strip()}
        except FileNotFoundError:
            print(
                f"Warning: Could not load COBOL verbs file for classifier at path {verbs_file}, will skip checking COBOL verbs for Copybook detection."
            )

    def is_cobol(self, code: str) -> bool:
        """Detect whether the code is COBOL program

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a COBOL program, False otherwise
        """
        preprocess_cobol = self.preprocess_cobol(code)

        lines = preprocess_cobol.splitlines()

        for line in lines:
            if (
                re.search(
                    r"^[A-Za-z0-9\s]{6}[\s\*]\s*procedure\s+division(\s+using)?",
                    line,
                    re.IGNORECASE,
                )
                and line[6] != "*"
            ):
                return True

        return False
    
    def is_pli_copy(self, code: str) -> bool:
        """Detect whether the code is a PL/I copybook.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a PL/I copybook, False otherwise
        """
        pli_data_types = r"(CHAR|CHARACTER|BIN|BINARY|FIXED|DECIMAL|FLOAT|BIT|PTR|POINTER|OFFSET|REAL|COMPLEX|GRAPHIC|VARYING|NONVARYING)"
        
        pli_attributes = r"(ALIGNED|UNALIGNED|INITIAL|INIT|STATIC|AUTOMATIC|BASED|DEFINED|EXTERNAL|INTERNAL|LIKE|POSITION|PRECISION|REFER|VALUE)"

        pli_var_patterns = [
            # DCL/DECLARE variable declarations
            fr"^\s*DCL\s+([A-Za-z0-9_#@]+)(\s+{pli_data_types}|\s+{pli_attributes}|\([^)]+\)|\s*,)",
            fr"^\s*DECLARE\s+([A-Za-z0-9_#@]+)(\s+{pli_data_types}|\s+{pli_attributes}|\([^)]+\)|\s*,)",
            
            # Multi-line DCL with entries and comma continuations
            r"^\s*DCL\s+[A-Za-z0-9_#@]+\s+ENTRY(\s+OPTIONS\s*\([^)]+\))?\s*,",
            
            # Continuation lines with additional entries
            r"^\s*[A-Za-z0-9_#@]+\s+ENTRY(\s+OPTIONS\s*\([^)]+\))?\s*,",
            
            # Structured level declarations (like COBOL levels but with PL/I syntax)
            fr"^\s*(\d{{1,2}})\s+([A-Za-z0-9_#@]+)(\s+{pli_data_types}|\s+{pli_attributes}|\([^)]+\)|\s*,)",
            
            # Variables with attributes in parentheses (typical PL/I style)
            fr"^\s*([A-Za-z0-9_#@]+)\s+{pli_data_types}\s*\([^)]+\)(\s+{pli_attributes})?,",
            
            # Special case for PIC with quoted format strings 
            r"^\s*(\d{1,2})\s+([A-Za-z0-9_#@]+)\s+PIC\s*['\"][\(\)0-9A-Z]+['\"](\s*;)?,",
            
            # Variables with semicolons (characteristic of PL/I)
            fr"^\s*([A-Za-z0-9_#@]+)(\s+{pli_data_types}|\s+{pli_attributes}|\([^)]+\))\s*;"
        ]
        
        lines = code.splitlines()
        
        for line in lines:
            for pattern in pli_var_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    return True
        
        return False

    def is_copy(self, code: str, encoding: str) -> bool:
        """Detect whether the code is a COBOL copybook.

        Args:
            code (str): The code to be classified
            encoding (str): The encoding of the code

        Returns:
            bool: True if the code is a copybook, False otherwise
        """
        # preprocess_cobol = self.preprocess_cobol(code)
        lines = code.splitlines()
        
        column_pattern = r"^[A-Za-z0-9\s]{6}[\s\*]?"
        
        level_pattern = r"\s*(\b\d{2}\b)\s+"
        name_pattern = r"([a-zA-Z][a-zA-Z0-9\-_]+|[A-Za-z0-9\-!@#$%'\"^&*()_=+;:{}\[\],\.\|]{2,})"
        
        pic_clause = r"(PIC|PICTURE)\s+[X9AVS][X9AVS\(\)\.\+\-]*"
        comp_clause = r"COMP(\-[1-5])?"
        usage_clause = r"USAGE\s+(DISPLAY|COMP(\-[1-5])?|BINARY|PACKED-DECIMAL|INDEX)"
        redefines_clause = r"REDEFINES\s+[A-Za-z0-9\-]+"
        value_clause = r"VALUE\s+[\w\'\-\+]+"
        occurs_clause = r"OCCURS\s+\d+(\s+TIMES)?"
        data_clauses = f"({pic_clause}|{comp_clause}|{usage_clause}|{redefines_clause}|{value_clause}|{occurs_clause})"
        
        cobol_ibm_variable_pattern = fr"{column_pattern}({level_pattern}){name_pattern}(\s+{data_clauses})?\."

        html = cobol_to_html(code, encoding=encoding)
        html = BeautifulSoup(html, "html.parser")
        err_element = html.find("span", {"class": "err"})
        
        # Check for copybook field definitions
        for line in lines:
            if re.search(cobol_ibm_variable_pattern, line):
                return True

        THRESHOLD = 0.3

        # Check for COBOL verbs without procedure division
        if self.cobol_verbs:
            first_word_of_lines_in_code = set()
            for line in lines:
                line = line[6:]
                if not line.strip().startswith("*"):  # Skip comments
                    first_word_of_lines = re.findall(r"^\s*[A-Z0-9-]+\s", line.upper())
                    first_word_of_lines = {word.strip() for word in first_word_of_lines}
                    first_word_of_lines_in_code.update(first_word_of_lines)

            cobol_verbs_found = first_word_of_lines_in_code.intersection(
                self.cobol_verbs
            )

            # the number of cobol verbs found is greater than threshold-% of the total number of first word of lines
            if len(cobol_verbs_found) > floor(
                THRESHOLD * len(first_word_of_lines_in_code)
            ):
                return True
        else:
            if not err_element:
                return True

        return False

    def preprocess_cobol(self, code: str) -> str:
        lines = code.splitlines()

        for i, line in enumerate(lines):
            lines[i] = " " * 6 + line[6:72]

        return "\n".join(lines)
    
    def _is_match_jcl_function(self, code: str) -> bool:
        lines = code.splitlines()

        jcl_function_name = r"(EXEC|DD)"
        jcl_function_regex = rf"^//[^\*]+\s+{jcl_function_name}\s+"

        for line in lines:
            if re.search(jcl_function_regex, line):
                return True

        return False
    
    def _is_match_jcl_pattern(self, code: str) -> bool:
        lines = code.splitlines()

        ibm_regex = r"^//?[^\*]+\s+JOB\s+.+"
        
        for line in lines:
            if re.search(ibm_regex, line):
                return True
        
        return False

    def is_jcl_ibm(self, code: str) -> bool:
        """Detect whether the code is JCL code used on IBM mainframe.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is JCL code used on IBM mainframe, False otherwise
        """
        return self._is_match_jcl_pattern(code)
    
    def _is_match_proc_pattern(self, code: str) -> bool:
        lines = code.splitlines()

        proc_regex = r"^//[^\*]+\s+PROC\s+.+"
        
        for line in lines:
            if re.search(proc_regex, line):
                return True
        
        return False

    def is_proc(self, code: str) -> bool:
        """Detect whether the code is a PROC file.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a PROC file, False otherwise
        """
        return self._is_match_proc_pattern(code) and not self._is_match_easy_pattern(code)
        
    def is_bms(self, code: str) -> bool:
        """Detect whether the code is a COBOL BMS (Basic Mapping Support) program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a COBOL BMS program, False otherwise
        """
        lines = code.splitlines()
        found_bms_section = False
        for line in lines:
            line = line.strip()
            if re.search(r"\s*DFHMSD", line, re.IGNORECASE):
                found_bms_section = True
            if found_bms_section and re.search(r"\s*DFHMDI", line, re.IGNORECASE):
                return True
        return False
    
    def is_cics(self, code: str) -> bool:
        """Detect whether the code is a CICS program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a CICS program, False otherwise
        """
        lines = code.splitlines()

        for line in lines:
            if re.search(r"\s*\b(MFLD|DFLD)\b", line, re.IGNORECASE):
                return True
        return False

    def is_wfl(self, code: str) -> bool:
        """Detect whether the code is a WFL program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a WFL program, False otherwise
        """

        pattern = r"BEGIN\s+JOB"

        return re.search(pattern, code, re.I | re.M) is not None

    def is_asm(self, code: str) -> bool:
        """Detect whether the code is Assembly language.
        
        Args:
            code (str): The code to be classified
            
        Returns:
            bool: True if the code is Assembly language, False otherwise
        """
        # Common assembly directives and instructions
        asm_patterns = [
            r"^\s*[A-Z0-9@$#_]+\s+(DS|DC|EQU|CSECT|DSECT|USING|DROP|TITLE|START|END|LTORG|PRINT|ORG|COPY|SPACE|EJECT)\s+",
            r"^\s*[A-Z0-9@$#_]+\s+(L|LA|LR|ST|STM|LM|AR|SR|MR|DR|CR|BNE|BE|BL|BH|BC|BAL|BALR|BCT|AP|SP|MP|DP|CP|MVC|MVI|MVZ|MVN|CLC|CLI)\s+",
            r"^\s*\*\s+REGISTER\s+EQUATES",
            r"^\s*R\d{1,2}\s+EQU\s+\d{1,2}"
        ]
        
        lines = code.splitlines()
        asm_line_count = 0
        
        for line in lines:
            for pattern in asm_patterns:
                if re.match(pattern, line, re.IGNORECASE):
                    asm_line_count += 1
                    break
        
        # If we have at least 3 assembly lines, consider it an assembly file
        if asm_line_count >= 3:
            return True
            
        return False

    def is_ldl(self, code: str) -> bool:
        """Detect whether the code is a COBOL LDL program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a LDL program, False otherwise
        """
        try:
            xml_tree = ElementTree.fromstring(code)
            method_tag = xml_tree.find(".//METHOD[@Language='LDL']")
            return method_tag is not None
        except ElementTree.ParseError:
            return False

    def is_dasdl(self, code: str) -> bool:
        """Detect whether the code is a DASDL file.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a DASDL file, False otherwise
        """

        pattern = re.compile(
            r"[a-zA-Z0-9\-]+\s+(ALPHA|REAL|NUMBER)\s+\((\s|\d)+\)", re.IGNORECASE
        )

        for line in code.splitlines():
            if pattern.search(line):
                return True

        return False
    
    def is_a_auto(self, code: str) -> bool:
        pattern = r"^\s*NO.\s+JOB-CODE\s+D-ID\s+PREVIOUS-JOB-NO\s+      RERUN\s+MAX-CD\s+JOB-USERS-FD\s+\*\s+NOTES"
        lines = code.splitlines()
        
        for line in lines:
            if re.search(pattern, line):
                return True
        return False

    
    def is_panel(self, code: str) -> bool:
        attr_pattern = r".\s+TYPE\(\w+\)(\s+INTENS\(\w+\))?\s+COLOR\(\w+\)"
        if re.search(attr_pattern, code):
            return True
        
        header_pattern = r"^\)(ATTR|BODY|INIT|PROC)"
        lines = code.splitlines()
        for line in lines:
            if re.match(header_pattern, line):
                return True
        
        return False
    
    def _is_match_easy_pattern(self, code: str) -> bool:
        easy_patterns = [
            r"^\s*PARM\s+(SCANCOL|LINESIZ|SCANCOL|FILLCHAR)=\d+",
            r"^\s*LIST\s+OFF",
            r"^\s*LIST\s+ON",
            r"^\s*FILE\s+[A-Za-z0-9]+",
            r"^\s*JOB[\s\n]+[A-Za-z0-9]+",
        ]
        
        lines = code.splitlines()
        for line in lines:
            for easy_pattern in easy_patterns:
                if re.match(easy_pattern, line):
                    return True
        return False
    
    def is_easy(self, code: str) -> bool:
        return self._is_match_easy_pattern(code) and not self._is_match_jcl_pattern(code) and not self._is_match_proc_pattern(code) and not self._is_match_jcl_function(code)
        
    def is_pli(self, code: str) -> bool:
        """Detect whether the code is a PL/I program with a MAIN procedure.
        
        Args:
            code (str): The code to be classified
            
        Returns:
            bool: True if the code is a PL/I program with MAIN option, False otherwise
        """
        
        lines = code.splitlines()
        for i, line in enumerate(lines):
            lines[i] = line[:72]  # COBOL line length limit
        code = "\n".join(lines)
        
        pattern = r"[A-Za-z0-9_]+[\s\n]*:[\s\n]*PROC"
        if re.search(pattern, code, re.IGNORECASE):
            return True
                
        return False

    def is_ddl(self, code: str) -> bool:
        """Detect whether the code is a mainframe DDL (Data Definition Language) file.
        
        Args:
            code (str): The code to be classified
            
        Returns:
            bool: True if the code is a DDL file, False otherwise
        """
        ddl_patterns = [
            # CREATE TABLE statements
            r"CREATE\s+TABLE\s+[A-Z0-9_]+\s*\(",
            # CREATE INDEX statements
            r"CREATE\s+(UNIQUE\s+)?(INDEX|INDEXSPACE)\s+[A-Z0-9_]+",
            # ALTER TABLE statements 
            r"ALTER\s+TABLE\s+[A-Z0-9_\.]+\s+(ADD|ALTER|DROP)",
            # COMMENT ON statements
            r"COMMENT\s+ON\s+(TABLE|COLUMN)\s+[A-Z0-9_\.]+",
            # DB2 specific tablespace creation
            r"CREATE\s+(UNIQUE\s+)?TABLESPACE\s+[A-Z0-9_]+",
            # GRANT statements for DB permissions
            r"GRANT\s+[A-Z0-9_\s,]+\s+ON\s+[A-Z0-9_\.]+\s+TO\s+",
            # PRIMARY KEY constraints
            r"CONSTRAINT\s+[A-Z0-9_]+\s+PRIMARY\s+KEY",
            # FOREIGN KEY constraints
            r"FOREIGN\s+KEY\s*\([A-Z0-9_,\s]+\)\s*REFERENCES",
            # LABEL ON statements for DB2 column/table labels
            r"LABEL\s+ON\s+([A-Z0-9_\.]+|TABLE\s+[A-Z0-9_\.]+)",
            # LABEL ON statements followed by parenthesis
            r"LABEL\s+ON\s+[A-Z0-9_\.]+\s*\(",
            # Column IS patterns inside labels
            r"[A-Z0-9_]+\s+IS\s+('|\")[^'\"]+(\'|\")",
            # SELECT FROM statements (common in SQL files, views, or embedded in DDL)
            r"SELECT\s+.+\s+FROM\s+[A-Z0-9_\.]+(\s+WHERE|\s+GROUP\s+BY|\s+ORDER\s+BY|\s+HAVING|\s*;|\s+WITH|\s+UNION|\s+EXCEPT|\s+INTERSECT)?",
            # SET CURRENT SQLID statement (common in DB2 DDL scripts)
            r"SET\s+CURRENT\s+SQLID\s*=\s*('[A-Z0-9]+'|\w+)",
            # DROP TABLESPACE statement (common in DB2 DDL scripts)
            r"DROP\s+TABLESPACE\s+[A-Z0-9_\.]+",
            # DROP TABLE statement
            r"DROP\s+TABLE\s+[A-Z0-9_\.]+",
            # DROP INDEX statement
            r"DROP\s+INDEX\s+[A-Z0-9_\.]+",
            # COMMIT statement (often found in DDL scripts)
            r"COMMIT\s*;"
        ]
        
        lines = code.splitlines()
        joined_text = ' '.join(lines)  # Join for multi-line patterns
        
        # Directly check for SET CURRENT SQLID and DROP TABLESPACE, which are very specific to DB2 DDL
        sqlid_pattern = r"SET\s+CURRENT\s+SQLID\s*=\s*'[A-Z0-9]+';"
        drop_ts_pattern = r"DROP\s+TABLESPACE\s+[A-Z0-9_\.]+;"
        
        if re.search(sqlid_pattern, joined_text, re.IGNORECASE) or re.search(drop_ts_pattern, joined_text, re.IGNORECASE):
            return True
        
        for pattern in ddl_patterns:
            if re.search(pattern, joined_text, re.IGNORECASE):
                return True
        
        return False

    def is_report(self, code: str) -> bool:
        """Detect whether the code is Overlay Generation Language (OGL) program.
        
        Args:
            code (str): The code to be classified
            
        Returns:
            bool: True if the code is an OGL program, False otherwise
        """
        # Common OGL patterns and keywords
        ogl_patterns = [
            # SETTEXT, SETPRT and similar directives
            r"^\s*SETTEXT\s+",
            r"^\s*SETPRT\s+",
            r"^\s*OVERLAY\s+(\w+)\s+SIZE\s+(\d{4})\s+PELS\s+(\d{4})\s+PELS",
            # Common OGL commands/statements
            r"^\s*POSITION\s+ABSOLUTE",
            r"^\s*PAGEDEF\s+",
            r"^\s*FORMDEF\s+",
            r"^\s*SEGMENT\s+",
            r"^\s*DRAWB\s+",
            r"^\s*FIELD\s+",
            r"^\s*FONT\s+",
            r"^\s*LAYOUT\s+",
            # Page formatting directives
            r"^\s*PAGE\s+XSIZE\s*=",
            r"^\s*PAGE\s+YSIZE\s*=",
            r"^\s*DIRECTION\s+",
            # Common OGL field types and attributes
            r"^\s*BOX\s+",
            r"^\s*ENDFORM", 
            r"^\s*ENDPAGE",
            r"^\s*ENDSEG",
            # Form definition sections
        ]
        
        lines = code.splitlines()
        
        for line in lines:
            for pattern in ogl_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    return True
                    
        return False
    
    def is_clist(self, code: str) -> bool:
        """Detect whether the code is a CLIST (Command List) file.
        
        Args:
            code (str): The code to be classified
            
        Returns:
            bool: True if the code is a CLIST file, False otherwise
        """
        # Common CLIST patterns and commands
        clist_proc_patterns = r"^\s*PROC\s+\d+"
        clist_exit_patterns = r"^\s*EXIT"
        
        if re.search(clist_proc_patterns, code, re.IGNORECASE | re.MULTILINE) and re.search(clist_exit_patterns, code, re.IGNORECASE | re.MULTILINE):
            return True
        return False

    def is_csd(self, code: str) -> bool:
        """Detect whether the code is a CICS System Definition (CSD) file.
        
        Args:
            code (str): The code to be classified
            
        Returns:
            bool: True if the code is a CSD file, False otherwise
        """
        # Keywords and attributes commonly found in CSD files
        define_resource_types = [
            "PROGRAM", "TRANSACTION", "FILE", "MAPSET", "PARTITIONSET",
            "PROFILE", "JOURNALMODEL", "TYPETERM", "CONNECTION", "SESSION",
            "TDQUEUE", "LSRPOOL", "DB2CONN", "DB2ENTRY", "DB2TRAN", "DOCTEMPLATE",
            "REQUESTMODEL", "TCPIPSERVICE", "TSMODEL", "WEBSERVICE", "LIBRARY",
            "BUNDLE", "PIPELINE", "URIMAP", "XMLTRANSFORM", "CORBASERVER"
        ]

        define_attributes = [
            "GROUP", "DESCRIPTION", "STATUS", "RLSACCESS", "READINTEG", "DSNSHARING",
            "STRINGS", "OPENTIME", "DISPOSITION", "DATABUFFERS", "INDEXBUFFERS", 
            "TABLE", "MAXNUMRECS", "UPDATEMODEL", "LOAD", "RECORDFORMAT", "ADD",
            "BROWSE", "DELETE", "READ", "UPDATE", "JOURNAL", "JNLREAD", "JNLSYNCREAD", 
            "JNLUPDATE", "JNLADD", "JNLSYNCWRITE", "RECOVERY", "FWDRECOVLOG", 
            "BACKUPTYPE", "DEFINETIME", "CHANGETIME", "CHANGEUSRID", "CHANGEAGENT",
            "CHANGEAGREL", "LANGUAGE", "CEDFSTATUS", "DATALOCATION", "EXECKEY",
            "REMOTESYSTEM", "REMOTENAME", "TRANSID", "DYNAMIC", "RESIDENT", 
            "USAGE", "USELPACOPY", "OPERATION", "TERMINAL", "RESTART", "SECURITY",
            "PRIMEDSIZE", "REMOTESYSNET", "PROTOCOL", "CONNTYPE", "QUEUELIMIT"
        ]

        # Main command patterns
        csd_commands = [
            # DEFINE commands for various resource types
            r"DEFINE\s+({})\s*\([A-Z0-9_\.]+\)".format("|".join(define_resource_types)),
        ]
        
        for pattern in csd_commands:
            if re.search(pattern, code, re.IGNORECASE):
                return True
        
        return False

    def detect_ibm(self, code: str, encoding: str) -> FileType:
        """Classify the code to supported types in IBM system.

        Args:
            code (str): The code to be classified

        Returns:
            FileType: The type of classified code.
        """
        if len(code.strip()) == 0:
            return FileType.OTHER

        is_cobol = self.is_cobol(code)
        if is_cobol:
            return FileType.COBOL
        
        is_clist = self.is_clist(code)
        if is_clist:
            return FileType.CLIST
        
        is_jcl_ibm = self.is_jcl_ibm(code)
        if is_jcl_ibm:
            return FileType.JCL
        
        is_pli = self.is_pli(code)
        if is_pli:
            return FileType.PLI

        is_proc = self.is_proc(code)
        if is_proc:
            return FileType.PROC

        is_bms = self.is_bms(code)
        if is_bms:
            return FileType.BMS
        
        is_cics = self.is_cics(code)
        if is_cics:
            return FileType.CICS
        
        is_csd = self.is_csd(code)
        if is_csd:
            return FileType.CSD
        
        is_report = self.is_report(code)
        if is_report:
            return FileType.REPORT
        
        is_a_auto = self.is_a_auto(code)
        if is_a_auto:
            return FileType.A_AUTO
        
        is_easy = self.is_easy(code)
        if is_easy:
            return FileType.EASY

        is_panel = self.is_panel(code)
        if is_panel:
            return FileType.PANEL
        
        is_asm = self.is_asm(code)
        if is_asm:
            return FileType.ASM
        
        is_ddl = self.is_ddl(code)
        if is_ddl:
            return FileType.DDL

        is_report = self.is_report(code)
        if is_report:
            return FileType.REPORT
        
        is_pli_copy = self.is_pli_copy(code)
        if is_pli_copy:
            return FileType.PLI_COPY
        
        is_copy = self.is_copy(code, encoding)
        if is_copy:
            return FileType.COPY

        return FileType.OTHER

    def detect_unisys(self, code: str, encoding: str) -> FileType:
        """Classify the code to supported types in Unisys system.

        Args:
            code (str): The code to be classified

        Returns:
            FileType: The type of classified code.
        """
        if len(code.strip()) == 0:
            return FileType.OTHER

        is_cobol = self.is_cobol(code)
        if is_cobol:
            return FileType.COBOL

        is_wfl = self.is_wfl(code)
        if is_wfl:
            return FileType.WFL

        is_ldl = self.is_ldl(code)
        if is_ldl:
            return FileType.LDL

        is_dasdl = self.is_dasdl(code)
        if is_dasdl:
            return FileType.DASDL

        is_copy = self.is_copy(code, encoding)
        if is_copy:
            return FileType.COPY

        return FileType.OTHER

    def detect_dnp(self, code: str, encoding: str) -> FileType:
        """Classify the code to supported types in DNP system.

        Args:
            code (str): The code to be classified

        Returns:
            FileType: The type of classified code.
        """
        if len(code.strip()) == 0:
            return FileType.OTHER

        is_cobol = self.is_cobol(code)
        if is_cobol:
            return FileType.COBOL

        is_copy = self.is_copy(code, encoding)
        if is_copy:
            return FileType.COPY

        return FileType.OTHER

    def detect(self, code: str, encoding: str, system_type: SystemType) -> FileType:
        """Classify the code to supported types based on the system type.

        Args:
            code (str): The code to be classified
            system_type (SystemType): The system type of the code

        Returns:
            FileType: The type of classified code.
        """

        match system_type:
            case SystemType.IBM:
                return self.detect_ibm(code, encoding)
            case SystemType.UNISYS:
                return self.detect_unisys(code, encoding)
            case SystemType.DNP:
                return self.detect_dnp(code, encoding)

        raise ValueError(f"Unsupported system type: '{system_type}'")
