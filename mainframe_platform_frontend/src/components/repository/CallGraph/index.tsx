import styled from "@emotion/styled";
import { Table } from "antd";
import { useCallback, useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { EdgeTypes, MarkerType, Position, addEdge, useEdgesState, useNodesState } from "reactflow";

import { blobApi } from "@api";
import { getCblCommonTableColumns } from "@pages/exploration/file/config";
import { Container } from "@pages/exploration/file/styles";
import { fileSelector } from "@store";
import { colorsDefines } from "@style";
import { CopyGraphBlob } from "@types";
import { formatDateNoTime } from "@utils";

import { FlowChart } from "../../FlowChart";
import { Flex, Typography } from "../../ui";
import { CustomEdge } from "../GraphContent";
import { CustomNode } from "../components";
import { WrapTable } from "../styles";

import { RelatedProgramTable } from "./RelatedProgramTable";

const WrapChart = styled.div`
  height: 300px;
  width: 80%;
`;

const nodeTypes = {
  custom: CustomNode
};

export const CallGraph = () => {
  const { t } = useTranslation();
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const { fileId } = useParams();
  const data = useSelector(fileSelector.selectData);

  const [copyGraph, setCopyGraph] = useState<CopyGraphBlob | null>(null);

  const onConnect = useCallback((params: any) => setEdges(eds => addEdge(params, eds)), [setEdges]);

  const edgeTypes: EdgeTypes = {
    custom: CustomEdge
  };

  useEffect(() => {
    const fetchCopyGraphData = async () => {
      if (!fileId) return;

      const response = await blobApi.getFileCopygraph(fileId);

      if (!response?.data) return;

      const mapPrograms: any = {};

      response.data.programs.forEach(item => {
        if (mapPrograms[item.program_id]) return;
        mapPrograms[item.program_id] = item;
      });
      setCopyGraph({
        details: response.data.details,
        programs: Object.values(mapPrograms)
      });
    };

    fetchCopyGraphData();
  }, [fileId]);

  useEffect(() => {
    if (!data) return;
    if (!copyGraph?.programs?.length) return;
    let initialXNode = -150;

    // NOTE : start_line and end_line not use, use for sort index of node ==))
    const newNodes: any = copyGraph.programs
      .filter(item => item.program_type === "Cobol")
      .map((item, index: number) => {
        initialXNode += 150;
        return {
          // ...item,
          id: String(index),
          position: {
            x: initialXNode,
            y: 150
          },
          data: {
            label: item?.program_name,
            content: item?.program_id
          },
          type: "custom",
          targetPosition: item?.index === 1 ? Position.Top : Position.Left,
          sourcePosition: Position.Right
        };
      });

    const newEdges = newNodes.map((node: any, id: number) => ({
      id: `start-link ${id}`,
      source: "-1",
      target: node.id,
      data: {
        label: ""
      },
      markerEnd: {
        type: MarkerType.ArrowClosed,
        width: 20,
        height: 20,
        color: colorsDefines.primary100
      },
      style: {
        stroke: colorsDefines.primary100
      }
    }));
    newNodes?.unshift({
      id: "-1",
      position: {
        x: 0,
        y: 20
      },
      sourcePosition: Position.Bottom,
      data: {
        content: data?.name
      },
      type: "custom"
    });

    setNodes(newNodes);
    setEdges(newEdges);
  }, [copyGraph?.programs]);
  const dataResources = [
    {
      name: data?.name,
      title: "AIC",
      creation_date: formatDateNoTime(data?.created_at || ""),
      update_date: formatDateNoTime(data?.updated_at || "")
    }
  ];

  return (
    <Container direction='column' gap={24}>
      <WrapTable>
        <Table
          columns={getCblCommonTableColumns(t)}
          dataSource={dataResources}
          pagination={false}
        />
      </WrapTable>
      <Flex direction='column'>
        <Typography level='h6-body1m' color='primary100' style={{ marginBottom: 17 }}>
          1. {t("page.file_explorer.cobol.call_graph.title")}
        </Typography>
        <WrapChart>
          <FlowChart
            nodes={nodes}
            edges={edges}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            edgeTypes={edgeTypes}
            nodeTypes={nodeTypes}
          />
        </WrapChart>
        <Flex direction='column' gap={16}>
          <Typography color='primary100' level='h6-body1m'>
            2. {t("page.file_explorer.cobol.call_graph.related_programs")}
          </Typography>
          <RelatedProgramTable data={copyGraph?.programs} />
        </Flex>
      </Flex>
    </Container>
  );
};
