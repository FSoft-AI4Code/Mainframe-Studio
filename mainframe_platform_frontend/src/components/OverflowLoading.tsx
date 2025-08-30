import styled from "@emotion/styled";
import { Spin, type SpinProps } from "antd";

export const WrapperSpin = styled.div`
  width: 100%;
  // height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const OverflowLoading: React.FC<SpinProps> = prop => {
  return (
    <WrapperSpin>
      <Spin {...prop} />
    </WrapperSpin>
  );
};
