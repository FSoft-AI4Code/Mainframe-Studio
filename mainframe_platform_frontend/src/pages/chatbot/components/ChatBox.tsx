import { useCallback, useRef } from "react";

import { Button, Flex } from "@components";
import { CirclePlusSvg, ClientInSvg, LogoSvg } from "@assets/svg";
import { allColors } from "@style";
import { useMessages, useSocket } from "@pages/workspace/WorkspacePage";
import { Message, WebSocketMessage } from "@types";
import { useRepository } from "@hooks";

import { InputMessage } from "./InputMessage";
import { LLMResponse } from "./LLMResponse";
import { AssessBtn, ReverseBtn } from "./Button";

export function UserBox() {
  return (
    <Flex
      center
      style={{
        width: 32,
        height: 32,
        borderRadius: "50%",
        marginTop: 8,
        backgroundColor: allColors.primary6
      }}
    >
      <ClientInSvg />
    </Flex>
  );
}

export function MachineBox() {
  return (
    <Flex
      center
      style={{
        width: 32,
        height: 32,
        borderRadius: "50%",
        marginTop: 8,
        backgroundColor: allColors.neutral1
      }}
    >
      <LogoSvg />
    </Flex>
  );
}

function MessageBox({ message }: { message: Message }) {
  const { role, content, action } = message;
  const isUser = role === "user";
  const { setAddNew } = useMessages();

  return (
    <Flex gap={8} style={{ padding: "8px 20px" }} direction='row' reverse={isUser}>
      {isUser ? <UserBox /> : <MachineBox />}
      <Flex
        direction='column'
        style={{
          width: "70%",
          flex: "1 1 0%",
          backgroundColor: isUser ? allColors.primary6 : allColors.neutral1,
          color: isUser ? allColors.neutral1 : allColors.neutral13,
          borderRadius: "4px",
          padding: "0 4px"
        }}
      >
        <LLMResponse response={content} isStreamFinished />
        {action === "assess_repository" ? (
          <AssessBtn />
        ) : action === "reverse_repository" ? (
          <ReverseBtn />
        ) : action === "upload_repository" ? (
          <Button
            iconPrefix={<CirclePlusSvg width={14} height={14} />}
            type='primary'
            style={{ borderRadius: 4, width: "min-content" }}
            onClick={() => setAddNew(true)}
          >
            Upload Source Code
          </Button>
        ) : null}
      </Flex>
    </Flex>
  );
}

export function ChatBox() {
  const { messages, setMessages } = useMessages();
  const { webSocket } = useSocket();
  const { repository } = useRepository();

  const messagesContainer = useRef<HTMLDivElement | null>(null);

  const sendMessage = useCallback(
    async (value: string) => {
      if (!webSocket) return;
      if (!repository) return;
      setMessages(prev => [{ role: "user", content: value }, ...prev]);

      const message: WebSocketMessage = {
        content: value.trim(),
        sender: "user",
        repository_id: repository.id || undefined,
        config: {
          is_assessed: repository.is_assessed,
          is_reversed: repository.is_reversed
        }
      };
      webSocket.send(JSON.stringify(message));
    },
    [webSocket, repository]
  );

  // useEffect(() => {
  //   if (messagesContainer.current) messagesContainer.current.scrollIntoView({ behavior: "smooth" });
  // }, [messages]);

  return repository ? (
    <Flex direction='column' style={{ height: "100%", width: "100%" }}>
      <Flex direction='column' style={{ flex: "1 1 0%", overflow: "auto" }}>
        <Flex direction='column' reverse gap={10} style={{ flex: "1 1 0%", overflow: "auto" }}>
          <div ref={messagesContainer}></div>
          {messages.map((message, index) => (
            <MessageBox key={`${message.content}_${index}`} message={message} />
          ))}

          <Flex direction='column' gap={8}>
            {repository ? null : (
              <MessageBox
                message={{
                  content:
                    "Welcome to Mainframe Migration to get started, please upload your source code.",
                  role: "assistant",
                  action: "upload_repository"
                }}
              />
            )}
            {repository.is_assessed ? null : (
              <MessageBox
                message={{
                  content: "Would you like to perform an assessment of the uploaded code?",
                  role: "assistant",
                  action: "assess_repository"
                }}
              />
            )}

            {repository.is_reversed ? null : (
              <MessageBox
                message={{
                  content: "Would you like to perform reverse parsing of the uploaded code?",
                  role: "assistant",
                  action: "reverse_repository"
                }}
              />
            )}
          </Flex>
        </Flex>
      </Flex>
      <InputMessage sendMessage={sendMessage} />
    </Flex>
  ) : null;
}
