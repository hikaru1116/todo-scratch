import React, { useContext, useState, useEffect } from "react";
import Grid from "@mui/material/Grid";
import { GroupSettingsOperateContext } from "../../../contexts/GroupSettingsContext";
import Button from "@mui/material/Button";
import SaveIcon from "@mui/icons-material/Save";
import Box from "@mui/material/Box";
import Typography2 from "../../compornents/Typographies/Typography2";
import Typography3 from "../../compornents/Typographies/Typography3";
import List from "@mui/material/List";
import TextField from "@mui/material/TextField";
import AddIcon from "@mui/icons-material/Add";
import IconButton from "@mui/material/IconButton";
import BackButton from "../BackButton";
import { toViewStateAction } from "../../../actions/GroupSettingsAction";
import GroupSettingsUpdateListItem from "./GroupSettingsUpdateListItem";
import GroupUserEditListItem from "../GroupCreate/GroupUserEditListItem";
import { putGroupInfoAction } from "../../../actions/GroupSettingsAction";
import { UserOperateContext } from "../../../contexts/UserContext";

const GroupSettingsEditDisplay = () => {
  const { dispatchGroupSettings, stateGroupSettings } = useContext(
    GroupSettingsOperateContext
  );
  const { stateUser } = useContext(UserOperateContext);

  const [groupName, setGroupName] = useState("");
  const [description, setDescription] = useState("");
  const [updateUserList, setUpdateUserList] = useState([]);
  const [addUserList, setAddUserList] = useState([
    {
      id: 1,
      identifier: "",
    },
  ]);

  const updateGroup = () => {
    putGroupInfoAction(
      dispatchGroupSettings,
      stateUser.selectedGroup.groupId,
      groupName,
      description,
      updateUserList,
      addUserList
    );
  };

  const addUserRow = () => {
    setAddUserList([
      ...addUserList,
      {
        id: addUserList.slice(-1)[0].id + 1,
        identifer: "",
        authType: 0,
      },
    ]);
  };

  useEffect(() => {
    console.log(stateGroupSettings);
    setGroupName(stateGroupSettings.groupName);
    setDescription(stateGroupSettings.description);
    setUpdateUserList(stateGroupSettings.users);
  }, []);

  return (
    <div>
      <Box mt={2}>
        <BackButton onClick={() => toViewStateAction(dispatchGroupSettings)} />
      </Box>
      <Grid container direction="column" spacing={3.5} mb={5}>
        <Grid item>
          <Typography2>グループ新規作成</Typography2>
        </Grid>
        {stateGroupSettings.validate.isValidate && (
          <Grid item>
            <Typography3 color={"red"}>
              {stateGroupSettings.validate.message}
            </Typography3>
          </Grid>
        )}
        <Grid item>
          <Box>
            <Typography2>グループ名</Typography2>
            <Box
              border={1}
              sx={{ borderRadius: "16px", color: "#c4c4c4" }}
              p={2}
            >
              <TextField
                required
                id="standard-basic"
                variant="standard"
                value={groupName}
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
            <Box
              border={1}
              sx={{ borderRadius: "16px", color: "#c4c4c4" }}
              p={2}
            >
              <TextField
                required
                id="standard-basic"
                variant="standard"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="グループの説明を入力してください"
                sx={{ width: "100%" }}
              />
            </Box>
          </Box>
        </Grid>
        <Grid item>
          <Box>
            <Typography2>参加ユーザ</Typography2>
            <Box border={1} sx={{ borderRadius: "16px", color: "#c4c4c4" }}>
              <List>
                {updateUserList.map((updateUser) => (
                  <GroupSettingsUpdateListItem
                    key={updateUser.id}
                    id={updateUser.id}
                    user={updateUser}
                    updateUserList={updateUserList}
                    setUpdateUserList={setUpdateUserList}
                  />
                ))}
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
              onClick={updateGroup}
              variant="contained"
              startIcon={<SaveIcon />}
              sx={{ width: "50%", backgroundColor: "#5CB5A5" }}
            >
              UPDATE
            </Button>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
};

export default GroupSettingsEditDisplay;
