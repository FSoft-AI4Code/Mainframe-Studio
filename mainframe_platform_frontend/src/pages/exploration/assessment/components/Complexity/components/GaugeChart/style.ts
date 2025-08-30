import styled from "@emotion/styled";

import { GaugeBaseSvg } from "@assets/svg";

export const WrapGauge = styled.div`
  display: flex;
  justify-content: center;
`;
export const CustomGaugeChart = styled.div`
  width: 100%;
  position: relative;
  height: 163px;
  svg {
    transition: all 0.25s 0.25s;
    path {
      transition: all 0.25s 0.25s;
    }
  }
`;
export const GaugeBaseSvgStyled = styled(GaugeBaseSvg)`
  min-width: 119px;
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
  top: 25px;
`;

export const ArrowGauge = styled.div<{ degPointed?: number }>`
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
  top: 52px;
  transition: all 0.25s 0.25s;
  transform-origin: bottom center;
  svg {
    transform: ${({ degPointed }) => `rotate(${degPointed}deg)`};
    transform-origin: bottom center;
    path {
      transition: all 0.25s 0.25s;
    }
  }
`;
export const GaugePercent = styled.div`
  font-size: 20px;
  text-align: center;
  left: 50%;
  transform: translate(-50%, 0);
  top: 105px;
  position: absolute;
`;
