import styled from "@emotion/styled";
import { Col } from "antd";

export const Wrapper = styled.div`
  background-color: ${({ theme }) => theme.colors.neutral};
  padding: 56px 51px;
  overflow: hidden auto;
  height: 100%;
  /* width */
  &::-webkit-scrollbar {
    width: 8px;
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

export const WrapCol = styled(Col)`
  margin-top: 32px;
`;

export const WrapperChart = styled.div`
  width: 100%;
  height: 100%;
  min-height: 420px;
  overflow: hidden;
`;

export const CardCustom = styled.div`
  padding: 16px;
  border-radius: 16px;
  background-color: ${({ theme }) => theme.colors.grey800};
  height: 100%;
  min-height: 200px;
`;
