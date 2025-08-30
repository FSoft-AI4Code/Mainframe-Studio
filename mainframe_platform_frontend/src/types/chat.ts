import { ApiResponse } from "@types";

export type ChatProject = {
  project_id: string;
  id: string;
  messages: {
    content: string;
    sender: "user" | "assistant";
  }[];
  created_at: string;
  updated_at: string;
};
export type ChatProjectResponse = ApiResponse<ChatProject>;

export type ChatConfig = {
  is_assessed: boolean;
  is_reversed: boolean;
};

export type WebSocketMessage = {
  content: string;
  sender: "user" | "assistant";
  repository_id?: string;
  config?: ChatConfig | null;
};

export type EventWebSocketResponse = {
  message?: string;
  success: boolean;
  type: "message";
  data: string;
};
