import json
import time

import networkx as nx

from app.config.nebula import NebulaClient, get_nebula_client
from app.constants.graph import NEBULA_SPACE_NAME_PREFIX
from app.schemas.common_schema import PyObjectId
from app.schemas import nebula_graph_schema


def networkx_to_nebula_mock(
    graph: nx.Graph,
    nebula_client: NebulaClient,
):
    time.sleep(6)

    node_schema_factory = {
        "OTHER": nebula_graph_schema.OtherNode,
        "COBOL": nebula_graph_schema.CobolNode,
        "COPY": nebula_graph_schema.CopyNode,
        "JCL_IBM": nebula_graph_schema.JclIbmNode,
        "BMS": nebula_graph_schema.BmsNode,
    }

    nodes = set()

    for node in graph.nodes(data=True):
        node = node[1]
        label = node["label"]

        node_schema = node_schema_factory.get(label, None)

        if node_schema is None:
            continue

        node_instance = node_schema(
            id=PyObjectId(node["id"]),
            name=node["name"],
            group=node["group"],
            status=node["status"],
        )
        nodes.add(node_instance)

    nebula_client.insert_node_batch(list(nodes))

    edges = []
    rank_map: dict[tuple[str, str], int] = {}

    for edge in graph.edges(data=True):
        edge = edge[2]
        source = edge["src"]
        target = edge["dst"]

        edge_type = edge["name"]
        props = edge["props"]

        match edge_type:
            case "JOB_RUN":
                for step in props["steps"]:
                    step_name = step["step_name"]

                    if len(step["statements"]) == 0:
                        rank_map[(source, target)] = (
                            rank_map.get((source, target), 0) + 1
                        )
                        edge = nebula_graph_schema.ExecPgm(
                            source=source,
                            target=target,
                            step_name=step_name,
                            dataset_name=None,
                            rank=rank_map.get((source, target), 0),
                        )

                        edges.append(edge)

                    for statement in step["statements"]:
                        if len(statement["dataset_map_list"]) == 0:
                            rank_map[(source, target)] = (
                                rank_map.get((source, target), 0) + 1
                            )
                            edge = nebula_graph_schema.ExecPgm(
                                source=source,
                                target=target,
                                step_name=step_name,
                                dataset_name=None,
                                rank=rank_map.get((source, target), 0),
                            )
                            edges.append(edge)

                        for dataset in statement["dataset_map_list"]:
                            rank_map[(source, target)] = (
                                rank_map.get((source, target), 0) + 1
                            )
                            edge = nebula_graph_schema.ExecPgm(
                                source=source,
                                target=target,
                                step_name=step_name,
                                dataset_name=dataset["dataset_name"],
                                rank=rank_map.get((source, target), 0),
                            )
                            edges.append(edge)
            case "STATIC_CALL":
                for call in props["calls"]:
                    params = call["identifier"]

                    if len(params) == 0:
                        rank_map[(source, target)] = (
                            rank_map.get((source, target), 0) + 1
                        )
                        edge = nebula_graph_schema.StaticCall(
                            source=source,
                            target=target,
                            procedure=call["paragraph"],
                            param=None,
                            rank=rank_map.get((source, target), 0),
                        )
                        edges.append(edge)

                    for param in call["identifier"]:
                        rank_map[(source, target)] = (
                            rank_map.get((source, target), 0) + 1
                        )
                        edge = nebula_graph_schema.StaticCall(
                            source=source,
                            target=target,
                            procedure=call["paragraph"],
                            param=param,
                            rank=rank_map.get((source, target), 0),
                        )
                        edges.append(edge)

            case "DYNAMIC_CALL":
                for call in props["calls"]:
                    params = call["identifier"]

                    if len(params) == 0:
                        rank_map[(source, target)] = (
                            rank_map.get((source, target), 0) + 1
                        )
                        edge = nebula_graph_schema.DynamicCall(
                            source=source,
                            target=target,
                            procedure=call["paragraph"],
                            param=None,
                            rank=rank_map.get((source, target), 0),
                        )
                        edges.append(edge)

                    for param in call["identifier"]:
                        rank_map[(source, target)] = (
                            rank_map.get((source, target), 0) + 1
                        )
                        edge = nebula_graph_schema.DynamicCall(
                            source=source,
                            target=target,
                            procedure=call["paragraph"],
                            param=param,
                            rank=rank_map.get((source, target), 0),
                        )
                        edges.append(edge)
            case "HAS_COPYBOOK":
                edge = nebula_graph_schema.HasCopybook(
                    source=source, target=target, rank=0
                )
                edges.append(edge)
            case "HAS_INTERACT":
                edge = nebula_graph_schema.HasInteract(
                    source=source, target=target, rank=0
                )
                edges.append(edge)

    print("rank map", rank_map)
    nebula_client.insert_edge_batch(edges)


def get_networkx_mock():
    with open("./app/mock/graph.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    G = nx.Graph()

    for node in data["nodes"]:
        G.add_node(node["id"], **node)
    for edge in data["edges"]:
        G.add_edge(edge["src"], edge["dst"], **edge)

    return G


def load_to_nebula_mock(nebula_client):
    graph = get_networkx_mock()

    networkx_to_nebula_mock(graph, nebula_client)


if __name__ == "__main__":
    nebula_client = get_nebula_client("sample_test")
    load_to_nebula_mock(nebula_client)
