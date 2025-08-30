import styled from "@emotion/styled";
import { Modal } from "antd";

export const { warning } = Modal;

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

  .ant-table-tbody > tr:hover > td {
    background: ${({ theme }) => theme.colors.neutral2} !important;
  }

  .ant-pagination {
    margin: 16px 0;
    .ant-pagination-item-active {
      background: ${({ theme }) => theme.colors.primary6};
      border-color: ${({ theme }) => theme.colors.primary6};
      a {
        color: ${({ theme }) => theme.colors.neutral1};
      }
    }
  }
`;

export const FilterSection = styled.div`
  display: flex;
  gap: 16px;
  margin-bottom: 16px;

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
