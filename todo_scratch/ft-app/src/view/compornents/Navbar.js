import React from "react";
import { styled } from "@mui/material/styles";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

const StyledTypography = styled(Typography)(({ theme }) => ({
  lexGrow: 1,
  backgroundColor: theme.palette.primary.main,
}));

const StyledAppBar = styled(AppBar)(({ theme }) => ({
  backgroundColor: theme.palette.primary.main,
}));

const Navbar = () => {
  return (
    <StyledAppBar position="static">
      <Toolbar>
        <StyledTypography variant="h5">TODO APP</StyledTypography>
      </Toolbar>
    </StyledAppBar>
  );
};

export default Navbar;
