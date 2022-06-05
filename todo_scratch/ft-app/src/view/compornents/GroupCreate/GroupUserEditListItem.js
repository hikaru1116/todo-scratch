import React from "react";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";

const GroupUserEditListItem = ({ id, addUserList, setAddUserList }) => {
  const editUser = (data) => {
    addUserList[id - 1].identifier = data;
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
        </Box>
      </ListItem>
    </React.Fragment>
  );
};

export default GroupUserEditListItem;
