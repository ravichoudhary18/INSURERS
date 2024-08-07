import { useEffect } from "react";
import axios from "axios";
const URL = import.meta.env.VITE_API_END_POINT;

const useAxiosPrivate = () => {
    const axiosPrivate = axios.create({
        baseURL: URL,
    });

    useEffect(() => {
        const requestIntercept = axiosPrivate.interceptors.request.use(
            (config) => {
                const token = JSON.parse(localStorage.getItem("token"));
                if (token) {
                    config.headers.Authorization = `Token ${token}`;
                }
                return config;
            },
            (error) => Promise.reject(error)
        );

        const responseIntercept = axiosPrivate.interceptors.response.use(
            (response) => response,
            (error) => {
                if (error.response && error.response.status === 401) {
                    // Handle 401 unauthorized (e.g., clear local storage or redirect to login)
                    localStorage.clear();
                }
                return Promise.reject(error);
            }
        );

        return () => {
            axiosPrivate.interceptors.request.eject(requestIntercept);
            axiosPrivate.interceptors.response.eject(responseIntercept);
        };
    }, [axiosPrivate]);

    return axiosPrivate;
};

export default useAxiosPrivate;