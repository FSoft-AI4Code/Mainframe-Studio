import styled from "@emotion/styled";

export const Title = styled.div`
  font-size: 20px;
  font-weight: 600px;
  margin-bottom: 16px;
`;

export const Wrapper = styled.div`
  line-height: 32px;
`;

export const WrapGauge = styled.div`
  display: flex;
  justify-content: center;
`;

export const WrapBadge = styled.div<{ align?: string }>`
  display: flex;
  flex-wrap: wrap;
  justify-content: ${({ align }) => align || "center"};
  align-items: center;
  margin-top: 20px;
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
