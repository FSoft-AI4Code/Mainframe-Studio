import { Tabs } from "antd";
import { lazy, useEffect, useMemo, useState } from "react";
import { useParams, useSearchParams } from "react-router-dom";

import { Flex, Typography } from "@components";
import { allColors } from "@style";
import { useGetReverseByPath } from "@services";
import { FileGroup, ReverseTypeEnum } from "@types";
import { useEntryPoint, useFilterGraph, useRoutesHandler } from "@hooks";

const OverviewPage = lazy(() => import("./Overview"));
const IOParameterPage = lazy(() => import("./IOParameter"));
const ProgramProcessLogicPage = lazy(() => import("./ProgramProcessLogic"));
const CallGraphPage = lazy(() => import("./CallGraph"));

const OverviewJCL = lazy(
  () => import("@pages/exploration/reports/components/JclReport/OverviewJCL")
);
const StepJCL = lazy(() => import("../reports/components/JclReport/StepJCL"));

const OverviewBMS = lazy(
  () => import("@pages/exploration/reports/components/BmsReport/OverviewBMS")
);
const ScreenLayoutBMS = lazy(
  () => import("@pages/exploration/reports/components/BmsReport/ScreenLayoutBMS")
);

const OverviewCOPY = lazy(
  () => import("@pages/exploration/reports/components/CopyReport/OverviewCOPY")
);

export function GraphDetail() {
  const { repoId } = useParams();
  const { setRecentRoute, pathname } = useRoutesHandler();

  const { entries, totalGraph } = useEntryPoint();

  const { selectedEntry, selectedEntries, setSelectedEntries } = useFilterGraph();

  // eslint-disable-next-line no-console
  console.log({ setSelectedEntries, selectedEntries });
  const [tab, setTab] = useState("overview");
  const overviewEntry = useMemo(
    () => entries?.find(entry => selectedEntry?.includes(entry.id)),
    [selectedEntry, entries]
  );
  const [searchParams] = useSearchParams();
  const selectedFile = searchParams.get("fileId") ?? "";

  const selectedFileDetail = useMemo(
    () => (totalGraph ? totalGraph.nodes.find(node => selectedFile === node._id) : null),
    [totalGraph, selectedFile]
  );

  const { fileType, name } = selectedFileDetail || {};

  const { reverseFile } = useGetReverseByPath({
    repoId: repoId as string,
    type: fileType as ReverseTypeEnum,
    name: name as string
  });

  const blobData = useMemo(() => reverseFile?.data.output, [reverseFile]);

  const data = useMemo(() => {
    const selected = selectedEntries[selectedFile];
    return !!selected ? selected : blobData;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
  }, [selectedFile, selectedEntries, blobData]) as Record<string, never | any>;

  useEffect(() => {
    if (selectedFile && !(selectedFile in selectedEntries) && blobData) {
      setSelectedEntries({ ...selectedEntries, [selectedFile]: blobData });
    }
  }, [selectedFile, blobData, selectedEntries]);

  useEffect(() => {
    if (!name) return;
    setRecentRoute({
      key: `Reverse ${name}`,
      path: `${pathname}?fileId=${selectedFile}`
    });
  }, [repoId, selectedFile, name]);

  const onChange = (key: string) => {
    setTab(key);
  };

  useEffect(() => {
    setTab("overview");
  }, [selectedFile]);

  return (
    <>
      {
        <Flex
          direction='column'
          style={{
            padding: 32,
            overflow: "auto",
            width: "100%",
            height: "100%"
          }}
        >
          <Flex
            style={{
              background: allColors.neutral1,
              padding: 16,
              borderRadius: "8px",
              minHeight: "calc(100vh - 72px - 64px)"
            }}
            direction='column'
            gap={16}
          >
            <Flex align='center' justify='space-between' style={{ width: "100%" }}>
              {name && (
                <>
                  <Typography
                    level='body-16b'
                    color='primary10'
                  >{`Reverse Review: ${name}`}</Typography>
                  <Flex
                    center
                    style={{
                      padding: "2px 8px",
                      background: allColors.primary6,
                      height: 24,
                      borderRadius: "100px",
                      cursor: "pointer"
                    }}
                  >
                    <Typography level='button-12m' color='neutral1'>
                      Confirm
                    </Typography>
                  </Flex>
                </>
              )}
            </Flex>
            {!!data && !!overviewEntry && (
              <Tabs
                activeKey={tab}
                items={
                  fileType === "COBOL"
                    ? [
                        {
                          key: "overview",
                          label: "Overview",
                          children: <OverviewPage overviewData={data.overview} />
                        },
                        {
                          key: "io",
                          label: "I/O Parameter Definition",
                          children: <IOParameterPage ioData={data.io_params_def} />
                        },
                        {
                          key: "program",
                          label: "Program Processing Logic",
                          children: (
                            <ProgramProcessLogicPage
                              programLogic={data.process_logic?.paragraph_level}
                            />
                          )
                        },
                        {
                          key: "graph",
                          label: "Call Graph",
                          children: (
                            <CallGraphPage copyGraphData={data.copy_graph} node={overviewEntry} />
                          )
                        }
                      ]
                    : fileType === "BMS"
                    ? [
                        {
                          key: "overview",
                          label: "Fields",
                          children: <OverviewBMS rows={data.data} />
                        },
                        {
                          key: "screen",
                          label: "Screen Layout",
                          children: <ScreenLayoutBMS screen_string={data.screen_string} />
                        }
                      ]
                    : fileType === "COPY"
                    ? [
                        {
                          key: "overview",
                          label: "Overview",
                          children: <OverviewCOPY data={data.variables} />
                        }
                      ]
                    : ["JCL_FUJITSU", "JCL_IBM", "JCL"].includes(fileType as FileGroup)
                    ? [
                        {
                          key: "overview",
                          label: "Overview",
                          children: (
                            <OverviewJCL title='JCL Overview' overviewData={data.overview} />
                          )
                        },
                        {
                          key: "step",
                          label: "Step",
                          children: <StepJCL steps={data.step_list} />
                        }
                      ]
                    : []
                }
                onChange={onChange}
                style={{ color: allColors.primary10, width: "100%", height: "100%" }}
              />
            )}
          </Flex>
        </Flex>
      }
    </>
  );
}
