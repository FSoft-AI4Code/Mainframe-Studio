/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
import { Button } from "antd";
import { useEffect, useState } from "react";

import { ArrowRightSvg } from "@assets/svg";
import { useLayout, useMessages } from "@hooks";
import { ElementViews } from "@store";
import { sleep } from "@utils";
import { allColors } from "@style";

import { generateId } from "./ChatBox";
import { messagesResponse } from "./contants";

interface AssessBtnProps {
  type?: Partial<ElementViews>;
}

export const AssessBtn = ({ type }: AssessBtnProps) => {
  const { setRenderElement, addMessage, updateLatestMessage } = useMessages();
  const [status, setStatus] = useState<"IDLE" | "LOADING" | "SUCCESS">("IDLE");
  const currentMessages = messagesResponse[type as keyof typeof messagesResponse] ?? "";

  const handleTriggerAssessment = async () => {
    if (status === "SUCCESS") return;
    setStatus("LOADING");
    addMessage({
      content: currentMessages?.reply_post_process || "",
      role: "assistant",
      loading: true,
      id: generateId(),
      isPending: true,
      action: "response_success",
      isTyping: false,
      type
    });
    await sleep(5000);
    setRenderElement({ isRendering: true });
    setStatus("SUCCESS");
    updateLatestMessage({ isPending: false, isTyping: true });
  };
  const isSuccess = status === "SUCCESS";
  const isLoading = status === "LOADING";
  return (
    <Button
      type='primary'
      icon={<ArrowRightSvg width={14} height={14} />}
      style={{
        borderRadius: 4,
        minWidth: 100,
        justifyContent: "center",
        opacity: isSuccess || isLoading ? 0.65 : 1,
        background: allColors.primary6,
        color: allColors.neutral1
      }}
      loading={isLoading}
      disabled={isSuccess}
      onClick={handleTriggerAssessment}
    >
      {isLoading ? "Processing..." : isSuccess ? "Completed" : "Start"}
    </Button>
  );
};
