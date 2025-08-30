/* eslint-disable unused-imports/no-unused-imports */
import { useMemo } from "react";
import ReactFlowChard, { MarkerType, Position } from "reactflow";

import { Flex, Typography } from "@components";
import { allColors, colorsNodeByStatus } from "@style";
import { Node, NodeWithPosition } from "@types";

import { TextUpdaterNode } from "./TextUpdaterNode";

const nodeTypes = { textUpdater: TextUpdaterNode };
export const legends = [
  { label: "BMS", color: allColors.brand3, types: ["BMS"] },
  { label: "JCL", color: allColors.brand4, types: ["JCL_FUJITSU", "JCL_IBM", "JCL"] },
  { label: "CBL", color: allColors.brand6, types: ["COBOL"] },
  { label: "CPY", color: allColors.brand7, types: ["COPY"] },
  { label: "UTL", color: allColors.brand8, types: ["UTILITY"] },
  { label: "DB", color: allColors.brand9, types: ["DB"] }
];
export function Graph({
  graphData,
  showNode,
  setShowNode
}: {
  graphData: {
    nodes: Array<Node>;
    edges: Array<{
      id: string;
      source: string;
      target: string;
    }>;
  };
  showNode: Record<string, boolean>;
  setShowNode: (nodeShow: Record<string, boolean>) => void;
}) {
  const parentNodes = useMemo(() => {
    const targetNodes = new Set(graphData.edges.map(({ target }) => target));
    return graphData.nodes.map(({ _id }) => _id).filter(id => !targetNodes.has(id));
  }, [graphData]);

  const allChildrenMaps = useMemo(() => {
    const edges = graphData.edges;
    const result: Record<string, Array<string>> = {};

    // Build a lookup for edges based on the source node
    const childrenMap: Record<string, Array<string>> = {};

    // Populate childrenMap with direct children
    edges.forEach(edge => {
      if (!childrenMap[edge.source]) {
        childrenMap[edge.source] = [];
      }
      childrenMap[edge.source].push(edge.target);
    });

    // Function to recursively get all children, including nested ones
    function getAllChildren(source: string, visited = new Set<string>()): Array<string> {
      if (visited.has(source)) return []; // Prevent infinite loops in case of cyclic graphs

      visited.add(source);
      const directChildren = childrenMap[source] || [];
      const allChildren = [...directChildren];

      // Recursively get children of children
      directChildren?.forEach(child => {
        allChildren.push(...getAllChildren(child, visited));
      });

      return allChildren;
    }

    // Build the result using the recursive function
    Object.keys(childrenMap).forEach(source => {
      result[source] = getAllChildren(source);
    });

    return result;
  }, [graphData]);
  // eslint-disable-next-line no-console

  const childrenMaps = useMemo(() => {
    const edges = graphData.edges;
    // Build a lookup for edges based on the source node
    const childrenMap: Record<string, Array<string>> = {};

    // Populate childrenMap with direct children
    edges.forEach(edge => {
      if (!childrenMap[edge.source]) {
        childrenMap[edge.source] = [];
      }
      childrenMap[edge.source].push(edge.target);
    });

    return childrenMap;
  }, [graphData]);

  const graphNodeWithPosition = useMemo(() => {
    if (!parentNodes || parentNodes?.length === 0) return;
    const nodes = childrenMaps;
    let position = graphData.nodes;

    function getDeepestDescendantsCount(node: string) {
      const children = nodes[node] || [];
      if (children.length === 0) return 1; // Leaf node

      let count = 0;
      children.forEach(child => {
        count += getDeepestDescendantsCount(child);
      });
      return count + 1;
    }

    // Function to recursively assign positions
    function setPosition(node: string, parentX: number, parentY: number) {
      // Assign position to the current node
      const x = parentX;
      const y = parentY;
      position = position.map(item => (item._id === node ? { ...item, position: { x, y } } : item));

      // Get children of the current node
      const children = nodes[node] || [];

      // Process each child node recursively
      let currentY = y;
      const childX = parentX + 300;
      children.forEach((child, index) => {
        if (index === 0) {
          // First child is placed bottom right (parentX + 200, parentY + 50)
          setPosition(child, childX, currentY + 25);
        } else {
          // Calculate the total descendants (deepest children) of the previous sibling
          const previousSibling = children[index - 1];
          const deepestChildren = getDeepestDescendantsCount(previousSibling);

          // Shift down the current sibling based on the deepest children of the previous sibling
          currentY += deepestChildren * 75 + 25;
          setPosition(child, childX, currentY);
        }
      });
    }

    // Start assigning positions from the root node (assuming node1 is the root)

    setPosition(parentNodes[0], 100, 50);

    return position as NodeWithPosition[];
  }, [childrenMaps, parentNodes]);

  const graphNodes = useMemo(
    () => graphNodeWithPosition?.filter(({ _id, status }) => status !== "DEAD" && showNode[_id]),
    [graphNodeWithPosition, showNode]
  );

  const handleShowNodeExpand = (id: string) => {
    const childNodes = childrenMaps[id] ?? [];
    const isExpanding = childNodes.every(child => showNode[child]);
    const updatedShowNode = { ...showNode };
    if (isExpanding) {
      for (const child of allChildrenMaps[id]) {
        updatedShowNode[child] = false;
      }
    } else {
      for (const child of childNodes) {
        updatedShowNode[child] = true;
      }
    }
    setShowNode(updatedShowNode);
  };

  const handleShowNodeExpandAll = () => {
    const isExpanding = Object.values(showNode).every(item => item);
    const newObj: Record<string, boolean> = {};
    for (const key in showNode) {
      if (parentNodes.includes(key)) {
        newObj[key] = true;
      } else {
        newObj[key] = !isExpanding;
      }
    }

    setShowNode(newObj);
  };

  const getColorByType = (fileType: string) =>
    legends.find(({ types }) => types.includes(fileType))?.color || allColors.brand8;
  // eslint-disable-next-line no-console
  const nodes = graphNodes?.map(
    ({ fileType, status, data, name, complexity, line_of_code, _id, ...node }, index) => {
      return {
        ...node,
        type: "textUpdater",
        id: _id,
        data: {
          ...data,
          fileType,
          name,
          complexity,
          line_of_code,
          id: _id,
          index,
          status,
          expand: childrenMaps[_id] ? childrenMaps[_id].every(item => showNode[item]) : null,
          expandAll: Object.values(showNode).every(item => item),
          setExpand: () => handleShowNodeExpand(_id),
          setExpandAll: () => handleShowNodeExpandAll()
        },
        sourcePosition: Position.Right,
        targetPosition: Position.Left,
        style: {
          width: "fit-content",
          height: "fit-content",
          border: "none",
          borderRadius: "100px",
          padding: "6px 16px",
          background: getColorByType(fileType),
          outline: ["DEAD", "MISSING"]?.includes(status)
            ? `5px dashed ${colorsNodeByStatus[status as keyof typeof colorsNodeByStatus]}`
            : "none"
        }
      };
    }
  );
  // eslint-disable-next-line no-console
  console.log({ nodes });
  return (
    <Flex
      style={{ padding: "8px 24px", background: allColors.neutral1, borderRadius: "0 0 8px 8px" }}
      gap={12}
      direction='column'
    >
      <Flex justify='space-between' align='center'>
        <Typography level='body-16b' color='primary10'>
          Graph Entry
        </Typography>
        <Flex direction='column' style={{ flexWrap: "wrap", justifyContent: "flex-end" }} gap={8}>
          <Flex style={{ flexWrap: "wrap", justifyContent: "flex-end" }} gap={8}>
            {legends?.map(({ label, color, types }) => (
              <Flex
                key={label}
                gap={4}
                style={{ padding: "4px 12px", background: color, borderRadius: "8px" }}
                center
              >
                <Typography level='h7-body2M' color='neutral1'>
                  {label}
                </Typography>
                <Flex
                  style={{
                    padding: "0px 4px",
                    borderRadius: "8px",
                    background: allColors.neutral1
                  }}
                >
                  <Typography level='h7-body2M' color='secondary10'>
                    {
                      graphData?.nodes?.filter(
                        ({ fileType, status }) => status !== "DEAD" && types?.includes(fileType)
                      )?.length
                    }
                  </Typography>
                </Flex>
              </Flex>
            ))}
          </Flex>
          <Flex align='center' justify='flex-end' gap={10}>
            <Typography color='primary10' level={"caption-12r"}>
              Missing:
            </Typography>
            {Object.keys(colorsNodeByStatus)?.map((key, index) => (
              <Flex gap={4} style={{ alignItems: "center" }} key={index}>
                <Flex
                  style={{
                    width: 24,
                    border: `3px dashed ${
                      colorsNodeByStatus[key as keyof typeof colorsNodeByStatus]
                    }`
                  }}
                />
                {/* <Typography
                  style={{
                    color: colorsNodeByStatus[key as keyof typeof colorsNodeByStatus],
                    textTransform: "capitalize"
                  }}
                  color='primary10'
                  level={"caption-12m"}
                >
                  {key?.toLocaleLowerCase()}
                </Typography> */}
              </Flex>
            ))}
          </Flex>
        </Flex>
      </Flex>
      <ReactFlowChard
        style={{ width: "100%", minHeight: 600 }}
        nodeTypes={nodeTypes}
        nodes={nodes}
        edges={graphData.edges.map(edge => ({
          ...edge,
          type: "smoothstep",
          markerEnd: {
            type: MarkerType.ArrowClosed
          }
        }))}
      ></ReactFlowChard>
    </Flex>
  );
}
