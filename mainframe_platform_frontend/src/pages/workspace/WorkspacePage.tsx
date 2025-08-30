/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable no-console */
import styled from "@emotion/styled";
import { Layout } from "antd";
import {
  createContext,
  Dispatch,
  lazy,
  SetStateAction,
  useContext,
  useEffect,
  useState
} from "react";
import { Outlet, useParams } from "react-router-dom";

import { AIInSvg, CodeSvg } from "@assets/svg";
import { Flex, Typography } from "@components";
import { wsURL } from "@configs";
import { isShowChatBox } from "@defines";
import { useFilterGlobal, useLayout } from "@hooks";
import { HEADER_DASHBOARD_HEIGHT } from "@layouts/TopbarLayout/config";
import { useGetChatProject, useGetRepositories, useProjectsQuery } from "@services";
import { allColors } from "@style";
import { EventWebSocketResponse, Message } from "@types";
import { getAuthToken, isJSON } from "@utils";

import { WrapperForm } from "./content/Repositories/components";

const ChatBotPage = lazy(() => import("@pages/chatbot"));

const { Sider, Header } = Layout;

export const Toggle = styled(Flex)`
  position: absolute;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: 1px solid rgba(0, 0, 0, 0.15);
  padding: 6px;
  top: ${HEADER_DASHBOARD_HEIGHT - 14}px;
  z-index: 50;
  right: calc(100% - 14px);
  background: ${({ theme }) => theme.v2Colors.neutral1};
  cursor: pointer !important;
  justify-content: space-between;
  &:hover {
    background-color: ${({ theme }) => theme.v2Colors.neutral3};
  }
`;
const MessageContext = createContext<{
  messages: Message[];
  setMessages: Dispatch<SetStateAction<Message[]>>;
  setAddNew: Dispatch<SetStateAction<boolean>>;
}>(
  {} as {
    messages: Message[];
    setMessages: Dispatch<SetStateAction<Message[]>>;
    setAddNew: Dispatch<SetStateAction<boolean>>;
  }
);

export const useMessages = () => {
  return useContext(MessageContext);
};

const SocketContext = createContext<{ webSocket: WebSocket | null }>(
  {} as unknown as { webSocket: WebSocket | null }
);

export const useSocket = () => {
  return useContext(SocketContext);
};

export const WorkspacePage: React.FC = () => {
  const [addNew, setAddNew] = useState<boolean>(false);
  const [webSocket, setWebSocket] = useState<WebSocket | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const { project } = useProjectsQuery();
  const { repoId } = useParams();
  const { isOpenChatBox, toggleChatBox } = useLayout();
  const { chatProject } = useGetChatProject({
    projectId: project?.id as string,
    enabled: false
  });
  const { refetch } = useGetRepositories({ limit: 100, skip: 0 });
  const { resetReportsFilter } = useFilterGlobal();
  useEffect(() => {
    const connectToChatWebSocket = async () => {
      if (!chatProject?.id) return;
      const token = getAuthToken();
      const ws = new WebSocket(`${wsURL}/chat/ws/${chatProject.id}?token=${token}`);
      ws.onopen = () => {
        console.log("Websocket open connection");
        setWebSocket(ws);
      };
      ws.onmessage = event => {
        const response = JSON.parse(event.data) as EventWebSocketResponse;
        console.log("Received message:", response);
        if (!response.success) {
          setMessages(prev => [
            {
              role: "assistant",
              content: `[Error] ${response.message}`
            },
            ...prev
          ]);
        }
        if (!response.data) return;
        if (isJSON(response.data)) {
          const responseData = JSON.parse(response.data);
          setMessages(prev => [
            { role: "assistant", content: responseData.message, action: responseData.operation },
            ...prev
          ]);
        } else {
          switch (response.type) {
            case "message":
              setMessages(prev => [{ role: "assistant", content: response.data }, ...prev]);
              break;
            default:
              break;
          }
        }
      };
      ws.onerror = error => {
        console.log(error);
        console.log("Error on connection to web socket");
        setWebSocket(null);
      };
      ws.onclose = () => {
        console.log("Close web socket connection");
        setWebSocket(null);
      };
    };
    connectToChatWebSocket();
    return () => setWebSocket(null);
  }, [chatProject?.id]);

  useEffect(() => {
    resetReportsFilter();
  }, [repoId]);

  return (
    <SocketContext.Provider value={{ webSocket }}>
      <MessageContext.Provider value={{ messages, setMessages, setAddNew }}>
        <Layout>
          <Flex
            style={{
              transition: "all 0.2s 0.2s",
              background: allColors.neutral4,
              width: isOpenChatBox ? "75vw" : "100vw",
              minHeight: "100vh"
            }}
          >
            <Outlet />
          </Flex>
          {isShowChatBox && (
            <Sider
              width={isOpenChatBox ? "25vw" : "0vw"}
              style={{ height: "100vh", transition: "all 0.2s 0.2s" }}
            >
              {isOpenChatBox && (
                <Toggle
                  style={{
                    width: isOpenChatBox ? "auto" : "0px"
                  }}
                  center
                  onClick={toggleChatBox}
                >
                  <CodeSvg
                    style={{
                      transition: "all 0.2s 0.2s",
                      transform: isOpenChatBox ? "rotate(180deg)" : "rotate(0deg)"
                    }}
                    stroke={isOpenChatBox ? allColors.neutral1 : allColors.neutral13}
                  />
                </Toggle>
              )}
              <Flex direction='column' style={{ height: "100%" }}>
                <Flex
                  style={{
                    width: "100%",
                    height: HEADER_DASHBOARD_HEIGHT,
                    background: "red",
                    borderBottom: `1px solid ${allColors.neutral6}`
                  }}
                ></Flex>
                <Layout
                  style={{
                    flex: "1 1 0%",
                    borderLeft: `1px solid ${allColors.neutral6}`,
                    position: "relative"
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
                  <ChatBotPage />
                </Layout>
                {/* {!isOpenChatBox && (
                  <FloatButton
                    onClick={toggleChatBox}
                    type='primary'
                    icon={isOpenChatBox ? <CloseOutlined /> : <CommentOutlined />}
                  />
                )} */}
              </Flex>
            </Sider>
          )}
        </Layout>
        {addNew ? (
          <WrapperForm addNew={addNew} setAddNew={setAddNew} refetchRepository={refetch} />
        ) : null}
      </MessageContext.Provider>
    </SocketContext.Provider>
  );
};
