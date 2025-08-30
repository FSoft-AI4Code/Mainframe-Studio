import { createSelector } from "@reduxjs/toolkit";

const selectSelf = (state: RootState) => state.chat;

export const selector = {
  messages: createSelector(selectSelf, state => state.messages),
  isRenderingElement: createSelector(selectSelf, state => state.isRenderingElement),
  elementViews: createSelector(selectSelf, state => state.elementViews)
};
