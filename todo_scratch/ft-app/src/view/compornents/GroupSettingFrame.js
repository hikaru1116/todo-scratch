import React from "react";
import Grid from "@mui/material/Grid";
import GroupSettingsMenu from "./GroupSettingsMenu";
import Box from "@mui/material/Box";

const GroupSettingFrame = ({ children }) => {
  return (
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
  );
};

export default GroupSettingFrame;
