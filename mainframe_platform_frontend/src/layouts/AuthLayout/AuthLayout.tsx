import { Layout } from "antd";
import { PropsWithChildren } from "react";
import styled from "@emotion/styled";

const Container = styled(Layout)`
  width: 100vw;
  height: 100vh;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: ${({ theme }) => theme.v2Colors.neutral1};

  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 67%;
    height: 80%;
    border-radius: 0px 0px 393px 0px;
    background: ${({ theme }) => theme.v2Colors.support00};
  }
`;

const Wrap = styled.div`
  z-index: 1;
`;

export const AuthLayout: React.FC<PropsWithChildren> = ({ children, ...props }) => {
  return (
    <Container>
      <Wrap {...props}>{children}</Wrap>
    </Container>
  );
};
