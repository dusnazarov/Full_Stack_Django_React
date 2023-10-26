import { AppBar, Box, Drawer, IconButton, Toolbar, Typography, useMediaQuery } from '@mui/material';
import {useTheme} from "@mui/material/styles"
import { Link } from '@mui/material';
import MenuIcon from "@mui/icons-material/Menu"
import React, { useState, useEffect } from 'react';


///////////////////////////////////////
// const PrimaryAppBar = () => {    
//     const theme = useTheme()   
//     return (
//         <AppBar
//             sx={{
//                 zIndex: (theme) => theme.zIndex.drawer + 2,
//                 backgroundColor: theme.palette.background.default,
//                 borderBottom: `1px solid ${theme.palette.divider}`
              
//             }}
//         >
//             <Toolbar
//                 variant='dense'
//                 sx={{
//                     height: theme.primaryAppBar.height,
//                     minHeight: theme.primaryAppBar.height,
                   
//                  }}
//             >
//                 <Box sx={{display: {xs: "block", sm: "none"}}}>
//                     <IconButton
//                         color='inherit'
//                         aria-label='open drawer'
//                         edge='start'                   
//                         sx={{mr:4}}
//                     >
//                         <MenuIcon />
//                     </IconButton>
//                 </Box>
//                 <Drawer anchor='left' open={true} >
//                     {[...Array(25)].map((_, i) => (
//                         <Typography key={i} paragraph>
//                             {i + 1}
//                         </Typography>
//                     ))}
//                 </Drawer>
//                 <Link href="/" underline='none' color="inherit">
//                     <Typography
//                         variant='h6'
//                         noWrap
//                         component="div"
//                         sx={{display:{fontWeight: 700, letterSpacing: "-0.5px"}}}
//                     >
//                        DJCHAT
//                     </Typography>                  
//                 </Link>
//             </Toolbar>        
//         </AppBar>
//     )
// }
// export default PrimaryAppBar


// ///////////////////////////////////////
// const PrimaryAppBar = () => {
//     const theme = useTheme()

//     const [sideMenu, setSideMenu] = useState(false);    

//     const toggleDrawer = (x: boolean) => () => {     
//         setSideMenu(x)
    
//     };
    

//     return (
//         <AppBar
//             sx={{
//                 zIndex: (theme) => theme.zIndex.drawer + 1,
//                 backgroundColor: theme.palette.background.default,
//                 borderBottom: `1px solid ${theme.palette.divider}`
//             }}
//         >
//             <Toolbar
//                 variant='dense'
//                 sx={{
//                     height: theme.primaryAppBar.height,
//                     minHeight: theme.primaryAppBar.height,
//                  }}
//             >
//                 <Box sx={{display: {xs: "block", sm: "none"}}}>
//                     <IconButton
//                         color='inherit'
//                         aria-label='open drawer'
//                         edge='start'
//                         onClick={toggleDrawer(true)}
//                         sx={{mr:2}}
//                     >
//                         <MenuIcon />
//                     </IconButton>
//                 </Box>
//                 <Drawer
//                     anchor='left'
//                     open={sideMenu}
//                     onClose={toggleDrawer(false)}
//                 >
//                     {[...Array(25)].map((_, i) => (
//                         <Typography key={i} paragraph>
//                             {i + 1}
//                         </Typography>
//                     ))}
//                 </Drawer>

//                 <Link href="/" underline='none' color="inherit">
//                     <Typography
//                         variant='h6'
//                         noWrap
//                         component="div"
//                         sx={{display:{fontWeight: 700, letterSpacing: "-0.5px"}}}
//                     >
//                        DJCHAT
//                     </Typography>                  
//                 </Link>
//             </Toolbar>
        
//         </AppBar>
//     )
// }
// export default PrimaryAppBar


// // //////////////////////////////////////
// const PrimaryAppBar = () => {
//     const [sideMenu, setSideMenu] = useState(false)
//     const theme = useTheme()
    
//     console.log(sideMenu) 

//     const toggleDrawer = (x: boolean) => ( event: React.KeyboardEvent | React.MouseEvent) => { 
//         if (
//             event.type === "keydown" && 
//             ((event as React.KeyboardEvent).key === "Tab" ||
//                 (event as React.KeyboardEvent).key === "Shift")
//         ) {
//             return;

//         }          
//             setSideMenu(x);
//         };

//     return (
//         <AppBar
//             sx={{
//                 zIndex: (theme) => theme.zIndex.drawer + 1,
//                 backgroundColor: theme.palette.background.default,
//                 borderBottom: `1px solid ${theme.palette.divider}`
//             }}
//         >
//             <Toolbar
//                 variant='dense'
//                 sx={{
//                     height: theme.primaryAppBar.height,
//                     minHeight: theme.primaryAppBar.height,
//                  }}
//             >
//                 <Box sx={{ display: {xs: "block", sm: "none"}}}>
//                     <IconButton
//                         color='inherit'
//                         aria-label='open drawer'
//                         edge='start'
//                         onClick={toggleDrawer(true)}
//                         sx={{mr:2}}
//                     >
//                         <MenuIcon />
//                     </IconButton>
//                 </Box>
//                 <Drawer
//                     anchor='left'
//                     open={sideMenu}
//                     onClose={toggleDrawer(false)}
//                 >
//                     {[...Array(50)].map((_, i) => (
//                         <Typography key={i} paragraph>
//                             {i + 1}
//                         </Typography>
//                     ))}
//                 </Drawer>

//                 <Link href="/" underline='none' color="inherit">
//                     <Typography
//                         variant='h6'
//                         noWrap
//                         component="div"
//                         sx={{display:{fontWeight: 700, letterSpacing: "-0.5px"}}}
//                     >
//                        DJCHAT
//                     </Typography>                  
//                 </Link>
//             </Toolbar>        
//         </AppBar>
//     )
// }
// export default PrimaryAppBar


// /////////////////////////////////////
const PrimaryAppBar = () => {
    const [sideMenu, setSideMenu] = useState(false)
    const theme = useTheme()

    const isSmallScreen = useMediaQuery(theme.breakpoints.up("sm"));
    console.log(isSmallScreen)
    // console.log(sideMenu)

    useEffect(() => {
        if (isSmallScreen && sideMenu) {                      
            setSideMenu(false)            
        }
    }, [isSmallScreen])

    const toggleDrawer = (x: boolean) => ( event: React.KeyboardEvent | React.MouseEvent) => { 
        if (
            event.type === "keydown" && 
            ((event as React.KeyboardEvent).key === "Tab" ||
                (event as React.KeyboardEvent).key === "Shift")
        ) {
            return;
        }          
            setSideMenu(x);
        };   

    return (

        <AppBar
            sx={{
                zIndex: (theme) => theme.zIndex.drawer + 1,
                backgroundColor: theme.palette.background.default,
                borderBottom: `1px solid ${theme.palette.divider}`
            }}
        >
            <Toolbar
                variant='dense'
                sx={{
                    height: theme.primaryAppBar.height,
                    minHeight: theme.primaryAppBar.height,
                 }}
            >
                <Box sx={{ display: {xs: "block", sm: "none"}}}>
                    <IconButton
                        color='inherit'
                        aria-label='open drawer'
                        edge='start'
                        onClick={toggleDrawer(true)}
                        sx={{mr:2}}
                    >
                        <MenuIcon />
                    </IconButton>
                </Box>
                <Drawer
                    anchor='left'
                    open={sideMenu}
                    onClose={toggleDrawer(false)}
                >
                    {[...Array(50)].map((_, i) => (
                        <Typography key={i} paragraph>
                            {i + 1}
                        </Typography>
                    ))}
                </Drawer>

                <Link href="/" underline='none' color="inherit">
                    <Typography
                        variant='h6'
                        noWrap
                        component="div"
                        sx={{display:{fontWeight: 700, letterSpacing: "-0.5px"}}}
                    >
                       DJCHAT
                    </Typography>                  
                </Link>
            </Toolbar>
        
        </AppBar>
    )
}
export default PrimaryAppBar;




