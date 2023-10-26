import {Box, Drawer, Typography, useMediaQuery} from "@mui/material"
import { useEffect, useState } from "react"
import {useTheme} from "@mui/material/styles"
import DrawerToggle from "../../components/PrimaryDraw/DrawerToggle"
import { Margin } from "@mui/icons-material"


const PrimaryDraw = () => {    
    return (  
      
        <Box >              
          <Box sx={{
            possition:'absolute',
            top: 0,
            right: 0,
            padding: 0,
            backgroundColor: "red"
       
             
                           
            }}
          >
            <DrawerToggle />         
           
            {[...Array(25)].map((_, i) => (
              <Typography key={i} paragraph>
                {i + 1 }
              </Typography>
            ))}
          </Box>            
        </Box>      
    
    )
  }
  export default PrimaryDraw;