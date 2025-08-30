import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage";

import { ReportFilter, GlobalFilterState, DatabaseFilterState } from "./type";

const initialFilterReportsState: ReportFilter = {
  searchText: "",
  type: null,
  status: null,
  page: undefined
};
const initialFilterDatabaseState: DatabaseFilterState = {
  searchText: "",
  type: [],
  status: null,
  page: undefined,
  searchTable: ""
};

const initialState: GlobalFilterState = {
  reports: { ...initialFilterReportsState },
  database: { ...initialFilterDatabaseState }
};

const filterSlice = createSlice({
  name: "filters",
  initialState,
  reducers: {
    setReportsFilter: (state, action: PayloadAction<Partial<ReportFilter>>) => {
      state.reports = { ...state.reports, ...action.payload };
    },
    resetReportsFilter: state => {
      state.reports = { ...initialFilterReportsState };
    },
    setDatabaseFilter: (state, action: PayloadAction<Partial<DatabaseFilterState>>) => {
      state.database = { ...state.database, ...action.payload };
    },
    resetDatabaseFilter: state => {
      state.database = { ...initialFilterDatabaseState };
    }
  }
});
const persistConfig = {
  key: "filters",
  storage,
  whitelist: ["reports"]
};

// > Export
// * Action
export const actions = { ...filterSlice.actions };
// * Reducer
export const reducer = persistReducer(persistConfig, filterSlice.reducer);
