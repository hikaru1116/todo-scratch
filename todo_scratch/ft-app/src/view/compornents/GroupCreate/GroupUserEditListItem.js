import React from "react";
import ListItem from "@mui/material/ListItem";
// import ListItemText from "@mui/material/ListItemText";
import ListItemIcon from "@mui/material/ListItemIcon";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Box from "@mui/material/Box";
// import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
// import Select from "@mui/material/Select";
// import MenuItem from "@mui/material/MenuItem";

const GroupUserEditListItem = ({ id, addUserList, setAddUserList }) => {
  const editUser = (data) => {
    addUserList[id - 1].identifer = data;
    setAddUserList(addUserList);
  };
  return (
    <React.Fragment key={id}>
      <ListItem>
        <ListItemIcon>
          <AccountCircleIcon />
        </ListItemIcon>
        <Box>
          <TextField
            id="standard-basic"
            variant="standard"
            onChange={(e) => editUser(e.target.value)}
            placeholder="ユーザ名またはメールアドレス"
            sx={{ width: "10000" }}
          />
          {/* <Grid
            container
            direction="row"
            justifyContent="space-between"
            alignItems="center"
          > */}
          {/* <Grid item></Grid> */}
          {/* <Grid item>
                  <Select
                    labelId="demo-select-small"
                    id="demo-select-small"
                    defaultValue={1}
                  >
                    <MenuItem value={0}>ホストユーザ</MenuItem>
                    <MenuItem value={1}>ユーザ</MenuItem>
                  </Select>
                </Grid> */}
          {/* </Grid> */}
        </Box>
      </ListItem>
    </React.Fragment>
  );
};

export default GroupUserEditListItem;
