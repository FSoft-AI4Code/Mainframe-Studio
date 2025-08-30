import { createSelector } from "@reduxjs/toolkit";

const selectSelf = (state: RootState) => state.user;

export const selector = {
  selectData: createSelector(selectSelf, state => state.data),
  selectIsAuthorized: createSelector(selectSelf, state => state.isAuthorized)
};
