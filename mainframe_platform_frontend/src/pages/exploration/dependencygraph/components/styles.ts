import styled from "@emotion/styled";

export const GraphWrapper = styled.div`
  position: relative;
  background-color: ${({ theme }) => theme.colors.neutral1};
  background-image: linear-gradient(
      ${({ theme }) => theme.colors.primary6}33 0.5px,
      transparent 0.1em
    ),
    linear-gradient(90deg, ${({ theme }) => theme.colors.primary6}33 0.5px, transparent 0.1em);
  border: 0.5px solid ${({ theme }) => theme.colors.primary6}33;
  background-size: 16.67% 8em;
  height: 100%;

  .node {
    font-size: 20px;
  }
`;

export const GraphSvg = styled.svg`
  background-color: transparent !important;
  width: 100%;
  height: 70vh !important;
`;

export const boxHeight = 25;
