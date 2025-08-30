/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
import { useCallback, useEffect, useRef, useState } from "react";

import { Flex } from "@components";
import { useMessages } from "@hooks";
import { containsAnyIgnoreCase, scrollToBottom, sleep } from "@utils";
import { ElementViews } from "@store";

import { messagesResponse } from "./contants";
import { InputMessage } from "./InputMessage";

import { MessageBox } from ".";

export const generateId = () => Date.now().toString(36) + Math.random().toString(36).substring(2);

export const getTypeFromInput = (inputValue: string) => {
  const typeKeywords: Record<string, ElementViews> = {
    how: "OVERVIEW",
    challenges: "ASSESSMENT",
    strategies: "EXPLORATION"
  };

  return (
    Object.entries(typeKeywords).find(([key, value]) =>
      containsAnyIgnoreCase(inputValue, key, value)
    )?.[1] || ""
  );
};

export function ChatBox() {
  const { messages, addMessage, updateLatestMessage } = useMessages();
  const scrollContentRef = useRef<HTMLParagraphElement | null>(null);
  const handleScroll = useCallback(() => {
    if (scrollContentRef.current) {
      scrollToBottom(scrollContentRef.current);
    }
  }, []);

  const sendMessage = useCallback(async (value: string) => {
    const type = getTypeFromInput(value) as ElementViews;
    const currentMessage = messagesResponse[type as keyof typeof messagesResponse];
    const { reply_pre_process: replyPreProcess = "" } = currentMessage || {};
    const userId = generateId();
    const botId = generateId();
    handleScroll();
    addMessage({
      id: userId,
      role: "user",
      type: type,
      content: value
    });
    if (!type) return;
    await sleep(200);
    if (replyPreProcess) {
      addMessage({
        id: botId,
        content: replyPreProcess,
        type,
        loading: true,
        isPending: true,
        role: "assistant",
        action: "assess_repository"
      });
      await sleep(2000);
      updateLatestMessage({ isPending: false, isTyping: true });
    }
  }, []);

  return (
    <Flex direction='column' style={{ height: "100%", width: "100%" }}>
      <Flex
        direction='column'
        ref={scrollContentRef}
        style={{ flex: "1 1 0%", overflow: "auto", scrollBehavior: "smooth" }}
      >
        <Flex direction='column' style={{ marginTop: "auto" }} reverse gap={10}>
          {messages.map(message => (
            <MessageBox key={message.id} message={message} handleScroll={handleScroll} />
          ))}
          <Flex direction='column' gap={8}>
            <MessageBox
              message={{
                content: "Welcome to Mainframe Migration! How would you like to get started?",
                role: "assistant"
              }}
            />
          </Flex>
        </Flex>
      </Flex>
      <InputMessage sendMessage={sendMessage} />
    </Flex>
  );
}
