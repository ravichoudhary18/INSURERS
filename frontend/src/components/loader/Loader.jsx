import { useContext } from 'react'
import MainContext from '../../context/MainContext';
import {
    Backdrop,
    Typography
} from "@mui/material";

const Loader = () => {
    const { isLodaing } = useContext(MainContext)
    console.log(isLodaing);

    return (
        <Backdrop
            sx={{ color: "#fff", zIndex: (theme) => theme.zIndex.drawer + 1 }}
            open={isLodaing}
        >        
            <Typography
                style={{
                    position: 'absolute',
                    top: '55%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)'
                }}
                className="main__loader"
            >
                Loading ...
            </Typography>
        </Backdrop>
    )
}

export default Loader;