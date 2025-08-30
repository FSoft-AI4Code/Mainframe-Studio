from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
from dotenv import load_dotenv
import os
from pydantic import BaseModel, SerializeAsAny
from typing import List, Optional
from antlr4 import CommonTokenStream, InputStream
from grammar.ibm_cobol.Cobol85Lexer import Cobol85Lexer
from grammar.ibm_cobol.Cobol85Parser import Cobol85Parser
from grammar.ibm_cobol.MyCobol85Visitor import MyCobol85Visitor
from grammar.ibm_cobol.cobol_schemas import CobolVariable

COPY_TEMPLATE = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. COPYBOOK.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
{}"""

class ParsedCopybook(BaseModel):
    variable_list: SerializeAsAny[list[CobolVariable]]

def parse_copybook(code: str) -> ParsedCopybook:
    try:
        # Normalize line endings and prepare the code
        code = "\n".join(code.splitlines())
        
        # Create lexer and token stream
        stream = CommonTokenStream(Cobol85Lexer(InputStream(code)))
        stream.fill()

        # Create and configure parser
        parser = Cobol85Parser(stream)
        parser.buildParseTrees = True
        tree = parser.startRule()

        # Create and run visitor
        visitor = MyCobol85Visitor(parser)
        tree.accept(visitor)

        # Create ParsedCopybook instance from visitor results
        
        if visitor.variable_list is None:
            return ParsedCopybook(variable_list=[])
        
        variable_list_with_data_type = []
        for variable in visitor.variable_list:
            print(variable)
            if variable.picture_clause is not None:
                if "X" in variable.picture_clause or "A" in variable.picture_clause:
                    data_type = "char"
                elif "9" in variable.picture_clause or "S9" in variable.picture_clause:
                    data_type = "numeric"
                else:
                    data_type = "unknown"
            else:
                data_type = "unknown"
            variable_list_with_data_type.append(variable.model_dump() | {"data_type": data_type})
        return ParsedCopybook(variable_list=variable_list_with_data_type)
    
    except Exception as e:
        raise ValueError(f"Failed to parse copybook: {str(e)}")

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
        copybook_df = df[df['label'] == 'COPY'].copy()
        # Print the 'content' field and parse it
        if 'content' in copybook_df.columns:
            content = copybook_df.iloc[5]['content']
            print("\nFirst Row Content:")
            print("--------------")
            print(content)
            
            # Parse the content
            parsed_copybook = parse_copybook(COPY_TEMPLATE.format(content))
            print("\nParsed Copybook:")
            print("--------------")
            print(parsed_copybook.model_dump_json(indent=2))
        else:
            print("The 'content' field does not exist in the DataFrame.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    read_blob_csv()
