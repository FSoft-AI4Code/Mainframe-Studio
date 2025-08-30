/* eslint-disable import/no-named-as-default */
import ReactFlow, {
  type Node,
  type Edge,
  Controls,
  Background,
  MiniMap,
  type NodeTypes,
  Handle,
  Position,
  type EdgeProps
} from "reactflow";
import { Card } from "antd";
import "reactflow/dist/style.css";

const StepNode = ({ data }: { data: { label: string; program: string } }) => (
  <Card
    style={{
      width: 150,
      padding: "8px",
      borderRadius: "8px",
      backgroundColor: "#52c41a",
      color: "white",
      textAlign: "center"
    }}
    bodyStyle={{ padding: "4px" }}
  >
    <Handle type='target' position={Position.Top} />
    <Handle type='source' position={Position.Bottom} />
    <div style={{ fontWeight: "bold" }}>{data.label}</div>
    <div style={{ fontSize: "12px" }}>({data.program})</div>
  </Card>
);

const FileNode = ({ data }: { data: { label: string; type: string } }) => (
  <Card
    style={{
      width: 150,
      padding: "8px",
      borderRadius: "8px",
      backgroundColor: data.type === "VSAM" ? "#722ed1" : "#ff7a45", // Purple for VSAM, Orange for FLAT
      color: "white",
      textAlign: "center"
    }}
    bodyStyle={{ padding: "4px" }}
  >
    <Handle type='target' position={Position.Top} />
    <Handle type='source' position={Position.Bottom} />
    <div style={{ fontWeight: "bold" }}>{data.label}</div>
    <div style={{ fontSize: "12px" }}>({data.type})</div>
  </Card>
);

const nodeTypes: NodeTypes = {
  step: StepNode,
  file: FileNode
};

const edgeTypes = {
  custom: ({ id, sourceX, sourceY, targetX, targetY, data, markerEnd }: EdgeProps) => {
    const edgePath = `M ${sourceX},${sourceY} L ${targetX},${targetY}`;
    const midX = (sourceX + targetX) / 2;
    const midY = (sourceY + targetY) / 2 - 10;

    return (
      <>
        <path id={id} className='react-flow__edge-path' d={edgePath} markerEnd={markerEnd} />
        {data?.label && (
          <foreignObject
            width={100}
            height={40}
            x={midX - 50}
            y={midY - 20}
            requiredExtensions='http://www.w3.org/1999/xhtml'
          >
            <div className='bg-white px-2 py-1 rounded-md shadow-sm border text-center text-xs font-bold'>
              {data.label}
            </div>
          </foreignObject>
        )}
      </>
    );
  }
};

export default function FlowChart() {
  const initialNodes: Node[] = [
    {
      id: "file1",
      type: "file",
      position: { x: 50, y: 50 },
      data: { label: "FILE1", type: "VSAM" }
    },
    {
      id: "file2",
      type: "file",
      position: { x: 250, y: 50 },
      data: { label: "FILE2", type: "FLAT" }
    },
    {
      id: "step1",
      type: "step",
      position: { x: 150, y: 200 },
      data: { label: "STEP1", program: "PROG1" }
    },
    {
      id: "file3",
      type: "file",
      position: { x: 150, y: 350 },
      data: { label: "FILE3", type: "FLAT" }
    },
    {
      id: "step2",
      type: "step",
      position: { x: 150, y: 500 },
      data: { label: "STEP2", program: "PROG2" }
    },
    {
      id: "file4",
      type: "file",
      position: { x: 150, y: 650 },
      data: { label: "FILE4", type: "VSAM" }
    }
  ];

  const initialEdges: Edge[] = [
    {
      id: "input-f1-s1",
      source: "file1",
      target: "step1",
      type: "custom",
      animated: true,
      data: { label: "INPUT" }
    },
    {
      id: "input-f2-s1",
      source: "file2",
      target: "step1",
      type: "custom",
      animated: true,
      data: { label: "INPUT" }
    },
    { id: "s1-f3", source: "step1", target: "file3", type: "custom" },
    { id: "f3-s2", source: "file3", target: "step2", type: "custom" },
    { id: "s1-s2", source: "step1", target: "step2", type: "custom" }, // Đường đi từ Step1 đến Step2 không qua File3
    {
      id: "s1-s2-f3",
      source: "step1",
      target: "file3",
      type: "custom",
      animated: true,
      data: { label: "PROCESS" }
    },
    {
      id: "s2-f4",
      source: "step2",
      target: "file4",
      type: "custom",
      animated: true,
      data: { label: "OUTPUT" }
    }
  ];

  return (
    <div style={{ width: "100%", height: "800px" }}>
      <ReactFlow
        nodes={initialNodes}
        edges={initialEdges}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        fitView
      >
        <Controls />
        <MiniMap />
        <Background color='#aaa' gap={16} />
      </ReactFlow>
    </div>
  );
}
