/* eslint-disable @typescript-eslint/no-shadow */
/* eslint-disable @typescript-eslint/naming-convention */
/* eslint-disable @typescript-eslint/no-non-null-assertion */
import { Edge, MarkerType, Node, Position } from "@xyflow/react";

import { TreeNode as BaseTreeNode, SummarizationData, TypeNodeEnum } from "@types";
import { getColorsWithOpacity } from "@utils";

// Extend the TreeNode type to include the missing properties
interface TreeNode extends BaseTreeNode {
  style?: React.CSSProperties;
  targetPosition?: Position;
  sourcePosition?: Position;
  edgeStyle?: {
    stroke: string;
    strokeWidth: number;
    strokeDasharray: string;
  };
  edgeMarker?: {
    type: MarkerType;
    color: string;
    height: number;
    width: number;
  };
  isExecFlow?: boolean;
  parentId?: string | null;
}

export const baseColors = [
  [255, 87, 51],
  [255, 51, 161],
  [51, 255, 87],
  [161, 51, 255],
  [51, 87, 255],
  [51, 255, 243],
  [255, 199, 51],
  [255, 51, 51],
  [51, 161, 255],
  [161, 255, 51]
];

export type NodeBase = { label: string; children: NodeBase[] } & Node;

export interface EdgeItem {
  source: string;
  target: string;
  type: string;
}

export interface GraphData {
  nodes: TreeNode[];
  edges: EdgeItem[];
}

export const { Left, Right } = Position;

export interface ProcessGraphData {
  dataFlow: { exec_flow_tree: TreeNode; exec_flow: GraphData; summarizations: SummarizationData };
  programId: string;
}

export const convertToReactFlow = (
  tree: TreeNode,
  summarizations: SummarizationData,
  position: { x: number; y: number },
  spacing: { x: number; y: number }
): { nodes: Node[]; edges: Edge[] } => {
  if (!tree) {
    return { nodes: [], edges: [] };
  }

  const nodes: Node[] = [];
  const edges: Edge[] = [];
  const nodeIds = new Set<string>();

  // Increase horizontal spacing specifically between nodes
  const horizontalSpacingMultiplier = 1.2;

  const traverseTree = (
    node: TreeNode,
    summarizations: SummarizationData,
    depth = 0,
    offset = 0,
    parentId: string | null = null
  ): number => {
    // Safety checks
    if (!node || !node.id) return offset;

    const uniqueNodeId = parentId ? `${node.id}-${parentId}` : node.id;

    // Skip duplicate nodes
    if (nodeIds.has(uniqueNodeId)) {
      return offset;
    }

    nodeIds.add(uniqueNodeId);

    const hasChildren = node?.children && node.children.length > 0;
    const colorIndex = Number(
      TypeNodeEnum[node.type as keyof typeof TypeNodeEnum] ?? TypeNodeEnum.other
    );
    const currentColorBorder = getColorsWithOpacity(baseColors, colorIndex);
    const currentColor = getColorsWithOpacity(baseColors, colorIndex, 0.4);

    // Apply the horizontal spacing multiplier here
    const horizontalPosition = position.x + depth * spacing.x * horizontalSpacingMultiplier;

    // If the node already has style information from the API, use it
    // Otherwise, generate the style based on type
    const nodeStyle = node.style || {
      background: currentColor,
      borderRadius: "6px",
      border: `1.5px solid ${currentColorBorder}`,
      fontWeight: node.isRoot ? 700 : 500,
      width: 180,
      fontSize: "12px",
      padding: "4px"
    };

    // Create node preserving any existing style and adding parent reference
    nodes.push({
      id: uniqueNodeId,
      data: {
        label: `${node.label || ""}`,
        type: node.type,
        isRoot: node.isRoot || node.level === 0,
        hasChildren,
        summarization: summarizations?.[node?.label],
        level: node.level,
        parentNode: parentId // Store parent reference to support collapse functionality
      },
      position: { x: horizontalPosition, y: position.y + offset * spacing.y },
      targetPosition: node.targetPosition || (node.isRoot ? Right : Left),
      sourcePosition: node.sourcePosition || (hasChildren ? Right : Left),
      type: "myCustomNode",
      style: nodeStyle
    });

    // Create edge if there's a parent
    if (parentId) {
      // Create an explicit and unique edge ID similar to the console.log data
      const timestamp = Date.now();
      const edgeId = `edge-${parentId}-to-${uniqueNodeId}-${timestamp}`;

      // Use edge style from API data if available
      const edgeStyle = node.edgeStyle || {
        stroke: currentColorBorder,
        strokeWidth: 2,
        strokeDasharray: "none"
      };

      const edgeMarker = node.edgeMarker || {
        type: MarkerType.ArrowClosed,
        color: currentColorBorder,
        height: 20,
        width: 20
      };

      edges.push({
        id: edgeId,
        source: parentId,
        target: uniqueNodeId,
        type: "smoothstep",
        animated: true,
        style: edgeStyle,
        markerEnd: edgeMarker,
        zIndex: 1000 - depth,
        data: {
          level: node.level,
          edgeType: "parent-child",
          sourceType: node.type
        }
      });
    }

    let currentOffset = offset;

    if (Array.isArray(node.children)) {
      node.children.forEach(child => {
        // Skip null children
        if (!child || !child.id) return;

        // Set parent reference in child node
        const childNode = { ...child } as TreeNode;
        childNode.parentId = uniqueNodeId;

        currentOffset = traverseTree(
          childNode,
          summarizations,
          depth + 1,
          currentOffset,
          uniqueNodeId
        );
      });
    }

    // Further increase space between siblings for better vertical spacing
    return hasChildren ? currentOffset + 0.3 : offset + 1.5;
  };

  traverseTree(tree, summarizations);

  // Ensure all edges have valid source and target nodes
  const validEdges = edges.filter(edge => {
    return nodeIds.has(edge.source) && nodeIds.has(edge.target);
  });

  return {
    nodes,
    edges: validEdges
  };
};

export const processGraphData = (
  data: { exec_flow_tree?: TreeNode; exec_flow?: GraphData; summarizations: SummarizationData },
  programId: string,
  position = { x: 0, y: 0 },
  spacing = { x: 250, y: 60 }
): { nodes: Node[]; edges: Edge[] } => {
  const { exec_flow, exec_flow_tree, summarizations } = data || {};

  // Preserve original styles and properties from incoming data
  // This ensures we don't override any styling that's already in the nodes/edges
  if (exec_flow_tree) {
    // If any node in the tree has style info, keep it intact
    const preserveStyles = (node: TreeNode): TreeNode => {
      if (!node) return node;

      // Preserve node styles if they exist
      const updatedNode = { ...node };

      // Recursively preserve styles for children
      if (Array.isArray(node.children)) {
        updatedNode.children = node.children.map(child => preserveStyles(child as TreeNode));
      }

      return updatedNode;
    };

    const processedTree = preserveStyles(exec_flow_tree);
    return convertToReactFlow(processedTree, summarizations, position, spacing);
  }

  if (!exec_flow) {
    return { nodes: [], edges: [] };
  }

  const buildTree = (data: GraphData): TreeNode | null => {
    if (!data || !data.nodes) return null;

    const nodeMap = new Map<string, TreeNode>();
    const childSet = new Set<string>();
    const sectionCount = new Map<string, number>();

    data.nodes.forEach(node => {
      if (!node || !node.id) return;

      const count = (sectionCount.get(node.id) || 0) + 1;
      if (count > 1) return;
      sectionCount.set(node.id, count);

      nodeMap.set(node.id, {
        id: node.id,
        isRoot: false,
        label: node.name || String(node.id),
        type: node.type,
        children: [],
        level: 0
      });
    });

    if (Array.isArray(data.edges)) {
      data.edges.forEach(({ source, target }) => {
        if (!source || !target) return;

        const sourceNode = nodeMap.get(source);
        const targetNode = nodeMap.get(target);

        if (sourceNode && targetNode) {
          if (!Array.isArray(sourceNode.children)) {
            sourceNode.children = [];
          }
          sourceNode.children.push(targetNode);
          childSet.add(target);
        }
      });
    }

    const rootNode = data.nodes.find(node => node && node.id && !childSet.has(node.id));
    const rootId = rootNode?.id;

    if (rootId && nodeMap.has(rootId)) {
      const root = nodeMap.get(rootId)!;
      root.isRoot = true;
      root.label = programId;
      root.isExecFlow = true;
      root.type = TypeNodeEnum[0] as keyof typeof TypeNodeEnum;

      return root;
    }

    return null;
  };

  const assignLevels = (
    node: TreeNode,
    level = 0,
    levelMap = new Map<string, number[]>()
  ): TreeNode => {
    if (!node || !node.id) {
      return node;
    }

    if (!levelMap.has(node.id)) {
      levelMap.set(node.id, []);
    }

    levelMap.get(node.id)!.push(level);

    const newNode = { ...node, level, children: [] as TreeNode[] };

    if (Array.isArray(node.children)) {
      newNode.children = node.children.map(child => {
        const maxParentLevel = Math.max(...(levelMap.get(node.id) || [0]));
        return assignLevels(child as TreeNode, maxParentLevel + 1, levelMap);
      });
    }

    return newNode;
  };

  const tree = buildTree(exec_flow);
  if (!tree) return { nodes: [], edges: [] };

  const processedTree = assignLevels(tree);
  const { nodes, edges } = convertToReactFlow(processedTree, summarizations, position, spacing);

  // Ensure edge IDs are unique and match the pattern from console.log data
  const timestamp = Date.now();
  const processedEdges = edges.map(edge => {
    return {
      ...edge,
      id: edge.id || `edge-${edge.source}-to-${edge.target}-${timestamp}`,
      type: "smoothstep",
      animated: true,
      style: {
        ...(edge.style || {}),
        strokeWidth: 2,
        strokeDasharray: "none",
        stroke: edge.style?.stroke || getColorsWithOpacity(baseColors, 0)
      },
      markerEnd: {
        ...(typeof edge.markerEnd === "object" ? edge.markerEnd : {}),
        type: MarkerType.ArrowClosed,
        height: 20,
        width: 20
      }
    };
  });

  // Create a nodeMap for quick lookup
  const nodeMap = new Map<string, Node>();
  nodes.forEach(node => nodeMap.set(node.id, node));

  // Double-check all edges have valid sources and targets
  const validEdges = processedEdges.filter(edge => {
    return nodeMap.has(edge.source) && nodeMap.has(edge.target);
  });

  return {
    nodes,
    edges: validEdges
  };
};
