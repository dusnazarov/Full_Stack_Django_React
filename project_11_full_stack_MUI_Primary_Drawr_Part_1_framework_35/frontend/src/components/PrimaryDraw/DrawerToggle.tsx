import {ChevronLeft}  from "@mui/icons-material"
import { Box, IconButton } from "@mui/material"


///////////////////////////
const DrawerToggle = () => {
  return (
    <Box sx={{
      height: "50px",
      display: "flex",
      alignItems: "cenetr",
      justifyContent: "center",  
      }}
    >
    
      <IconButton >
        <ChevronLeft />
      </IconButton>    

    
        
    </Box>
  )
}
export default DrawerToggle;
