import React, { useContext } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography2 from "../compornents/Typographies/Typography2";
import Typography3 from "../compornents/Typographies/Typography3";
import { GroupSettingsOperateContext } from "../../contexts/GroupSettingsContext";
import List from "@mui/material/List";
import GroupUserListItem from "./GroupUserListItem";
import Button from "@mui/material/Button";
import EditIcon from "@mui/icons-material/Edit";
import { toEditState } from "../../actions/GroupSettingsAction";

const GroupSettingsViewDisplay = () => {
  const { stateGroupSettings, dispatchGroupSettings } = useContext(
    GroupSettingsOperateContext
  );

  const toEdit = () => toEditState(dispatchGroupSettings);

  return (
    <div>
      <Grid container direction="column" spacing={3.5} mt={2}>
        <Grid item>
          <Typography2>参加グループ設定</Typography2>
        </Grid>
        <Grid item>
          <Box>
            <Typography2>グループ名</Typography2>
            <Box
              border={1}
              sx={{ borderRadius: "16px", color: "#c4c4c4" }}
              p={2}
            >
              <Typography3>{stateGroupSettings.group_name}</Typography3>
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
              <Typography3>{stateGroupSettings.description}</Typography3>
            </Box>
          </Box>
        </Grid>
        <Grid item>
          <Box>
            <Typography2>参加ユーザ</Typography2>
            <Box border={1} sx={{ borderRadius: "16px", color: "#c4c4c4" }}>
              {stateGroupSettings.users.length > 0 ? (
                <List>
                  {stateGroupSettings.users.map((user) => (
                    <GroupUserListItem user={user} key={user.user_id} />
                  ))}
                </List>
              ) : (
                <Box width={"100%"} height={50} />
              )}
            </Box>
          </Box>
        </Grid>
        <Grid item>
          <Box textAlign="center">
            <Button
              variant="outlined"
              onClick={toEdit}
              startIcon={<EditIcon />}
              sx={{ width: "50%" }}
            >
              Edit
            </Button>
          </Box>
        </Grid>
      </Grid>
    </div>
  );
};

export default GroupSettingsViewDisplay;
