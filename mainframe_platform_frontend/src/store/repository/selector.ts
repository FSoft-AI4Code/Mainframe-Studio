import { createSelector } from "@reduxjs/toolkit";

const selectSelf = (state: RootState) => state.repository;

export const selector = {
  selectRepositoryData: createSelector(selectSelf, state => state),
  selectRepositoryId: createSelector(selectSelf, state => state?.id),
  selectRepositoryCopyGraph: createSelector(selectSelf, state => state?.copy_graph),
  selectRepositoryCluster: createSelector(selectSelf, state => state?.clusters),
  selectRepositoryTreeView: createSelector(selectSelf, state => state?.tree_view),
  selectRepositoryStats: createSelector(selectSelf, state => state?.stats),
  selectRepositoryDone: createSelector(selectSelf, state => state?.done),
  selectComplexity: createSelector(selectSelf, state => state?.complexity)
};
