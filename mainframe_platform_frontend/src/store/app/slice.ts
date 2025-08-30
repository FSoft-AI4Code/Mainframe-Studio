import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { ENVIRONMENT, storage } from "@defines";

import { State } from "./type";

const initialState: State = {
  developMode: false,
  isOpenChatBox: false,
  isCollapsed: false
};

export const slice = createSlice({
  name: "app",
  initialState,
  reducers: {
    clean: () => {},
    setDevelopMode: (state, action: PayloadAction<boolean>) => {
      state.developMode = action.payload;
      localStorage.setItem(
        storage.ENVIRONMENT,
        action.payload ? ENVIRONMENT.DEVELOPMENT : ENVIRONMENT.PRODUCTION
      );
    },
    setTopBarShow: (state, action: PayloadAction<boolean | undefined>) => {
      state.isTopBarShow = action.payload;
    },
    setOpenChatbox: (state, action: PayloadAction<boolean | undefined>) => {
      state.isOpenChatBox = action.payload;
    },
    setCollapsedSidebar: (state, action: PayloadAction<boolean | undefined>) => {
      state.isCollapsed = action.payload;
    },
    setNotificationData: (state, action: PayloadAction<State["notification"]>) => {
      state.notification = action.payload;
    }
  }
});

// > Export
// * Action
export const actions = { ...slice.actions };
// * Reducer
export const { reducer } = slice;
