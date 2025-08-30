import json
from typing import Dict, List

from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from loguru import logger

from app.config.llm_client import get_llm
from app.config.nebula import NebulaClient, get_nebula_client
from app.constants.graph import NEBULA_SPACE_NAME_PREFIX

llm = get_llm(model_type="assistant")


def check_repository_states(config: RunnableConfig) -> dict[str, str]:
    """
    Check the states of the current repository to perform essential operations. If no operation is needed, user can start chat with the assistant.

    Returns:
        list[dict]: A list of operation dictionaries containing the operation name and message for user.
    """
    configuration = config.get("configurable", {})
    repository_id = configuration.get("repository_id")
    is_assessed = configuration.get("is_assessed")
    is_reversed = configuration.get("is_reversed")

    if not repository_id:
        return {
            "operation": "upload_repository",
            "message": "No repository uploaded. Please upload the repository via git link.",
        }

    if not is_assessed:
        return {
            "operation": "assess_repository",
            "message": "Repository is not assessed. Please assess the repository to continue.",
        }

    if not is_reversed:
        return {
            "operation": "reverse_repository",
            "message": "Repository is not reversed. Please run reverse engineering on the repository to continue.",
        }

    return None


@tool
def query_relation_legacy_system(user_query: str, config: RunnableConfig) -> str:
    """
    Query relationships between different types of files in a legacy system using natural language.
    This tool translates natural language queries into Nebula Graph queries to analyze file dependencies and connections.

    Args:
        user_query (str): Natural language query from the user (e.g., "What are the main components of the login system?")

    Returns:
        str: Natural language response in a concise format, using bullet points for relationships between nodes
    """
    state_check = check_repository_states(config)
    if state_check:
        return state_check

    try:
        # 1. Translate natural language to Cypher query using LLM
        cypher_query = translate_to_cypher(user_query)

        logger.info(f"Translated query: {cypher_query}")

        configuration = config.get("configurable", {})
        repository_id = configuration.get("repository_id")

        space_name = f"{NEBULA_SPACE_NAME_PREFIX}{repository_id}"

        # 2. Execute Cypher query on Nebula Graph
        graph_results = execute_nebula_query(cypher_query, space_name)
        logger.info(f"Query results: {graph_results}")

        # 3. Format results into natural language
        formatted_response = format_graph_response(user_query, graph_results)
        return formatted_response.content

    except Exception as e:
        logger.error(f"Error in chat_with_nebula_graph: {str(e)}")
        return f"I encountered an error while processing your query: {str(e)}"


@tool
def query_variable_possible_value(user_query: str, config: RunnableConfig) -> str:
    """
    Query all possible values of a 88-level variable in a COBOL program using natural language. This tool translates natural language queries into Nebula Graph queries to analyze variable values.


    Args:
        user_query (str): Natural language query from the user (e.g., "What are the possible values of variable ERR-FLG-OFF?")

    Returns:
        str: Natural language response in a concise format, using bullet points for relationships between nodes
    """
    state_check = check_repository_states(config)

    if state_check:
        return state_check

    try:
        # 1. Translate natural language to Cypher query using LLM
        cypher_query = translate_to_cypher_statement(user_query)
        logger.info(f"Translated query: {cypher_query}")

        configuration = config.get("configurable", {})
        repository_id = configuration.get("repository_id")

        space_name = f"{NEBULA_SPACE_NAME_PREFIX}{repository_id}"

        # 2. Execute Cypher query on Nebula Graph
        graph_results = execute_nebula_query(cypher_query, space_name)
        logger.info(f"Query results: {graph_results}")

        # 3. Format results into natural language
        formatted_response = format_graph_response(user_query, graph_results)
        return formatted_response.content

    except Exception as e:
        logger.error(f"Error in chat_with_nebula_graph: {str(e)}")
        return f"I encountered an error while processing your query: {str(e)}"


def translate_to_cypher_statement(user_query: str) -> str:
    """
    Translate natural language query to Nebula Graph cypher (nGQL) query using LLM.
    """
    # Example prompt for the LLM
    system_prompt = f"""
Your task is to generate a query in NebulaGraph Cypher dialect(rather than standard):
1. it requires explicit label specification only when referring to node properties: v.Foo.name
2. note explicit label specification is not needed for edge properties, so it's e.name instead of e.`Bar`.name
3. it uses double equals sign for comparison: `==` rather than `=`
 
Use ONLY the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.


    
    Here is the graph schema:
    {NebulaClient.get_graph_schema_statement()}

    Example queries:
    MATCH (n:IDENTIFIER) RETURN n;

    MATCH (n:IDENTIFIER) RETURN n.IDENTIFIER.name;
    
    MATCH (n)-[:HAS_PARAGRAPH]->(m:PARAGRAPH) RETURN n, m;
    
    You can extract the possible values of a variable by getting the default value of its children, you should return the names of the children. If the level of the children is not 88, you should say that the variable is not a 88-level variable:
    MATCH (n:IDENTIFIER)-[:HAS_CHILD*]->(m:IDENTIFIER) RETURN n, m;

    You must return only the Nebula Graph Query, nothing else. Do not include ```nGQL``` or ```cypher``` in your response.
    """

    user_prompt = f"""
    Given this question: "{user_query}"
    Generate a Nebula Graph cypher query that will answer this question.
    You should focus on finding the relationships between identifiers, literals, and statements.
    """

    # Use LLM to generate Cypher query
    response = llm(system_prompt + user_prompt)
    return response.content


def translate_to_cypher(user_query: str) -> str:
    """
    Translate natural language query to Nebula Graph cypher (nGQL) query using LLM.
    """
    # Example prompt for the LLM
    system_prompt = f"""
Your task is to generate a query in NebulaGraph Cypher dialect(rather than standard):
1. it requires explicit label specification only when referring to node properties: v.Foo.name
2. note explicit label specification is not needed for edge properties, so it's e.name instead of e.`Bar`.name
3. it uses double equals sign for comparison: `==` rather than `=`
 
Use ONLY the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided. There are only 6 types of file types: COBOL, COPY, JCL_IBM, BMS, OTHER, UTILITY.
    
    Here is the graph schema:
    {NebulaClient.get_graph_schema_file()}

    Example queries:
    MATCH (n:COBOL) RETURN n;

    MATCH (n:COPY) RETURN n.COPY.name;
    
    MATCH (n:JCL_IBM)-[:EXEC_PGM]->(m:COBOL) RETURN n, m;

    You must return only the Nebula Graph Query, nothing else. Do not include ```nGQL``` or ```cypher``` in your response.
    """

    user_prompt = f"""
    Given this question: "{user_query}"
    Generate a Nebula Graph cypher query that will answer this question.
    Focus on finding relevant components and their relationships.
    """

    # Use LLM to generate Cypher query
    response = llm(system_prompt + user_prompt)
    return response.content


def execute_nebula_query(cypher_query: str, space_name: str) -> List[Dict]:
    """
    Execute the cypher query on Nebula Graph and return results.
    """
    try:
        # Initialize Nebula Graph session
        session = get_nebula_client(space_name)

        # Execute query and get results
        result = session.execute(cypher_query, timeout=1)

        # Process and return results
        processed_results = process_query_results(result)

        return processed_results

    except Exception as e:
        logger.error(f"Nebula Graph query error: {str(e)}")
        raise


def format_graph_response(question: str, graph_results: List[Dict]) -> str:
    """
    Format graph query results into natural language with bullet points.
    """
    # Example prompt for the LLM
    system_prompt = """
    You are an expert in explaining software architecture.
    Convert the technical graph results into clear, concise natural language.
    Keep the explanation technical but understandable.
    You must provide a concise explanation of the graph query results do not include any additional information.
    Focus on the relationships between components. You can format the response as a bullet list if needed.
    You must provide explanations for each component and their relationships(if any).
    """

    results_prompt = f"""
    Given these graph query results: {json.dumps(graph_results, indent=4)}
    
    Question: {question}
    """

    # Use LLM to format response
    response = llm(system_prompt + results_prompt)
    return response


# Helper function to get Nebula Graph session
def get_nebula_session():
    """Get or create a Nebula Graph session."""
    # Implementation depends on your Nebula Graph setup
    from nebula3.Config import Config
    from nebula3.gclient.net import ConnectionPool

    config = Config()
    connection_pool = ConnectionPool()

    # Initialize connection pool
    connection_pool.init([("localhost", 9669)], config)

    # Get session
    session = connection_pool.get_session("root", "password")

    return session


def process_query_results(query_output) -> List[Dict]:
    """Get the record from the query result, removing unnecessary data from the query output."""

    output = []

    result = query_output["results"][0]

    data = result["data"]

    for record in data:
        output.append(record["row"])

    return output
