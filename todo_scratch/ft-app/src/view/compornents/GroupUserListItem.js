import React from "react";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import ListItemIcon from "@mui/material/ListItemIcon";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Box from "@mui/material/Box";
import Typography3 from "../compornents/Typographies/Typography3";
import Grid from "@mui/material/Grid";
import { toAuthTypeStr } from "../../enums/AuthTypeEnum";

const GroupUserListItem = ({ user }) => {
  return (
    <React.Fragment key={user.user_id}>
      <ListItem>
        <ListItemIcon>
          <AccountCircleIcon />
        </ListItemIcon>
        <ListItemText
          secondary={user.user_status == 0 && "未承認"}
          primary={
            <Box>
              <Grid
                container
                direction="row"
                justifyContent="space-between"
                alignItems="center"
              >
                <Grid item>
                  <Typography3
                    color={user.user_status == 0 ? "#c4c4c4" : "#111111"}
                  >
                    {user.user_name}
                  </Typography3>
                </Grid>
                <Grid item>
                  <Typography3
                    color={user.user_status == 0 ? "#c4c4c4" : "#111111"}
                  >
                    {toAuthTypeStr(user.auth_type)}
                  </Typography3>
                </Grid>
              </Grid>
            </Box>
          }
        />
      </ListItem>
    </React.Fragment>
  );
};

export default GroupUserListItem;
