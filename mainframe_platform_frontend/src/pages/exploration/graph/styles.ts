import styled from "@emotion/styled";

import { Flex } from "@components";

export const Wrapper = styled(Flex)`
  background-color: ${({ theme }) => theme.colors.neutral};
  padding: 18px 72px;
`;

export const GraphWrapper = styled.div`
  position: relative;
  background-color: ${({ theme }) => theme.colors.neutral};
  background-image: linear-gradient(
      ${({ theme }) => theme.colors.primary100}33 0.5px,
      transparent 0.1em
    ),
    linear-gradient(90deg, ${({ theme }) => theme.colors.primary100}33 0.5px, transparent 0.1em);
  border: 0.5px solid ${({ theme }) => theme.colors.primary100}33;
  background-size: 16.67% 8em;

  .node {
    font-size: 20px;
  }
`;

export const Graph = styled.svg`
  background-color: transparent !important;
`;

export const ToolWrapper = styled(Flex)`
  width: 100%;

  .search-input {
    width: 350px;

    .ant-select {
      width: 100%;
    }
  }
`;
