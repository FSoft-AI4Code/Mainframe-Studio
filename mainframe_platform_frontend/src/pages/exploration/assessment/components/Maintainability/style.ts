import styled from "@emotion/styled";

export const Title = styled.div`
  font-size: 20px;
  font-weight: 600px;
`;

export const WrapperProcess = styled.div`
  margin-top: 36px;
  margin-bottom: 32px;
  display: flex;
  justify-content: center;
  .ant-progress-text {
    width: 63px !important;
    height: 63px;
    background-color: ${({ theme }) => theme.colors.actionDanger};
    border-radius: 50%;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute !important;
    left: 37px !important;
  }
`;

export const WrapBadge = styled.div<{ align?: string }>`
  display: flex;
  flex-wrap: wrap;
  justify-content: ${({ align }) => align || "center"};
  align-items: center;
  .ant-badge {
    padding: 0px 12px;
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
