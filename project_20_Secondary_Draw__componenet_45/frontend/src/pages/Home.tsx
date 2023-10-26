import {Box, CssBaseline} from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import PrimaryDraw from "./templates/PrimaryDraw";
import SecondaryDraw from "./templates/SecondaryDraw";
import Main from "./templates/Main";
import PopularChanels from "../components/PrimaryDraw/PopularChanels";


const Home = () => {
  return (
    <Box sx={{ display:"flex" }}>
      < CssBaseline />
      <PrimaryAppBar />
      <PrimaryDraw>
        <PopularChanels />  
      </PrimaryDraw >  
      <SecondaryDraw />
      <Main />    
    </Box>
  )
}
export default Home;
