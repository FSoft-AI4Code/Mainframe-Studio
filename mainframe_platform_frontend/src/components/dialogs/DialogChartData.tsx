import styled from "@emotion/styled";
import { Modal, ModalProps } from "antd";
import { ReactNode } from "react";

import { OverflowLoading } from "../OverflowLoading";

type Props = ModalProps & {
  left?: ReactNode;
  right?: ReactNode;
  loading?: boolean;
  height?: number;
  borderColor?: string;
  closeIcon?: ReactNode;
};

const Content = styled.div<{ height?: number }>`
  display: flex;
  flex-direction: column;
  padding: 16px 24px;
  width: 100%;
  gap: 10px;
`;

const WrapModal = styled(Modal)<ModalProps & { borderColor?: string }>`
  .ant-modal-content {
    padding: 0;
    border-color: ${({ theme, borderColor }) =>
      borderColor ? borderColor : theme.colors.primary100} !important;
  }
  .ant-modal-footer {
    margin-top: 0px;
  }
`;

export const DialogChartData: React.FC<Props> = ({
  left,
  closeIcon,
  borderColor,
  right,
  loading,
  height,
  ...props
}) => {
  return (
    <WrapModal
      {...props}
      centered
      footer
      closable={closeIcon ? false : true}
      borderColor={borderColor}
    >
      <Content height={height}>
        {closeIcon && closeIcon}
        {loading ? (
          <OverflowLoading />
        ) : (
          <>
            {left}
            {right ? right : null}
          </>
        )}
      </Content>
    </WrapModal>
  );
};
