import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter as Routers } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.min.css';
import { MainProvider } from './context/MainContext'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Routers >
      <MainProvider>
        <App />
      </MainProvider>
    </Routers>
  </React.StrictMode>,
)
