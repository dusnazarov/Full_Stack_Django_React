import React from 'react'
import {
    List,
    ListItem,
    ListItemButton,
    ListItemIcon,
    Box,
    Typography,
} from "@mui/material";
import useCrud from '../../hooks/useCrud';
import {useEffect} from "react"
import ListItemAvatar from '@mui/material';
import Avatar from '@mui/material';
import { MEDIA_URL } from '../../config';
import { Link} from "react-router-dom"

type Props = {
    open: boolean;
}

const PopularChanels: React.FC<Props> = ({ open }) => {
  return (
    <>
      <Box
        sx={{
            height: 50,
            p:2,
            display: "flex",
            alignItems: "center",
            flex: "1 1 100% ",
            // backgroundColor: "blue"
        }}
      >
        <Typography sx={{ display: open ? "block": "none"}}> 
            Popular
        </Typography>

      </Box>
      
    </>
  )
}

export default PopularChanels
