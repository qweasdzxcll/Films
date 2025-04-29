import { createBrowserRouter } from 'react-router-dom'
import { Layout } from './Layout'
import { Home, SignUp, SignIn } from '../../pages'

export const router = createBrowserRouter([
    {
        path: '/',
        element: <Layout />,
        children: [
            {
                path: '/home',
                element: <Home />
            },
            {
                path: '/sign-up',
                element: <SignUp />
            },
            {
                path: '/sign-in',
                element: <SignIn />
            },
        ]
    }
])