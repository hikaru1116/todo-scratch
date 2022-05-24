import React from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import { Link } from "react-router-dom";
import Typography3 from "../compornents/Typographies/Typography3";

const GroupSettingsMenu = () => {
  return (
    <div>
      <Grid
        mt={2}
        container
        direction="column"
        justifyContent="center"
        alignItems="center"
        spacing={2.5}
      >
        <Grid item>
          <Box
            borderBottom={1}
            borderColor="primary.main"
            pl={2}
            pr={2}
            pb={1}
            mt={2}
            mb={2}
          >
            <Typography3 align={"center"}>Group Setting</Typography3>
          </Box>
        </Grid>
        <Grid item>
          <Link to="/group-settings" style={{ textDecoration: "none" }}>
            <Typography3 align={"center"}>参加グループ設定</Typography3>
          </Link>
        </Grid>
        <Grid item>
          <Link to="/group-settings" style={{ textDecoration: "none" }}>
            <Typography3 align={"center"}>参加グループ一覧</Typography3>
          </Link>
        </Grid>
        <Grid item>
          <Link to="/group-settings" style={{ textDecoration: "none" }}>
            <Typography3 align={"center"}>グループ承認</Typography3>
          </Link>
        </Grid>
        <Grid item>
          <Link to="/group/create" style={{ textDecoration: "none" }}>
            <Typography3 align={"center"}>グループ作成</Typography3>
          </Link>
        </Grid>
      </Grid>
    </div>
  );
};

export default GroupSettingsMenu;
