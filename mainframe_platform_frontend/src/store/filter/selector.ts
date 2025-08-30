import { createSelector } from "@reduxjs/toolkit";

export const selectSelf = (state: RootState) => state.filterGlobal;

export const selector = {
  filterReports: createSelector(selectSelf, state => state.reports),
  filterDatabase: createSelector(selectSelf, state => state.database),
  filterGlobalStore: selectSelf
};
