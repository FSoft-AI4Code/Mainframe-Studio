import { ColumnsType } from "antd/es/table";
import { EdgeTypes, Handle, Position, useEdgesState, useNodesState } from "reactflow";
import { FC, useMemo } from "react";

import { CustomEdge, Flex, FlowChart, Typography } from "@components";
import { allColors } from "@style";

import { CustomTable } from "../styles";
import { CopyGraphProgram } from "../fake/blob";

const columns: ColumnsType<any> = [
  {
    title: "No",
    dataIndex: "index",
    key: "index",
    width: 70,
    align: "center"
  },
  {
    title: "Program ID",
    dataIndex: "program_id",
    key: "program_id"
  },
  {
    title: "Program Category",
    dataIndex: "program_type",
    key: "program_type"
  },
  {
    title: "Call Type",
    dataIndex: "call_type",
    key: "call_type"
  },
  {
    title: "Location",
    dataIndex: "locations",
    key: "locations"
  },
  {
    title: "Parameter",
    dataIndex: "paragraph",
    key: "paragraph"
  },
  {
    title: "Condition",
    dataIndex: "identifier",
    key: "identifier",
    render(value) {
      return (value ?? []).join(", ");
    }
  }
];

type Props = {
  id: string;
  data?: {
    label: string;
    content: string;
  };
};

const CustomNode: FC<Props> = ({ id, data, sourcePosition, targetPosition }: any) => {
  return (
    <Flex direction='column' style={{ maxWidth: 200, border: `1px solid ${allColors.neutral7}` }}>
      <Flex
        center
        style={{
          background: allColors.primary2,
          borderBottom: `1px solid ${allColors.neutral7}`,
          padding: "4px 2 4px"
        }}
      >
        <Typography level='body-16r'>{data.label}</Typography>
      </Flex>
      <Flex center style={{ padding: "4px 24px" }}>
        <Typography level='body-16r'>{data.content}</Typography>
      </Flex>
      <Handle type='source' position={sourcePosition || Position.Right} id={id} />
      <Handle type='target' position={targetPosition || Position.Right} id={id} />
    </Flex>
  );
};

const edgeTypes: EdgeTypes = {
  custom: CustomEdge
};

const nodeTypes = {
  custom: CustomNode
};

export default function CallGraphPage({
  copyGraphData,
  node
}: {
  copyGraphData: {
    programs: CopyGraphProgram[];
    details: string[];
  };
  node: any;
}) {
  // eslint-disable-next-line unused-imports/no-unused-vars, @typescript-eslint/no-unused-vars
  const [edges, setEdges, onEdgesChange] = useEdgesState(
    copyGraphData.programs.map((program, id) => ({
      id: `edge-${id}`,
      source: "-1",
      target: id.toString(),
      data: {
        label: program.call_type
      }
    }))
  );
  // eslint-disable-next-line unused-imports/no-unused-vars, @typescript-eslint/no-unused-vars
  const [nodes, setNodes, onNodesChange] = useNodesState(
    copyGraphData.programs.map((program, id) => ({
      id: id.toString(),
      data: program,
      position: { x: 0, y: 0 }
    }))
  );

  const displayedNodes = useMemo(() => {
    let initialXNode = -100;

    // NOTE : start_line and end_line not use, use for sort index of node ==))
    const newNodes: any = nodes.map((item, index: number) => {
      initialXNode += 200;
      return {
        // ...item,
        id: String(index),
        position: {
          x: initialXNode,
          y: 150
        },
        data: {
          content: item.data.program_name,
          label: item.data.program_type
        },
        type: "custom",
        targetPosition: Position.Top,
        sourcePosition: Position.Right
      };
    });

    newNodes?.unshift({
      id: "-1",
      position: {
        x: 50,
        y: 20
      },
      sourcePosition: Position.Bottom,
      data: {
        content: node.value,
        label: "COBOL"
      },
      type: "custom"
    });

    return newNodes;
  }, [edges, node]);

  return (
    <Flex gap={16} direction='column'>
      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>1. Call Graph</Typography>
        <Typography level='body-16r'>Job-based processing</Typography>
        <Flex style={{ width: "100%", height: 350 }} center>
          <FlowChart
            style={{ width: "80%" }}
            nodes={displayedNodes}
            edges={edges.map(edge => ({ ...edge, type: "custom" }))}
            nodeTypes={nodeTypes}
            edgeTypes={edgeTypes}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
          />
        </Flex>
      </Flex>
      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>2. List of Related Programs</Typography>

        <CustomTable
          columns={columns}
          dataSource={copyGraphData.programs.map((item, index) => ({ ...item, index: index + 1 }))}
          pagination={false}
          scroll={{ y: "calc(100vh - 400px)" }}
        />
      </Flex>
      <Flex gap={4} direction='column'>
        <Typography level='body-16b'>3. Details</Typography>
        {copyGraphData.details.map((detail, index) => (
          <Typography level='body-16r' key={`${detail}-${index}`}>
            {detail}
          </Typography>
        ))}
      </Flex>
    </Flex>
  );
}
