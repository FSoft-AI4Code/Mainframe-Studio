import re
from enum import Enum
from xml.etree import ElementTree

import sqlglot
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_ibm_cobol_lexer import IBMCOBOLLexer, IBMCOBOLStyle


class FileType(str, Enum):
    """Enumeration of file types for mainframe migration."""

    COBOL = "COBOL"
    PLI = "PLI"
    CSD = "CSD"
    DB = "DB"
    COPY = "COPY"
    JCL_IBM = "JCL_IBM"
    JCL_FUJITSU = "JCL_FUJITSU"
    SQL = "SQL"
    BMS = "BMS"
    OTHER = "OTHER"
    UTILITY = "UTILITY"
    LDL = "LDL"
    DASDL = "DASDL"
    WFL = "WFL"


class SystemType(str, Enum):
    """Enumeration of mainframe system types."""

    IBM = "IBM"
    UNISYS = "UNISYS"
    DNP = "DNP"


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

    def is_cobol(self, code: str) -> bool:
        """Detect whether the code is COBOL program

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a COBOL program, False otherwise
        """
        preprocess_cobol = self.preprocess_cobol(code)

        lines = preprocess_cobol.splitlines()

        found_procedure_division = False
        found_screen_section = False

        for line in lines:
            line = line.strip()

            if re.search(
                r"(^\s*procedure\s+division\s*)\.?", line, re.IGNORECASE
            ) and not line.startswith("*"):
                found_procedure_division = True

            if re.match(
                r"^([0-9]*)?(\s*screen\s+section\s*)\.", line, re.IGNORECASE
            ) and not line.startswith("*"):
                found_screen_section = True

        if found_procedure_division and not found_screen_section:
            return True

        return False

    def is_copy(self, code: str, encoding: str) -> bool:
        """Detect whether the code is a COBOL copybook.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a copybook, False otherwise
        """

        preprocess_cobol = self.preprocess_cobol(code)

        pattern = re.compile(
            r"^\s*(\d{2})\s+([a-zA-Z][a-zA-Z0-9\-]+|[A-Za-z0-9\-!@#$%^&*()_=+;:{}\[\],\.|]+)(\s+(COMP\s+)?(PICTURE|PIC|REDEFINES))?",
            re.IGNORECASE,
        )

        for line in preprocess_cobol.splitlines():
            if pattern.search(line):
                return True

        html = cobol_to_html(preprocess_cobol, encoding=encoding)
        html = BeautifulSoup(html, "html.parser")

        err_element = html.find("span", {"class": "err"})

        if not err_element:
            return True

        return False

    def preprocess_cobol(self, code: str) -> str:
        lines = code.splitlines()

        for i, line in enumerate(lines):
            lines[i] = " " * 6 + line[6:]

        return "\n".join(lines)

    def is_jcl_ibm(self, code: str) -> bool:
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
        return False

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

    def is_wfl(self, code: str) -> bool:
        """Detect whether the code is a WFL program.

        Args:
            code (str): The code to be classified

        Returns:
            bool: True if the code is a WFL program, False otherwise
        """

        pattern = r"BEGIN\s+JOB"

        return re.search(pattern, code, re.I | re.M) is not None

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

        is_jcl_ibm = self.is_jcl_ibm(code)
        if is_jcl_ibm:
            return FileType.JCL_IBM

        is_bms = self.is_bms(code)
        if is_bms:
            return FileType.BMS

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
