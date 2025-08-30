import { useEffect, useMemo } from "react";
import { useParams } from "react-router-dom";

import { useGetDependencyGraph } from "@services";
import { Edge, EntryPoint, Node } from "@types";

import { useFilterGraph } from "./graph";

type EdgeComputed = { source: string; target: string; id: string };
type ITotalGraph = { nodes: Array<Node>; edges: Array<EdgeComputed> };

export const getConnectedNodesAndEdges = (
  entryId: string,
  totalGraph: ITotalGraph
): ITotalGraph => {
  const visitedNodes = new Set<string>();
  const visitedEdges: EdgeComputed[] = [];

  const traverse = (nodeId: string) => {
    visitedNodes.add(nodeId);

    // Find edges where the source is the current nodeId
    totalGraph.edges.forEach(edge => {
      if (edge.source === nodeId && !visitedNodes.has(edge.target)) {
        visitedEdges.push(edge);
        traverse(edge.target); // Recursively traverse the child node
      }
    });
  };

  traverse(entryId);

  // Filter the nodes that were visited
  const nodes = totalGraph.nodes.filter(node => visitedNodes.has(node._id));

  return { nodes, edges: visitedEdges };
};

export const useEntryPoint = () => {
  const { repoId = "" } = useParams();
  const {
    selectedEntry,
    setSelectedEntry,
    setShowNode,
    showNode,
    nodeLimit,
    loc: locFilter,
    complexity: complexityFilter,
    pageNumber
  } = useFilterGraph();

  const {
    graphData,
    isLoading: loadingGraph,
    total,
    pageSize
  } = useGetDependencyGraph({
    repoId,
    node_limit: Boolean(nodeLimit) ? (nodeLimit as number) : null,
    loc_filter: Boolean(locFilter) ? (locFilter as number) : null,
    complexity_filter: Boolean(complexityFilter) ? (complexityFilter as number) : null,
    page_number: pageNumber
  });

  // eslint-disable-next-line no-console
  console.log("graphData", graphData);

  const entries = useMemo(
    () =>
      graphData?.entry_points
        ?.filter((item: EntryPoint) =>
          graphData?.nodes?.some(
            (node: Node) => node._id === item.refer_id && node.status !== "DEAD"
          )
        )
        ?.map((item: EntryPoint) => {
          return {
            value: item.name,
            type: item.label === "BMS" ? "bms" : "jcl",
            id: item._id,
            refer_id: item.refer_id
          };
        }),
    [graphData?.entry_points, graphData?.nodes, repoId]
  );

  const selectedId = useMemo(
    () => (!!selectedEntry && selectedEntry?.split("-")?.at(0)) || "",
    [selectedEntry]
  );

  const selectedReferId = useMemo(
    () => entries?.find(({ id }) => id === selectedId),
    [selectedEntry, entries]
  )?.refer_id;

  // eslint-disable-next-line no-console
  console.log("selectedReferId", selectedReferId);
  // eslint-disable-next-line no-console
  console.log("selectedEntry", selectedEntry);

  const totalGraph = useMemo(
    () => ({
      edges:
        graphData?.edges?.map(({ target, source }: Edge) => ({
          id: `${source}-${target}`,
          source,
          target
        })) ?? [],
      nodes:
        graphData?.nodes?.map(({ _id, label, name, status, complexity, line_of_code }: Node) => {
          return {
            _id,
            data: { label: name },
            fileType: label,
            complexity,
            line_of_code,
            name,
            status
          };
        }) ?? []
    }),
    [graphData, repoId]
  ) as ITotalGraph;

  const selectedGraph = useMemo(() => {
    if (!selectedReferId || !totalGraph) return { nodes: [], edges: [] };
    return getConnectedNodesAndEdges(selectedReferId, totalGraph);
  }, [selectedReferId, totalGraph]);

  useEffect(() => {
    /**
     * Temporarily disabled logic to expand all nodes on first selection
     */
    // const targetNodes = new Set(selectedGraph.edges.map(({ target }) => target));
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    // const parentNodes = selectedGraph.nodes
    //   .map(({ _id }) => _id)
    //   .filter(id => !targetNodes.has(id));
    const newShowNode = selectedGraph.nodes.reduce<Record<string, boolean>>((result, { _id }) => {
      const next = { ...result };
      next[_id] = true;
      return next;
    }, {});
    const shouldKeepShowNode = Object.keys(newShowNode).every(key => key in showNode);
    if (!shouldKeepShowNode) {
      setShowNode(newShowNode);
    }
  }, [selectedGraph.edges, selectedGraph.nodes]);

  useEffect(() => {
    if (!entries?.length) {
      setSelectedEntry("");
      return;
    }
    const firstEntry = entries[0];
    const isEntryValid = entries?.some(
      ({ value, id, refer_id }) =>
        `${id}-${value}` === selectedEntry && refer_id === selectedReferId
    );

    // eslint-disable-next-line no-console
    console.log("isEntryValid", isEntryValid);
    // const isEntryValid = entries?.some(({ value, id }) => `${id}-${value}` === selectedEntry);
    if (!isEntryValid && typeof selectedEntry === "string") {
      setSelectedEntry(`${firstEntry.id}-${firstEntry.value}`);
    }
  }, [entries, selectedEntry]);

  return {
    graphData,
    total,
    pageSize,
    loadingGraphData: loadingGraph,
    loadingGraph,
    entries,
    totalGraph,
    selectedGraph,
    selectedId,
    selectedReferId
  };
};
