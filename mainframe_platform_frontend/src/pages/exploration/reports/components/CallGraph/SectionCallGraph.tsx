/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable unused-imports/no-unused-vars */
/* eslint-disable @typescript-eslint/no-non-null-assertion */
import {
  Background,
  BackgroundVariant,
  Controls,
  ReactFlow,
  useEdgesState,
  useNodesState,
  Panel,
  MiniMap,
  ReactFlowInstance,
  Node,
  Edge,
  NodeChange,
  MarkerType
} from "@xyflow/react";
import { useEffect, useMemo, useState, useRef, useCallback } from "react";
import { Button, Tooltip } from "antd";
import { UndoOutlined, LockOutlined, UnlockOutlined, ReloadOutlined } from "@ant-design/icons";

import "@xyflow/react/dist/style.css";

import { addPropertiesToItems, getColorsWithOpacity } from "@utils";
import { SummarizationValue, TypeNodeEnum } from "@types";
import { allColors } from "@style";

import Legends from "../../Legends";

import CustomNode from "./CustomNode";
import { baseColors, processGraphData, ProcessGraphData } from "./graphUtil";
import ControlPanel from "./components/ControlPanel";

// Define the node data type that matches what's expected by CustomNode
export type CustomNodeData = {
  label: string;
  type?: string;
  isRoot?: boolean;
  hasChildren?: boolean;
  summarization?: SummarizationValue;
  level?: number;
  parentNode?: string | null;
};

// Define a type for node hierarchy information
export type NodeHierarchyInfo = {
  id: string;
  parentId: string | null;
  childrenIds: string[];
  level: number;
};

// Our component needs this specific type of data
const HorizontalFlow = ({ dataFlow, programId }: ProcessGraphData) => {
  // Configuration
  const spacing = { x: 650, y: 120 };

  // Process initial graph data
  const { nodes: initialNodes, edges: initialEdges } = useMemo(
    () => processGraphData(dataFlow, programId, spacing),
    [dataFlow, programId]
  );

  // State and refs
  const renderedNodesRef = useRef<Node[]>([]);
  const renderedEdgesRef = useRef<Edge[]>([]);
  const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges);
  const [searchText, setSearchText] = useState("");
  const [filteredNodes, setFilteredNodes] = useState<Node[]>([]);
  const [panelCollapsed, setPanelCollapsed] = useState(true);
  const [nodesMovable, setNodesMovable] = useState(false);
  const [hasNodesMoved, setHasNodesMoved] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [edgesMissing, setEdgesMissing] = useState(false);
  const [collapsedNodes, setCollapsedNodes] = useState<Set<string>>(new Set());
  const reactFlowInstance = useRef<ReactFlowInstance | null>(null);
  const initialPositions = useRef<Record<string, { x: number; y: number }>>({});
  const maxRenderAttempts = useRef(0);
  const renderRetryTimer = useRef<NodeJS.Timeout | null>(null);

  // Prevent auto-fit when just expanding/collapsing nodes
  const [shouldAutoFit, setShouldAutoFit] = useState(true);
  const isFilterChangeRef = useRef(false);

  // Keep track of node hierarchy for collapsing/expanding
  const nodeHierarchy = useRef<Map<string, NodeHierarchyInfo>>(new Map());

  // Extract unique node levels
  const nodeLevels = useMemo(() => {
    const levels = new Set<number>();
    initialNodes?.forEach((node: Node) => {
      if (typeof node.data?.level === "number") {
        levels.add(node.data.level);
      }
    });
    return Array.from(levels).sort((a, b) => a - b);
  }, [initialNodes]);

  const [selectedLevels, setSelectedLevels] = useState<number[]>(nodeLevels);

  // Initialize selected levels
  useEffect(() => {
    setSelectedLevels(nodeLevels);
  }, [nodeLevels]);

  // Cleanup timers on unmount
  useEffect(() => {
    return () => {
      if (renderRetryTimer.current) {
        clearTimeout(renderRetryTimer.current);
      }
    };
  }, []);

  // Store initial node positions
  useEffect(() => {
    const positions: Record<string, { x: number; y: number }> = {};
    initialNodes?.forEach((node: Node) => {
      positions[node.id] = { x: node.position.x, y: node.position.y };
    });
    initialPositions.current = positions;
  }, [initialNodes]);

  // Build node hierarchy for expansion/collapse functionality
  useEffect(() => {
    const hierarchy = new Map<string, NodeHierarchyInfo>();

    // First pass: create entries for each node
    initialNodes?.forEach((node: Node) => {
      hierarchy.set(node.id, {
        id: node.id,
        parentId: typeof node.data?.parentNode === "string" ? node.data.parentNode : null,
        childrenIds: [],
        level: typeof node.data?.level === "number" ? node.data.level : 0
      });
    });

    // Second pass: populate children arrays
    initialEdges?.forEach((edge: Edge) => {
      const sourceInfo = hierarchy.get(edge.source);
      const targetInfo = hierarchy.get(edge.target);

      if (sourceInfo && targetInfo) {
        sourceInfo.childrenIds.push(edge.target);

        // Update parent reference if not already set
        if (!targetInfo.parentId) {
          targetInfo.parentId = edge.source;
        }
      }
    });

    nodeHierarchy.current = hierarchy;
  }, [initialNodes, initialEdges]);

  // Initialize the graph with nodes and edges
  useEffect(() => {
    maxRenderAttempts.current = 0;
    setIsLoading(true);
    setEdgesMissing(false);

    if (renderRetryTimer.current) {
      clearTimeout(renderRetryTimer.current);
      renderRetryTimer.current = null;
    }

    // Clear nodes and edges to start fresh
    setNodes([]);
    setEdges([]);

    // Staggered rendering to improve performance
    const timer1 = setTimeout(() => {
      // Enhance nodes with parent information
      const enhancedNodes = initialNodes.map(node => ({
        ...node,
        data: {
          ...node.data,
          parentNode: nodeHierarchy.current.get(node.id)?.parentId || null
        }
      }));

      renderedNodesRef.current = enhancedNodes;
      setNodes(enhancedNodes);

      const timer2 = setTimeout(() => {
        renderedEdgesRef.current = initialEdges;
        setEdges(initialEdges);
        setIsLoading(false);

        // Check if edges are properly rendered
        const timer3 = setTimeout(() => {
          if (
            initialEdges.length > 0 &&
            (!reactFlowInstance.current?.getEdges().length ||
              reactFlowInstance.current?.getEdges().length !== initialEdges.length)
          ) {
            setEdgesMissing(true);
          }
        }, 500);

        // Fit view to show all nodes
        const timer4 = setTimeout(() => {
          if (reactFlowInstance.current) {
            reactFlowInstance.current.fitView({ padding: 0.2 });
          }
        }, 800);
      }, 300);
    }, 100);

    // Cleanup function
    return () => {
      if (renderRetryTimer.current) {
        clearTimeout(renderRetryTimer.current);
        renderRetryTimer.current = null;
      }
    };
  }, [initialNodes, initialEdges, setNodes, setEdges]);

  // Check for missing edges and retry rendering if needed
  const checkEdgesAndRetry = useCallback(() => {
    if (maxRenderAttempts.current >= 3) {
      return;
    }

    if (
      initialEdges.length > 0 &&
      (!reactFlowInstance.current?.getEdges().length ||
        reactFlowInstance.current?.getEdges().length !== initialEdges.length)
    ) {
      maxRenderAttempts.current += 1;
      setIsLoading(true);

      // Reset nodes first
      setNodes([]);
      const timer1 = setTimeout(() => {
        setNodes(initialNodes);
        const timer2 = setTimeout(() => {
          // Create refreshed edges with unique IDs
          const refreshedEdges: Edge[] = initialEdges.map((edge: Edge, idx: number) => ({
            ...edge,
            id: edge.id || `edge-${idx}-${Date.now()}`
          }));

          setEdges(refreshedEdges);
          setIsLoading(false);

          renderRetryTimer.current = setTimeout(() => {
            if (reactFlowInstance.current) {
              reactFlowInstance.current.fitView({ padding: 0.2 });

              if (reactFlowInstance.current.getEdges().length !== initialEdges.length) {
                setEdgesMissing(true);
              } else {
                setEdgesMissing(false);
              }
            }
          }, 500);
        }, 300);
      }, 100);
    }
  }, [initialEdges, initialNodes, setNodes, setEdges]);

  // Check if nodes have moved from their original positions
  const checkNodesMovement = useCallback(
    (currentNodes: Node[]) => {
      if (!hasNodesMoved && initialPositions.current) {
        for (const node of currentNodes) {
          const initial = initialPositions.current[node.id];
          if (initial && (initial.x !== node.position.x || initial.y !== node.position.y)) {
            setHasNodesMoved(true);
            break;
          }
        }
      }
    },
    [hasNodesMoved]
  );

  // Handle node drag stop event
  const handleNodeDragStop = useCallback(() => {
    checkNodesMovement(nodes);
  }, [nodes, checkNodesMovement]);

  // Reset graph to original layout
  const resetGraphLayout = useCallback(() => {
    if (initialPositions.current && Object.keys(initialPositions.current).length) {
      setIsLoading(true);
      const resetNodes = nodes.map(node => {
        const initialPos = initialPositions.current[node.id];
        if (initialPos) {
          return {
            ...node,
            position: { x: initialPos.x, y: initialPos.y }
          };
        }
        return node;
      });

      setTimeout(() => {
        setNodes(resetNodes);
        setHasNodesMoved(false);
        setIsLoading(false);

        setTimeout(() => {
          if (reactFlowInstance.current) {
            reactFlowInstance.current.fitView({ padding: 0.2 });
          }
        }, 100);
      }, 50);
    }
  }, [nodes, setNodes]);

  // Toggle node dragging capability
  const toggleNodeDragging = useCallback(() => {
    setNodesMovable(prev => !prev);
  }, []);

  // Force reload the graph (for fixing edge rendering issues)
  const handleForceReload = useCallback(() => {
    setIsLoading(true);
    maxRenderAttempts.current = 0;
    setEdgesMissing(false);

    if (renderRetryTimer.current) {
      clearTimeout(renderRetryTimer.current);
      renderRetryTimer.current = null;
    }

    setNodes([]);
    setEdges([]);

    // Staggered rendering with new IDs for edges
    const timer1 = setTimeout(() => {
      // Add draggable property to nodes
      const nodesWithDrag = initialNodes.map((node: Node) => ({
        ...node,
        draggable: nodesMovable
      }));

      setNodes(nodesWithDrag);

      const timer2 = setTimeout(() => {
        // Create refreshed edges with new IDs
        const refreshedEdges = initialEdges.map((edge: Edge, idx: number) => ({
          ...edge,
          id: `edge-${idx}-${Date.now()}`,
          type: "smoothstep",
          animated: true
        }));

        setEdges(refreshedEdges);

        const timer3 = setTimeout(() => {
          setIsLoading(false);
          if (reactFlowInstance.current) {
            reactFlowInstance.current.fitView({ padding: 0.2 });
          }

          const timer4 = setTimeout(() => {
            if (
              reactFlowInstance.current &&
              reactFlowInstance.current.getEdges().length !== initialEdges.length
            ) {
              setEdgesMissing(true);
            } else {
              setEdgesMissing(false);
            }
          }, 500);
        }, 200);
      }, 300);
    }, 100);
  }, [initialNodes, initialEdges, setNodes, setEdges, nodesMovable]);

  // Handle node position changes
  const handleNodesChange = useCallback(
    (changes: NodeChange[]) => {
      onNodesChange(changes);

      const hasPositionChange = changes.some(
        change => change.type === "position" && !change.dragging
      );

      if (hasPositionChange) {
        setTimeout(() => checkNodesMovement(nodes), 50);
      }
    },
    [onNodesChange, nodes, checkNodesMovement]
  );

  // Function to get all descendant node IDs (recursive)
  const getAllDescendants = useCallback((nodeId: string, visited = new Set<string>()): string[] => {
    if (visited.has(nodeId)) return [];
    visited.add(nodeId);

    const nodeInfo = nodeHierarchy.current.get(nodeId);
    if (!nodeInfo || !nodeInfo.childrenIds.length) return [];

    const descendants = [...nodeInfo.childrenIds];

    for (const childId of nodeInfo.childrenIds) {
      descendants.push(...getAllDescendants(childId, visited));
    }

    return descendants;
  }, []);

  // Toggle node expansion/collapse
  const toggleNodeExpansion = useCallback((nodeId: string) => {
    // Disable auto-fitting when toggling nodes
    setShouldAutoFit(false);
    isFilterChangeRef.current = false;

    setCollapsedNodes(prevCollapsed => {
      const newCollapsed = new Set(prevCollapsed);

      if (newCollapsed.has(nodeId)) {
        // Expand this node
        newCollapsed.delete(nodeId);
      } else {
        // Collapse this node
        newCollapsed.add(nodeId);
      }

      return newCollapsed;
    });
  }, []);

  // Expand/Collapse All Functions
  const handleExpandAll = useCallback(() => {
    setCollapsedNodes(new Set());
  }, []);

  const handleCollapseAll = useCallback(() => {
    const nodesToCollapse = new Set<string>();

    // Find all nodes at level 1 (not beyond level 1) that have children
    initialNodes.forEach((node: Node) => {
      const nodeInfo = nodeHierarchy.current.get(node.id);
      const nodeLevel = typeof node.data?.level === "number" ? node.data.level : 0;

      // Only collapse nodes AT level 1 that have children
      if (nodeInfo && nodeInfo.childrenIds.length > 0 && nodeLevel === 1) {
        nodesToCollapse.add(node.id);
      }
    });

    setCollapsedNodes(nodesToCollapse);
  }, [initialNodes]);

  // Improved level control - Set expansion state to exactly the clicked level
  const handleLevelControl = useCallback(
    (targetLevel: number) => {
      setCollapsedNodes(prevCollapsed => {
        const newCollapsed = new Set<string>();

        // Process all nodes and set collapsed state based on level
        initialNodes.forEach((node: Node) => {
          const nodeLevel = typeof node.data?.level === "number" ? node.data.level : 0;
          const nodeInfo = nodeHierarchy.current.get(node.id);

          // If node has children and is DEEPER than targetLevel, collapse it
          if (nodeInfo && nodeInfo.childrenIds.length > 0) {
            if (nodeLevel >= targetLevel) {
              newCollapsed.add(node.id);
            }
          }
        });

        return newCollapsed;
      });
    },
    [initialNodes]
  );

  // Handle level filter changes with auto-fit
  const handleLevelChange = useCallback((checkedValues: number[]) => {
    // Enable auto-fitting for level changes
    setShouldAutoFit(true);
    isFilterChangeRef.current = true;
    setSelectedLevels(checkedValues);
  }, []);

  // Handle search text changes with auto-fit
  const handleSearch = useCallback((value: string) => {
    // Enable auto-fitting for search changes
    setShouldAutoFit(true);
    isFilterChangeRef.current = true;
    setSearchText(value);
  }, []);

  // Filter nodes based on level selection, search text, and collapsed state
  useEffect(() => {
    if (!initialNodes?.length) return;

    // Skip expensive filtering if panel is collapsed and no active filters or collapsed nodes
    if (
      panelCollapsed &&
      !searchText.trim() &&
      selectedLevels.length === nodeLevels.length &&
      collapsedNodes.size === 0
    ) {
      // Reset to initial state
      setNodes(initialNodes);
      setEdges(initialEdges);
      return;
    }

    const tempNodes = initialNodes.map((node: Node) => {
      const nodeLevel = typeof node.data?.level === "number" ? node.data.level : 0;
      const isLevelMatch = selectedLevels.length > 0 && selectedLevels.includes(nodeLevel);

      const label = String(node.data?.label || "");
      const searchLower = searchText.toLowerCase().trim();
      const isSearchMatch = !searchLower || label.toLowerCase().includes(searchLower);

      // Check if any parent is collapsed
      let isParentCollapsed = false;
      let currentParentId: string | null =
        typeof node.data?.parentNode === "string" ? node.data.parentNode : null;

      while (currentParentId && !isParentCollapsed) {
        if (collapsedNodes.has(currentParentId)) {
          isParentCollapsed = true;
          break;
        }
        const parentInfo = nodeHierarchy.current.get(currentParentId);
        currentParentId = parentInfo?.parentId || null;
      }

      // Node is visible if it matches level filter AND search filter AND no parent is collapsed
      const isVisible = isLevelMatch && !isParentCollapsed;

      // Preserve all original styling, only modify opacity/display for filtering
      return {
        ...node,
        style: {
          ...node.style,
          opacity: !isVisible ? 0 : isSearchMatch ? 1 : 0.2,
          display: !isVisible ? "none" : "block"
        },
        draggable: nodesMovable
      };
    });

    const searchMatchNodes = tempNodes.filter(
      (node: Node) => node.style?.display !== "none" && node.style?.opacity === 1
    );

    // Filter edges to only include connections between visible nodes
    const visibleNodeIds = new Set(
      tempNodes.filter(node => node.style?.display !== "none").map(node => node.id)
    );

    const filteredEdges = initialEdges.filter(
      edge => visibleNodeIds.has(edge.source) && visibleNodeIds.has(edge.target)
    );

    setNodes(tempNodes);
    setEdges(filteredEdges);
    setFilteredNodes(searchMatchNodes);

    // Only fit view after filtering if explicitly requested (search, level change)
    // or if it's the first render with filters applied
    if (
      shouldAutoFit &&
      searchMatchNodes.length > 0 &&
      reactFlowInstance.current &&
      (isFilterChangeRef.current || searchText.trim() || selectedLevels.length < nodeLevels.length)
    ) {
      const timeoutId = setTimeout(() => {
        if (reactFlowInstance.current) {
          reactFlowInstance.current.fitView({
            padding: 0.2,
            includeHiddenNodes: false,
            nodes: searchMatchNodes.map(node => ({ id: node.id }))
          });
        }
        // Reset after fitting
        setShouldAutoFit(false);
      }, 300);

      return () => clearTimeout(timeoutId);
    }
  }, [
    searchText,
    selectedLevels,
    initialNodes,
    initialEdges,
    nodeLevels,
    setNodes,
    setEdges,
    nodesMovable,
    panelCollapsed,
    collapsedNodes,
    shouldAutoFit
  ]);

  // Handle fit view button click
  const handleFitView = useCallback(() => {
    if (reactFlowInstance.current) {
      reactFlowInstance.current.fitView({ padding: 0.2 });
      setTimeout(checkEdgesAndRetry, 300);
    }
  }, [checkEdgesAndRetry]);

  // Check if a node is visible based on both level filter and collapse state
  const isNodeVisible = useCallback(
    (node: Node): boolean => {
      // Check level filter first (higher priority)
      const nodeLevel = typeof node.data?.level === "number" ? node.data.level : 0;
      const levelMatch = selectedLevels.includes(nodeLevel);
      if (!levelMatch) return false;

      // Check if any parent is collapsed
      let currentParentId: string | null =
        typeof node.data?.parentNode === "string" ? node.data.parentNode : null;
      while (currentParentId) {
        if (collapsedNodes.has(currentParentId)) {
          return false;
        }
        const parentInfo = nodeHierarchy.current.get(currentParentId);
        currentParentId = parentInfo?.parentId || null;
      }

      return true;
    },
    [selectedLevels, collapsedNodes]
  );

  // Toggle control panel visibility
  const togglePanel = useCallback(() => {
    setPanelCollapsed(prev => !prev);
  }, []);

  // Check if a node is collapsed
  const isNodeCollapsed = useCallback(
    (nodeId: string) => {
      return collapsedNodes.has(nodeId);
    },
    [collapsedNodes]
  );

  // Extract unique node types for legend
  const typesNode = useMemo(
    () =>
      Array.from(
        new Set(initialNodes?.map((item: any) => item?.data?.type).filter(Boolean))
      ) as (keyof typeof TypeNodeEnum)[],
    [initialNodes]
  );

  // Register custom node types
  const nodeTypes = useMemo(
    () => ({
      myCustomNode: (props: any) => (
        <CustomNode
          {...props}
          onToggleExpand={toggleNodeExpansion}
          isCollapsed={typeof props.id === "string" ? isNodeCollapsed(props.id) : false}
        />
      )
    }),
    [toggleNodeExpansion, isNodeCollapsed]
  );

  return (
    <>
      <ReactFlow
        nodesConnectable={false}
        key={programId}
        nodes={nodes}
        edges={edges}
        proOptions={{ hideAttribution: true }}
        nodeTypes={nodeTypes}
        onNodesChange={handleNodesChange}
        onEdgesChange={onEdgesChange}
        onNodeDragStop={handleNodeDragStop}
        fitView
        minZoom={0.1}
        maxZoom={2}
        defaultEdgeOptions={{
          type: "smoothstep",
          animated: true,
          style: { strokeWidth: 2 },
          markerEnd: {
            type: MarkerType.ArrowClosed,
            width: 20,
            height: 20
          }
        }}
        attributionPosition='bottom-left'
        onInit={instance => {
          reactFlowInstance.current = instance;
          setTimeout(() => {
            instance.fitView({ padding: 0.2 });
            setTimeout(checkEdgesAndRetry, 500);
          }, 300);
        }}
        nodesDraggable={nodesMovable}
      >
        {/* Background elements */}
        <Background color='#ccc' variant={BackgroundVariant.Dots} />
        <Controls />
        <MiniMap
          nodeStrokeWidth={3}
          zoomable
          pannable
          style={{ backgroundColor: "#fff", border: "1px solid #f0f0f0" }}
        />

        {/* Control panel with updated expand/collapse functionality */}
        <Panel position='top-left'>
          <ControlPanel
            programId={programId}
            searchText={searchText}
            selectedLevels={selectedLevels}
            nodeLevels={nodeLevels}
            filteredNodes={filteredNodes}
            isPanelCollapsed={panelCollapsed}
            onSearch={handleSearch}
            onLevelChange={handleLevelChange}
            onFitView={handleFitView}
            onTogglePanel={togglePanel}
            onExpandAll={handleExpandAll}
            onCollapseAll={handleCollapseAll}
            onLevelControl={handleLevelControl}
          />
        </Panel>

        {/* Action buttons */}
        <Panel
          position='top-right'
          style={{ display: "flex", flexDirection: "column", gap: "10px" }}
        >
          <Tooltip title='Reload graph (fixes missing edges)' placement='left'>
            <Button
              type='primary'
              shape='circle'
              icon={<ReloadOutlined />}
              onClick={handleForceReload}
              loading={isLoading}
              style={{
                boxShadow: "0px 2px 8px rgba(0, 0, 0, 0.15)",
                backgroundColor: edgesMissing ? allColors.error : allColors.primary6,
                borderColor: edgesMissing ? allColors.error : allColors.primary6
              }}
            />
          </Tooltip>

          {hasNodesMoved && (
            <Tooltip title='Reset to original layout' placement='left'>
              <Button
                type='primary'
                shape='circle'
                icon={<UndoOutlined />}
                onClick={resetGraphLayout}
                style={{
                  boxShadow: "0px 2px 8px rgba(0, 0, 0, 0.15)",
                  backgroundColor: allColors.warning,
                  borderColor: allColors.warning
                }}
              />
            </Tooltip>
          )}

          <Tooltip title={nodesMovable ? "Lock nodes" : "Unlock nodes to move"} placement='left'>
            <Button
              type={nodesMovable ? "default" : "primary"}
              shape='circle'
              icon={nodesMovable ? <UnlockOutlined /> : <LockOutlined />}
              onClick={toggleNodeDragging}
              style={{ boxShadow: "0px 2px 8px rgba(0, 0, 0, 0.15)" }}
            />
          </Tooltip>
        </Panel>
      </ReactFlow>

      {/* Legend for node types */}
      {typesNode?.length > 0 && (
        <Legends
          data={addPropertiesToItems(
            typesNode,
            (type, i) => ({
              label: type || "",
              id: type || i,
              style: {
                color: getColorsWithOpacity(baseColors, TypeNodeEnum[type], 0.5),
                border: `1px solid ${getColorsWithOpacity(baseColors, TypeNodeEnum[type], 1)}`
              }
            }),
            true
          )}
        />
      )}
    </>
  );
};

export default HorizontalFlow;
