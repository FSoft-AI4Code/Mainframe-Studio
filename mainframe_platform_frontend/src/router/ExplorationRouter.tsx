import styled from "@emotion/styled";
import { Button } from "antd";
import { lazy } from "react";

import {
  AIAgentIcon,
  GraphInSvg,
  OverviewSvg,
  SysAssessmentSvg,
  SysExplorationSvg
} from "@assets/svg";
import { ROUTERS } from "@defines";
import { useRoutesHandler } from "@hooks";
import { ExplorationContent } from "@pages/exploration/ExplorationContent";

export const ExportBtn = styled(Button)`
  background-color: ${({ theme }) => theme.colors.primary100}80;

  div {
    display: flex;
    align-items: center;
    .icon {
      margin-left: 6px;
    }
  }
`;

const TopbarLayout = lazy(() => import("@layouts/TopbarLayout"));

const ExplorationRouter = () => {
  const { onChangeSegmented, route } = useRoutesHandler();

  return (
    <TopbarLayout
      key='topbar-layout'
      segmented={{
        options: [
          {
            label: "Overview",
            key: "overview",
            icon: <OverviewSvg />
          },
          {
            label: "Assessment",
            key: ROUTERS.EXPLORATION_ASSESSMENT,
            icon: <SysAssessmentSvg />
          },
          {
            label: "Exploration",
            key: ROUTERS.EXPLORATION_EXPLORATION,
            icon: <SysExplorationSvg />,
            children: [
              {
                label: "Entrypoints",
                key: ROUTERS.EXPLORATION_ENTRYPOINTS
              },
              {
                label: "CRUD Database",
                key: ROUTERS.EXPLORATION_DATABASE
              },
              {
                label: "Dataset",
                key: ROUTERS.EXPLORATION_DATASET
              },
              {
                label: "Duplication",
                key: ROUTERS.EXPLORATION_DUPLICATE
              },
              {
                label: "Utilities",
                key: ROUTERS.EXPLORATION_UTILITIES
              }
            ]
          },
          {
            label: "Report",
            key: ROUTERS.EXPLORATION_REPORTS,
            icon: <GraphInSvg />
          },
          {
            label: "AI Agent",
            key: ROUTERS.EXPLORATION_AI_AGENT,
            icon: <AIAgentIcon />
          }
        ],
        onChange: onChangeSegmented,
        defaultValue: "overview",
        value: route
      }}
    >
      <ExplorationContent />
    </TopbarLayout>
  );
};
export default ExplorationRouter;
