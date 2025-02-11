import axios from 'axios'
import { BASE_URL } from '../constants/constants'
import { IFilms } from '../constants/types'
import { createApi, fetchBaseQuery, retry } from "@reduxjs/toolkit/query/react";

export const getFilms = (): Promise<IFilms[]> => {
    return axios.get(`${BASE_URL}/films/`)
        .then(res => {
            return res.data
        })
}

export const getRTKFilms = createApi({
    reducerPath: 'films',
    baseQuery: retry(fetchBaseQuery({
        baseUrl: BASE_URL
    })),
    endpoints: (builder) => ({
        getAllFilms: builder.query<IFilms[], void>({
            query: () => '/films/'
        })
    })
})

export const { useGetAllFilmsQuery } = getRTKFilms