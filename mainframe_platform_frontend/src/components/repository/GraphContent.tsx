import { useSelector } from "react-redux";
import { useCallback, useEffect } from "react";
import {
  useNodesState,
  useEdgesState,
  addEdge,
  MarkerType,
  EdgeProps,
  BaseEdge,
  EdgeLabelRenderer,
  EdgeTypes,
  getSmoothStepPath
} from "reactflow";

import { fileSelector } from "@store";
import { FlowChart, FlowChartEdge } from "@components";
import { NodeModel } from "@types";

import { CustomEdgeLabel } from "./styles";

export const CustomEdge: React.FC<EdgeProps> = ({
  id,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  markerEnd,
  style,
  data
}: any) => {
  const [edgePath, labelX, labelY] = getSmoothStepPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition
  });

  return (
    <>
      <BaseEdge id={id} path={edgePath} markerEnd={markerEnd} style={style} />
      <EdgeLabelRenderer>
        <CustomEdgeLabel
          style={{
            transform: `translate(-50%, -50%) translate(${labelX + 40}px,${labelY}px)`
          }}
          className='nodrag nopan'
        >
          {data?.label}
        </CustomEdgeLabel>
      </EdgeLabelRenderer>
    </>
  );
};

export const GraphContent: React.FC = () => {
  const data = useSelector(fileSelector.selectData);
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  const onConnect = useCallback((params: any) => setEdges(eds => addEdge(params, eds)), [setEdges]);
  const handleSortNode = (listNode: NodeModel[]) => {
    if (!listNode?.length) {
      return [];
    }
    const listSorted =
      [...listNode]?.sort((a, b) => Number(a?.end_line) - Number(b?.end_line)) || [];
    return listSorted;
  };
  useEffect(() => {
    if (!data || !data.flow_graph?.nodes) return;
    const listNodeSorted = handleSortNode(data?.flow_graph?.nodes || []);
    let initialXNode = 0;

    // NOTE : start_line and end_line not use, use for sort index of node ==))
    const newNodes: any = listNodeSorted?.map((item: NodeModel) => {
      initialXNode += 85;
      return {
        ...item,
        id: item.name,
        position: {
          x: 240,
          y: initialXNode
        },
        data: {
          label: item.name
        },
        sourcePosition: "right",
        targetPosition: "right"
      };
    });
    const newEdges = data?.flow_graph?.links?.map((item: FlowChartEdge, index: number) => {
      return {
        ...item,
        id: index.toString(),
        source: item.source,
        target: item.target,
        type: "custom",
        data: {
          label: item?.label
        },
        markerEnd: {
          type: MarkerType.ArrowClosed,
          width: 20,
          height: 20,
          color: "#f6d053"
        },
        style: {
          stroke: "#f6d053"
        }
      };
    });
    // if (newNodes?.length) {
    //   newNodes?.unshift({
    //     ...newNodes?.[0],
    //     id: '0',
    //     position: {
    //       x: 240,
    //       y: 20
    //     },
    //     data: {
    //       label: 'Start'
    //     },
    //     style: { borderRadius: 50 }
    //   })
    //   newNodes?.push({
    //     ...newNodes?.[newNodes?.length - 1],
    //     id: String(newNodes?.length),
    //     position: {
    //       x: 240,
    //       y: initialXNode + 85
    //     },
    //     data: {
    //       label: 'End'
    //     },
    //     style: { borderRadius: 50 }
    //   })
    // }
    setNodes(newNodes);
    setEdges(newEdges);
  }, [data]);

  const edgeTypes: EdgeTypes = {
    custom: CustomEdge
  };

  return (
    <FlowChart
      nodes={nodes}
      edges={edges}
      onNodesChange={onNodesChange}
      onEdgesChange={onEdgesChange}
      onConnect={onConnect}
      edgeTypes={edgeTypes}
    />
  );
};
