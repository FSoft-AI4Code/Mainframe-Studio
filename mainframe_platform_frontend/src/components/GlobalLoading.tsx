import styled from "@emotion/styled";
import { Spin } from "antd";

const Wrap = styled.div`
  position: fixed;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: ${({ theme }) => theme.colors.primary200};
`;

export const GlobalLoading: React.FC = () => (
  <Wrap>
    <Spin size='large' />
  </Wrap>
);
