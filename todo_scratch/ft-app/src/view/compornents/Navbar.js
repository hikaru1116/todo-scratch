import React, { useContext, useState } from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Box from "@mui/material/Box";
import { UserOperateContext } from "../../contexts/UserContext";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Grid from "@mui/material/Grid";
import MenuIcon from "@mui/icons-material/Menu";
import IconButton from "@mui/material/IconButton";
import Drawer from "react-modern-drawer";
import "react-modern-drawer/dist/index.css";
import DrawerMenu from "./DrawerMenu";
import Typography1 from "../compornents/Typographies/Typography1";
import Typography2 from "../compornents/Typographies/Typography2";

const Navbar = () => {
  const { stateUser } = useContext(UserOperateContext);
  const [isOpen, setIsOpen] = useState(false);

  const toggleDrawer = () => {
    setIsOpen((prevState) => !prevState);
  };

  return (
    <AppBar
      position="static"
      sx={{ backgroundColor: (theme) => theme.palette.primary.main }}
    >
      <Drawer open={isOpen} onClose={toggleDrawer} direction="right">
        <DrawerMenu
          userName={stateUser.user ? stateUser.user.user_name : "no user"}
          closeDraw={toggleDrawer}
        />
      </Drawer>
      <Toolbar>
        <Typography1 color={"#FFFFFF"}>TODO APP</Typography1>
        <div style={{ flexGrow: 1 }}></div>
        {stateUser.user && (
          <Box>
            <Grid
              container
              direction="row"
              justifyContent="center"
              alignItems="center"
            >
              <Grid item>
                <Box mt={0.5}>
                  <AccountCircleIcon sx={{ color: "#FFFFFF" }} />
                </Box>
              </Grid>
              <Grid item>
                <Typography2 color={"#FFFFFF"}>
                  {stateUser.user.user_name}
                </Typography2>
              </Grid>
              <Grid item>
                <IconButton onClick={toggleDrawer} sx={{ color: "#FFFFFF" }}>
                  <MenuIcon />
                </IconButton>
              </Grid>
            </Grid>
          </Box>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
