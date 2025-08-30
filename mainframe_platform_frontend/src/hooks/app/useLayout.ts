import { useDispatch, useSelector } from "react-redux";

import { appActions, appSelector } from "@store";

export function useLayout() {
  const isCollapsed = useSelector(appSelector.isCollapsed);
  const dispatch = useDispatch();
  const toggleSidebar = () => dispatch(appActions.setCollapsedSidebar(!isCollapsed));
  const isOpenChatBox = useSelector(appSelector.isOpenChatBox);
  const toggleChatBox = () => dispatch(appActions.setOpenChatbox(!isOpenChatBox));

  return {
    isCollapsed,
    toggleSidebar,
    isOpenChatBox,
    toggleChatBox
  };
}
