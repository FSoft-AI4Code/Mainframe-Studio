import { createSelector } from "@reduxjs/toolkit";

const selectSelf = (state: RootState) => state.file;

export const selector = {
  selectData: createSelector(selectSelf, state => state.data),
  selectTreeFileSelected: createSelector(selectSelf, state => state.treeFileSelected),
  selectMatchingTreeFileSelected: createSelector(
    selectSelf,
    state => state.treeMatchingFileSelected
  ),
  selectCobolMatchingFileSelected: createSelector(
    selectSelf,
    state => state.cobolMatchingFileSelected
  ),
  selectLoading: createSelector(selectSelf, state => state.loading),
  selectFileContents: createSelector(selectSelf, state => state.fileContents)
};
