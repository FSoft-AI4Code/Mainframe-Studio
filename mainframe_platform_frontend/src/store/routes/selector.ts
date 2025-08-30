import { createSelector } from "@reduxjs/toolkit";

const selectSelf = (state: RootState) => state.routes;

export const selector = {
  recentRoutes: createSelector(selectSelf, state => state.recentRoutes)
};
