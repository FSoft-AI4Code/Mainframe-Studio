import { createSelector } from "@reduxjs/toolkit";

import { ENVIRONMENT } from "@defines";

const selectSelf = (state: RootState) => state.app;

export const selector = {
  isDevelopMode: createSelector(selectSelf, state =>
    process.env.REACT_APP_ENVIRONMENT === ENVIRONMENT.PRODUCTION ? false : state.developMode
  ),
  isTopBarShow: createSelector(selectSelf, state => state.isTopBarShow),
  isOpenChatBox: createSelector(selectSelf, state => state.isOpenChatBox),
  isCollapsed: createSelector(selectSelf, state => state.isCollapsed),
  selectNotificationData: createSelector(selectSelf, state => state.notification)
};
