import { Spin } from "antd";
import { useEffect } from "react";
import { useParams } from "react-router-dom";

import { Flex } from "@components";
import { useRoutesHandler } from "@hooks";
import { useGetReverseByPath } from "@services";
import { ReverseBMSData, ReverseCobolData, ReverseCopybookData, ReverseTypeEnum } from "@types";

import { BMSReport, CobolReport, CopyBookReport, EmptyReport, JCLReport } from "./components";

export default function ReportDetailPage() {
  const { repoId = "", type = "", name = "" } = useParams();
  const { setRecentRoute, pathname } = useRoutesHandler();

  const curentType = type as ReverseTypeEnum;

  const {
    reverseFile,
    isLoading,
    refetch: refetchReport
  } = useGetReverseByPath({
    repoId: repoId,
    type: curentType,
    name: name
  });
  const { data: reverseData } = reverseFile || {};
  const contentReportWithType: Record<ReverseTypeEnum, JSX.Element> = {
    [ReverseTypeEnum.COBOL]: (
      <CobolReport refetchReport={refetchReport} cobolData={reverseData as ReverseCobolData} />
    ),
    [ReverseTypeEnum.COPY]: <CopyBookReport copybookData={reverseData as ReverseCopybookData} />,
    [ReverseTypeEnum.BMS]: (
      <BMSReport loading={isLoading} bmsData={reverseData as ReverseBMSData} />
    ),
    [ReverseTypeEnum.JCL]: <JCLReport loading={isLoading} jclData={reverseData as never} />,
    [ReverseTypeEnum.DEFAULT]: <EmptyReport />
  };

  const renderContentReportByType = () => {
    // if (!reverseData) return contentReportWithType.DEFAULT;
    if (curentType?.startsWith(ReverseTypeEnum.JCL)) return contentReportWithType.JCL;
    return contentReportWithType[curentType] ?? contentReportWithType.DEFAULT;
  };

  // Add effect for recent routes
  useEffect(() => {
    if (!name) return;
    setRecentRoute({ key: `Report file: ${name}`, path: pathname });
  }, [name, setRecentRoute]);

  if (isLoading) {
    return (
      <Flex center style={{ width: "100%", height: "100%" }}>
        <Spin size='large' />
      </Flex>
    );
  }

  return renderContentReportByType();
}
