/* eslint-disable unused-imports/no-unused-imports */
// eslint-disable-next-line import/order
import { Empty } from "antd";
import { useCallback } from "react";
import { useNavigate } from "react-router-dom";

import { SysAssessmentSvg } from "@assets/svg";
import { Flex, PageSkeleton } from "@components";
import { ROUTERS } from "@defines";
import { useMessages } from "@hooks";
import AIAgentLayout from "@layouts/AIAgentLayout/AIAgentLayout";
import { HEADER_DASHBOARD_HEIGHT } from "@layouts/AIAgentLayout/config";
import AssessmentPage from "@pages/exploration/assessment";
import ExplorationPage from "@pages/exploration/exploration";
import OverviewPage from "@pages/exploration/overview";
import { ElementViews } from "@store";

const content: Record<ElementViews, JSX.Element> = {
  OVERVIEW: <OverviewPage />,
  EXPLORATION: <ExplorationPage />,
  ASSESSMENT: <AssessmentPage />,
  DEFAULT: (
    <Flex
      direction='column'
      gap={24}
      center
      align='center'
      style={{
        padding: 24,
        overflow: "auto",
        width: "100%",
        height: `calc(100vh - ${2 * HEADER_DASHBOARD_HEIGHT}px)`
      }}
    >
      <Empty />
    </Flex>
  )
};
const renderContent = (view: ElementViews) => content[view] || content.DEFAULT;

export function AIAgentPage() {
  const navigate = useNavigate();
  const onChangeSegmented = useCallback((value: string) => {
    navigate(`/${value}`);
  }, []);
  const { isRenderingElement, elementViews } = useMessages();

  return (
    <AIAgentLayout
      segmented={{
        options: [
          {
            label: "Repository List",
            key: ROUTERS.WORKSPACE_REPOSITORIES.replace("/", ""),
            icon: <SysAssessmentSvg />,
            breadcrumb: "List File"
          }
        ],
        onChange: onChangeSegmented,
        defaultValue: ROUTERS.WORKSPACE_REPOSITORIES.replace("/", ""),
        value: location.pathname.slice(1)
      }}
    >
      {isRenderingElement ? (
        <Flex
          direction='column'
          align='flex-start'
          style={{
            margin: "24px",
            borderRadius: 12,
            height: "100%",
            overflow: "hidden",
            background: "white"
          }}
        >
          <PageSkeleton />
        </Flex>
      ) : (
        <Flex direction='column' style={{ overflow: "auto" }}>
          {renderContent(elementViews)}
        </Flex>
      )}
    </AIAgentLayout>
  );
}
