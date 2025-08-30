import styled from "@emotion/styled";

import { CommonButtonWrapper } from "./components";

export const CustomLink = styled.div`
  text-decoration: underline;
  display: inline-block;
  cursor: pointer;
  &:hover {
    color: ${({ theme }) => theme.colors.primary100};
  }
`;

export const ButtonWrapper = styled(CommonButtonWrapper)`
  border-radius: 8px;
  padding: 6px 16px;
  height: 40px;
`;
