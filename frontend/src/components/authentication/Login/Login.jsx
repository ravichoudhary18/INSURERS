import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';
import useAxiosPrivate from '../../../hooks/useAxiosPrivate';
import { useNavigate } from 'react-router-dom';
import styles from './Login.module.css'

const Login = () => {

    const [inputs, setInputes] = useState({
        username: '',
        password: '',
    })
    const [errorMessage, setErrorMessage] = useState('')
    const style = { color: "#e5e5e5", "&.Mui-focused": { color: "#e5e5e5" } }
    const axiosPrivate = useAxiosPrivate()
    const navigate = useNavigate()

    const loginHandler = (event) => {
        setInputes({ ...inputs, [event.target.name]: event.target.value })
    }

    const submitHandler = (event) => {
        event.preventDefault()
        const formData = new FormData(event.target);
        const payload = Object.fromEntries(formData.entries());
        axiosPrivate.post('/authentication/login', payload)
            .then((res) => {
                localStorage.setItem('userInfo', JSON.stringify(res.data.user_info))
                localStorage.setItem('token', JSON.stringify(res.data.token))
                navigate('/')
            })
            .catch((error) => {
                if (error.response && error.response.data && Array.isArray(error.response.data.error)) {
                    setErrorMessage(error.response.data.error);
                } else {
                    setErrorMessage('An unexpected error occurred.');
                }
            })
    }
    return (
        <section className={styles.login__body}>
            <div className={styles.login__background}>
                <div className={`${styles.login__shape} ${styles.login__shapeFirst}`}></div>
                <div className={`${styles.login__shape} ${styles.login__shapeLast}`}></div>
            </div>
            <form onSubmit={submitHandler} className={styles.login__form}>
                <h3 className={styles.login__form__title}>Login</h3>
                <TextField
                    required
                    id="username"
                    variant="standard"
                    label="Username"
                    name='username'
                    value={inputs.username}
                    className={styles.login__form__input}
                    InputLabelProps={{sx: style}}
                    InputProps={{
                        className: styles.login__form__input,
                    }}
                    onChange={loginHandler}
                />
                <TextField
                    id="standard-password-input"
                    required
                    label="Password"
                    type="password"
                    name='password'
                    autoComplete="current-password"
                    variant="standard"
                    className={styles.login__form__input}
                    InputLabelProps={{sx: style}}
                    InputProps={{
                        className: styles.login__form__input
                    }}
                    value={inputs.password}
                    onChange={loginHandler}
                />
                <p style={{color: 'red'}}>{errorMessage? errorMessage : ''}</p>
                <Button
                    variant="contained"
                    type="submit"
                    className={styles.login__form__button}
                >Login</Button>
                {inputs.result}
            </form>
        </section>
    );
}

export default Login;
