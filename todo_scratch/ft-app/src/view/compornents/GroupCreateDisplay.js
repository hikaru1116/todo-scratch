import React, { useState, useContext } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography2 from "../compornents/Typographies/Typography2";
import Typography3 from "../compornents/Typographies/Typography3";
import { GroupCreateOperateContext } from "../../contexts/GroupCreateContext";
import List from "@mui/material/List";
import Button from "@mui/material/Button";
import SaveIcon from "@mui/icons-material/Save";
import TextField from "@mui/material/TextField";
import GroupUserEditListItem from "./GroupUserEditListItem";
import AddIcon from "@mui/icons-material/Add";
import IconButton from "@mui/material/IconButton";
import { createGroupAction } from "../../actions/GroupCreateAction";
import { Navigate } from "react-router-dom";
import { AuthOperateContext } from "../../contexts/AuthContext";

const GroupCreateDisplay = () => {
  const { stateGroupCreate, dispatchGroupCreate } = useContext(
    GroupCreateOperateContext
  );
  const { dispatch } = useContext(AuthOperateContext);

  const [groupName, setGroupName] = useState("");
  const [discription, setDiscription] = useState("");
  const [addUserList, setAddUserList] = useState([
    {
      id: 1,
      identifer: "",
    },
  ]);

  const createGroup = () => {
    createGroupAction(
      dispatchGroupCreate,
      dispatch,
      groupName,
      discription,
      addUserList
    );
  };

  const addUserRow = () => {
    setAddUserList([
      ...addUserList,
      {
        id: addUserList.slice(-1)[0].id + 1,
        identifer: "",
      },
    ]);
  };

  return stateGroupCreate.toPath ? (
    <Navigate to={stateGroupCreate.toPath} />
  ) : (
    <div>
      <Grid container direction="column" spacing={3.5} mt={2}>
        <Grid item>
          <Typography2>グループ新規作成</Typography2>
        </Grid>
        {stateGroupCreate.validate.isValidate && (
          <Grid item>
            <Typography3 color={"red"}>
              {stateGroupCreate.validate.message}
            </Typography3>
          </Grid>
        )}
        <Grid item>
          <Box>
            <Typography2>グループ名</Typography2>
            <Box border={1} sx={{ borderRadius: "16px" }} p={2}>
              <TextField
                required
                id="standard-basic"
                variant="standard"
                onChange={(e) => setGroupName(e.target.value)}
                placeholder="グループ名を入力してください"
                sx={{ width: "100%" }}
              />
            </Box>
          </Box>
        </Grid>

        <Grid item>
          <Box>
            <Typography2>説明</Typography2>
            <Box border={1} sx={{ borderRadius: "16px" }} p={2}>
              <TextField
                required
                id="standard-basic"
                variant="standard"
                onChange={(e) => setDiscription(e.target.value)}
                placeholder="グループの説明を入力してください"
                sx={{ width: "100%" }}
              />
            </Box>
          </Box>
        </Grid>
        <Grid item>
          <Box>
            <Typography2>参加ユーザ</Typography2>
            <Box border={1} sx={{ borderRadius: "16px" }}>
              <List>
                {addUserList.map((addUser) => (
                  <GroupUserEditListItem
                    key={addUser.id}
                    id={addUser.id}
                    addUserList={addUserList}
                    setAddUserList={setAddUserList}
                  />
                ))}
              </List>
              <Box textAlign="center">
                <IconButton aria-label="delete" onClick={addUserRow}>
                  <AddIcon />
                </IconButton>
              </Box>
            </Box>
          </Box>
        </Grid>
        <Grid item>
          <Box textAlign="center">
            <Button
              onClick={createGroup}
              variant="contained"
              startIcon={<SaveIcon />}
              sx={{ width: "50%", backgroundColor: "#5CB5A5" }}
            >
              Create
            </Button>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
};

export default GroupCreateDisplay;
