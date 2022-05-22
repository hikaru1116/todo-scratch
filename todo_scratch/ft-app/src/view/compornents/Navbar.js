import React from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

const Navbar = () => {
  return (
    <AppBar
      position="static"
      sx={{ backgroundColor: (theme) => theme.palette.primary.main }}
    >
      <Toolbar>
        <Typography
          variant="h5"
          sx={{
            color: "#FFFFFF",
            fontSize: {
              sm: 16,
              md: 24,
            },
          }}
        >
          TODO APP
        </Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
