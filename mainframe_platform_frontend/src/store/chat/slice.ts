import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { Message } from "@types";

import { ElementViews, State } from "./type";

const initialState: State = {
  messages: [],
  elementViews: "DEFAULT",
  isRenderingElement: false
};

export const slice = createSlice({
  name: "chat",
  initialState,
  reducers: {
    addMessage: (state, action: PayloadAction<Message>) => {
      state.messages.forEach(msg => (msg.isPending = false));
      state.messages.unshift(action.payload);
    },
    markMessagePending: (state, action: PayloadAction<string>) => {
      const message = state.messages.find(msg => msg.id === action.payload);
      if (message) message.isPending = true;
    },
    updateMessage: (state, action: PayloadAction<Partial<Message>>) => {
      const message = state.messages.find(msg => msg.id === action.payload.id);
      if (message) {
        message.content = action.payload.content || "";
        message.isPending = false;
      }
    },
    updateLatestMessage: (state, action: PayloadAction<Partial<Message>>) => {
      if (state.messages.length > 0 && action.payload) {
        Object.assign(state.messages[0], action.payload);
      }
    },
    deleteMessage: (state, action: PayloadAction<string>) => {
      state.messages = state.messages.filter(msg => msg.id !== action.payload);
    },
    clearMessages: state => {
      state.messages = [];
    },
    setRenderElement: (
      state,
      action: PayloadAction<{ isRendering: boolean; view?: ElementViews }>
    ) => {
      state.isRenderingElement = action.payload.isRendering;
      if (!action.payload.view) return;
      state.elementViews = action.payload.view;
    }
  }
});

// > Export
// * Action
export const actions = { ...slice.actions };
// * Reducer
export const { reducer } = slice;
