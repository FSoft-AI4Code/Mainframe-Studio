from pydantic import BaseModel
from typing import List, Optional, Tuple
import copy

class BMSOverview(BaseModel):
    """
    Represents an overview of a BMS file.

    Attributes:
        name (str): The name of the BMS file.
        file_name (str): The file name of the BMS file.
        related_pgms (List[str]): A list of related program names.
    """
    name: str
    file_name: str
    related_pgms: Optional[List[str]] = None


class BMSDefItem(BaseModel):
    """
    Represents a BMS definition item.

    Attributes:
        name (str): The name of the item.
        item_type (str): The type of the item.
        position (Optional[Tuple[int, int]]): The position of the item (optional).
        size (Optional[Tuple[int, int]]): The size of the item (optional).
        length (int): The length of the item.
        attribute (str): The attribute of the item.
        color (str): The color of the item.
        initial_value (str): The initial value of the item.
        comment (str): The comment for the item.
    """
    name: str
    item_type: str
    position: Optional[Tuple[int, int]]
    size: Optional[Tuple[int, int]]
    length: int
    attribute: str
    color: str
    initial_value: str
    comment: str


class BMSAccessItem(BaseModel):
    file_name: str
    cmd: str  # access_mode
    content: str  # cics_cmd
    map: Optional[str] = None
    mapset: Optional[str] = None

class AnalyzedBMS(BaseModel):
    file_name: str
    content: Optional[str] = None
    encoding: Optional[str] = None

    definitions: Optional[list] = None
    overview: Optional[BMSOverview] = None
    data: Optional[List[BMSDefItem]] = None
    screen_access: Optional[List[BMSAccessItem]] = None
    screen_string: Optional[str] = None

    def extract_data(self):
        """
        Extracts data from the BMS blob.

        Returns:
            list: A list of BMSDefItem objects representing the extracted data.
        """

        self.overview = BMSOverview(
            name=self.file_name,
            file_name=self.file_name.split(".")[0],
            related_pgms=[]
        )
        if self.definitions is None:
            raise ValueError("Definitions are required to parse BMS")
        self.data = []
        for value in self.definitions:
            position = None
            size = None
            length = 0
            attribute = ""
            color = ""
            initial_value = ""
            comment = ""
            if "params" in value:
                for param in value['params']:
                    if param.startswith('POS='):
                        position = tuple(
                            map(int, param.split('=')[1].strip('()').split(',')))
                    elif param.startswith('SIZE='):
                        size = tuple(map(int, param.split('=')[
                            1].strip('()').split(',')))
                    elif param.startswith('LENGTH='):
                        try:
                            length = int(param.split('=')[1])
                        except ValueError:
                            length = 0  # or any default value you prefer
                    elif param.startswith('ATTRB='):
                        attribute = param.split('=')[1]
                    elif param.startswith('COLOR='):
                        color = param.split('=')[1]
                    elif param.startswith('INITIAL='):
                        initial_value = "=".join(
                            param.split('=')[1:]
                        ).strip("'")

            self.data.append(
                BMSDefItem(
                    name=value["name"],
                    item_type=value["cmd"],
                    position=position,
                    size=size,
                    length=length,
                    attribute=attribute,
                    color=color,
                    initial_value=initial_value,
                    comment=comment,
                )
            )
        self.draw_screen()
        return {
            "overview": self.overview.model_dump(),
            "data": [item.model_dump() for item in self.data] if self.data else [],
            "screen_string": self.screen_string
        }

    def draw_screen(self, screen_rows=24, screen_cols=80):
        # Create an empty screen
        screen = [[' ' for _ in range(screen_cols)]
                  for _ in range(screen_rows)]

        bms_info = copy.deepcopy(self.data)
        for entry in bms_info:
            if entry.position is None:
                continue
            row, col = entry.position
            row_index = row - 1
            col_index = col - 1

            # Check to ensure it does not exceed the screen size
            if row_index < screen_rows and col_index < screen_cols:
                # If there is no INITIAL value, replace with 'X' * LENGTH
                if (entry.initial_value is None or entry.initial_value == " " or entry.initial_value == ""):
                    entry.initial_value = 'X' * entry.length

                # Place the value on the screen
                for i in range(entry.length):
                    # Check to ensure it does not exceed the column
                    if col_index + i < screen_cols and entry.initial_value is not None:
                        if i < len(entry.initial_value):
                            screen[row_index][col_index +
                                              i] = entry.initial_value[i]
        rows = [''.join(row) for row in screen]
        self.screen_string = '\n'.join(rows)
        return self.screen_string