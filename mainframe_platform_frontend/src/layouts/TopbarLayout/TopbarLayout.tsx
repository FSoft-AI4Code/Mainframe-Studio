/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
import styled from "@emotion/styled";
import { Layout, Menu, MenuProps } from "antd";
import React, { PropsWithChildren, useState } from "react";
import { generatePath, useNavigate, useParams } from "react-router-dom";

import { CodeSvg, LogoFullSvg, LogOutSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { ROUTERS } from "@defines";
import { useLogout } from "@services";
import { allColors } from "@style";
import { useLayout } from "@hooks";

import { HEADER_DASHBOARD_HEIGHT } from "./config";

const { Sider } = Layout;

export type MenuItem = Required<MenuProps>["items"][number] & {
  breadcrumb?: string;
  icon?: JSX.Element;
  label: React.ReactNode;
  key: string;
  children?: MenuItem[];
};
export type Props = PropsWithChildren & {
  segmented: {
    options: Array<MenuItem>;
    onChange: (value: string) => void;
    defaultValue: string;
    value?: string;
  };
};

export const Main = styled(Layout)`
  flex: 1 1 0%;
  width: 100%;
  background: ${({ theme }) => theme.allColors.neutral4};
`;

const Container = styled(Layout)`
  height: 100vh;
  display: flex;
  width: 100vw;
  overflow: hidden;
`;

const Toggle = styled(Flex)`
  position: absolute;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0.15);
  padding: 6px;
  top: ${HEADER_DASHBOARD_HEIGHT}px;
  left: 100%;
  transform: translate(-50%, -50%);
  background: ${({ theme }) => theme.v2Colors.neutral1};
  cursor: pointer;
  justify-content: space-between;

  &:hover {
    background-color: ${({ theme }) => theme.v2Colors.neutral3};
  }
`;

export const TopbarLayout: React.FC<Props> = ({ children, segmented }) => {
  const { isCollapsed, toggleSidebar } = useLayout();
  const navigate = useNavigate();
  const { repoId = "" } = useParams();
  const { mutate: logout } = useLogout();
  const settings = [
    {
      label: "Logout",
      key: "logout",
      icon: <LogOutSvg />
    }
  ];
  // const [selectedKeys, setSelectedKeys] = useState<string[]>([]);
  // eslint-disable-next-line no-console

  const handleClick = ({ key, keyPath }: { key: string; keyPath: string[] }) => {
    if (key === ROUTERS.EXPLORATION_AI_AGENT)
      return navigate(
        generatePath(`/${ROUTERS.EXPLORATION_AI_AGENT}`, {
          repoId
        })
      );
    const value = keyPath?.reverse()?.join("/");
    // setSelectedKeys([key]);
    segmented.onChange(value);
  };

  // const handleTitleClick = (key: string) => {
  //   if (key === ROUTERS.EXPLORATION_EXPLORATION) {
  //     setSelectedKeys([key]);
  //     navigate(key);
  //     segmented.onChange(key);
  //   }
  // };

  return (
    <>
      <Sider
        defaultCollapsed={false}
        collapsedWidth={92}
        width={"18vw"}
        trigger={null}
        collapsible
        collapsed={isCollapsed}
        style={{ height: "100vh" }}
      >
        <Toggle center onClick={toggleSidebar}>
          <CodeSvg />
        </Toggle>
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
          style={{ flex: "1 1 0%", height: `calc(100% - ${HEADER_DASHBOARD_HEIGHT}px)` }}
        >
          <Flex style={{ padding: "24px 18px 8px" }} center={isCollapsed}>
            <Typography level='caption-10s' color='neutral7'>
              MAIN
            </Typography>
          </Flex>
          <Menu
            theme='light'
            className='main-sidebar'
            defaultSelectedKeys={[(segmented.value as string) ?? segmented.defaultValue]}
            activeKey={segmented.value}
            // selectedKeys={selectedKeys}
            mode={"inline"}
            items={segmented.options}
            triggerSubMenuAction='hover'
            // _internalRenderSubMenuItem={(originNode, subMenuItemProps) => {
            //   if (selectedKeys?.[0] === ROUTERS.EXPLORATION_EXPLORATION) return originNode;
            //   return React.cloneElement(originNode, {
            //     onClick: () => {
            //       handleTitleClick(subMenuItemProps.eventKey);
            //     }
            //   });
            // }}
            onClick={handleClick}
          />
          <Flex
            style={{
              padding: "24px 18px 8px",
              marginTop: "auto",
              borderTop: `1px solid ${allColors.neutral6}`
            }}
            className='ant-menu-submenu-title'
            center={isCollapsed}
          >
            <Typography level='caption-10s' color='neutral7'>
              SETTINGS
            </Typography>
          </Flex>
          <Menu
            theme='light'
            mode={!isCollapsed ? "inline" : "vertical"}
            items={settings}
            onClick={() => logout()}
            className='main-sidebar'
          />
        </Flex>
      </Sider>
      <Container>
        <Main>{children}</Main>
      </Container>
    </>
  );
};
