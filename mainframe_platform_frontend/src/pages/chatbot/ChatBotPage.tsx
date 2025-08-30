import { Flex } from "@components";

import { ChatBox } from "./components/ChatBox";

export function ChatBotPage() {
  return (
    <Flex center style={{ flex: "1 1 0%", maxHeight: "calc(100% - max(5vh, 48px))" }}>
      <ChatBox />
    </Flex>
  );
}
