import axios from 'axios'
import { FILMS_URL } from '../constants/constants'
import { IFilms } from '../constants/types'
import { createApi, fetchBaseQuery, retry } from "@reduxjs/toolkit/query/react";

export const getFilms = (): Promise<IFilms[]> => {
    return axios.get(FILMS_URL)
        .then(res => {
            return res.data
        })
}

export const getRTKFilms = createApi({
    reducerPath: 'films',
    baseQuery: retry(fetchBaseQuery({
        baseUrl: FILMS_URL
    })),
    endpoints: (builder) => ({
        getAllFilms: builder.query<IFilms[], void>({
            query: () => ''
        })
    })
})

export const { useGetAllFilmsQuery } = getRTKFilms