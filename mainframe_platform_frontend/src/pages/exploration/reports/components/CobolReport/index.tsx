import { Card, message, Table, Typography as TypographyAntd } from "antd";
import { useParams } from "react-router-dom";
import { useState } from "react";
import confirm from "antd/es/modal/confirm";
import { ExclamationCircleFilled } from "@ant-design/icons";

import { Button, Flex, Typography } from "@components";
import { allColors } from "@style";
import { CobolProgram, ReverseCobolData, ReverseTypeEnum, TreeNode } from "@types";
import { useListReverses, useTriggerSummariztions } from "@services";
import { addPropertiesToItems, handleErrorMessage } from "@utils";

import { IOFlowChart } from "../IOGraph";
import { ScrollableWrapper, TableWrapper } from "../styles";
import { CallGraph, GraphData } from "../CallGraph";

const { Text } = TypographyAntd;

interface CobolReportProps {
  cobolData: ReverseCobolData;
  refetchReport: () => void;
}

export default function CobolReport({ cobolData, refetchReport }: CobolReportProps) {
  const program = cobolData?.output || {};
  const { repoId = "", name = "", type = "" } = useParams();
  const [pageSize, setPageSize] = useState(10);
  const [page, setPage] = useState(1);
  const [messageApi] = message.useMessage();
  const { files: copyFiles } = useListReverses({
    repoId: repoId,
    type: ReverseTypeEnum.COPY
  });

  const {
    mutate: startSummarization,
    isPending,
    data: summarizationData
  } = useTriggerSummariztions();
  const { summarization } = summarizationData?.data || {};

  const handleStartSumarizationReport = () => {
    confirm({
      title: (
        <>
          Are you sure you want to start the summarization for{" "}
          <Text type='secondary' style={{ color: "blue" }}>
            {name}
          </Text>
          ?
        </>
      ),
      icon: <ExclamationCircleFilled color='blue' />,
      closable: true,
      maskClosable: true,
      type: "info",
      okButtonProps: { loading: isPending },
      async onOk() {
        if (!repoId || !type || !name) return;
        startSummarization(
          { name, repository_id: repoId, type },
          {
            onSuccess() {
              messageApi.open({
                type: "success",
                content: "Summarization started successfully!"
              });
              refetchReport();
            },
            onError(error) {
              handleErrorMessage(error as never, { show: true });
            }
          }
        );
      },
      onCancel() {
        // eslint-disable-next-line no-console
        console.log("Cancel");
      }
    });
  };
  const getCurrentCopyFile = (copyName: string) => copyFiles?.find(file => file?.name === copyName);
  const handleSizeChange = (_: number, size: number) => {
    setPageSize(size);
  };
  return (
    <ScrollableWrapper direction='column'>
      <Card
        title={
          <Typography level='title-24b' color='primary10'>
            COBOL Program Report: {name}
          </Typography>
        }
        extra={
          <Button
            onClick={handleStartSumarizationReport}
            loading={isPending}
            style={{ borderRadius: 8 }}
            type='primary'
          >
            Summarization
          </Button>
        }
        style={{ background: allColors.neutral1, width: "100%" }}
      >
        <Flex direction='column' gap={24}>
          <Card title='Program Description' style={{ background: allColors.neutral2 }}>
            <pre style={{ whiteSpace: "pre-wrap" }}>{program.description}</pre>
          </Card>
          <Card
            title='IO Graph'
            bodyStyle={{
              width: "100%",
              height: "500px"
            }}
            style={{ background: allColors.neutral2 }}
          >
            <IOFlowChart
              data={{ ...(program as CobolProgram), program_id: program.program_id || name }}
            />
          </Card>

          <Card title='Input/Output Files' style={{ background: allColors.neutral2 }}>
            <TableWrapper>
              <Table
                columns={[
                  { title: "No.", dataIndex: "no" },
                  { title: "Name", dataIndex: "name" },
                  {
                    title: "Open Type",
                    dataIndex: "open_type",
                    render: value => value || "None"
                  },
                  {
                    title: "Copybooks",
                    dataIndex: "copybooks",
                    render: copybooks => copybooks?.[0]?.copybook_name || "None"
                  },
                  {
                    title: "RL",
                    dataIndex: "copybooks",
                    render: copybooks => {
                      const value = copybooks?.[0]?.copybook_name || "";
                      const copyLength = getCurrentCopyFile(value)?.output?.copy_length || "";
                      const regex = /RL=(\d+)/;
                      const match = copyLength?.match(regex);
                      return match ? match?.[1] : "None";
                    }
                  },
                  {
                    title: "Access Mode",
                    dataIndex: "access_mode"
                  }
                ]}
                dataSource={addPropertiesToItems(program.io_files, (item, index) => ({
                  no: index + 1
                }))}
                rowKey='no'
                pagination={false}
                scroll={{ x: 500 }}
              />
            </TableWrapper>
          </Card>

          <Card title='Working Storage Variables' style={{ background: allColors.neutral2 }}>
            <TableWrapper>
              <Table
                columns={[
                  { title: "Level", dataIndex: "level" },
                  { title: "Name", dataIndex: "name" },
                  { title: "Data Type", dataIndex: "data_type" },
                  { title: "Length", dataIndex: "length" },
                  { title: "Default Value", dataIndex: "default_value" },
                  { title: "Remarks", dataIndex: "remarks" }
                ]}
                dataSource={addPropertiesToItems(program.working_storage_variables, (_, index) => ({
                  no: index + 1
                }))}
                rowKey={"no"}
                pagination={{
                  defaultCurrent: 10,
                  pageSize: pageSize,
                  showSizeChanger: true,
                  onShowSizeChange: handleSizeChange,
                  current: page,
                  onChange(curentPage) {
                    setPage(curentPage);
                  }
                }}
                scroll={{ x: 500, y: 480 }}
              />
            </TableWrapper>
          </Card>

          <Card title='Subroutines Called' style={{ background: allColors.neutral2 }}>
            <TableWrapper>
              <Table
                columns={[
                  { title: "No.", dataIndex: "no" },
                  { title: "Name", dataIndex: "name" },
                  { title: "Comment", dataIndex: "business_name" }
                ]}
                rowKey='no'
                dataSource={addPropertiesToItems(program.subroutines_called, (_, index) => ({
                  no: index + 1
                }))}
                pagination={false}
                scroll={{ x: 500 }}
              />
            </TableWrapper>
          </Card>
          <Card
            title='Paragraph/Section call graph'
            bodyStyle={{
              width: "100%",
              height: "75vh"
            }}
            style={{ background: allColors.neutral2 }}
          >
            <CallGraph
              programId={program?.program_id || name}
              dataFlow={{
                exec_flow_tree: program?.exec_flow_tree as TreeNode,
                exec_flow: program?.exec_flow as GraphData,
                summarizations: summarization || {}
              }}
            />
          </Card>
          <Card title='Output Variables Value' style={{ background: allColors.neutral2 }}>
            <TableWrapper>
              <Table
                key={type + name}
                columns={[
                  { title: "No", dataIndex: "no" },
                  { title: "Name", dataIndex: "name" },
                  { title: "Bussiness Explain", dataIndex: "business_name" },
                  { title: "Type", dataIndex: "data_type" },
                  { title: "Length", dataIndex: "Length" },
                  { title: "Src variable", dataIndex: "src_variable" },
                  { title: "Type", dataIndex: "src_data_type" },
                  { title: "Len", dataIndex: "src_len" },
                  { title: "Value", dataIndex: "value" }
                ]}
                rowKey='no'
                dataSource={addPropertiesToItems(program.variables_flow, (_, index) => ({
                  no: index + 1
                }))}
                scroll={{ x: 500 }}
                pagination={{ defaultPageSize: 10 }}
              />
            </TableWrapper>
          </Card>
        </Flex>
      </Card>
      {/* {contextHolder} */}
    </ScrollableWrapper>
  );
}
