import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage";

import { Edge, Node } from "@types";

import { State } from "./type";

const initialState: State = {
  selectedEntry: "",
  nodeLimit: 0,
  selectedGroup: [],
  showNode: {},
  selectedType: null,
  entries: [],
  selectedEntries: {},
  selectedGraph: { nodes: [], edges: [] },
  complexity: 0,
  pageNumber: 1,
  pageLimit: 0,
  loc: 0
};

const graphSlice = createSlice({
  name: "filterGraph",
  initialState,
  reducers: {
    setSelectedEntries: (state, action: PayloadAction<Record<string, never | unknown>>) => {
      state.selectedEntries = action.payload;
    },
    setSelectedEntry: (state, action: PayloadAction<string>) => {
      state.selectedEntry = action.payload;
    },
    setSelectedGroup: (state, action: PayloadAction<string[]>) => {
      state.selectedGroup = action.payload;
    },
    setSelectType: (state, action: PayloadAction<"jcl" | "bms" | null>) => {
      state.selectedType = action.payload;
    },
    setNodeLimit: (state, action: PayloadAction<number>) => {
      state.nodeLimit = action.payload;
    },
    setComplexity: (state, action: PayloadAction<number>) => {
      state.complexity = action.payload;
    },
    setShowNode: (state, action: PayloadAction<Record<string, boolean>>) => {
      state.showNode = action.payload;
    },
    setSelectedGraph: (state, action: PayloadAction<{ nodes: Node[]; edges: Edge[] }>) => {
      state.selectedGraph = action.payload;
    },

    setGraphFilters: (state, action: PayloadAction<Partial<State>>) => {
      Object.assign(state, action.payload);
    },
    resetFilters: () => initialState
  }
});

const persistConfig = {
  key: "graph",
  storage,
  whitelist: ["selectedEntry", "showNode"]
};

// > Export
// * Action
export const actions = { ...graphSlice.actions };
// * Reducer
export const reducer = persistReducer(persistConfig, graphSlice.reducer);
