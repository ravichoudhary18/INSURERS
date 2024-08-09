import React, { useState, useContext, useRef } from 'react'
import { Button } from '@mui/material';
import './UploadArea.css'
import useAxiosPrivate from '../../hooks/useAxiosPrivate'
import MainContext from '../../context/MainContext';

const UploadArea = ({
    setData, setDownloadID
}) => {

    const { setIsLoading } = useContext(MainContext)
    const fileInputRef = useRef(null);
    const axiosPrivate = useAxiosPrivate()
    const [form, setForm] = useState({
        file: '',
        button_status: false
    });


    const formChangeHandler = (event) => {
        const { name, value, type } = event.target
        if (type === 'file') {
            const { files } = event.target
            setForm({ ...form, [name]: files[0] })
            return
        }
        setForm({ ...form, [name]: value })
    }


    const submitHandler = (event) => {
        event.preventDefault();
        setIsLoading(true)
        const payload = new FormData();
        payload.append('file', form.file)
        if (form.file) {
            axiosPrivate.post('/file/file-upload/', payload)
                .then((res) => {
                    setData(res.data.records)
                    setDownloadID(res.data.download_id)
                    setForm({ ...form, button_status: true })
                })
                .catch((err) => {
                    console.log(err);
                }).finally(() => {
                    console.log('upload complete');
                    setIsLoading(false)
                })

            // You can handle the file upload here, e.g., sending it to a server
        } else {
            console.error("No file selected.");
        }
    }

    const ClearHandler = (event) => {
        event.preventDefault();
        setForm({ ...form, button_status: true, file: '' })
        setData(null)
        if (fileInputRef.current) {
            fileInputRef.current.value = ''; // Clear the file input
        }
    }

    return (
        <section className='upload__area'>
            <h4>Upload file</h4>
            <form onSubmit={submitHandler} className='upload__area__form'>
                <input onChange={formChangeHandler} ref={fileInputRef} type="file" name='file' accept="
               application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,
               application/vnd.ms-excel" required={true} />
                <Button type='submit' variant="contained" color="primary" disabled={form.button_status}>
                    Upload
                </Button>
                {form.file && <Button onClick={ClearHandler} type='button' variant="contained" color="error">
                    Clear
                </Button>}
            </form>
        </section>
    )
}

export default UploadArea