import { Card, Tabs } from "antd";
import { lazy, useState } from "react";
import { useParams } from "react-router-dom";

import { Flex, Typography } from "@components";
import { allColors } from "@style";
import { Repository, ReverseBMSData } from "@types";
import { useDetailEntryPointByName } from "@services";

import { ScrollableWrapper } from "../../../data-asset/styles";

const OverviewBMS = lazy(
  () => import("@pages/exploration/reports/components/BmsReport/OverviewBMS")
);
const ScreenLayoutBMS = lazy(
  () => import("@pages/exploration/reports/components/BmsReport/ScreenLayoutBMS")
);
const TransformedWebInterface = lazy(
  () => import("@pages/exploration/reports/components/BmsReport/TransformedBMS")
);
const SourceExplorerBMS = lazy(
  () => import("@pages/exploration/reports/components/BmsReport/SourceExplorerBMS")
);
interface BmsReportProps {
  bmsData: ReverseBMSData;
  loading: boolean;
}

export default function BMSReport({ bmsData, loading }: BmsReportProps) {
  const { screen_string: screenString, data } = bmsData?.output || {};
  const { type: fileType = "", name = "", repoId = "" } = useParams();

  const { entryPoint, refetchDetailEntrypoint } = useDetailEntryPointByName({
    repository_id: repoId,
    name: name,
    label: fileType
  });
  // eslint-disable-next-line no-console
  console.log("entryPoint", entryPoint);
  const status = entryPoint?.status;

  const [tab, setTab] = useState("overview");

  const onChange = (key: string) => {
    setTab(key);
  };

  return (
    <ScrollableWrapper direction='column'>
      <Card
        title={
          <Typography level='title-24b' color='primary10'>
            {fileType} Report: {name}
          </Typography>
        }
        // extra={
        //   <Button
        //     onClick={handleConvert}
        //     loading={isPending}
        //     style={{
        //       borderRadius: 8
        //     }}
        //     shape='round'
        //     type='primary'
        //   >
        //     Convert to Java
        //   </Button>
        // }
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
              {
                <Tabs
                  activeKey={tab}
                  items={[
                    {
                      key: "overview",
                      label: "Fields",
                      children: <OverviewBMS loading={loading} rows={data} />
                    },
                    {
                      key: "screen",
                      label: "Screen Layout",
                      children: <ScreenLayoutBMS loading={loading} screen_string={screenString} />
                    },
                    {
                      key: "modernization",
                      label: "Modernization",
                      children: <TransformedWebInterface />
                    },
                    {
                      key: "source-code",
                      label: "Source Code",
                      children: (
                        <SourceExplorerBMS
                          status={status as Repository["status"]}
                          refetchStatus={refetchDetailEntrypoint}
                        />
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
              }
            </Flex>
          }
        </Flex>
      </Card>
    </ScrollableWrapper>
  );
}
