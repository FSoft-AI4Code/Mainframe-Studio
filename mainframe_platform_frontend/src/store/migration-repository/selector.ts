import { createSelector } from "@reduxjs/toolkit";

const selectSelf = (state: RootState) => state.migrationRepository;

export const selector = {
  selectMigrationRepositoryData: createSelector(selectSelf, state => state),
  selectMigrationRepositoryId: createSelector(selectSelf, state => state.id),
  selectMigrationRepositoryCopyGraph: createSelector(selectSelf, state => state.copy_graph),
  selectMigrationRepositoryCluster: createSelector(selectSelf, state => state.clusters),
  selectMigrationRepositoryTreeView: createSelector(selectSelf, state => state.tree_view),
  selectMigrationRepositoryStats: createSelector(selectSelf, state => state.stats),
  selectMigrationRepositoryDone: createSelector(selectSelf, state => state.done)
};
