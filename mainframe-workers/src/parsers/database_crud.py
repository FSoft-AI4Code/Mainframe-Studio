from collections import defaultdict
from enum import Enum
from typing import Dict, List, Optional, Set, Union

import sqlparse
from pydantic import BaseModel
from sqlparse.sql import Identifier, IdentifierList
from sqlparse.tokens import DML, Keyword, Punctuation, Whitespace

from parsers.execution_flow import iterate_statements
from parsers.grammar.common.base_cobol_schemas import Database, DatabaseTable, Statement
from parsers.grammar.ibm_cobol.ibm_cobol_schemas import ExecSqlStatement2
from parsers.grammar.unisys_cobol.cobol_unisys_schemas import (
    CreateStatement,
    FindStatement,
    LockStatement,
)


class DatabaseOperation(str, Enum):
    CREATE = "CREATE"
    READ = "READ"
    UPDATE = "UPDATE"
    DELETE = "DELETE"


class DatabaseTableDescriptor(BaseModel):
    """
    Database table descriptor containing information about the table used in the COBOL program.
    """

    database_name: str
    table_name: str
    invoke_names: List[str]
    operations: List[DatabaseOperation]


def extract_crud(
    statements: List[Statement],
    database_info: Optional[Union[Database, DatabaseTable]] = None,
) -> List[DatabaseTableDescriptor]:
    """Extract CRUD operations performed on database tables.

    This function identifies Create, Read, Update, and Delete operations performed on database tables
    in COBOL programs. It handles both COBOL85 (via EXEC SQL statements) and COBOL Unisys formats.

    Args:
        statements (List[Statement]): List of statements of the COBOL program
        database_info (Optional[Union[Database, DatabaseTable]]): The extracted database information
            from the COBOL program. Can be either a Database object or a
            DatabaseTable object (for Unisys COBOL). If None, the function will attempt to extract
            information from EXEC SQL statements (for COBOL85).

    Returns:
        List[DatabaseTableDescriptor]: List of database descriptors containing information about
        tables used in the program and the operations performed on them (CREATE, READ, UPDATE, DELETE).
    """

    # Extract database_info from EXEC SQL statement if not provided
    # Used for COBOL85
    if not database_info:
        return _extract_crud_from_exec_sql_statement(statements)

    # Extract database_info from DatabaseTable object if provided
    if isinstance(database_info, DatabaseTable):
        table = database_info
        entry = _init_table_descriptor(
            database_name="", table=table, table_invoke_names_map={}
        )
        entry = entry[0]

        entry.operations = _extract_table_operations_from_statements(
            entry.table_name,
            statements,
            invoke_names=entry.invoke_names,
        )

        return [entry]

    # Extract database_info from Database object if provided
    # The database_info object contains multiple tables
    tables = database_info.tables

    table_invoke_names_map = _extract_table_alias(database_info)

    table_descriptors: List[DatabaseTableDescriptor] = []

    for table in tables:

        is_table_added = any(
            table.table_name in entry.table_name
            or (
                table.invoke_name and table.invoke_name in entry.table_name
            )  # invoke name is the actual table name if provided
            for entry in table_descriptors
        )

        if is_table_added:
            continue

        entry = _init_table_descriptor(
            database_info.database_name, table, table_invoke_names_map
        )
        table_descriptors.extend(entry)

    for entry in table_descriptors:
        entry.operations = _extract_table_operations_from_statements(
            entry.table_name,
            statements,
            invoke_names=entry.invoke_names,
        )

    return table_descriptors


def _init_table_descriptor(
    database_name: str,
    table: DatabaseTable,
    table_invoke_names_map: Dict[str, List[str]],
) -> List[DatabaseTableDescriptor]:

    entries = []

    table_entry = DatabaseTableDescriptor(
        database_name=database_name,
        table_name=table.invoke_name or table.table_name,
        invoke_names=(
            table_invoke_names_map.get(table.invoke_name, [])
            if table.invoke_name
            else []
        ),
        operations=[],
    )
    entries.append(table_entry)

    return entries


def _extract_table_alias(database_info: Database) -> Dict[str, List[str]]:
    tables = database_info.tables
    table_alias = defaultdict(list)

    for table in tables:
        table_name = table.table_name
        if table.invoke_name:
            table_alias[table.invoke_name].append(table_name)

    return table_alias


def _extract_crud_from_exec_sql_statement(
    statements: List[Statement],
) -> List[DatabaseTableDescriptor]:
    """
    Extract CRUD operations performed on database tables from EXEC SQL statements.

    Args:
        statements: List of statements to analyze

    Returns:
        List of database table descriptors
    """

    table_descriptor_dict = {}

    for statement in iterate_statements(statements):
        if not isinstance(statement, ExecSqlStatement2):
            continue

        sql_code = statement.sql_code

        parsed_sql = sqlparse.parse(sql_code)

        for sql_statement in parsed_sql:
            # Identify the first significant token to determine the type of DML statement.
            first_token = sql_statement.token_first(skip_cm=True)
            if first_token is None or first_token.ttype != DML:
                continue  # Skip if not a DML command

            sql_statement_type = sql_statement.get_type()

            # --- Handle SELECT statements ---
            if sql_statement_type == "SELECT":
                from_seen = False
                for token in sql_statement.tokens:
                    # Identify the FROM keyword
                    if token.ttype is Keyword and token.value.upper() == "FROM":
                        from_seen = True
                        continue

                    # After FROM, process the next tokens to extract table names.
                    if from_seen:
                        # Multiple tables might be listed in an IdentifierList (e.g., with JOINs)
                        if isinstance(token, IdentifierList):
                            for identifier in token.get_identifiers():
                                table_name = identifier.value.strip()
                                if table_name not in table_descriptor_dict:
                                    table_descriptor = DatabaseTableDescriptor(
                                        database_name="",
                                        table_name=table_name,
                                        invoke_names=[],
                                        operations=[DatabaseOperation.READ],
                                    )
                                    table_descriptor_dict[table_name] = table_descriptor
                                else:
                                    table_descriptor_dict[table_name].operations.append(
                                        DatabaseOperation.READ
                                    )
                            break
                        # Single table identifier
                        elif isinstance(token, Identifier):
                            table_name = token.get_real_name()
                            if table_name not in table_descriptor_dict:
                                table_descriptor = DatabaseTableDescriptor(
                                    database_name="",
                                    table_name=table_name,
                                    invoke_names=[],
                                    operations=[DatabaseOperation.READ],
                                )
                                table_descriptor_dict[table_name] = table_descriptor
                            else:
                                table_descriptor_dict[table_name].operations.append(
                                    DatabaseOperation.READ
                                )
                            break

            # --- Handle INSERT statements ---
            elif sql_statement_type == "INSERT":
                into_seen = False
                for token in sql_statement.tokens:
                    if token.ttype is Keyword and token.value.upper() == "INTO":
                        into_seen = True
                        continue

                    if into_seen and hasattr(token, "tokens"):
                        sub_tokens = token.tokens

                        if len(sub_tokens) == 0:
                            continue
                        first_sub_token = sub_tokens[0]

                        if isinstance(first_sub_token, Identifier):
                            table_name = first_sub_token.get_real_name()
                            if table_name not in table_descriptor_dict:
                                table_descriptor = DatabaseTableDescriptor(
                                    database_name="",
                                    table_name=table_name,
                                    invoke_names=[],
                                    operations=[DatabaseOperation.CREATE],
                                )
                                table_descriptor_dict[table_name] = table_descriptor
                            else:
                                table_descriptor_dict[table_name].operations.append(
                                    DatabaseOperation.CREATE
                                )
                            break

            # --- Handle UPDATE statements ---
            elif sql_statement_type == "UPDATE":
                update_seen = False
                for token in sql_statement.tokens:
                    if token.ttype is DML and token.value.upper() == "UPDATE":
                        update_seen = True
                        continue

                    if update_seen and token.value.strip():
                        table_name = token.value.strip()
                        if table_name not in table_descriptor_dict:
                            table_descriptor = DatabaseTableDescriptor(
                                database_name="",
                                table_name=table_name,
                                invoke_names=[],
                                operations=[DatabaseOperation.UPDATE],
                            )
                            table_descriptor_dict[table_name] = table_descriptor
                        else:
                            table_descriptor_dict[table_name].operations.append(
                                DatabaseOperation.UPDATE
                            )
                        break

            # --- Handle DELETE statements ---
            elif sql_statement_type == "DELETE":
                # First, try to find the FROM keyword (common in many DELETE syntaxes)
                from_seen = False
                for token in sql_statement.tokens:
                    if token.ttype is Keyword and token.value.upper() == "FROM":
                        from_seen = True
                        continue

                    if from_seen and token.value.strip():
                        if isinstance(token, Identifier):
                            table_name = token.get_real_name()
                            if table_name not in table_descriptor_dict:
                                table_descriptor = DatabaseTableDescriptor(
                                    database_name="",
                                    table_name=table_name,
                                    invoke_names=[],
                                    operations=[DatabaseOperation.DELETE],
                                )
                                table_descriptor_dict[table_name] = table_descriptor
                                break
                            else:
                                table_descriptor_dict[table_name].operations.append(
                                    DatabaseOperation.DELETE
                                )
                                break

    # Remove duplicate operations
    for table_name, table_descriptor in table_descriptor_dict.items():
        table_descriptor_dict[table_name].operations = list(
            set(table_descriptor.operations)
        )

    return list(table_descriptor_dict.values())


def _extract_table_operations_from_statements(
    table_name: str,
    statements: List[Statement],
    invoke_names: Optional[List[str]] = None,
) -> List[DatabaseOperation]:
    """
    Extract database operations performed on a specific table based on Find, Lock, and Create statements.

    Args:
        table_name: Name of the database table
        statements: List of statements to analyze
        invoke_names: Optional list of alternative names for the table

    Returns:
        Set of database operations performed on the table
    """
    operations = set()

    for statement in iterate_statements(statements):
        if isinstance(statement, FindStatement):
            is_target_table = table_name in statement.record_name
            is_table_alias = invoke_names is not None and any(
                invoke_name in statement.record_name for invoke_name in invoke_names
            )
            if is_target_table or is_table_alias:
                operations.add(DatabaseOperation.READ)

        elif isinstance(statement, LockStatement):
            is_target_table = table_name in statement.database_name
            is_table_alias = invoke_names is not None and any(
                invoke_name in statement.database_name for invoke_name in invoke_names
            )
            if is_target_table or is_table_alias:
                operations.add(DatabaseOperation.UPDATE)

        elif isinstance(statement, CreateStatement):
            is_target_table = table_name in statement.identifier
            is_table_alias = invoke_names is not None and any(
                invoke_name in statement.identifier
                for invoke_name in statement.identifier
            )
            if is_target_table or is_table_alias:
                operations.add(DatabaseOperation.CREATE)

    return list(operations)
