import { createRoot } from 'react-dom/client'
import App from './app/App.tsx'
import { QueryClientProvider } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import { client } from './app/client/client.ts'

createRoot(document.getElementById('root')!).render(
  <QueryClientProvider client={client}>
    <App />
    <ReactQueryDevtools initialIsOpen={false} />
  </QueryClientProvider>
)
