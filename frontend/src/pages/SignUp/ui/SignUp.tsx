import React, { ChangeEvent, useState } from 'react'
import styles from './SignUp.module.scss'

export const SignUp = () => {

  const [ formData, setFormData ] = useState({
    phone: '',
    password: '',
    password2: '', 
  })

  const changeFormData = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }))
  }

  const submitForm = (e: ChangeEvent<HTMLInputElement>) => {
    e.preventDefault()
     
  }

  return (
    <div>
      
    </div>
  )
}