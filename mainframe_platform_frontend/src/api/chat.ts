import { ChatProjectResponse } from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class ChatApi {
  static getChatProject = (projectId: string) => {
    return HttpClient.get<ChatProjectResponse>(`${API_ENPOINTS.CHAT_PROJECTS}/${projectId}`);
  };
}
