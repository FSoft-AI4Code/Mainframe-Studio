import styled from "@emotion/styled";
import { Empty, EmptyProps } from "antd";

export const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

type OverflowEmptyProps = EmptyProps;
export const OverflowEmpty: React.FC<OverflowEmptyProps> = props => {
  return (
    <Wrapper>
      <Empty {...props} />
    </Wrapper>
  );
};
