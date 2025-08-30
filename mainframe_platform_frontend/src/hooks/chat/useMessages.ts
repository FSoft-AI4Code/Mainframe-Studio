import { useDispatch, useSelector } from "react-redux";

import { chatSelector, chatActions, ElementViews } from "@store";
import { Message } from "@types";

export function useMessages() {
  const messages = useSelector(chatSelector.messages);
  const isRenderingElement = useSelector(chatSelector.isRenderingElement);
  const elementViews = useSelector(chatSelector.elementViews);
  const dispatch = useDispatch();

  const addMessage = (message: Message) => dispatch(chatActions.addMessage(message));

  const updateMessage = (message: Message) => dispatch(chatActions.updateMessage(message));

  const deleteMessage = (id: string) => dispatch(chatActions.deleteMessage(id));

  const clearMessages = () => dispatch(chatActions.clearMessages());

  const markMessagePending = (id: string) => dispatch(chatActions.markMessagePending(id));

  const setRenderElement = (payload: { isRendering: boolean; view?: ElementViews }) =>
    dispatch(chatActions.setRenderElement(payload));

  const updateLatestMessage = (payload: Partial<Message>) =>
    dispatch(chatActions.updateLatestMessage(payload));

  return {
    messages,
    isRenderingElement,
    elementViews,
    addMessage,
    updateMessage,
    deleteMessage,
    clearMessages,
    markMessagePending,
    setRenderElement,
    updateLatestMessage
  };
}
