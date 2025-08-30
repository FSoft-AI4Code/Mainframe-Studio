import re
import os
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import copy
from dotenv import load_dotenv
from antlr4 import CommonTokenStream, InputStream
from grammar.bms import BMSLexer, BMSParser, MyBMSVisitor
from contextlib import redirect_stdout, redirect_stderr
from pydantic import BaseModel
from typing import List, Optional, Tuple

def remove_bms_title_line(content: str) -> str:
    content = re.sub(r'^\s*TITLE.*$', '', content,
                     flags=re.MULTILINE).strip()
    return content

def parse_bms(content):
    # Redirect the standard output and standard error to devnull
    # non unix-like sys or windows: with open('nul', 'w') as devnull
    with open(os.devnull, 'w', encoding='utf-8') as devnull:
        with redirect_stdout(devnull), redirect_stderr(devnull):
            stream = CommonTokenStream(BMSLexer(InputStream(content)))
            stream.fill()

            # tokens = stream.getTokens(0, 100000000)

            parser = BMSParser(stream)
            parser.buildParseTrees = True
            tree = parser.program()

            visitor = MyBMSVisitor()
            tree.accept(visitor)

    return visitor.definitions

def read_blob_csv():
    # Load environment variables
    load_dotenv()
    
    # Get Azure Storage details from environment variables
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
    blob_name = "674e70091cee5460a6f8091c_classified.csv"
    
    # Validate environment variables
    if not all([connection_string, container_name, blob_name]):
        raise ValueError("Missing required environment variables. Please check your .env file.")
    
    try:
        # Create blob service client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Get container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Get blob client
        blob_client = container_client.get_blob_client(blob_name)
        
        # Download blob content
        blob_data = blob_client.download_blob()
        
        # Convert to pandas dataframe
        df = pd.read_csv(io.StringIO(blob_data.content_as_text()))
        bms_df = df[df['label'] == 'BMS'].copy()
        for _, row in bms_df.iterrows():
            yield row
    except Exception as e:
        print(f"An error occurred: {str(e)}")

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
            assert self.content is not None, "Content is required to parse BMS"
            self.definitions = parse_bms(self.content)
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
                        length = int(param.split('=')[1])
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

def reverse_bms(name, parsed_bms):
    bms = AnalyzedBMS(
        file_name=name,
        definitions=parsed_bms,
    )
    return bms.extract_data()

class ReverseEngineeringUpdate(BaseModel):
    status: str
    output: Optional[dict] = None
    type: Optional[str] = None

if __name__ == "__main__":
    for row in read_blob_csv():
        row['content'] = remove_bms_title_line(row["content"])
        parsed_bms = parse_bms(row["content"])
        reversed_bms = reverse_bms(row["name"], parsed_bms)

        reverse_update_payload = ReverseEngineeringUpdate(
            status="done",
            output={
                "label": "BMS",
                "overview": reversed_bms.get("overview"),
                "data": reversed_bms.get("data"),
                "screen_string": reversed_bms.get("screen_string"),
            },
            type="BMS",
        )
        print(reverse_update_payload)