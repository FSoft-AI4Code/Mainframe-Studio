import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { ClusterDataType, NetworkingDataType, RepoModel, TreeView } from "@types";

import { State } from "./type";

const initialState: State = {};

export const slice = createSlice({
  name: "migrationRepository",
  initialState,
  reducers: {
    clean: () => initialState,
    setMigrationRepositoryData: (state, action: PayloadAction<RepoModel>) => {
      return action.payload;
    },
    setCopyGraph: (state, action: PayloadAction<NetworkingDataType>) => {
      state.copy_graph = action.payload;
    },
    setClusters: (state, action: PayloadAction<ClusterDataType>) => {
      state.clusters = action.payload;
    },
    setTreeView: (state, action: PayloadAction<TreeView>) => {
      state.tree_view = action.payload;
    },
    setStats: (state, action: PayloadAction<TreeView>) => {
      state.tree_view = action.payload;
    },
    setDone: state => {
      state.done = true;
    }
  }
});

// > Export
// * Action
export const actions = { ...slice.actions };
// * Reducer
export const { reducer } = slice;
