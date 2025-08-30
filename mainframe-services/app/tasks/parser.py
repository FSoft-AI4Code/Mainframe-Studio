import os
import re
import uuid
import subprocess
import json
import math
import itertools
from typing import List, Dict, Optional

from loguru import logger
from pydantic import BaseModel

from .reverse.copy import COPY_TEMPLATE


def replace_colons_in_pattern(text):
    """
    Replaces colons in specific patterns with the word "COLON".

    Args:
    - text (str): The input text where replacements are to be made.

    Returns:
    - str: The modified text with replacements.
    """
    # Regex to find the pattern :XYZ: (where XYZ is any text), not part of another word or inside quotes
    pattern = r'(?<![\w"\'`]):([^:]+):(?![\w"\'`])'

    # Function to replace the colons with the word "COLON"
    def replace_with_colon(match):
        return f"COL{match.group(1)}COL"

    # Replace the pattern in the text
    modified_text = re.sub(pattern, replace_with_colon, text)

    return modified_text


def clean_code(input_text):
    lines = input_text.splitlines()
    cleaned_lines = []
    pattern = re.compile(r"^\d+\s*")
    for line in lines:
        new_line = pattern.sub(lambda m: " " * len(m.group(0)), line)
        cleaned_lines.append(new_line)

    # Join the cleaned lines back into a single string
    cleaned_output = "\n".join(cleaned_lines)
    return cleaned_output


def comment_specific_lines(code: str) -> str:
    # Split the code into lines
    lines = code.splitlines()
    for i, line in enumerate(lines):
        # Remove comments from the line
        if "*>" in line:
            line = line.split("*>")[0].rstrip()

        # Check for @OPTIONS and modify the line accordingly
        if line.strip().startswith("@OPTIONS"):
            line = line[:6] + "*" + line[6:].lstrip()

        # Truncate the line to 72 characters
        lines[i] = line[:72].rstrip()
        if line.strip().startswith("*"):
            lines[i] = ""

    # Join the lines back into a single string
    return "\n".join(lines)


def read_file(file_path: str):
    try:
        with open(file_path, "r", encoding="shift_jis") as f:
            content = clean_code(f.read())
            content = comment_specific_lines(content)
            return content
    except UnicodeDecodeError:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = clean_code(f.read())
                content = comment_specific_lines(content)
                return content
        except Exception as e:
            logger.error(
                f"Error reading file {file_path} with UTF-8 encoding: {e}")
    except Exception as e:
        logger.error(f"Error to parse file {file_path} {e}")


def format_data(data):
    """
    Recursively formats the given data by replacing spaces in the keys with underscores.

    Args:
        data (dict): The data to be formatted.

    Returns:
        dict: The formatted data.
    """
    formatted_data = {}
    for key, value in data.items():
        formatted_key = key.replace(" ", "_")
        if isinstance(value, dict):
            formatted_data[formatted_key] = format_data(value)
        elif isinstance(value, list):
            formatted_list = []
            for item in value:
                if isinstance(item, dict):
                    formatted_list.append(format_data(item))
                else:
                    formatted_list.append(item)
            formatted_data[formatted_key] = formatted_list
        else:
            formatted_data[formatted_key] = value
    return formatted_data


def replace_colons_in_pattern(text):
    """
    Replaces colons in specific patterns with the word "COLON".

    Args:
    - text (str): The input text where replacements are to be made.

    Returns:
    - str: The modified text with replacements.
    """
    # Regex to find the pattern :XYZ: (where XYZ is any text), not part of another word or inside quotes
    pattern = r'(?<![\w"\'`]):([^:]+):(?![\w"\'`])'

    # Function to replace the colons with the word "COLON"
    def replace_with_colon(match):
        return f"COL{match.group(1)}COL"

    # Replace the pattern in the text
    modified_text = re.sub(pattern, replace_with_colon, text)

    return modified_text


def find_copy_statements(lines: List[str]) -> List[str]:
    """Find COPY statements in the COBOL file lines."""
    return [
        line
        for line in lines
        if re.match(r"^\s+COPY\s+.*\.", line) and not line.lstrip().startswith("*")
    ]


def extract_copy_filenames(copy_lines: List[str]) -> List[str]:
    """Extract filenames from COPY statements."""
    return [
        re.search(r"^\s+COPY\s+([^\s]+)", line).group(1).split(".")[0]
        for line in copy_lines
    ]


def replace_copy_statement_with_content(
    line: str, copy_content: str, copy_map: Dict[str, str]
) -> str:
    """Replace a COPY statement with the actual content from the corresponding file, handling nested COPY statements and removing comments."""
    # Split the content into lines for processing
    copy_content_lines = copy_content.split("\n")

    # Handle the REPLACING directive if present
    if "REPLACING" in line:
        match = re.search(
            r"REPLACING\s+(==\s+)?([^\s]+)(\s+==)?\s+BY\s+(==\s+)?([^\s]+)(\s+==)?",
            line,
        )
        if match:
            source, target = match.group(2).replace("==", ""), match.group(5).strip(".").replace("==", "")
            # logger.debug(f"Replacing {source} with {target} in {line}")
            # Perform the replacement in copy_content_lines
            copy_content_lines = [
                line.replace(source, target) for line in copy_content_lines
            ]

            # logger.debug(copy_content_lines)
    # Check for nested COPY statements and resolve them recursively
    nested_copy_lines = find_copy_statements(copy_content_lines)
    if nested_copy_lines:
        nested_copy_filenames = extract_copy_filenames(nested_copy_lines)
        for nested_filename in nested_copy_filenames:
            if nested_filename in copy_map:
                nested_content = copy_map[nested_filename]
                nested_resolved_content = replace_copy_statement_with_content(
                    "COPY " + nested_filename, nested_content, copy_map
                )
                # Replace the nested COPY line with its resolved content
                copy_content_lines = [
                    (
                        nested_resolved_content
                        if "COPY " + nested_filename in line
                        else line
                    )
                    for line in copy_content_lines
                ]

    # Adjust indentation for the included content
    indentation = line[: line.index("COPY")]
    adjusted_content = []
    for line in copy_content_lines:
        if line.strip():  # If the line is not empty
            # Apply indentation to non-comment lines
            if not line.lstrip().startswith("*"):
                adjusted_line = indentation + line.lstrip()
            else:
                # For comment lines, maintain their original indentation
                adjusted_line = line
        else:
            adjusted_line = ""
        adjusted_content.append(adjusted_line)

    return "\n".join(adjusted_content)


def merge_cpy(code: str, copy_map: Dict[str, str]) -> str:
    """Preprocess a COBOL file: remove comments, empty lines, and replace COPY statements with actual content.

    Args:
        code (str): The COBOL code as a single string.
        copy_map (Dict[str, str]): A mapping of COPY statement filenames to their content.

    Returns:
        str: The preprocessed COBOL code as a single string.
    """
    lines = code.split("\n")
    # Remove comments and empty lines
    lines = [
        line for line in lines if line.strip() and not line.lstrip().startswith("*")
    ]
    # logger.debug(lines)
    copy_lines = find_copy_statements(lines)
    # logger.debug(copy_lines)
    copy_filenames = extract_copy_filenames(copy_lines)
    # logger.debug(copy_filenames)

    for i, line in enumerate(lines):
        if line in copy_lines:
            copy_filename = copy_filenames[copy_lines.index(line)]
            copy_content = clean_code(copy_map.get(copy_filename, ""))
            if copy_content:
                lines[i] = replace_copy_statement_with_content(
                    line, copy_content, copy_map
                )

    # Return the processed lines as a single string
    return "\n".join(lines)


def find_sql_include_statements(lines: List[str]) -> List[str]:
    """Find EXEC SQL INCLUDE statements in the COBOL file lines."""
    return [
        line
        for line in lines
        if re.match(r"^\s*EXEC\s+SQL\s+INCLUDE\s+.*\s*END-EXEC\.", line, re.IGNORECASE)
    ]


def extract_include_filenames(sql_include_lines: List[str]) -> List[str]:
    """Extract filenames from EXEC SQL INCLUDE statements."""
    return [
        re.search(
            r"^\s*EXEC\s+SQL\s+INCLUDE\s+([^\s]+)\s*END-EXEC\.", line, re.IGNORECASE
        ).group(1)
        for line in sql_include_lines
    ]


def replace_sql_include_with_content(line: str, copy_map: Dict[str, str]) -> str:
    """Replace an EXEC SQL INCLUDE statement with the actual content from the corresponding COPY BOOK."""
    filename = re.search(
        r"^\s*EXEC\s+SQL\s+INCLUDE\s+([^\s]+)\s*END-EXEC\.", line, re.IGNORECASE
    ).group(1)
    # Assuming the filename in the copy_map does not include file extension or paths
    copy_content = copy_map.get(filename, "")
    if copy_content:
        # No need for indentation adjustment as SQL includes are typically not indented further
        return copy_content
    else:
        return line


def merge_include(code: str, copy_map: Dict[str, str]) -> str:
    """Preprocess a COBOL file: replace EXEC SQL INCLUDE statements with actual content from COPY BOOKS.

    Args:
        code (str): The COBOL code as a single string.
        copy_map (Dict[str, str]): A mapping of EXEC SQL INCLUDE filenames to their content.

    Returns:
        str: The preprocessed COBOL code as a single string.
    """
    lines = code.split("\n")
    sql_include_lines = find_sql_include_statements(lines)

    for i, line in enumerate(lines):
        if line in sql_include_lines:
            lines[i] = replace_sql_include_with_content(line, copy_map)

    # Return the processed lines as a single string
    return "\n".join(lines)


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


class Parser():

    def __init__(self, cache_path, cobol_parser_path, jcl_parser_path):
        """
        Initializes the BaseParser.

        Raises:
            ImportError: If the cobol and jcl parser paths are not set up.
        """
        try:
            if not os.path.exists(cache_path):
                os.makedirs(cache_path)

            self.cache_path = cache_path

            self.cobol_parser = cobol_parser_path
            logger.info(
                f"The cobol parser has been loaded from {self.cobol_parser}")

            self.jcl_parser = jcl_parser_path
            logger.info(
                f"The jcl parser has been loaded from {self.jcl_parser}")

        except ImportError:
            raise ImportError(
                "The cobol and jcl parser paths are not set up, please download the parser and set the paths /java_core/koopa.jar and /java_core/jcl_parser.jar"
            )

    def format_data(self, data):
        """
        Recursively formats the given data by replacing spaces in the keys with underscores.

        Args:
            data (dict): The data to be formatted.

        Returns:
            dict: The formatted data.
        """
        formatted_data = {}
        for key, value in data.items():
            formatted_key = key.replace(" ", "_")
            if isinstance(value, dict):
                formatted_data[formatted_key] = self.format_data(value)
            elif isinstance(value, list):
                formatted_list = []
                for item in value:
                    if isinstance(item, dict):
                        formatted_list.append(self.format_data(item))
                    else:
                        formatted_list.append(item)
                formatted_data[formatted_key] = formatted_list
            else:
                formatted_data[formatted_key] = value
        return formatted_data

    def replace_colons_in_pattern(self, text):
        """
        Replaces colons in specific patterns with the word "COLON".

        Args:
        - text (str): The input text where replacements are to be made.

        Returns:
        - str: The modified text with replacements.
        """
        # Regex to find the pattern :XYZ: (where XYZ is any text), not part of another word or inside quotes
        pattern = r'(?<![\w"\'`]):([^:]+):(?![\w"\'`])'

        # Function to replace the colons with the word "COLON"
        def replace_with_colon(match):
            return f"COL{match.group(1)}COL"

        # Replace the pattern in the text
        modified_text = re.sub(pattern, replace_with_colon, text)

        return modified_text

    def parse_jcl(
        self,
        code: str,
        encoding="utf-8",
        **kwargs,
    ):
        """
        Parses a JCL file and returns the parsed JCL.

        Args:
            path (str): The path to the JCL file.
            **kwargs: Additional keyword arguments.

        Returns:
            ParsedJCL: The parsed JCL.

        Raises:
            Exception: If an error occurs during parsing.

        """
        try:
            code = "\n".join(
                code.splitlines()
            )  # normalize newline character in different os
            tmp_file = f"{uuid.uuid4().hex}.jcl"
            with open(
                os.path.join(self.cache_path, tmp_file), "w", encoding=encoding
            ) as f:
                f.write(code)
            path = os.path.join(self.cache_path, tmp_file)
            # Extract file name without extension
            file = os.path.basename(path)
            subprocess.call(
                [
                    "java",
                    "-classpath",
                    self.jcl_parser,
                    "ParseDataJCL",
                    path,
                ], stdout=subprocess.DEVNULL
            )
            os.rename(
                os.path.join(file + "_jcl_map.json"),
                os.path.join(self.cache_path, file.split(".")[0] + ".json"),
            )
            data = json.load(
                open(os.path.join(self.cache_path,
                     file.split(".")[0] + ".json"))
            )
            data = self.format_data(data)
            # logger.info(f"Successfully parsed the jcl file at {path}")
            # Remove the temporary file
            os.remove(os.path.join(self.cache_path,
                      file.split(".")[0] + ".json"))
            os.remove(path)
            # os.remove("tmp.jcl")
            return data

        except Exception as e:
            raise e

    def _parse_cobol(
        self,
        # program_blob: BlobInput,
        code: str,
        last_depth: str = "200",
        parse_func: str = "ParseFileForSectionChart",
        encoding: str = "utf-8",
        **kwargs,
    ) -> dict:
        """
        Parses a COBOL file and returns the parsed program.

        Args:
            code (str): The COBOL source code.
            last_depth (str, optional): The last depth to parse. Defaults to "200".
            parse_func (str, optional): The parse function to use. Defaults to "ParseFileForSectionChart".
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The parsed program data.

        Raises:
            Exception: If an error occurs during parsing.

        """
        try:
            # Write code to a temporary file
            tmp_file = f"{uuid.uuid4().hex}.cbl"
            tmp_parsed_file = f"{uuid.uuid4().hex}.json"
            with open(
                os.path.join(self.cache_path, tmp_file), "w", encoding=encoding
            ) as f:
                f.write(code)
            path = os.path.join(self.cache_path, tmp_file)
            temporary_output = os.path.join(self.cache_path, tmp_parsed_file)
            subprocess.call(
                [
                    "java",
                    "-classpath",
                    self.cobol_parser,
                    f"koopa.examples.basic.{parse_func}",
                    path,
                    temporary_output,
                    last_depth,
                    self.cache_path,
                ], stdout=subprocess.DEVNULL
            )
            with open(temporary_output, "r", encoding="utf-8") as f:
                data = json.load(f)
            data = self.format_data(data)
            # logger.info(f"Successfully parsed the cobol file at {path}")
            # Remove the temporary file
            os.remove(os.path.join(self.cache_path, tmp_file))
            os.remove(os.path.join(self.cache_path, tmp_parsed_file))
            return data
        except Exception as e:
            print(path)
            print(temporary_output)
            raise e

    def parse_cobol(
        self, code: str, copy_map: dict[str, str], encoding: str = "utf-8", **kwargs
    ) -> dict:
        code_lines = code.splitlines()
        # normalize newline character in different os
        code = "\n".join(code_lines)

        try:
            parse_file_output = self._parse_cobol(
                code,
                parse_func="ParseFile",
                encoding=encoding,
                **kwargs,
            )


            compile_code = merge_cpy(code, copy_map)
            compile_code = merge_include(compile_code, copy_map)

            parse_file_for_sql_analysis_output = self._parse_cobol(
                compile_code,
                parse_func="ParseFileForSQLAnalysis",
                encoding=encoding,
                **kwargs,
            )

            parse_file_for_section_chart_output = self._parse_cobol(
                code, parse_func="ParseFileForSectionChart", encoding=encoding, **kwargs
            )

            parse_file_for_program_design_output = self._parse_cobol(
                compile_code,
                parse_func="ParseFileForProgramDesign",
                encoding=encoding,
                **kwargs,
            )

            parse_file_for_cics_analysis = self._parse_cobol(
                code, parse_func="ParseFileForCICSAnalysis", encoding=encoding, **kwargs
            )

            call_loc_file_map: dict[str,
                                    str] = parse_file_output["callLocFileMap"]
            call_line_regex = re.compile(r"\s*CALL\s+(\S+)", re.IGNORECASE)

            for line_number in list(call_loc_file_map.keys()):
                inparser_program_id = call_loc_file_map[line_number]

                # program name inside quotes is not affected
                if "'" in inparser_program_id or '"' in inparser_program_id:
                    continue

                line_index = int(line_number) - 1
                line = code_lines[line_index]

                match = call_line_regex.match(line)
                if match is None:
                    print(f"Replace exception - {line_number} {line}")
                    continue
                infile_program_id = match.group(1)

                # program_id::call_type
                if "::" in inparser_program_id:
                    inparser_program_id = inparser_program_id.split("::")[0]

                call_loc_file_map[line_number] = call_loc_file_map[line_number].replace(
                    inparser_program_id, infile_program_id
                )

            # temporarily fix parser float data type in data_map_list, var_dec_map, io_map_list, linkage_map_list
            var_dec_map = parse_file_for_sql_analysis_output["varDecMap"]
            data_map_list = parse_file_for_program_design_output["analysisMap"]["dataMapList"]
            io_map_list = parse_file_for_program_design_output["analysisMap"]["ioMapList"]
            linkage_map_list = parse_file_for_program_design_output["analysisMap"]["linkageMapList"]

            for i, data_map in enumerate(data_map_list):
                if "pic" not in data_map:
                    continue

                label_name = data_map.get("label_name", "")
                pic = data_map["pic"]
                compression_format: Optional[str] = data_map.get("data_type")

                length = calculate_cobol_variable_length(
                    pic=pic, compression_format=compression_format
                )

                data_map_list[i]["num_digits"] = str(length)

                if label_name in var_dec_map:
                    var_dec_map[label_name]["Length"] = str(length)

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
            # end fix

            # Return the parsed data as a dictionary instead of using ParsedProgram
            parsed_program = {
                "copyLocFileMap": parse_file_output["copyLocFileMap"],
                "selectLocFileMap": parse_file_output["selectLocFileMap"],
                "callLocFileMap": parse_file_output["callLocFileMap"],
                "startSectionMap": parse_file_for_section_chart_output["startSectionMap"],
                "statsMap": parse_file_output["statsMap"],
                "sqlLocFileMap": parse_file_output["sqlLocFileMap"],
                "divisionContentMap": parse_file_output["divisionContentMap"],
                "analysisMap": parse_file_for_program_design_output["analysisMap"],
                "sqlPropertiesMap": parse_file_for_sql_analysis_output["sqlPropertiesMap"],
                "varDecMap": parse_file_for_sql_analysis_output["varDecMap"],
                "cics_map": parse_file_for_cics_analysis,
            }

            return parsed_program
        except Exception as e:
            # logger.info("Cannot parse the cobol file due to an error")
            raise e

    def parse_copy(
        self, code: str, copy_map: dict[str, str], encoding="utf-8", **kwargs
    ):
        """
        Parses a copybook file and returns the parsed copybook.

        Args:
            code (str): The code to parse.
            **kwargs: Additional keyword arguments.

        Returns:
            str: The parsed copybook.

        """
        try:
            # Remove all the comments from the code
            code = re.sub(r"^\s*\*.*", "", code, flags=re.MULTILINE)
            code = "\n".join(
                [line for line in code.split("\n") if line.strip()])
            code = replace_colons_in_pattern(code)
            code = code.lstrip()
            copy_code = COPY_TEMPLATE.format(code)
            return self.parse_cobol(
                copy_code, encoding=encoding, copy_map=copy_map, **kwargs
            )
        except Exception as e:
            raise e

    def find_relevant_copybook_database_names(
        self, code: str, is_copybook=False, encoding="utf-8"
    ) -> list[str]:
        """Find included copybook, database file names in COBOL file or copybook file

        Args:
            code (str): Code of the file
            is_copybook (bool, optional): Whether the code file is the copybook. Defaults to False.
            encoding (str, optional): Encoding of the code file. Defaults to "utf-8".

        Returns:
            list[str]: List of included copybook, database file names.
        """
        if is_copybook:
            code = re.sub(r"^\s*\*.*", "", code, flags=re.MULTILINE)
            code = "\n".join(
                [line for line in code.split("\n") if line.strip()])
            code = replace_colons_in_pattern(code)
            code = code.lstrip()
            code = COPY_TEMPLATE.format(code)

        parse_file_output = self.parse_cobol(
            code,
            parse_func="ParseFile",
            encoding=encoding,
        )

        program_ids = set()

        for program_id in parse_file_output["sqlLocFileMap"].values():
            program_ids.add(program_id)

        for program_id in parse_file_output["copyLocFileMap"].values():
            program_ids.add(program_id)

        return list(program_ids)