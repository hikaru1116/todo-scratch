import React from "react";
import Grid from "@mui/material/Grid";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import Button from "@mui/material/Button";

const BackButton = ({ onClick }) => {
  return (
    <Grid
      container
      direction={"row"}
      justifyContent={"left"}
      alignItems={"center"}
    >
      <Grid item>
        <ArrowBackIcon
          fontSize="small"
          sx={{ color: (theme) => theme.palette.primary.main }}
        />
      </Grid>
      <Grid item>
        <Button onClick={onClick}>Back</Button>
      </Grid>
    </Grid>
  );
};

export default BackButton;
