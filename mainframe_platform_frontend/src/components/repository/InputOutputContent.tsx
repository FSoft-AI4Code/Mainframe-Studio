import styled from "@emotion/styled";
import { useSelector } from "react-redux";

import { OverflowEmpty } from "@components";
import { fileSelector } from "@store";

const Wrapper = styled.div`
  white-space: pre-line;
`;

export const InputOutputContent: React.FC = () => {
  const data = useSelector(fileSelector.selectData);
  if (!data?.meta?.["input/output"]) return <OverflowEmpty />;
  return <Wrapper>{data.meta["input/output"]}</Wrapper>;
};
