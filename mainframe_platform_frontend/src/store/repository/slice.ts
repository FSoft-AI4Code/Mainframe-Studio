import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { ClusterDataType, ComplexityModel, NetworkingDataType, RepoModel, TreeView } from "@types";

import { State } from "./type";

const initialState: State = {};

export const slice = createSlice({
  name: "repository",
  initialState,
  reducers: {
    clean: () => initialState,
    setRepositoryData: (state, action: PayloadAction<RepoModel>) => {
      // eslint-disable-next-line @typescript-eslint/naming-convention, unused-imports/no-unused-vars
      const { copy_graph, ...data } = action.payload || {};
      return data || {};
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
    setComplexity: (state, action: PayloadAction<ComplexityModel>) => {
      state.complexity = action.payload;
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
