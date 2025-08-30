import styled from "@emotion/styled";
import ReactFlowChart, { Background, BackgroundVariant, Controls, ReactFlowProps } from "reactflow";
import "reactflow/dist/style.css";

export type FlowChartEdge = {
  target: string;
  label: string;
  source: string;
};

const Wrapper = styled.div`
  width: 100%;
  height: 100%;
  .react-flow__panel {
    display: none;
  }
  .react-flow__node-default {
    border: 1px solid #f6d053;
    background-color: transparent;
    color: white;
  }
`;

export const FlowChart: React.FC<ReactFlowProps> = ({ ...props }) => {
  return (
    <Wrapper>
      <ReactFlowChart {...props}>
        {/* <MiniMap /> */}
        <Controls />
        <Background color='#ccc' variant={BackgroundVariant.Dots} />
      </ReactFlowChart>
    </Wrapper>
  );
};
