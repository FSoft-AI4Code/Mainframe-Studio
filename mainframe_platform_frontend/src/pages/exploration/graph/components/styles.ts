import styled from "@emotion/styled";
import { Button } from "antd";

export const WrapInfo = styled.div`
  background-color: ${({ theme }) => theme.colors.grey700};
  padding: 4px 12px;
  border-radius: 4px;
`;

export const WrapContent = styled.div<{ thumbColor?: string }>`
  background-color: ${({ theme }) => theme.colors.grey700};
  padding: 6px 12px;
  border-radius: 4px;
  max-height: 294px;
  gap: 6px;
  overflow: auto;
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
    background: ${({ theme, thumbColor }) => (thumbColor ? thumbColor : theme.colors.primary100)};
    border-radius: 4px;
  }

  /* Handle on hover */
  &::-webkit-scrollbar-thumb:hover {
    background: ${({ theme, thumbColor }) => (thumbColor ? thumbColor : theme.colors.primary100)};
  }
  .content {
    color: ${({ theme }) => theme.colors.grey300};
    white-space: pre-line;
  }
`;

export const WrapDeadcode = styled.div<{ isDeadCode?: boolean }>`
  display: flex;
  align-items: center;
  text-decoration: ${({ isDeadCode }) => (isDeadCode ? "auto" : "line-through")};
`;

export const WrapAction = styled.div`
  display: flex;
  align-items: center;
  justify-content: flex-end;
  svg {
    cursor: pointer;
  }
`;

export const WrapClose = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: ${({ theme }) => theme.colors.grey};
  margin-left: 6px;
  cursor: pointer;
`;
export const WrapExport = styled.div`
  text-align: right;
`;

export const ExportBtn = styled(Button)`
  background-color: rgba(246, 208, 83, 0.5);
  div {
    display: flex;
    align-items: center;
    .icon {
      margin-left: 6px;
    }
  }
`;

export const GraphSvg = styled.svg`
  background-color: transparent !important;
`;
