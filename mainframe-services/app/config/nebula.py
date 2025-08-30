import json
import time
from typing import Any, List

from loguru import logger
from nebula3.common.ttypes import ErrorCode
from nebula3.Config import Config
from nebula3.gclient.net import ConnectionPool
from networkx import edges

from app.config.settings import get_settings
from app.schemas import nebula_graph_schema


class NebulaConnection:
    def __init__(
        self,
        host: str,
        port: str,
        username: str,
        password: str,
        max_connection_pool_size: int,
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        # Initialize connection pool configuration
        config = Config()
        config.max_connection_pool_size = max_connection_pool_size
        self.config = config
        self.connection_pool = ConnectionPool()

    def init_pool(self):
        """Initialize the connection pool."""
        if not self.connection_pool.init([(self.host, self.port)], self.config):
            raise RuntimeError("Failed to initialize the Nebula connection pool.")

    def get_session(self):
        """Retrieve a session from the connection pool."""
        return self.connection_pool.get_session(self.username, self.password)

    def close(self):
        """Close the connection pool when done."""
        self.connection_pool.close()


class NebulaClient:
    support_tags = [
        nebula_graph_schema.CobolNode,
        nebula_graph_schema.CopyNode,
        nebula_graph_schema.JclIbmNode,
        nebula_graph_schema.BmsNode,
        nebula_graph_schema.OtherNode,
        nebula_graph_schema.UtilityNode,
        nebula_graph_schema.ParagraphNode,
        nebula_graph_schema.IdentifierNode,
        nebula_graph_schema.LiteralNode,
        nebula_graph_schema.SetStatementNode,
    ]

    support_edges = [
        nebula_graph_schema.ExecPgm,
        nebula_graph_schema.StaticCall,
        nebula_graph_schema.DynamicCall,
        nebula_graph_schema.HasCopybook,
        nebula_graph_schema.HasInteract,
        nebula_graph_schema.HasParagraph,
        nebula_graph_schema.HasChild,
        nebula_graph_schema.Owns,
        nebula_graph_schema.Source,
        nebula_graph_schema.Target,
    ]

    def __init__(
        self,
        connection: NebulaConnection,
        space: str,
    ):
        self.connection = connection
        self.space = space
        self.session = connection.get_session()

        if self.space_exists(space):
            self.use_space()
        else:
            logger.info(f"Space {space} does not exist, creating it.")
            self.create_space()

    def space_exists(self, space: str) -> bool:
        result = self.session.execute("SHOW SPACES;")
        if not result.is_succeeded():
            raise RuntimeError(f"Error checking spaces: {result.error_msg()}")
        spaces = [row["Name"] for row in result.as_primitive()]
        return space in spaces

    @staticmethod
    def get_graph_schema_file():
        file_tags = [
            nebula_graph_schema.CobolNode,
            nebula_graph_schema.CopyNode,
            nebula_graph_schema.JclIbmNode,
            nebula_graph_schema.BmsNode,
            nebula_graph_schema.OtherNode,
            nebula_graph_schema.UtilityNode,
        ]

        file_edges = [
            nebula_graph_schema.ExecPgm,
            nebula_graph_schema.StaticCall,
            nebula_graph_schema.DynamicCall,
            nebula_graph_schema.HasCopybook,
            nebula_graph_schema.HasInteract,
        ]
        schema = ""

        schema += "Nodes"
        for tag in file_tags:
            schema += f"\n\n{tag.create_vertex_statement()}"

        schema += "Edges"
        for edge in file_edges:
            schema += f"\n\n{edge.create_edge_statement()}"

        return schema

    @staticmethod
    def get_graph_schema_statement():
        statement_tags = [
            nebula_graph_schema.ParagraphNode,
            nebula_graph_schema.IdentifierNode,
            nebula_graph_schema.LiteralNode,
            nebula_graph_schema.SetStatementNode,
        ]

        statement_edges = [
            nebula_graph_schema.HasParagraph,
            nebula_graph_schema.HasChild,
            nebula_graph_schema.Owns,
            nebula_graph_schema.Source,
            nebula_graph_schema.Target,
        ]

        schema = ""

        schema += "Nodes"
        for tag in statement_tags:
            schema += f"\n\n{tag.create_vertex_statement()}"

        schema += "Edges"
        for edge in statement_edges:
            schema += f"\n\n{edge.create_edge_statement()}"

        return schema

    def create_space(self):
        self.session.execute(
            f"CREATE SPACE IF NOT EXISTS {self.space} (vid_type = FIXED_STRING(100));"
        )
        self.use_space()
        self._create_tags()
        self._create_tag_index()
        self._create_edges()
        self._create_edge_index()
        self._rebuild_index()

    def _create_tags(self):
        statement = ""

        for tag in NebulaClient.support_tags:
            statement += tag.create_vertex_statement() + "\n"

        self.execute(statement)

    def _create_tag_index(self):
        statement = ""
        for tag in NebulaClient.support_tags:
            statement += tag.create_tag_index_statement() + "\n"

        self.execute(statement)

    def _create_edges(self):
        statement = ""

        for edge in NebulaClient.support_edges:
            statement += edge.create_edge_statement() + "\n"

        self.execute(statement)

    def _create_edge_index(self):
        statement = ""
        for edge in NebulaClient.support_edges:
            statement += edge.create_edge_index_statement() + "\n"

        self.execute(statement)

    def _rebuild_index(self):
        statement = ""

        for tag in NebulaClient.support_tags:
            statement += tag.rebuild_index_statement() + "\n"

        for edge in NebulaClient.support_edges:
            statement += edge.rebuild_index_statement() + "\n"

        self.execute(statement)

    def use_space(self):
        self.execute(f"USE {self.space};")

    def execute(
        self, statement: str, params: dict[str, Any] | None = None, timeout: int = 60
    ):
        start_time = time.time()

        while True:

            response = self.session.execute_json(statement)
            result = json.loads(response)

            if result["errors"][0]["code"] == ErrorCode.SUCCEEDED:
                break

            elapsed = time.time() - start_time

            if elapsed > timeout:
                raise RuntimeError(
                    f"Error executing statement: '{statement}' with parameters '{params}', {result.error_msg()}"
                )

            logger.info(
                f"Query execution failed in space '{self.space}', query: '{statement}'. Retrying..."
            )
            time.sleep(1)

        return result

    def insert_node_batch(self, nodes: List[nebula_graph_schema.BaseNode]):
        try:
            for node in nodes:
                self.execute(node.insert_vertex_statement())
        except Exception:
            logger.info(f"Error executing statement: {node.insert_vertex_statement()}")
            raise

    def insert_edge_batch(self, edges: List[nebula_graph_schema.BaseEdge]):
        try:
            for edge in edges:
                self.execute(edge.insert_edge_statement())
        except Exception:
            logger.info(f"Error executing statement: {edge.insert_edge_statement()}")
            raise

    def execute_query(self, query: str):
        result = self.session.execute(query)
        if not result.is_succeeded():
            raise RuntimeError(
                f"Error executing query: '{query}', {result.error_msg()}"
            )
        return result

    def delete_space(self):
        self.session.execute(f"DROP SPACE {self.space};")

    def close(self):
        self.session.release()

    def __del__(self):
        self.close()


_nebula_connection = None


def get_nebula_connection() -> NebulaConnection:
    global _nebula_connection

    settings = get_settings()
    if _nebula_connection is None:
        _nebula_connection = NebulaConnection(
            host=settings.NEBULA_HOST,
            port=settings.NEBULA_PORT,
            username=settings.NEBULA_USERNAME,
            password=settings.NEBULA_PASSWORD,
            max_connection_pool_size=settings.NEBULA_MAX_CONNECTION_POOL_SIZE,
        )
        _nebula_connection.init_pool()

    return _nebula_connection


def get_nebula_client(space: str) -> NebulaClient:
    nebula_connection = get_nebula_connection()
    return NebulaClient(nebula_connection, space)
