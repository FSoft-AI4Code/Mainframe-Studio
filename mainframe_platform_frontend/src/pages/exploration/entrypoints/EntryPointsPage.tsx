import { useSearchParams } from "react-router-dom";
import { Spin } from "antd";

import { Flex, Typography } from "@components";
import { useEntryPoint, useFilterGraph, useRepository } from "@hooks";

import { ListEntries } from "./components/ListEntries";
import { Graph } from "./components/Graph";
import { GraphDetail } from "./GraphDetail";

function EntryPointsDetail() {
  const { totalGraph, selectedGraph } = useEntryPoint();
  const { showNode, setShowNode } = useFilterGraph();
  const [searchParams] = useSearchParams();
  const selectedFile = searchParams.get("fileId");

  return !!totalGraph ? (
    selectedFile ? (
      <GraphDetail />
    ) : (
      <Flex direction='column' style={{ padding: 32, overflow: "auto", width: "100%" }}>
        <ListEntries />
        {selectedGraph ? (
          <Graph graphData={selectedGraph} showNode={showNode} setShowNode={setShowNode} />
        ) : null}
      </Flex>
    )
  ) : null;
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
            <EntryPointsDetail />
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
