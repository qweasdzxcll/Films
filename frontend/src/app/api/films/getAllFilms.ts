import { BASE_URL } from "../../constants/constants"
import { useQuery } from "@tanstack/react-query"

const fetchData = async () => {
    const response = await fetch(BASE_URL)
    const data = await response.json()
    return data
}

export const useGetAllFilms = () => {
    return useQuery({
        queryKey: ['films'],
        queryFn: fetchData
    })
}