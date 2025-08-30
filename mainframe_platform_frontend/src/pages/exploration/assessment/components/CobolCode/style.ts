import styled from "@emotion/styled";
import { Col } from "antd";

export const Title = styled.div`
  font-size: 20px;
  font-weight: 600px;
  span {
    cursor: pointer;
  }
`;

export const TitleHightLight = styled.span`
  color: ${({ theme }) => theme.colors.primary100};
`;

export const WrapperCobolCode = styled.div`
  line-height: 32px;
`;

export const WrapperProcess = styled.div`
  margin-top: 25px;
  padding-left: 32px;
`;

export const ProcessItem = styled.div<{ strokeColor: string }>`
  position: relative;
  margin-bottom: 12px;
  &:last-child {
    margin-bottom: 0px;
    .ant-progress-line {
      margin-bottom: 0px !important;
    }
  }

  .ant-progress .ant-progress-outer {
    background: transparent;
  }
  .ant-progress.ant-progress-default .ant-progress-bg {
    background-color: ${({ strokeColor }) => strokeColor} !important;
  }
  /* .ant-progress-inner {
      background-color: ${({ theme }) => theme.colors.actionSucess} !important;
      filter: brightness(85%);
    } */
  .ant-progress-text {
    position: absolute;
    top: -12px;
    right: 37px;
    font-size: 14px;
    width: 150px;
    text-align: right;
    color: ${({ strokeColor }) => strokeColor} !important;
  }
  .ant-progress-line {
    top: -8px;
  }
`;

export const ProcessName = styled.div`
  position: absolute;
  top: -24px;
  font-size: 14px;
  padding-right: 10px;
`;

export const WrapBadge = styled.div<{ align?: string }>`
  display: flex;
  flex-wrap: wrap;
  justify-content: ${({ align }) => align || "center"};
  align-items: center;
  margin-bottom: 16px;
  .ant-badge {
    padding-right: 20px;
    flex-wrap: wrap;
    .ant-badge-status-dot {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      margin-right: 6px;
    }
    .ant-badge-status-text {
      font-size: 14px;
    }
  }
`;
export const WrapAnalysisBlock = styled(Col)`
  display: flex;
  align-items: center;
`;
export const AnalysisBlock = styled.div`
  margin-bottom: 2px;
  background-color: ${({ theme }) => theme.colors.green};
  padding: 19px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 92px;
  width: 100%;
  &:first-child {
    border-radius: 3px 3px 3px 3px;
  }
  /* &:last-child {
    margin-bottom: 0px;
    border-radius: 0px 0px 3px 3px;
  } */
`;
