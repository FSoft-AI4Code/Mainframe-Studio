import React, { useEffect } from "react";
import ReactFlowChart, {
  Background,
  BackgroundVariant,
  Controls,
  useEdgesState,
  useNodesState
} from "reactflow";

import { Flex, OverflowEmpty } from "@components";
import { CobolProgram } from "@types";
import { addPropertiesToItems, getColorsWithOpacity } from "@utils";

import Legends from "../../Legends";

import { baseColors, LabelByModeEnum, NodeModeEnum, nodeTypes, processData } from "./CustomNode";

import "reactflow/dist/style.css";

interface IOFlowChartProps {
  data: CobolProgram;
}

const IOFlowChart: React.FC<IOFlowChartProps> = ({ data }) => {
  const { nodes: initialNodes, edges: initialEdges } = processData(data);
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  useEffect(() => {
    setNodes(initialNodes);
    setEdges(initialEdges);
  }, [initialEdges, initialNodes]);

  const nodesMode = [
    ...new Set(initialNodes?.map(item => (item.data.isOther ? "OTHER" : item.data.mode)))
  ];
  // const nodesMode = [
  //   ...new Map(
  //     initialNodes?.map(item => [
  //       `${item.data.mode}-${item.data.open_type}`,
  //       { mode: item.data.mode, openType: item.data.open_type }
  //     ])
  //   ).values()
  // ];

  const isEmpty = !initialNodes || initialNodes?.length === 0;

  return (
    <Flex style={{ height: "450px" }}>
      {isEmpty ? (
        <OverflowEmpty />
      ) : (
        <>
          <ReactFlowChart
            nodes={nodes}
            edges={edges}
            nodeTypes={nodeTypes}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            fitView
            proOptions={{ hideAttribution: true }}
            defaultEdgeOptions={{
              style: {
                stroke: "black",
                strokeWidth: 1
              }
            }}
            fitViewOptions={{ padding: 1 }}
          >
            <Background color='#ccc' variant={BackgroundVariant.Dots} />
            <Controls />
          </ReactFlowChart>
          <Legends
            style={{ minWidth: 100 }}
            variant='secondary'
            data={addPropertiesToItems(
              nodesMode,
              mode => ({
                id: mode,
                label: LabelByModeEnum[mode as keyof typeof NodeModeEnum],
                style: {
                  color: getColorsWithOpacity(
                    baseColors,
                    NodeModeEnum[mode as keyof typeof NodeModeEnum],
                    0.8
                  ),
                  border: `1px solid ${getColorsWithOpacity(
                    baseColors,
                    NodeModeEnum[mode as keyof typeof NodeModeEnum]
                  )}`
                }
              }),
              true
            )}
          />
        </>
      )}
    </Flex>
  );
};

export default IOFlowChart;
