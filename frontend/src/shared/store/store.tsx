import { combineReducers, configureStore } from "@reduxjs/toolkit";
import counterReducer from './features/counter'
import { getRTKFilms } from "../api/api";

export const rootReducer = combineReducers({
    counter: counterReducer
})

export const store = configureStore({
    reducer: {
        [getRTKFilms.reducerPath]: getRTKFilms.reducer,
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware().concat(getRTKFilms.middleware),
});

export type RootState = ReturnType<typeof rootReducer>