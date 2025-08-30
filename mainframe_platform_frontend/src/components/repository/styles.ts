import styled from "@emotion/styled";
import { Table } from "antd";
import { RefTable } from "antd/es/table/interface";

export const Wrapper = styled.div`
  white-space: pre-line;
  word-break: break-all;
`;

export const WrapTabs = styled.div`
  max-width: 600px;
  .ant-tabs {
    margin-bottom: 32px;
  }
`;

export const Title = styled.div`
  font-size: 16px;
  color: ${({ theme }) => theme.colors.primary100};
`;

export const WrapLoading = styled.div`
  margin-bottom: 20px;
  color: ${({ theme }) => theme.colors.primary100};
`;

export const MatchingProcess = styled.div`
  max-width: 300px;
  margin-bottom: 32px;
  display: flex;
  .ant-progress .ant-progress-outer {
    background: transparent;
  }
  .ant-progress.ant-progress-default .ant-progress-bg {
    background-color: ${({ theme }) => theme.colors.actionSucess} !important;
  }
  .ant-progress-text {
    position: absolute;
    top: -20px;
    right: 37px;
    width: 60px;
    text-align: right;
    font-size: 16px;
    color: ${({ theme }) => theme.colors.primary100};
  }
`;

export const TestCaseWrap = styled.div`
  .ant-pagination {
    justify-content: center;
  }
`;

export const TestCaseProcess = styled.div`
  max-width: 300px;
  margin-bottom: 32px;
`;

export const GroupPriority = styled.div`
  display: flex;
  justify-content: center;
  svg {
    margin-right: 8px;
  }
`;

export const CustomTable = styled(Table)<RefTable & any>`
  td {
    vertical-align: top;
  }
`;

export const CustomEdgeLabel = styled.div<{ labelX?: string; labelY?: string }>`
  position: absolute;
  background: #766b45;
  font-size: 14px;
  padding-right: 5px;
  padding-left: 7px;
  color: #d9d9d9;
  border-radius: 2px;
  &::after {
    content: "";
    display: block;
    width: 7px;
    height: 7px;
    transform: rotate(45deg);
    top: 10px;
    left: -3px;
    position: absolute;
    background: #766b45;
  }
`;

export const WrapTable = styled.div`
  // overflow: auto;
  font-weight: 400;
  .ant-table-cell {
    font-size: 16px;
    font-style: normal;
  }
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

export const WrapCol = styled.div<{ mw?: number }>`
  min-width: ${({ mw }) => `${mw}px` || "50px"};
`;
