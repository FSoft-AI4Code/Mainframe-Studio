import styled from "@emotion/styled";
import { Layout, Menu, MenuProps } from "antd";
import React, { PropsWithChildren, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { AIInSvg, CloseSvg, LogoFullSvg, LogOutSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { ROUTERS } from "@defines";
import { useLogout } from "@services";
import { allColors } from "@style";
import { useLayout, useMessages } from "@hooks";
import { CodeTree } from "@pages/ai-agent/components";
import { ChatBox } from "@pages/ai-agent/components/ChatBox";
import { ElementViews } from "@store";

import { HEADER_DASHBOARD_HEIGHT } from "./config";

const { Sider, Header } = Layout;
export type MenuItem = Required<MenuProps>["items"][number] & {
  breadcrumb?: string;
};
export type Props = PropsWithChildren & {
  segmented: {
    options: Array<MenuItem>;
    onChange: (value: string) => void;
    defaultValue: string;
    value?: string;
  };
};

const Container = styled(Layout)`
  height: 100vh;
  width: 100vw;
  overflow: hidden;
`;

export const Main = styled(Layout)`
  flex: 1 1 0%;
  background: ${({ theme }) => theme.allColors.neutral4};
`;

const AIAgentLayout: React.FC<Props> = ({ children }) => {
  const { isCollapsed } = useLayout();
  const navigate = useNavigate();
  const { mutate: logout } = useLogout();
  const settings = [
    {
      label: "Logout",
      key: "logout",
      icon: <LogOutSvg />
    }
  ];
  const { elementViews, setRenderElement } = useMessages();
  const [recentRoutes, setRecentRoutes] = useState<Record<string, string>>({});

  useEffect(() => {
    if (elementViews && elementViews !== "DEFAULT" && !recentRoutes[elementViews.toLowerCase()]) {
      setRecentRoutes((prev: Record<string, string>) => ({
        ...prev,
        [elementViews.toLowerCase()]: elementViews.toLowerCase()
      }));
    }
  }, [elementViews]);

  const removeRoute = (route: string) => {
    setRecentRoutes((prev: Record<string, string>) => {
      if (Object.keys(prev).length <= 1) {
        return prev;
      }
      const updatedRoutes = { ...prev };
      delete updatedRoutes[route];
      return updatedRoutes;
    });
    if (elementViews?.toLowerCase() === route) {
      const remainingRoutes = Object.values(recentRoutes).filter(r => r !== route) as string[];
      setRenderElement({
        isRendering: false,
        view: remainingRoutes[0]?.toUpperCase() as ElementViews
      });
    }
  };

  const closable = Object.keys(recentRoutes)?.length > 1;

  return (
    <>
      <Sider
        defaultCollapsed={false}
        collapsedWidth={92}
        width={"24vw"}
        trigger={null}
        collapsible
        collapsed={false}
        style={{
          borderRight: `1px solid ${allColors.neutral6}`,
          height: "100vh"
        }}
      >
        <div
          style={{
            height: HEADER_DASHBOARD_HEIGHT,
            padding: isCollapsed ? "18px 26px" : "18px 24px",
            borderBottom: `1px solid ${allColors.neutral6}`,
            transition: "padding .3s"
          }}
        >
          <Flex
            gap={5}
            style={{ overflow: "hidden", cursor: "pointer" }}
            onClick={() => navigate(ROUTERS.WORKSPACE_REPOSITORIES)}
          >
            <Flex center style={{ height: 36 }}>
              <LogoFullSvg height={36} />
            </Flex>
          </Flex>
        </div>

        <Flex
          direction='column'
          justify='space-between'
          style={{
            flex: "1 1 0%",

            height: `calc(100% - ${HEADER_DASHBOARD_HEIGHT}px)`
          }}
        >
          <Flex
            style={{
              flex: "1 1 0%",
              margin: 12,
              overflowX: "hidden",
              height: `calc(100% - ${HEADER_DASHBOARD_HEIGHT}px)`
            }}
          >
            <CodeTree />
          </Flex>
          <Menu
            style={{ marginTop: "auto", borderTop: `1px solid ${allColors.neutral6}` }}
            theme='light'
            mode={!isCollapsed ? "inline" : "vertical"}
            items={settings}
            onClick={() => logout()}
            className='main-sidebar'
          />
        </Flex>
      </Sider>
      <Container>
        <Main>
          <Flex
            style={{
              width: "100%",
              height: "72px",
              minHeight: "72px",
              overflow: "auto",
              padding: "0 16px ",
              borderBottom: `1px solid ${allColors.neutral6}`
            }}
            gap={16}
            justify='flex-start'
            align='center'
          >
            {Object.entries(recentRoutes)?.map(([key, value]) => (
              <Flex
                gap={8}
                style={{
                  borderRadius: "4px",
                  background:
                    elementViews?.toLocaleLowerCase() === value
                      ? allColors.neutral2
                      : allColors.neutral1,
                  padding: "8px",
                  cursor: "pointer",
                  minWidth: "max-content"
                }}
                onClick={() =>
                  setRenderElement({
                    isRendering: false,
                    view: (value as string)?.toUpperCase() as ElementViews
                  })
                }
                key={key}
                center
              >
                <Typography
                  level='caption-12m'
                  color={elementViews?.toLocaleLowerCase() === value ? "primary10" : "neutral6"}
                  style={{ whiteSpace: "nowrap", textTransform: "capitalize" }}
                >
                  {key}
                </Typography>
                <CloseSvg
                  stroke={
                    elementViews?.toLocaleLowerCase() === value && closable
                      ? allColors.primary10
                      : allColors.neutral6
                  }
                  onClick={e => {
                    e.stopPropagation();
                    removeRoute(value as string);
                  }}
                />
              </Flex>
            ))}
          </Flex>
          {children}
        </Main>
      </Container>
      <Sider
        style={{ height: "100vh" }}
        defaultCollapsed={false}
        width={"25vw"}
        trigger={null}
        collapsible
      >
        <Layout
          style={{
            flex: "1 1 0%",
            borderLeft: `1px solid ${allColors.neutral6}`,
            position: "relative",
            height: "100vh"
          }}
        >
          <Header
            style={{
              height: HEADER_DASHBOARD_HEIGHT,
              padding: "8px 20px",
              background: allColors.neutral3,
              borderBottom: `1px solid ${allColors.neutral6}`
            }}
          >
            <Flex
              align='center'
              style={{
                height: "100%"
              }}
              gap={8}
            >
              <AIInSvg />
              <Typography level='button-16s' color='primary10'>
                XMainframe
              </Typography>
            </Flex>
          </Header>
          <Flex style={{ height: "calc(100% - 72px)" }}>
            <ChatBox />
          </Flex>
        </Layout>
      </Sider>
    </>
  );
};

export default AIAgentLayout;
