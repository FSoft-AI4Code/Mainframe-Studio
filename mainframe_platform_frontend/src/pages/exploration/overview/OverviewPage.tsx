/* eslint-disable unused-imports/no-unused-vars */
import { Divider, Pagination, Row, Select, Space, Spin } from "antd";
import { useLocation, useParams } from "react-router-dom";

import { CustomCard, DropdowSliderFilter, Flex, PieChartSkeleton, Typography } from "@components";
import { useFilterGraph, useInventoryData, useSystemGraph } from "@hooks";
import { useDetailRepository, useReverseCoverage } from "@services";
import { v2CommonColors } from "@style";
import { generatePath, roundToDecimalPlaces } from "@utils";
import { ROUTERS } from "@defines";

import { DependencyGraph, LegendDependencyGraph } from "../dependencygraph/components";
import { CmLOC } from "../inventory/components";

import { AssessmentFileCount, WorksFlow } from "./components";

export function OverviewPage() {
  const { repoId = "" } = useParams();
  const { pathname } = useLocation();
  const { repositoryInfo } = useDetailRepository({ repositoryId: repoId || "" });
  const { totalCoverage } = useReverseCoverage({ repoId });
  const { loc, comment, loadingInventory } = useInventoryData();
  const {
    loc: locFilter,
    selectedGroup,
    setSelectedGroup,
    setNodeLimit,
    nodeLimit,
    setGraphFilter,
    complexity,
    pageNumber
  } = useFilterGraph();
  const { groups, nodes, loadingGraph, total, pageSize } = useSystemGraph();
  const isAIAgent = generatePath(`/${ROUTERS.EXPLORATION_AI_AGENT}`, { repoId }) === pathname;
  const isShowPagination = total > 0 && nodeLimit > 0 && total > nodeLimit;
  return (
    <Flex direction='column' gap={24} style={{ padding: 24, overflow: "auto", width: "100%" }}>
      <Flex style={{ background: v2CommonColors.neutral1, padding: 24, borderRadius: 8 }}>
        <Typography style={{ fontWeight: 700 }} level='h5-subtitles' color='primary10'>
          Overview Repository{repositoryInfo?.name ? `: ${repositoryInfo?.name}` : ""}
        </Typography>
      </Flex>
      <Row gutter={[24, 24]}>
        <AssessmentFileCount />
        <CustomCard
          loading={loadingInventory}
          title={
            <Typography level='body-16b' color='primary10'>
              Actual vs Comment Line of Codes
            </Typography>
          }
          style={{ width: "100%", height: "100%" }}
          colProps={{ lg: isAIAgent ? 24 : 12, xs: 24, md: 24, style: { width: "100%" } }}
        >
          {loadingInventory ? (
            <>
              <PieChartSkeleton style={{ width: "100%" }} />
            </>
          ) : (
            <CmLOC
              options={{ cutout: 45 }}
              width={180}
              height={180}
              code={loc - comment}
              comment={comment}
            />
          )}
        </CustomCard>
      </Row>
      <Row gutter={[24, 0]}>
        <Spin style={{ height: "100%" }} spinning={loadingGraph}>
          <CustomCard
            bodyStyle={{
              padding: "24px 0"
            }}
            colProps={{ xs: 24, style: { width: "100%" } }}
          >
            <Flex style={{ padding: "0 24px" }} justify='space-between' align='flex-start'>
              <Typography
                style={{ whiteSpace: "nowrap", width: "260px", display: "block" }}
                level='body-16b'
                color='primary10'
              >
                System Graph (Coverage: {`${roundToDecimalPlaces(totalCoverage, 2)}%`})
              </Typography>
              <Flex gap={8} align='flex-end' direction='column'>
                {isShowPagination && (
                  <Pagination
                    onChange={page => setGraphFilter({ pageNumber: page })}
                    style={{ width: "fit-content" }}
                    simple
                    pageSize={pageSize}
                    defaultCurrent={pageNumber}
                    total={total}
                  />
                )}
                <Space wrap style={{ justifyContent: "end" }}>
                  <DropdowSliderFilter
                    dropdownStyle={{ width: 300 }}
                    style={{ width: 150, marginLeft: "auto" }}
                    placeholder='Loc'
                    label='Loc filter'
                    value={locFilter ? locFilter : null}
                    min={0}
                    max={10000}
                    defaultValue={0}
                    onFilterChange={value =>
                      setGraphFilter({
                        loc: value as number
                      })
                    }
                  />
                  <DropdowSliderFilter
                    dropdownStyle={{ width: 300 }}
                    style={{ width: 150 }}
                    placeholder='Complexity'
                    label='Complexity filter'
                    value={complexity ? complexity : null}
                    min={0}
                    max={1000}
                    defaultValue={0}
                    onFilterChange={value =>
                      setGraphFilter({
                        complexity: value as number
                      })
                    }
                  />
                  <DropdowSliderFilter
                    dropdownStyle={{ width: 300 }}
                    style={{ width: 150 }}
                    placeholder='Node limit'
                    label='Node limit filter'
                    value={nodeLimit ? nodeLimit : null}
                    min={0}
                    max={1000}
                    defaultValue={1000}
                    onFilterChange={setNodeLimit as never}
                  />
                  <Select
                    style={{ maxWidth: 465, minWidth: 150 }}
                    options={groups.map(group => ({ value: group, label: group }))}
                    value={selectedGroup}
                    virtual
                    onChange={setSelectedGroup}
                    placeholder='Choose group'
                    allowClear
                    mode='multiple'
                  />
                </Space>
              </Flex>
            </Flex>
            <Divider />
            <Flex direction='column' style={{ padding: "0 24px" }}>
              <LegendDependencyGraph nodes={nodes} />
              <DependencyGraph initialScale={0.5} />
            </Flex>
          </CustomCard>
        </Spin>
      </Row>
      <WorksFlow />
    </Flex>
  );
}
