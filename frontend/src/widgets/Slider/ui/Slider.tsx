import React, { useEffect, useState } from 'react'
import styles from './Slider.module.scss'
import { useGetAllFilms } from '../../../app/api/films'

export const Slider = () => {

    const filmsData = useGetAllFilms()

    return (
        <div>
            {filmsData.data &&
                filmsData.data.map(item => (
                    <div key={item.id}>
                        <h2>{item.title} - {item.time}</h2>
                    </div>
                ))}
        </div>
    )
}