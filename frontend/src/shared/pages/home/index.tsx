import { IFilms } from '../../constants/types'
import { useQuery } from '@tanstack/react-query'
import { getFilms } from '../../api/api'
import Loader from '../../ui/components/loader'
import FilmCard from "../../ui/filmCard"
import { useGetAllFilmsQuery } from '../../api/api'

function Home() {

  const { data: filmsData, isLoading } = useGetAllFilmsQuery()

  if (isLoading) return <Loader />

  return (
    <>
      {filmsData &&
        filmsData.map(film => <FilmCard key={film.title} item={film} />)
      }
    </>
  )
}

export default Home