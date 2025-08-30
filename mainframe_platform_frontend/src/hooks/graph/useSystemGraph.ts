import { useMemo } from "react";
// import { useParams } from "react-router-dom";

// import { useGetDependencyGraph } from "@services";
import { useEntryPoint, useFilterGraph } from "@hooks";

export const useSystemGraph = () => {
  const { selectedGroup } = useFilterGraph();
  const { graphData, loadingGraph, total, pageSize } = useEntryPoint();

  const nodes = useMemo(
    () =>
      graphData
        ? selectedGroup.length > 0
          ? graphData.nodes.filter(({ group }) => group.some(item => selectedGroup.includes(item)))
          : graphData.nodes
        : [],
    [selectedGroup, graphData]
  );
  const links = useMemo(() => {
    if (!graphData) return [];
    const setGroupNodes = nodes.map(({ _id }) => _id);

    return graphData.edges
      .filter(
        ({ source, target }) => setGroupNodes.includes(source) && setGroupNodes.includes(target)
      )
      .map(({ source, target, type }) => ({
        source,
        target,
        type
      }));
  }, [nodes]);

  const groups = useMemo(
    () =>
      graphData
        ? graphData?.entry_points
            ?.filter(entry =>
              graphData?.nodes?.some(node => node._id === entry.refer_id && node.status !== "DEAD")
            )
            ?.map(entry => entry.name)
        : [],
    [graphData]
  );
  return {
    nodes,
    groups,
    links,
    loadingGraph,
    total,
    pageSize
  };
};
