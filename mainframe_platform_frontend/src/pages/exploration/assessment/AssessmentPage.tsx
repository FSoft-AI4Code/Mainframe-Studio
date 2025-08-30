import { Card, Col, Row, Statistic, Typography as TypographyAntd } from "antd";
import { useMemo } from "react";
import { useParams } from "react-router-dom";

import { CustomCard, Flex, Typography } from "@components";
import { useInventoryData } from "@hooks";
import { useComplexitiesDistributionQuery, useDeadCodeFile } from "@services";
import { v2CommonColors } from "@style";
import { DistComplexity, FileDeadCode } from "@types";
import { roundToDecimalPlaces } from "@utils";

import { ComplexityDistribution, Deadcode, DecompositionsComponent } from "./components";

const { Text } = TypographyAntd;

export function AssessmentPage() {
  const { repoId = "" } = useParams();

  const { locFileType, loadingInventory } = useInventoryData();

  const computedLocFileType = useMemo(
    () => Object.keys(locFileType)?.sort((a, b) => (locFileType[b] || 0) - (locFileType[a] || 0)),
    [locFileType]
  );

  const { complexitiesDistribution, isLoading } = useComplexitiesDistributionQuery({
    repoId,
    reprocess: false
  });
  const limit = 10;
  const page = 1;
  const skip = (page - 1) * limit;

  const {
    files,
    deadAndTotal,
    complexityReduction,
    isLoading: loadingDeadcode
  } = useDeadCodeFile({
    repoId,
    skip: skip,
    limit: limit
  });
  const { dead = 0, total = 0 } = deadAndTotal || {};

  return (
    <Flex direction='column' gap={24} style={{ padding: 24, overflow: "auto", width: "100%" }}>
      <>
        <Row gutter={[24, 24]}>
          <CustomCard
            loading={loadingInventory}
            title={
              <Typography level='body-16b' color='primary10'>
                Lines of Code by File Type
              </Typography>
            }
            style={{ height: "100%" }}
            colProps={{ xl: 24, lg: 24, xs: 24, md: 24, style: { width: "100%" } }}
          >
            <Row wrap gutter={[16, 16]}>
              {computedLocFileType?.map((key, i) => {
                const title = key?.split("_")?.join(" ") || "";
                const value = locFileType[key] || "";
                const columnCount = Math.min(computedLocFileType.length, 4);
                const colSize = Math.floor(24 / columnCount);
                return (
                  <Col key={i} xs={24} md={colSize}>
                    <Card
                      loading={loadingInventory}
                      style={{ background: v2CommonColors.neutral3 }}
                      bordered={false}
                    >
                      <Statistic
                        title={<Text style={{ textTransform: "uppercase" }}>{title}</Text>}
                        style={{
                          direction: "revert",
                          display: "flex",
                          flexDirection: "column-reverse"
                        }}
                        value={value}
                        // precision={2}
                        valueStyle={{
                          color: v2CommonColors.primary6,
                          fontWeight: 700,
                          fontSize: 24
                        }}
                        // suffix='%'
                      />
                    </Card>
                  </Col>
                );
              })}
            </Row>
          </CustomCard>
        </Row>
        <Row gutter={[24, 0]}>
          <CustomCard
            title={
              <Typography level='body-16b' color='primary10'>
                Complexity Distribution
              </Typography>
            }
            colProps={{ xs: 24, style: { width: "100%" } }}
          >
            <ComplexityDistribution
              loading={isLoading}
              data={complexitiesDistribution as DistComplexity}
            />
          </CustomCard>
        </Row>
        <Row gutter={[24, 24]}>
          <CustomCard
            title={
              <Typography level='body-16b' color='primary10'>
                Decomposition (Components)
              </Typography>
            }
            style={{ height: "100%" }}
            colProps={{ xl: 24, lg: 24, xs: 24, md: 24, style: { width: "100%" } }}
          >
            <Row style={{ padding: 8 }} wrap gutter={[16, 16]}>
              <DecompositionsComponent />
            </Row>
          </CustomCard>
        </Row>
        <Row gutter={[24, 24]}>
          <CustomCard
            title={
              <Typography level='body-16b' color='primary10'>
                Deadcode
              </Typography>
            }
            style={{ height: "100%" }}
            colProps={{ xl: 24, lg: 24, xs: 24, md: 24, style: { width: "100%" } }}
          >
            <Row wrap gutter={[16, 16]}>
              <Col xs={24} xl={6}>
                <Card
                  loading={loadingInventory}
                  style={{ background: v2CommonColors.neutral3 }}
                  bordered={false}
                >
                  <Statistic
                    title={
                      <Typography level='body-14m' color='primary10'>
                        Dead/Total
                      </Typography>
                    }
                    value={`${dead}/${total}`}
                    valueStyle={{
                      color: v2CommonColors.primary6,
                      fontWeight: 700,
                      fontSize: 24
                    }}
                  />
                </Card>
                <Card
                  loading={loadingInventory}
                  style={{ background: v2CommonColors.neutral3, marginTop: 24 }}
                  bordered={false}
                >
                  <Statistic
                    title={
                      <Typography level='body-14m' color='primary10'>
                        Complexity Reductions
                      </Typography>
                    }
                    value={`${roundToDecimalPlaces(complexityReduction, 2)}`}
                    valueStyle={{
                      color: v2CommonColors.primary6,
                      fontWeight: 700,
                      fontSize: 24
                    }}
                    suffix='%'
                  />
                </Card>
              </Col>
              <Col xs={24} xl={18}>
                <Deadcode loading={loadingDeadcode} data={files as FileDeadCode[]} />
              </Col>
            </Row>
          </CustomCard>
        </Row>
      </>
    </Flex>
  );
}
