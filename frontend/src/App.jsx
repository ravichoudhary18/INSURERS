import { useEffect } from 'react'
import './App.css'
import { Routes, Route, useNavigate } from 'react-router-dom'
import Home from './components/home/Home'
import Login from './components/authentication/Login/Login'
import Loader from './components/loader/Loader'

function App() {

  const navigate = useNavigate();

  useEffect(() => {
    const token = JSON.parse(localStorage.getItem('token'));
    if (token) {
      navigate('/');
    } else {
      navigate('/login');
    }
  }, []);

  return (
    <>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/login' element={<Login />} />
      </Routes>
      <Loader />
    </>
  )
}

export default App
