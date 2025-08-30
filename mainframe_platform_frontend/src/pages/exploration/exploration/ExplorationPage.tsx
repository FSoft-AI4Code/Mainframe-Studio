/* eslint-disable @typescript-eslint/no-unused-vars */
import { Spin } from "antd";

import { Flex } from "@components";
import { useEntryPoint, useFilterGraph } from "@hooks";

// import { GraphDetail } from "../entrypoints/GraphDetail";
import { Graph } from "../entrypoints/components/Graph";
import { ListEntries } from "../entrypoints/components/ListEntries";

function EntryPointsDetail() {
  const { totalGraph, selectedGraph, loadingGraph } = useEntryPoint();
  const { showNode, setShowNode } = useFilterGraph();

  return (
    <Spin style={{ width: "100%" }} spinning={loadingGraph}>
      <Flex direction='column' style={{ padding: 32, overflow: "auto", width: "100%" }}>
        {totalGraph && (
          <>
            <ListEntries />
            {selectedGraph ? (
              <Graph graphData={selectedGraph} showNode={showNode} setShowNode={setShowNode} />
            ) : null}
          </>
        )}
      </Flex>
    </Spin>
  );
}

export function ExplorationPage() {
  return (
    <>
      <EntryPointsDetail />
    </>
  );
}
