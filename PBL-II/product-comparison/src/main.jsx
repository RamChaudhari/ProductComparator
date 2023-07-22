import React from 'react'
import ReactDOM from 'react-dom/client'
import { ChakraBaseProvider, extendTheme } from '@chakra-ui/react'
import { RouterProvider } from 'react-router-dom'
import router from './router'
import theme from './theme'
import './global.css'

ReactDOM.createRoot(document.getElementById('root')).render(
    <ChakraBaseProvider theme={theme}>
        <React.StrictMode>
            {localStorage.setItem('chakra-ui-color-mode', 'dark')}
            <RouterProvider router={router} />
        </React.StrictMode>
    </ChakraBaseProvider>
)
