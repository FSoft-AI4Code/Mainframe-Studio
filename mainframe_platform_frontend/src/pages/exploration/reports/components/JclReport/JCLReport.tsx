import { Card, List, Tabs, Tag } from "antd";
import { lazy, useState } from "react";
import { useParams } from "react-router-dom";
import { ColumnsType } from "antd/es/table";

import { Flex, OverflowEmpty, Typography } from "@components";
import { allColors } from "@style";
import { Overview, JCLStep } from "@types";
import { addPropertiesToItems } from "@utils";

import { ScrollableWrapper, CustomTable } from "../../../data-asset/styles";

const OverviewJCL = lazy(() => import("./OverviewJCL"));

export interface JCLReportData {
  overview: Overview;
  step_list: JCLStep[];
}
export interface JCLReportPageProps {
  jclData: {
    output: JCLReportData;
  };
  loading?: boolean;
}

export const jclDocs = {
  jobName: {
    description: "The name that identifies this job in the system",
    details: null
  },
  class: {
    description: "Job class 'A' typically indicates:",
    details: [
      "Standard priority processing",
      "General-purpose workload",
      "Default system resources allocation"
    ]
  },
  mssclass: {
    description: "Message Class determines:",
    details: [
      "Where job output messages are routed",
      "How job output is handled",
      "Output retention period"
    ]
  },
  timeLimit: {
    description: "Maximum execution time allowed for the job:",
    details: [
      "Helps prevent runaway jobs",
      "System terminates job if time limit exceeded",
      "NULL means no specific time limit set"
    ]
  },
  notify: {
    description: "&SYSUID indicates:",
    details: [
      "The system will notify the submitting user",
      "Job completion status will be sent",
      "Automatic notification when job ends"
    ]
  }
};
export const getCurrentJclDetail = (type: string) => jclDocs[type as keyof typeof jclDocs];

const columns: ColumnsType<Partial<JCLStep>> = [
  {
    title: "DDNAME",
    dataIndex: "ddname",
    key: "ddname",
    width: "20%"
  },
  {
    title: "Parameters",
    dataIndex: "parameters_map",
    key: "parameters_map",
    width: "40%",
    render: (parameters = {}) =>
      Object.keys(parameters)?.map((label, index) => (
        <Tag key={index} color='processing'>
          {label}: {parameters[label] || ""}
        </Tag>
      )) || "N/A"
  },
  {
    title: "Logic",
    dataIndex: "logic",
    width: "40%",
    key: "logic",
    render: value => value || "N/A"
  }
];
export default function JCLReport({ jclData, loading }: JCLReportPageProps) {
  const { overview, step_list: stepList } = jclData?.output || {};
  const { type: fileType, name } = useParams();
  const [tab, setTab] = useState("overview");

  const onChange = (key: string) => {
    setTab(key);
  };

  return (
    <>
      <ScrollableWrapper direction='column'>
        <Card
          title={
            <Typography level='title-24b' color='primary10'>
              {fileType} Report: {name}
            </Typography>
          }
          style={{ background: allColors.neutral1, width: "100%" }}
        >
          <Flex direction='column' gap={24}>
            {
              <Flex
                style={{
                  background: allColors.neutral1,
                  borderRadius: "8px",
                  minHeight: "calc(100vh - 228px)"
                }}
                direction='column'
                gap={16}
              >
                <Tabs
                  activeKey={tab}
                  items={[
                    {
                      key: "overview",
                      label: "Overview",
                      children: (
                        <Flex
                          style={{
                            minHeight: "calc(100vh - 228px)"
                          }}
                          direction='column'
                          gap={16}
                        >
                          <Card
                            title={
                              <>
                                <Typography level='body-16b' color='primary10'>
                                  JCL Overview
                                </Typography>
                                <Typography
                                  style={{ marginTop: 2 }}
                                  level='body-14r'
                                  color='neutral7'
                                >
                                  General infomation about the JCL job.
                                </Typography>
                              </>
                            }
                            style={{ background: allColors.neutral2 }}
                          >
                            <OverviewJCL overviewData={overview} />
                          </Card>
                          <Card
                            headStyle={{
                              direction: "revert-layer"
                            }}
                            loading={loading}
                            title={
                              <>
                                <Typography level='body-16b' color='primary10'>
                                  IO Statement
                                </Typography>
                                <Typography
                                  style={{ marginTop: 2 }}
                                  level='body-14r'
                                  color='neutral7'
                                >
                                  Input/ouput statement for all steps .
                                </Typography>
                              </>
                            }
                            style={{ background: allColors.neutral2 }}
                          >
                            {stepList?.length > 0 ? (
                              <Flex direction='column' gap={10}>
                                {stepList?.map((step, index: number) => {
                                  const { io_statements: ioStatements, step_name: stepName } =
                                    step || {};
                                  const currentIoStatement =
                                    ioStatements?.length > 0
                                      ? ioStatements
                                      : ["No I/O statements for step"];
                                  return (
                                    <List
                                      key={index}
                                      style={{
                                        borderBottom: "1px solid rgba(5, 5, 5, 0.1)"
                                      }}
                                      header={
                                        <Typography level={"body-14b"}>{stepName}</Typography>
                                      }
                                      itemLayout='horizontal'
                                      dataSource={currentIoStatement}
                                      renderItem={(item: string, i: number) => (
                                        <List.Item key={i}>
                                          <Typography color='neutral10' level={"body-14r"}>
                                            {item}
                                          </Typography>
                                        </List.Item>
                                      )}
                                    />
                                  );
                                })}
                              </Flex>
                            ) : (
                              <OverflowEmpty />
                            )}
                          </Card>
                        </Flex>
                      )
                    },
                    {
                      key: "step",
                      label: "Step Detail",
                      children: (
                        <Flex direction='column' gap={16}>
                          <Card loading={loading} style={{ background: allColors.neutral2 }}>
                            {stepList?.length > 0 ? (
                              <Flex direction='column' gap={16}>
                                {stepList?.map((step, index: number) => {
                                  return (
                                    <Card
                                      bordered
                                      title={
                                        <>
                                          <Typography level='body-16b' color='primary10'>
                                            {step?.step_name}
                                          </Typography>
                                          <Typography
                                            style={{ marginTop: 2 }}
                                            level='body-14r'
                                            color='neutral7'
                                          >
                                            Program executed: {step?.program_executed || "N/A"}
                                          </Typography>
                                        </>
                                      }
                                      style={{ background: allColors.neutral2 }}
                                      key={index}
                                    >
                                      <Typography
                                        style={{
                                          marginBottom: 12
                                        }}
                                        level='body-14b'
                                        color='primary10'
                                      >
                                        DD Statements
                                      </Typography>
                                      <CustomTable
                                        rowKey={"no"}
                                        columns={columns}
                                        dataSource={addPropertiesToItems(
                                          step?.dd_statement,
                                          (_, no) => ({
                                            no: no + 1
                                          })
                                        )}
                                        pagination={false}
                                        scroll={{ x: 500 }}
                                      />
                                    </Card>
                                  );
                                })}
                              </Flex>
                            ) : (
                              <Flex direction='column' gap={16}>
                                <OverflowEmpty />
                              </Flex>
                            )}
                          </Card>
                        </Flex>
                      )
                    }
                  ]}
                  onChange={onChange}
                  style={{
                    color: allColors.primary10,
                    width: "100%",
                    height: "100%"
                  }}
                />
              </Flex>
            }
          </Flex>
        </Card>
      </ScrollableWrapper>
    </>
  );
}
