import styled from "@emotion/styled";

export const WrapProcessMultilSteps = styled.div`
  position: relative;
`;
export const WrapLine = styled.div`
  display: flex;
  width: 100%;
  min-height: 8px;
  margin: 8px 0px;
  border-radius: 100px;
  background-color: ${({ theme }) => theme.colors.colorLink};
  overflow: hidden;
`;
export const PercentSucess = styled.div`
  position: absolute;
  top: -31px;
  right: 0px;
  font-size: 16px;
  color: ${({ theme }) => theme.colors.primary100};
`;

export const LineCustom = styled.div<{ color?: string; percent: number }>`
  background-color: ${({ color }) => color};
  width: ${({ percent }) => `${percent}px`};
`;
