import React, {useState} from 'react'
import { Button } from '@mui/material';
import './UploadArea.css'
import useAxiosPrivate from '../../hooks/useAxiosPrivate'

const UploadArea = () => {


    const axiosPrivate = useAxiosPrivate()
    const [form, seForm] = useState({
        file: '',
    });


    const formChangeHandler = (event) => {
        const { name, value, type } = event.target
        if(type === 'file') {
            const {files} = event.target
            seForm({ ...form, [name]: files[0] })
            return
        }
        seForm({ ...form, [name]: value })
    }


    const submitHandler = (event) => {
        event.preventDefault()
        const payload = new FormData();
        payload.append('file', form.file)
        console.log(payload);
        if (form.file) {
            axiosPrivate.post('/file/file-upload/', payload)
            .then((res) => {
                console.log(res.data);
            })
            .catch((err) => {
                console.log(err);
            }).finally(() => {
                console.log('upload complete');
            })
            
            // You can handle the file upload here, e.g., sending it to a server
          } else {
            console.error("No file selected.");
          }
    }

    return (
        <section className='upload__area'>
            <h4>Upload file</h4>
            <form onSubmit={submitHandler} className='upload__area__form'>
                <input onChange={formChangeHandler} type="file" name='file' required={true} />
                <Button type='submit' variant="contained" color="primary">
                    Upload
                </Button>
            </form>
        </section>
    )
}

export default UploadArea