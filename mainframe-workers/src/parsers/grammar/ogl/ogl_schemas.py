from typing import List, Optional, Union
from pydantic import BaseModel, SerializeAsAny


class Command(BaseModel):
    raw: str
    start_line: int
    stop_line: int
    start_idx: int
    start_idx: int 
    tag: str

class ControlCommand(Command):
    storages: Optional[List[str]]
    messages: Optional[List[str]]
    summaries: Optional[List[str]]
    sosi_options: Optional[List[str]]


class OverlayCommand(Command):
    name: str
    width: str
    height: str
    offset_x: str
    offset_y: str


class OrientCommand(Command):
    degree: int


class FontCommand(Command):
    type: str
    mem_id: Optional[str]
    font_name: Optional[str]
    charset: Optional[str]
    codepage: Optional[str]
    ddname: Optional[str]
    height: Optional[str]
    scale: Optional[str]
    color: Optional[str]
    ucolor: Optional[str]
    filetype: Optional[str]


class DefineGroupCommand(Command):
    group_name: str
    commands:SerializeAsAny[List[Command]]


class PositionCommand(Command):
    x: str
    y: str

class Line(BaseModel):
    font_name: List[str]
    sosi_mode: Optional[str]
    underlying: Optional[str]
    text_type: Optional[str]
    texts: List[str]

class BoxWithtext(BaseModel):
    box: Optional[str]
    orient: Optional[str]
    format: Optional[str]
    line_spacing: Optional[str]
    line: List[Line]

class DrawboxCommand(Command):
    width: str
    height: str
    border_thickness: Optional[str]
    border_type: Optional[str]
    rounded_option: Optional[str]
    diagonal_option: Optional[str]
    repeat: Optional[str]
    shade: Optional[str]
    color: Optional[str]
    withtext: Optional[List[BoxWithtext]]


class DrawruleCommand(Command):
    direction: Optional[str]
    length: str
    thickness: Optional[Union[str, int]]
    rule_type: Optional[str]
    repeated: Optional[str]


class PlaceCommand(Command):
    type: str  # SEGID or GROUP
    name: str


class SetunitsCommand(Command):
    default: Optional[List[str]]
    linesp: Optional[str]
    corner_length: Optional[str]
    text_margin: Optional[str]
    positioning: Optional[str]


class SettextCommand(Command):
    orientation: Optional[int]
    format: Optional[str]
    alignment: Optional[Union[str, dict]]
    lines: List[str]


class DefinePatternCommand(Command):
    name: str
    code_type: str
    code_lines: List[str] 


class PlacePatternCommand(Command):
    pattern_name: str
    orientation: Optional[int]
    shade: Optional[List[str]]
    mirror: Optional[str]
    negative: Optional[str]
    color: Optional[str]


class SegmentCommand(Command):
    name: Optional[str]
    mem_id: str
    ddname: Optional[str]
    filetype: Optional[str]
