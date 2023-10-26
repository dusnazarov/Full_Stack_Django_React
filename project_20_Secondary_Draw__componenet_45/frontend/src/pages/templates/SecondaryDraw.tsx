import React from 'react'
import {useTheme} from "@mui/material/styles"
import { Box, Typography } from '@mui/material'
import axios from 'axios'
import useAxiosWithInterceptor from '../../helpers/jwtinterceptor'


///////////////////////////////////////////
// const SecondaryDraw = () => {
//     const theme = useTheme()

//     axios.get('http://127.0.0.1:8000/api/server/select/?category=cat1')
//         .then(response => {
//             console.log(response.data)
//     })
//     .catch((error) => {
//         console.log(error)
//     })  

//     return (
//         <Box sx={{
//             minWidth:  `${theme.secondaryDraw.width}`,
//             height: `calc(100vh - ${theme.primaryAppBar.height}px)`, 
//             width: theme.primaryDraw.width,
//             mt: `${theme.primaryAppBar.height}px`,
//             borderRight: `1px solid ${theme.palette.divider}`,        
//             display: {xs: "none", sm: "block"},
//             overflow: "auto",
            
//             }}
//         >
//             {[...Array(50)].map((_, i) => (
//                     <Typography key={i} paragraph>
//                         {i + 1}
//                     </Typography>
//             ))}
//         </Box>
//     )
//     }

// export default SecondaryDraw

///////////////////////////////////////////
const SecondaryDraw = () => {

    const theme = useTheme()
    const jwtAxios = useAxiosWithInterceptor()

    jwtAxios.get('http://127.0.0.1:8000/api/server/select/?category=cat1')
        .then(response => {
            console.log(response.data)
    })
    .catch((error) => {
        console.log(error)
    })

    return (
        <Box sx={{
            minWidth:  `${theme.secondaryDraw.width}`,
            height: `calc(100vh - ${theme.primaryAppBar.height}px)`, 
            width: theme.primaryDraw.width,
            mt: `${theme.primaryAppBar.height}px`,
            borderRight: `1px solid ${theme.palette.divider}`,        
            display: {xs: "none", sm: "block"},
            overflow: "auto",
            
            }}
        >
            {[...Array(50)].map((_, i) => (
                <Typography key={i} paragraph>
                    {i + 1}
                </Typography>
            ))}
        </Box>
    )
    }
export default SecondaryDraw;

