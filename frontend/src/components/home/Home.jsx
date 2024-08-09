import React, {useState} from 'react';
import UploadArea from '../upload/UploadArea';
import DataTable from '../datatable/DataTable';

const Home = () => {

    const [data, setData] = useState(null)

    return (
        <>
            <UploadArea setData={setData}/>
            <br />
            {data && <DataTable data={data}/>}
        </>
    );
}

export default Home;