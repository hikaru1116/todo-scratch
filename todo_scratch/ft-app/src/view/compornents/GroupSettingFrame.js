import React, { useState } from "react";
import Grid from "@mui/material/Grid";
import GroupSettingsMenu from "./GroupSettingsMenu";
import Box from "@mui/material/Box";
import { useMediaQuery } from "@mui/material";
import Drawer from "react-modern-drawer";
import "react-modern-drawer/dist/index.css";
import MenuOpenIcon from "@mui/icons-material/MenuOpen";
import IconButton from "@mui/material/IconButton";

const GroupSettingFrame = ({ children }) => {
  const matches = useMediaQuery("(min-width: 600px)");

  const [isOpen, setIsOpen] = useState(false);

  const toggleDrawer = () => {
    setIsOpen((prevState) => !prevState);
  };

  return matches ? (
    <div>
      <Grid container>
        <Grid item xs={2} />
        <Grid item xs={2}>
          <GroupSettingsMenu />
        </Grid>
        <Grid item xs={6}>
          <Box maxWidth={800}>{children}</Box>
        </Grid>
        <Grid item xs={2} />
      </Grid>
    </div>
  ) : (
    <Box sx={{ width: "80%", maxWidth: 600 }} ml={"auto"} mr={"auto"}>
      <Box
        sx={{
          margin: 0,
          top: 87,
          right: "auto",
          bottom: "auto",
          left: 200,
          position: "fixed",
        }}
      >
        <IconButton
          color="primary"
          aria-label="upload picture"
          component="span"
          onClick={toggleDrawer}
        >
          <MenuOpenIcon />
        </IconButton>
      </Box>
      <Drawer open={isOpen} onClose={toggleDrawer} direction="left">
        <GroupSettingsMenu />
      </Drawer>
      {children}
    </Box>
  );
};

export default GroupSettingFrame;
