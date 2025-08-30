import styled from "@emotion/styled";
import { Button } from "antd";

import { Flex } from "@components";

export const Container = styled(Flex)`
  overflow-y: scroll;
  flex: 1 1 0%;
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

export const ExportBtn = styled(Button)`
  width: auto;
  position: absolute;
  right: 32px;
  top: 38px;
  background-color: rgba(246, 208, 83, 0.5);

  div {
    display: flex;
    align-items: center;
    .icon {
      margin-left: 6px;
    }
  }
`;

export const WrapTabs = styled.div`
  // overflow: auto;
  padding-right: 145px;
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
