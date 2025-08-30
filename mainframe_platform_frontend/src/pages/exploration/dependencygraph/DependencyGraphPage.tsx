import { Select, Spin } from "antd";

import { Flex, Typography } from "@components";
import { useFilterGraph, useRepository, useSystemGraph } from "@hooks";
import { allColors } from "@style";

import { DependencyGraph, LegendDependencyGraph } from "./components";

function GraphDetail() {
  // const { render, onHoverInNode, onHoverOutNode } = useChartTooltip();
  const { selectedGroup, setSelectedGroup } = useFilterGraph();
  const { groups, nodes } = useSystemGraph();

  return (
    <Flex style={{ padding: 24, width: "100%", height: "100%" }}>
      <Flex
        style={{
          width: "100%",
          height: "100%",
          background: allColors.neutral1,
          borderRadius: "8px"
        }}
        direction='column'
      >
        <Flex
          justify='space-between'
          align='center'
          style={{ padding: 20, borderBottom: `1px solid ${allColors.neutral6}` }}
        >
          <Typography color='primary10' level='body-16b'>
            Module Dependency Graph
          </Typography>
          <Select
            style={{ maxWidth: 500, minWidth: 150 }}
            options={groups.map(group => ({ value: group, label: group }))}
            value={selectedGroup}
            onChange={setSelectedGroup}
            placeholder='Choose group'
            allowClear
            mode='multiple'
          />
        </Flex>
        <Flex style={{ padding: "10px 20px 20px", flex: "1 1 0%" }} gap={8} direction='column'>
          <LegendDependencyGraph nodes={nodes} />
          <DependencyGraph initialScale={0.8} />
        </Flex>
      </Flex>
    </Flex>
  );
}

export function DependencyGraphPage() {
  const { repository, loadingRepository } = useRepository();

  return (
    <>
      {loadingRepository || !repository ? (
        <Flex center style={{ width: "100%", height: "100%" }}>
          <Spin size='default' />
        </Flex>
      ) : (
        <>
          {!!repository ? (
            <GraphDetail />
          ) : (
            <Flex
              center
              style={{ width: "100%", background: "white", margin: "24px", borderRadius: "8px" }}
            >
              <Typography level='body-16b' color='primary10'>
                Reverse repository hasn't finished yet. Come back later
              </Typography>
            </Flex>
          )}
        </>
      )}
    </>
  );
}
