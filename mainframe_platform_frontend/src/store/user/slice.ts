import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { UserModel } from "@types";
import { checkHasAuthToken } from "@utils";

import { State } from "./type";

const initialState: State = {
  isAuthorized: Boolean(checkHasAuthToken())
};

export const slice = createSlice({
  name: "user",
  initialState,
  reducers: {
    clean: () => initialState,
    setUser: (state, action: PayloadAction<UserModel | undefined>) => {
      state.data = action.payload;
    },
    setIsAuthorized: (state, action: PayloadAction<boolean>) => {
      state.isAuthorized = action.payload;
    }
  }
});

// > Export
// * Action
export const actions = {
  ...slice.actions
};
// * Reducer
export const { reducer } = slice;
