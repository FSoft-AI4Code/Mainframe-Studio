import { configureStore } from "@reduxjs/toolkit";
import { persistStore } from "redux-persist";

import { rootReducer } from "./reducer";

// > Config
export const store = configureStore({
  reducer: rootReducer,
  middleware: getDefaultMiddleware =>
    getDefaultMiddleware({
      immutableCheck: false,
      serializableCheck: false
    })
});

export const persistor = persistStore(store);
// > Logger
// eslint-disable-next-line
// store.subscribe(() => console.log(store.getState()))

type StoreState = ReturnType<typeof store.getState>;
type StoreDispatch = typeof store.dispatch;

declare global {
  type RootState = StoreState;
  type AppDispatch = StoreDispatch;
}
