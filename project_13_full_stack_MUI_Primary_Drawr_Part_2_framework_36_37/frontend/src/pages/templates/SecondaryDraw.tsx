import React from 'react'
import {useTheme} from "@mui/material/styles"
import { Box, Typography } from '@mui/material'

const SecondaryDraw = () => {

    const theme = useTheme()
    return (
    <Box sx={{
        minWidth:  `${theme.secondaryDraw.width}`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`, 
        mt: `${theme.primaryAppBar.height}px`,
        width: theme.secondaryDraw.width,
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

export default SecondaryDraw
