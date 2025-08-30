import { Skeleton } from "antd";
import { useEffect, useState, useTransition } from "react";

import { Flex } from "@components";
import { useMessages } from "@hooks";
import { MachineBox, UserBox } from "@pages/chatbot/components/ChatBox";
import { allColors } from "@style";
import { Message } from "@types";

import { AssessBtn } from "./Button";
import { LLMResponse } from "./LLMResponse";

export function MessageBox({
  message,
  handleScroll
}: {
  message: Message;
  handleScroll?: () => void;
}) {
  const { role, content, action, type, isPending, isTyping } = message;
  const isUser = role === "user";
  const { setRenderElement, updateLatestMessage } = useMessages();

  const [displayedText, setDisplayedText] = useState("");
  // eslint-disable-next-line @typescript-eslint/naming-convention, @typescript-eslint/no-unused-vars
  const [_, startTransition] = useTransition();

  useEffect(() => {
    if (!content || isPending || !isTyping) return;
    let i = 0;
    setDisplayedText("");
    const intervalId = setInterval(() => {
      startTransition(() => {
        setDisplayedText(content.slice(0, i + 1));
        i++;
        if (i >= content.length) {
          clearInterval(intervalId);
          updateLatestMessage({ isPending: false, isTyping: false });
        }
      });
    }, 20);

    return () => clearInterval(intervalId);
  }, [content, isPending, isTyping]);

  useEffect(() => {
    if (content === displayedText && action === "response_success" && type) {
      setRenderElement({ isRendering: false, view: type });
    }
  }, [content, displayedText, action, type]);

  useEffect(() => {
    handleScroll?.();
  }, [displayedText]);

  return (
    <Flex gap={8} style={{ padding: "8px 20px" }} direction='row' reverse={isUser}>
      {isUser ? <UserBox /> : <MachineBox />}
      {isPending && !isUser ? (
        <Skeleton paragraph={{ rows: 1 }} />
      ) : (
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
          <LLMResponse response={!isUser && isTyping ? displayedText : content} isStreamFinished />
          {action === "assess_repository" && !isPending && !isTyping ? (
            <AssessBtn type={type} />
          ) : null}
        </Flex>
      )}
    </Flex>
  );
}
