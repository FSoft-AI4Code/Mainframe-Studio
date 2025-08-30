import styled from "@emotion/styled";
import Table from "antd/es/table";
import { Modal } from "antd";

import { allColors } from "@style";
import { Flex } from "@components";

export const { confirm } = Modal;

export const ScrollableWrapper = styled(Flex)`
  width: 100%;
  height: 100%;
  overflow: auto;
  padding: 24px;

  // Hide scrollbar for Chrome, Safari and Opera
  &::-webkit-scrollbar {
    display: none;
  }

  // Hide scrollbar for IE, Edge and Firefox
  -ms-overflow-style: none;
  scrollbar-width: none;
`;

export const TableWrapper = styled.div`
  width: 100%;

  .ant-table {
    background: ${({ theme }) => theme.colors.neutral1};
  }

  .ant-table-thead > tr > th {
    background: ${({ theme }) => theme.colors.neutral2} !important;
    color: ${({ theme }) => theme.colors.primary10};
    font-weight: 600;
    padding: 12px 16px;
    border-bottom: 1px solid ${({ theme }) => theme.colors.neutral6};
  }

  .ant-table-tbody > tr > td {
    color: ${({ theme }) => theme.colors.primary10};
    padding: 12px 16px;
    border-bottom: 1px solid ${({ theme }) => theme.colors.neutral6};
  }
`;

export const CustomTable = styled(Table)`
  .ant-table-thead {
    .ant-table-cell {
      background: ${allColors.neutral3};
      // border-color: ${allColors.neutral7};
      // border-radius: none;
      padding: 6px 12px;
    }
  }
  .ant-table-tbody {
    .ant-table-cell {
      vertical-align: top;
      padding: 6px 12px;
      font-size: 14px;
    }
  }
`;

export const FilterSection = styled.div`
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  justify-content: space-between;
  .ant-input {
    max-width: 300px;
    background: ${({ theme }) => theme.colors.neutral2};
    border: 1px solid ${({ theme }) => theme.colors.neutral6};
    color: ${({ theme }) => theme.colors.primary10};
    &::placeholder {
      color: ${({ theme }) => theme.colors.neutral8};
    }
  }

  .ant-select {
    min-width: 150px;
    .ant-select-selector {
      background: ${({ theme }) => theme.colors.neutral2} !important;
      border: 1px solid ${({ theme }) => theme.colors.neutral6} !important;
    }
    .ant-select-selection-item {
      color: ${({ theme }) => theme.colors.primary10};
    }
  }
`;
