import { createSelector } from "@reduxjs/toolkit";

export const selectSelf = (state: RootState) => state.graphFilter;

export const selector = {
  selectedGraph: createSelector(selectSelf, state => state.selectedGraph),
  entries: createSelector(selectSelf, state => state.entries),
  selectedEntry: createSelector(selectSelf, state => state.selectedEntry),
  selectedEntries: createSelector(selectSelf, state => state.selectedEntries),
  selectedGroup: createSelector(selectSelf, state => state.selectedGroup),
  selectedType: createSelector(selectSelf, state => state.selectedType),
  showNode: createSelector(selectSelf, state => state.showNode),
  selectShowNode: createSelector(selectSelf, state => state.showNode),
  nodeLimit: createSelector(selectSelf, state => state.nodeLimit),
  graphFilterStore: selectSelf
};
