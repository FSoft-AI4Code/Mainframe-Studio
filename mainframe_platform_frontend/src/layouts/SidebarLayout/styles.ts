import styled from "@emotion/styled";
import { Layout, Breadcrumb as BreadcrumbUI, Progress as ProgressUI } from "antd";

import { HEADER_HEIGHT } from "@layouts/TopbarLayout/config";

const { Sider: SiderUI, Content: ContentUI } = Layout;

export const WrapSider = styled.div<{ existheader?: boolean }>`
  overflow: hidden;
  height: ${({ existheader }) => {
    return existheader ? `calc(100vh - ${HEADER_HEIGHT}px)` : "100vh";
  }};
  background-color: ${({ theme }) => theme.colors.neutral};
`;

export const Sider = styled(SiderUI)<{ existheader?: boolean }>`
  overflow: hidden scroll;
  height: calc(100vh - ${HEADER_HEIGHT}px);
  height: ${({ existheader }) => {
    return existheader ? `calc(100vh - ${HEADER_HEIGHT}px)` : "100vh";
  }};
  &::-webkit-scrollbar {
    width: 6px;
    height: 6px;
  }

  /* Track */
  &::-webkit-scrollbar-track {
    background: transparent;
  }

  /* Handle */
  &::-webkit-scrollbar-thumb {
    background: ${({ theme }) => theme.colors.primary100};
    border-radius: 4px;
  }

  /* Handle on hover */
  &::-webkit-scrollbar-thumb:hover {
    background: ${({ theme }) => theme.colors.primary100};
  }
`;

export const Main = styled(Layout)`
  height: 100%;
`;

export const Content = styled(ContentUI)`
  background: ${({ theme }) => theme.colors.neutral} !important;
  margin-right: 0 !important;
  margin-bottom: 0 !important;
  border-top-left-radius: 16px;
  height: 100%;
  display: flex;
  flex-direction: column;
  // &::-webkit-scrollbar {
  //   width: 6px;
  //   height: 6px;
  // }

  // /* Track */
  // &::-webkit-scrollbar-track {
  //   background: transparent;
  // }

  // /* Handle */
  // &::-webkit-scrollbar-thumb {
  //   background: ${({ theme }) => theme.colors.primary100};
  //   border-radius: 4px;
  // }

  // /* Handle on hover */
  // &::-webkit-scrollbar-thumb:hover {
  //   background: ${({ theme }) => theme.colors.primary100};
  // }
`;

export const Breadcrumb = styled(BreadcrumbUI)`
  padding: 40px 20px;
  height: 96px;
  li {
    padding-bottom: 5px;
  }
  .ant-breadcrumb-link {
    display: flex;
    font-size: 16px;
    font-weight: 500;
    line-height: 24px;

    & > *:not(:last-child) {
      margin-right: 6px;
    }
  }
  a.ant-breadcrumb-link {
    color: ${({ theme }) => theme.colors.primary100};
    text-decoration: underline;
  }
`;

export type ContainerType = "narrow" | "normal";
export const Container = styled(Layout)<{ type?: ContainerType }>`
  height: 100vh;
  display: flex;
  flex-direction: row;
`;

export const Progress = styled(ProgressUI)`
  margin: 0;
  padding: 0;
  line-height: 0;
  position: fixed;
  z-index: 1;
`;
