import React, { useContext, useEffect } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography2 from "../compornents/Typographies/Typography2";
import Typography3 from "../compornents/Typographies/Typography3";
import { GroupJoinedOperateContext } from "../../contexts/GroupJoinedContext";
import { Navigate } from "react-router-dom";
import List from "@mui/material/List";
import JoinedGroupListItem from "../JoinedGroupListItem";
import { getJoinedGroup } from "../../actions/GroupJoinedAction";
import { AuthOperateContext } from "../../contexts/AuthContext";
import { changeGroup } from "../../actions/GroupJoinedAction";

const GroupJoinedListDisplay = () => {
  const { stateGroupjoined, dispatchGroupJoined } = useContext(
    GroupJoinedOperateContext
  );
  const { state, dispatch } = useContext(AuthOperateContext);

  useEffect(() => {
    getJoinedGroup(dispatchGroupJoined);
  }, []);

  const chengeGroup = (groupId) => {
    changeGroup(dispatchGroupJoined, dispatch, groupId);
  };
  return stateGroupjoined.toPath != null ? (
    <Navigate to={stateGroupjoined.toPath} />
  ) : (
    <>
      <Grid container direction="column" spacing={3.5} mt={2}>
        <Grid item>
          <Typography2>参加済みグループ</Typography2>
        </Grid>
        <Grid item>
          <Box sx={{ color: "#c4c4c4" }}>
            <Box border={1} sx={{ borderRadius: "16px" }} p={2}>
              {stateGroupjoined.joinedGroups.length > 0 ? (
                <List>
                  {stateGroupjoined.joinedGroups.map((group) => (
                    <JoinedGroupListItem
                      group={group}
                      selected_group_id={state.selected_group.group_id}
                      changeGroupFunction={chengeGroup}
                      key={group.group_id}
                    />
                  ))}
                </List>
              ) : (
                <Box>
                  <Typography3 color={"#c4c4c4"}>
                    参加中のグループはありません
                  </Typography3>
                </Box>
              )}
            </Box>
          </Box>
        </Grid>
      </Grid>
    </>
  );
};

export default GroupJoinedListDisplay;
