import React, { useContext, useState } from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Box from "@mui/material/Box";
import { AuthOperateContext } from "../../contexts/AuthContext";
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
  const { state } = useContext(AuthOperateContext);
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
        <DrawerMenu user_name={"hikaru"} />
      </Drawer>
      <Toolbar>
        <Typography1 color={"#FFFFFF"}>TODO APP</Typography1>
        <div style={{ flexGrow: 1 }}></div>
        {state.user && (
          <Box>
            <Grid
              container
              direction="row"
              justifyContent="center"
              alignItems="center"
            >
              <Grid item>
                <AccountCircleIcon sx={{ color: "#FFFFFF" }} />
              </Grid>
              <Grid item>
                <Typography2 color={"#FFFFFF"}>
                  {state.user.user_name}
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
