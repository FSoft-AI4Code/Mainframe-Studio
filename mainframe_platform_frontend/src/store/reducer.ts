import { AnyAction, combineReducers } from "@reduxjs/toolkit";
// import storage from "redux-persist/lib/storage";

import { reducer as userReducer } from "./user";
import { reducer as appReducer } from "./app";
import { reducer as repositoryReducer } from "./repository";
import { reducer as fileReducer } from "./file";
import { reducer as migrationRepositoryReducer } from "./migration-repository";
import { reducer as graphFilterReducer } from "./graph";
import { reducer as filterGlobalReducer } from "./filter";
import { reducer as routesReducer } from "./routes";
import { reducer as chatReducer } from "./chat";

const reducer = {
  app: appReducer,
  user: userReducer,
  file: fileReducer,
  graphFilter: graphFilterReducer,
  filterGlobal: filterGlobalReducer,
  repository: repositoryReducer,
  migrationRepository: migrationRepositoryReducer,
  routes: routesReducer,
  chat: chatReducer
};

const combinedReducers = combineReducers(reducer);

export const rootReducer = (
  state: ReturnType<typeof combinedReducers> | undefined,
  action: AnyAction
) => {
  if (action.type === ("GLOBAL_RESET" as const)) {
    state = undefined;
    return combinedReducers(state, action);
  }

  return combinedReducers(state, action);
};
