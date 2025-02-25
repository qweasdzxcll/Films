import { IActor } from '../../constants/types'
import { useState } from 'react'
import { ACTORS_URL } from '../../constants/constants'
import { ChangeEvent, FormEvent } from 'react'

function Home() {


  const [ formData, setFormData ] = useState<IActor>({
    firstname: '',
    lastname: ''
  })

  const changeForm = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }))
  }

  const submitForm = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    fetch(ACTORS_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token 8811be43b65c4076cc07985d4e8bd3cd69b3c327'
      },
      body: JSON.stringify(formData)
    })
  }

  return (
    <>
      <form method="post" onSubmit={submitForm}>
        <label htmlFor="firstname">FIRSTNAME</label>
        <input type="text" name="firstname" id="firstname" value={formData.firstname} onChange={changeForm} />
        <label htmlFor="lastname">LASTNAME</label>
        <input type="text" name="lastname" id="lastname" value={formData.lastname} onChange={changeForm} />
        <input type="submit" value="Send.." id="submit" style={{ cursor: 'pointer' }} />
      </form>
    </>
  )
}

export default Home