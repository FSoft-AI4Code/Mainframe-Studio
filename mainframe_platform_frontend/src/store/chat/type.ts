import { Message } from "@types";

export type ElementViews = "OVERVIEW" | "DEFAULT" | "EXPLORATION" | "ASSESSMENT";

export interface State {
  messages: Array<Message>;
  isRenderingElement: boolean;
  elementViews: ElementViews;
}
