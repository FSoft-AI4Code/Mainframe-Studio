import styled from "@emotion/styled";
import { FC } from "react";
import { Handle, Position } from "reactflow";

import { Typography } from "../../ui";

const CustomNodeStyled = styled.div`
  border: solid 1px;
  border-color: ${({ theme }) => theme.colors.primary100};
  min-width: 100px;
  .custom-node__header {
    border-bottom: solid 1px;
    border-color: ${({ theme }) => theme.colors.primary100};
    background-color: ${({ theme }) => theme.colors.secondary100};
    padding: 4px 6px;
    font-size: 12px;
    font-style: normal;
    font-weight: 600;
  }
  .custom-node__body {
    padding: 4px 6px;
  }
`;

type Props = {
  id: string;
  data?: {
    label?: string;
  };
};

export const CustomNode: FC<Props> = ({ id, data, sourcePosition, targetPosition }: any) => {
  return (
    <CustomNodeStyled>
      {data.label ? <div className='custom-node__header'>{data.label}</div> : null}
      <div className='custom-node__body'>
        <Typography level='h8-captionm'>{data.content || ""}</Typography>
      </div>
      <Handle type='source' position={sourcePosition || Position.Right} id={id} />
      <Handle type='target' position={targetPosition || Position.Right} id={id} />
    </CustomNodeStyled>
  );
};
