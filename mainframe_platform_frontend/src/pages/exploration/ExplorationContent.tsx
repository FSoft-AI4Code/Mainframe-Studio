/* eslint-disable no-console */
/* eslint-disable @typescript-eslint/no-unused-vars */
import { Layout } from "antd";
import { Outlet, useLocation } from "react-router-dom";

import { CloseSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { HEADER_DASHBOARD_HEIGHT } from "@layouts/TopbarLayout/config";
import { allColors } from "@style";
import { useRoutesHandler } from "@hooks";

const { Header } = Layout;

export const ExplorationContent = () => {
  const { updateRoutes, recentRoutes, navigate } = useRoutesHandler();
  const { pathname, search } = useLocation();
  const path = `${pathname}${search}`;
  const closable = Object.keys(recentRoutes)?.length > 1;

  return (
    <>
      <Header
        id='main-header'
        style={{
          height: HEADER_DASHBOARD_HEIGHT,
          borderBottom: `1px solid ${allColors.neutral6}`,
          background: allColors.neutral4,
          padding: "0 16px"
        }}
      >
        <Flex
          style={{ width: "100%", height: "100%", overflow: "auto", padding: "0 16px " }}
          gap={16}
          justify='flex-start'
          align='center'
        >
          {Object.entries(recentRoutes).map(([key, value]) => (
            <Flex
              gap={8}
              style={{
                borderRadius: "4px",
                background: path === value ? allColors.neutral2 : allColors.neutral1,
                padding: "8px",
                cursor: "pointer",
                minWidth: "max-content"
              }}
              onClick={() => navigate(value)}
              key={key}
              center
            >
              <Typography
                level='caption-12m'
                color={path === value ? "primary10" : "neutral6"}
                style={{ whiteSpace: "nowrap" }}
              >
                {key}
              </Typography>
              <CloseSvg
                style={{
                  cursor: closable ? "pointer" : "default",
                  stroke: path === value && closable ? allColors.primary10 : allColors.neutral6
                }}
                onClick={e => {
                  e.stopPropagation();
                  const keys = Object.keys(recentRoutes);
                  if (keys.length <= 1) return;
                  const index = keys.indexOf(key);
                  const previousRouteKey = index > 0 ? keys[index - 1] : keys[1];
                  const previousRoute = previousRouteKey ? recentRoutes[previousRouteKey] : null;
                  updateRoutes(key);
                  if (path === value && previousRoute) navigate(previousRoute);
                }}
              />
            </Flex>
          ))}
        </Flex>
      </Header>
      <Layout>
        <Flex style={{ background: allColors.neutral4, flex: "1 1 0%", height: "100%" }}>
          <Outlet />
        </Flex>
      </Layout>
    </>
  );
};
