import { Card, Col, Row, Statistic, Typography as TypographyAntd } from "antd";
import { useMemo } from "react";
import { useLocation, useParams } from "react-router-dom";
import { DownloadOutlined } from "@ant-design/icons";

import { Button, CustomCard, Typography } from "@components";
import { useAssessmentFileCountRepository, useExportStatisticReport } from "@services";
import { v2CommonColors } from "@style";
import { generatePath, sortBy } from "@utils";
import { ROUTERS } from "@defines";

const { Text } = TypographyAntd;

export function AssessmentFileCount() {
  const { repoId = "" } = useParams();

  const { pathname } = useLocation();
  const { assessmentFileCount, isLoading } = useAssessmentFileCountRepository({
    repoId
  });

  const assessmentFileCountSorted = useMemo(
    () => sortBy(assessmentFileCount, ["count", "label"], ["desc", "asc"]),
    [assessmentFileCount, repoId]
  );
  const isAIAgent = generatePath(`/${ROUTERS.EXPLORATION_AI_AGENT}`, { repoId }) === pathname;

  const { mutate: exportStatisticReport, isPending } = useExportStatisticReport();
  const handleExportStatistic = () => {
    if (!repoId) return;
    exportStatisticReport(repoId);
  };

  return (
    <CustomCard
      loading={isLoading || !assessmentFileCount}
      title={
        <Typography level='body-16b' color='primary10'>
          Assets
        </Typography>
      }
      extra={
        <Button
          style={{ borderRadius: 4 }}
          onClick={handleExportStatistic}
          shape='default'
          loading={isPending}
          icon={<DownloadOutlined />}
        >
          Export Report
        </Button>
      }
      style={{ height: "100%" }}
      colProps={{ lg: isAIAgent ? 24 : 12, xs: 24, md: 24, style: { width: "100%" } }}
    >
      <Row wrap gutter={[16, 16]}>
        {assessmentFileCountSorted?.map(({ count, label }) => {
          const cols = assessmentFileCountSorted?.length >= 3 ? 8 : 12;
          return (
            <Col key={label} xs={24} sm={12} md={cols}>
              <Card style={{ background: v2CommonColors.neutral3 }} bordered={false}>
                <Statistic
                  title={<Text>{label}</Text>}
                  style={{
                    direction: "revert",
                    display: "flex",
                    flexDirection: "column-reverse"
                  }}
                  value={count}
                  valueStyle={{ color: v2CommonColors.primary6, fontWeight: 700, fontSize: 24 }}
                  // suffix='%'
                />
              </Card>
            </Col>
          );
        })}
      </Row>
    </CustomCard>
  );
}
