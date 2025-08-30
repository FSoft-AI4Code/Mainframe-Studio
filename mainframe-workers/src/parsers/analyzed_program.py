from dotenv import load_dotenv
from typing import List, Dict, Optional
from pydantic import BaseModel
load_dotenv()

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
