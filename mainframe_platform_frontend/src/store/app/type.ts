export type State = {
  developMode: boolean;
  notification?: { type?: "pending" | "success"; timeout?: number; message: string };
  isTopBarShow?: boolean;
  isOpenChatBox?: boolean;
  isCollapsed?: boolean;
};
