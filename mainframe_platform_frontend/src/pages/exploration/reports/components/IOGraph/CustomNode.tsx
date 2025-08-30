import React from "react";
import { Edge, Handle, MarkerType, Node, NodeTypes, Position } from "reactflow";

import { CylinderSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { CobolProgram, IOFile, OpenType } from "@types";
import { getColorsWithOpacity } from "@utils";

export enum NodeModeEnum {
  MAIN,
  SIDE,
  IN,
  OT,
  OTHER
}

export enum LabelByModeEnum {
  MAIN = "Program",
  SIDE = "Subroutines",
  IN = "Input",
  OT = "Output",
  OTHER = "Other"
}
export type DataNodeProps = {
  data: {
    label: string;
    mode: keyof typeof NodeModeEnum;
    openType?: OpenType;
    hasSideNode?: boolean;
    isEmptyOutput?: boolean;
    isEmptyInput?: boolean;
  };
};

export type ProcessData = { nodes: Node[]; edges: Edge[] };

export const baseColors = [
  [255, 87, 51],
  [128, 61, 236],
  [235, 195, 71],
  [67, 141, 87],
  [51, 87, 255],
  [51, 255, 243],
  [255, 199, 51],
  [255, 51, 51],
  [51, 161, 255],
  [161, 255, 51]
];

export const isValidOpenType = (type: OpenType | undefined, types?: OpenType[]): boolean => {
  const validTypes: OpenType[] = types && types?.length > 0 ? types : ["INPUT", "OUTPUT", "I-O"];
  return validTypes.includes(type?.toUpperCase() as OpenType);
};
export const isValidRountine = (subroutine: string | undefined): boolean => {
  const validRountine = ["SUBSYSIN_SJ"];
  return validRountine.includes(subroutine?.toUpperCase() as string);
};

export const MainNode: React.FC<DataNodeProps> = ({ data }) => {
  return (
    <Flex
      style={{
        padding: "10px",
        borderRadius: "5px",
        background: getColorsWithOpacity(baseColors, NodeModeEnum[data?.mode], 0.8),
        border: `1.5px solid ${getColorsWithOpacity(baseColors, NodeModeEnum[data?.mode])}`,
        justifyContent: "center",
        textAlign: "center",
        color: "#030852",
        width: 120,
        fontSize: 14
      }}
    >
      <strong>{data.label}</strong>

      {!data.isEmptyInput && (
        <>
          <Handle id='top' type='target' position={Position.Top} style={{ background: "#555" }} />
        </>
      )}
      {!data.isEmptyOutput && (
        <>
          <Handle
            id='bottom'
            type='source'
            position={Position.Bottom}
            style={{ background: "#555" }}
          />
        </>
      )}
      {data?.hasSideNode && (
        <Handle id='left' type='target' position={Position.Left} style={{ background: "#555" }} />
      )}
    </Flex>
  );
};
export const IOFileNode: React.FC<DataNodeProps> = ({ data }) => {
  const currenType = isValidOpenType(data.openType) ? NodeModeEnum[data?.mode] : NodeModeEnum.OTHER;
  return (
    <Flex
      style={{
        width: 120,
        justifyContent: "center",
        textAlign: "center"
      }}
    >
      <Typography
        style={{
          position: "absolute",
          top: "50%",
          left: "50%",
          transform: "translate(-50%,-50%)",
          zIndex: 10
        }}
        level={"button-12m"}
      >
        {data.label}
      </Typography>
      <CylinderSvg
        fill={getColorsWithOpacity(baseColors, currenType)}
        stroke={getColorsWithOpacity(baseColors, currenType)}
        style={{
          position: "relative"
        }}
      />
      <Handle
        type={data.mode === "IN" ? "source" : "target"}
        position={data.mode === "IN" ? Position.Bottom : Position.Top}
        style={{ background: "#555" }}
      />
    </Flex>
  );
};
export const SideNode: React.FC<DataNodeProps> = ({ data }) => (
  <div>
    <Flex
      style={{
        position: "relative",
        left: -2,
        textAlign: "center",
        justifyContent: "center",
        alignItems: "center",
        background: getColorsWithOpacity(baseColors, NodeModeEnum[data?.mode], 0.8),
        minHeight: 40,
        minWidth: 80,
        transform: "skew(-20deg)",
        border: `1.5px solid ${getColorsWithOpacity(baseColors, NodeModeEnum[data?.mode])}`
      }}
    >
      <Typography
        style={{
          transform: "skew(20deg)",
          padding: "0 8px"
        }}
        level={"body-14r"}
      >
        {data.label}
      </Typography>
    </Flex>
    <Handle type='source' position={Position.Right} style={{ background: "#555" }} />
  </div>
);
export const nodeTypes: NodeTypes = {
  main: MainNode,
  io: IOFileNode,
  side: SideNode
};

// eslint-disable-next-line @typescript-eslint/default-param-last
export const getNodesByTypeName = (data: IOFile[] = [], typeName: OpenType) => {
  const inputNodes = data.filter(file => ["INPUT", "I-O"].includes(file?.open_type?.toUpperCase()));
  const outputNodes = data.filter(file =>
    ["OUTPUT", "I-O"].includes(file?.open_type?.toUpperCase())
  );
  const hasInputNode = inputNodes.length > 0;
  const hasOutputNode = outputNodes.length > 0;
  if (!hasInputNode && !hasOutputNode) {
    const middleIndex = Math.ceil(data.length / 2);
    return typeName === "INPUT" ? data.slice(0, middleIndex) : data.slice(middleIndex);
  }
  return typeName === "INPUT" ? inputNodes : outputNodes;
};

export const processData = (data: CobolProgram): ProcessData => {
  const {
    program_id: programId,
    io_files: ioFiles,
    subroutines_called: subroutinesCalled
  } = data || {};

  const inputFiles = getNodesByTypeName(ioFiles, "INPUT") || [];
  const outputFiles = getNodesByTypeName(ioFiles, "OUTPUT") || [];

  const isEmptyInput = !inputFiles || inputFiles?.length === 0;
  const isEmptyOutput = !outputFiles || outputFiles?.length === 0;

  const verticalSpacing = 100;
  const centerX = 250;
  const horizontalSpacing = 100;
  const sideNodeLabel = subroutinesCalled?.[0]?.name?.replace(/"([^"]+)"/g, "$1");
  if (!programId) return {} as ProcessData;

  const mainNode: Node = {
    id: "main",
    type: "main",
    position: { x: centerX, y: (inputFiles?.length + 1) * verticalSpacing },
    data: {
      label: programId,
      isEmptyInput: !!isEmptyInput,
      isEmptyOutput: !!isEmptyOutput,
      hasSideNode: Boolean(sideNodeLabel && isValidRountine(sideNodeLabel)),
      mode: "MAIN"
    }
  };
  const sideNode =
    sideNodeLabel && isValidRountine(sideNodeLabel)
      ? {
          id: "side",
          type: "side",
          position: {
            x: centerX - 150,
            y: (inputFiles.length + 1) * verticalSpacing + 2
          },
          data: { label: sideNodeLabel, mode: "SIDE" }
        }
      : null;

  // Input Nodes
  const inputNodes =
    inputFiles?.map((file: IOFile, index: number) => {
      const totalNodes = inputFiles?.length;
      const totalWidth = (totalNodes - 1) * horizontalSpacing;
      const xPosition = centerX - totalWidth / 2 + index * horizontalSpacing;
      return {
        id: `${file.name}-in`,
        type: "io",
        position: { x: xPosition, y: verticalSpacing * (totalNodes - 0.25) },
        data: {
          label: file.name,
          openType: file?.open_type,
          isOther: !isValidOpenType(file?.open_type),
          mode: "IN"
        }
      };
    }) || [];

  // Output Nodes
  const outputNodes =
    outputFiles?.map((file: IOFile, index: number) => {
      const totalNodes = outputFiles.length;
      const totalWidth = (totalNodes - 1) * horizontalSpacing;
      const xPosition = centerX - totalWidth / 2 + index * horizontalSpacing;
      const yPosition = (inputFiles.length + 2) * verticalSpacing;
      return {
        id: `${file.name}-out`,
        type: "io",
        position: { x: xPosition, y: yPosition },
        data: {
          label: file.name,
          isOther: !isValidOpenType(file?.open_type),
          openType: file.open_type,
          mode: "OT"
        }
      };
    }) || [];

  // Input Edges
  const inputEdges =
    inputFiles?.map((file: IOFile) => ({
      id: `edge-${file?.name}-in-main`,
      source: `${file?.name}-in`,
      target: "main",
      type: "straight",
      markerEnd: isValidOpenType(file?.open_type, ["INPUT", "I-O"])
        ? {
            type: MarkerType.ArrowClosed,
            color: "black"
          }
        : "circle"
    })) || [];

  // Output Edges
  const outputEdges =
    outputFiles?.map((file: IOFile) => ({
      id: `edge-main-${file.name}-out`,
      source: "main",
      target: `${file.name}-out`,
      type: "straight",
      markerEnd: isValidOpenType(file?.open_type, ["OUTPUT", "I-O"])
        ? {
            type: MarkerType.ArrowClosed,
            color: "black"
          }
        : "circle"
    })) || [];

  const sideEdge: Edge[] = sideNode
    ? [
        {
          id: "edge-side-main",
          source: "side",
          target: "main",
          sourceHandle: "right",
          targetHandle: "left",
          type: "straight",
          markerEnd: {
            type: MarkerType.ArrowClosed,
            color: "black"
          }
        }
      ]
    : [];

  return {
    nodes: sideNode
      ? [mainNode, sideNode, ...inputNodes, ...outputNodes]
      : [mainNode, ...inputNodes, ...outputNodes],
    edges: [...inputEdges, ...outputEdges, ...sideEdge]
  };
};
