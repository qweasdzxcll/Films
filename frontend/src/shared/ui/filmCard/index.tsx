import { IFilms } from '../../constants/types'

type Props = {
    item: IFilms
}

const FilmCard = ({ item }: Props) => {

  console.log(item.preview)

  return (
    <>
      <h2>{item.actor}</h2>
    </>
  )
}

export default FilmCard