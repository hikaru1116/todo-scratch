import React, { useState } from "react";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Box from "@mui/material/Box";
import Typography3 from "../../compornents/Typographies/Typography3";
import Grid from "@mui/material/Grid";
import ListItemText from "@mui/material/ListItemText";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";

const GroupSettingsUpdateListItem = ({
  id,
  user,
  updateUserList,
  setUpdateUserList,
}) => {
  const [authType, setAuthType] = useState(user.auth_type);

  const handleChange = (event) => {
    console.log(updateUserList);
    updateUserList.map((updateUser) => {
      if (updateUser.user_id == user.user_id) {
        updateUser.auth_type = event.target.value;
      }
    });
    setUpdateUserList(updateUserList);
    setAuthType(event.target.value);
  };
  return (
    <React.Fragment key={id}>
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
                  <Select value={authType} onChange={handleChange}>
                    <MenuItem value={0}>
                      <Typography3>ホストユーザ</Typography3>
                    </MenuItem>
                    <MenuItem value={1}>
                      <Typography3>ユーザ</Typography3>
                    </MenuItem>
                  </Select>
                </Grid>
              </Grid>
            </Box>
          }
        />
      </ListItem>
    </React.Fragment>
  );
};

export default GroupSettingsUpdateListItem;
