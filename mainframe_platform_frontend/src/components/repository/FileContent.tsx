import styled from "@emotion/styled";

import { OverflowEmpty } from "@components";

const Wrapper = styled.div`
  white-space: pre-line;
`;

export const FileContent: React.FC<{ code: string }> = ({ code }) => {
  if (!code) return <OverflowEmpty />;
  return <Wrapper>{code}</Wrapper>;
};
