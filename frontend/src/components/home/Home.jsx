import React from 'react';
import useAxiosPrivate from '../../hooks/useAxiosPrivate'
import UploadArea from '../upload/UploadArea';

const Home = () => {

    const axiosPrivate = useAxiosPrivate()

    const logout = () => {
        axiosPrivate.post('/authentication/logout')
        .then((res) => {
            if(res.status === 204){
                localStorage.clear()
                sessionStorage.clear()
                console.log('logout call');
                // navigator('/login')
            }
        })
    }

    return (
        <>
            <UploadArea />
        </>
    );
}

export default Home;
