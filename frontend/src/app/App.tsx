import { RouterProvider } from 'react-router-dom'
import './App.scss'
import './styles/fonts/fonts.css'
import { router } from './router/router'
import { QueryClientProvider } from '@tanstack/react-query'
import { client } from './client/client'

function App() {
  return (
    <QueryClientProvider client={client}>
      <RouterProvider router={router}>
      </RouterProvider>
    </QueryClientProvider>
  )
}

export default App
