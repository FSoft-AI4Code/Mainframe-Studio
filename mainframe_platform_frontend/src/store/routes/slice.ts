import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { RecentRoutesState } from "./type";

const initialState: RecentRoutesState = {
  recentRoutes: {}
};

export const slice = createSlice({
  name: "routes",
  initialState,
  reducers: {
    clearRoutes: () => {},
    setRecentRoute: (state, action: PayloadAction<{ key: string; path: string }>) => {
      state.recentRoutes[action.payload.key] = action.payload.path;
    },
    updateRoutes: (state, action: PayloadAction<string>) => {
      const key = action.payload;
      // eslint-disable-next-line @typescript-eslint/naming-convention
      const { [key]: _, ...newRoutes } = state.recentRoutes;
      state.recentRoutes = newRoutes;
    }
  }
});

// > Export
// * Action
export const actions = { ...slice.actions };
// * Reducer
export const { reducer } = slice;
