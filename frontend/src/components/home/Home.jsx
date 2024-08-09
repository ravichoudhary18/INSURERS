import React, {useState} from 'react';
import UploadArea from '../upload/UploadArea';
import DataTable from '../datatable/DataTable';

const Home = () => {
    
    const [data, setData] = useState(null)
    const [downloadID, setDownloadID] = useState(null)

    return (
        <>
            <UploadArea setData={setData} setDownloadID={setDownloadID} />
            <br />
            {data && <DataTable data={data} id={downloadID} />}
        </>
    );
}

export default Home;