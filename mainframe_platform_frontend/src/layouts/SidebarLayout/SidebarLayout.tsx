import { BreadcrumbProps, ProgressProps } from "antd";
import { PropsWithChildren, ReactNode } from "react";

import { DividerSvg } from "@assets/svg";
import { ResizableComponent } from "@components";

import {
  Breadcrumb,
  Container,
  ContainerType,
  Content,
  Main,
  Progress,
  Sider,
  WrapSider
} from "./styles";

type Props = PropsWithChildren & {
  breadcrumb: BreadcrumbProps;
  progress?: ProgressProps;
  type?: ContainerType;
  existHeader?: boolean;
  renderContent?: () => ReactNode;
};

export const SidebarLayout: React.FC<Props> = ({
  children,
  breadcrumb,
  progress,
  type,
  existHeader,
  renderContent = null
}) => {
  const currentWidth = Number(document.getElementById("root")?.clientWidth);
  const currentHeight = Number(document.getElementById("root")?.clientHeight);

  return (
    <Container type={type}>
      {Boolean(progress) && <Progress {...progress} showInfo={false} />}
      <WrapSider existheader={existHeader}>
        <ResizableComponent
          initialWidth={(currentWidth / 100) * 28}
          initialHeight={currentHeight - 70}
          minWidth={(currentWidth / 100) * 20}
          maxWidth={(currentWidth / 100) * 50}
        >
          <Sider trigger={null} width={"100%"} existheader={existHeader}>
            {renderContent?.()}
          </Sider>
        </ResizableComponent>
      </WrapSider>
      <Main>
        <Breadcrumb separator={<DividerSvg />} {...breadcrumb} />
        <Content
          style={{
            margin: "0 20px",
            minHeight: 280
          }}
        >
          {children}
        </Content>
      </Main>
    </Container>
  );
};
