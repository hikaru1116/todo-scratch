import React, { useContext } from "react";
import { UserOperateContext } from "../../../contexts/UserContext";
import Typography2 from "../../compornents/Typographies/Typography2";
import Grid from "@mui/material/Grid";
import { TaskListOperateContext } from "../../../contexts/TaskListContext";
import Box from "@mui/material/Box";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import { useNavigate } from "react-router-dom";

const TaskListDisplay = () => {
  const { stateUser } = useContext(UserOperateContext);
  const { stateTaskList } = useContext(TaskListOperateContext);
  const navigate = useNavigate();

  const toTaskCreate = () => navigate("/task/create");

  return (
    <Box>
      {stateUser.selectedGroup.groupId !== null && (
        <Fab color="primary" aria-label="add" onClick={toTaskCreate}>
          <AddIcon />
        </Fab>
      )}

      <Grid
        container
        direction="column"
        alignItems="center"
        justify="center"
        mt={1}
      >
        <Grid item>
          <Typography2>
            参加グループ設定 {stateUser.selectedGroup.groupId}
          </Typography2>
        </Grid>
        <Grid item>
          {stateTaskList.taskList == null ? (
            <Box>
              <Typography2>タスクがありません</Typography2>
            </Box>
          ) : (
            <Box>
              <Typography2>タスクあります</Typography2>
            </Box>
          )}
        </Grid>
      </Grid>
    </Box>
  );
};

export default TaskListDisplay;
