import styled from "@emotion/styled";
import { Layout, Modal, ModalProps } from "antd";
import { Dispatch, lazy, SetStateAction, Suspense } from "react";

import { AIInSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { allColors } from "@style";
const ChatBotPage = lazy(() => import("@pages/chatbot"));

const { Header } = Layout;

const WrapModal = styled(Modal)<ModalProps>`
  .ant-modal-content {
    padding: 0px;
    background-color: white !important;
    overflow: hidden;
    position: relative;
    width: 24vw;
  }
  .ant-modal-close {
    position: absolute;
    top: 12px;
    right: 16px;
  }
  .ant-modal-footer {
    background: white;
  }
`;

export function ChatBoxModal({
  setOpen,
  open
}: {
  setOpen: Dispatch<SetStateAction<boolean>>;
  open: boolean;
}) {
  const handleCancel = () => {
    setOpen(false);
  };
  return (
    <WrapModal
      footer={false}
      closable
      open={open}
      style={{ position: "fixed", top: "auto", bottom: 120, right: 24, margin: 0, height: "70vh" }}
      width={"24vw"}
      okText='Save Change'
      onCancel={handleCancel}
      maskStyle={{
        backgroundColor: "rgba(0, 0, 0, 0)"
      }}
      bodyStyle={{
        background: "white"
      }}
    >
      <Layout
        style={{
          flex: "1 1 0%",
          width: "24vw",
          height: "70vh",
          // borderLeft: `1px solid ${allColors.neutral6}`,
          borderRadius: 8
        }}
      >
        <Header
          style={{
            height: "calc(max(5vh, 48px))",
            padding: "8px 20px",
            background: allColors.neutral3,
            borderBottom: `1px solid ${allColors.neutral6}`
          }}
        >
          <Flex align='center' gap={8}>
            <AIInSvg />
            <Typography level='button-16s' color='primary10'>
              XMainframe
            </Typography>
          </Flex>
        </Header>
        <Suspense fallback={null}>
          <ChatBotPage />
        </Suspense>
      </Layout>
    </WrapModal>
  );
}
