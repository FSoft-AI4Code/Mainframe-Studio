import { createSlice, PayloadAction } from "@reduxjs/toolkit";

import { File, FileBlobModel } from "@types";

import { State } from "./type";

const initialState: State = {
  fileContents: []
};

export const slice = createSlice({
  name: "file",
  initialState,
  reducers: {
    clean: () => initialState,
    setData: (state, action: PayloadAction<FileBlobModel>) => {
      state.data = action.payload;
      if (state.fileContents.every(o => o._id !== action.payload._id)) {
        const isContentFile = /.*\.cbl$/i.test(action.payload.name);
        if (!isContentFile || (isContentFile && action.payload.meta))
          state.fileContents.push(action.payload);
      }
    },
    setDataCobol: (state, action: PayloadAction<FileBlobModel>) => {
      state.cobolMatchingFileSelected = action.payload;
    },

    setTreeFileSelected: (state, action: PayloadAction<File>) => {
      state.treeFileSelected = action.payload;
    },
    setMatchingTreeFileSelected: (state, action: PayloadAction<File>) => {
      state.treeMatchingFileSelected = action.payload;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    },
    setFileContent: (state, action: PayloadAction<FileBlobModel>) => {
      if (state.fileContents.every(o => o._id !== action.payload._id)) {
        const isContentFile = /.*\.cbl$/i.test(action.payload.name);
        if (!isContentFile || (isContentFile && action.payload.meta))
          state.fileContents.push(action.payload);
      }
    }
  }
});

// > Export
// * Action
export const actions = { ...slice.actions };
// * Reducer
export const { reducer } = slice;
