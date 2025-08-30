/* eslint-disable @typescript-eslint/no-unused-vars */
import { AlignLeftOutlined, ApartmentOutlined, DownloadOutlined } from "@ant-design/icons";
import { Button, Card, Col, Row, Statistic, Typography as TypographyAnt } from "antd";
import { useState } from "react";
import { useParams } from "react-router-dom";

import { Flex, Tabs, Typography } from "@components";
import { useLayout } from "@hooks";
import { useExportDatasetFile, useStatisticDatasetsQuery } from "@services";
import { v2CommonColors } from "@style";
import { DatasetsInput, ViewExportType } from "@types";

import RelationShipTab from "./components/relationship-view/relationship-view.tab";
import { TableViewTab } from "./components/table-view/table-view.tab";

const { Text } = TypographyAnt;

function PageContent() {
  const [activeTab, setActiveTab] = useState<string>("table-view");
  const [filter, setFilter] = useState<Partial<DatasetsInput & { view: ViewExportType }>>({
    view: "job"
  });
  const { repoId = "" } = useParams();

  const { view, ...filterStatistic } = filter || {};

  const { statisticDataset, isLoading } = useStatisticDatasetsQuery({
    repository_id: repoId,
    ...filterStatistic
  });
  const { files, jobs, steps, programs } = statisticDataset || {};
  const data = [
    { label: "Jobs", value: jobs },
    { label: "Steps", value: steps },
    { label: "Programs", value: programs },
    { label: "Files", value: files }
  ];
  const items = [
    {
      key: "table-view",
      label: "Table View",
      children: <TableViewTab filter={filter} setFilter={setFilter} />,
      icon: <AlignLeftOutlined />
    },
    {
      key: "relationship",
      label: "Relationship Graph",
      children: <RelationShipTab />,
      icon: <ApartmentOutlined />
    }
  ];

  const { mutate: exportDataset, isPending } = useExportDatasetFile();
  const handleExportDataset = () => {
    if (!repoId || !view) return;
    exportDataset({
      repository_id: repoId,
      view,
      ...filterStatistic
    });
  };

  const hasStatistic = statisticDataset && Object.values(statisticDataset).some(Boolean);
  return (
    <>
      <Flex
        direction='column'
        style={{ background: v2CommonColors.neutral1, padding: 24, borderRadius: 8 }}
      >
        <Typography style={{ fontWeight: 700 }} level='h5-subtitles' color='primary10'>
          Dataset Assignment
        </Typography>
        <Typography color='primary10' level='body-14b'>
          Visualize and analyze JCL mapping information
        </Typography>
      </Flex>
      <Card
        style={{
          width: "100%"
        }}
      >
        <Flex gap={24} direction='column'>
          <Row style={{ width: "100%", margin: 0 }} wrap gutter={[16, 16]}>
            {data?.map((item, i) => {
              const { label, value } = item || {};
              return (
                <Col key={i} xs={24} md={12} lg={6}>
                  <Card
                    bodyStyle={{
                      padding: 4,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center"
                    }}
                    style={{ background: v2CommonColors.neutral3 }}
                    bordered={false}
                  >
                    <Statistic
                      loading={isLoading}
                      title={<Text style={{ textTransform: "uppercase" }}>{label}</Text>}
                      style={{
                        direction: "revert",
                        display: "flex",
                        flexDirection: "column-reverse",
                        justifyItems: "center",
                        justifyContent: "center",
                        textAlign: "center"
                      }}
                      value={value}
                      valueStyle={{
                        color: v2CommonColors.primary6,
                        fontWeight: 700,
                        fontSize: 24
                      }}
                    />
                  </Card>
                </Col>
              );
            })}
          </Row>
          {hasStatistic && (
            <Flex gap={16} justify='flex-end'>
              <Button
                style={{ borderRadius: 4 }}
                onClick={handleExportDataset}
                shape='default'
                loading={isPending}
                icon={<DownloadOutlined />}
              >
                Export CSV
              </Button>
            </Flex>
          )}
        </Flex>
      </Card>
      <Card
        style={{
          width: "100%"
        }}
      >
        <Flex gap={24} direction='column'>
          <Tabs
            activeKey={activeTab}
            onChange={key => {
              setActiveTab(key);
            }}
            items={items}
          />
        </Flex>
      </Card>
    </>
  );
}

export function DataAssetPage() {
  const { isCollapsed, isOpenChatBox } = useLayout();

  return (
    <Flex
      direction='column'
      gap={24}
      style={{
        margin: 24,
        overflowY: "auto",
        width:
          isCollapsed && isOpenChatBox
            ? "57vw"
            : isCollapsed || isOpenChatBox
            ? isOpenChatBox
              ? "calc(75vw - 92px)"
              : "100%"
            : "calc(100vw - 18vw)"
      }}
    >
      <PageContent />
    </Flex>
  );
}
