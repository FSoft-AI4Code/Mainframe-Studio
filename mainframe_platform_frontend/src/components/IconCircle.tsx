import styled from "@emotion/styled";
import { ReactNode } from "react";

const DEFAULT_SIZE = 32;

const Container = styled.span<{ active?: boolean; size?: number; isStroke?: boolean }>`
  display: flex;
  justify-content: center;
  align-items: center;
  width: ${({ size }) => size || DEFAULT_SIZE}px;
  height: ${({ size }) => size || DEFAULT_SIZE}px;
  border-radius: 50%;
  background-color: ${({ theme, active }) =>
    active ? theme.colors.neutral : theme.colors.primary100};

  & svg {
    width: ${({ size }) => (size || DEFAULT_SIZE) * 0.7}px;
    height: ${({ size }) => (size || DEFAULT_SIZE) * 0.7}px;

    path {
      fill: ${({ theme, active }) => (active ? "white" : theme.colors.neutral)};

      ${props =>
        props.active &&
        props.isStroke &&
        `
         stroke:white;
    `}
    }
  }
`;

type Props = {
  icon: ReactNode;
  size?: number;
  active?: boolean;
  isStroke?: boolean;
};

export const IconCircle: React.FC<Props> = ({ icon, size, active, isStroke }) => (
  <Container active={active} size={size} isStroke={isStroke}>
    {icon}
  </Container>
);
