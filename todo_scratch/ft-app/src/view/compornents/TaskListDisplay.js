import React, { useContext } from "react";
import { AuthOperateContext } from "../../contexts/AuthContext";
import Typography2 from "../compornents/Typographies/Typography2";
import Grid from "@mui/material/Grid";
import { TaskListOperateContext } from "../../contexts/TaskListContext";
import Box from "@mui/material/Box";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";

const TaskListDisplay = () => {
  const { state } = useContext(AuthOperateContext);
  const { stateTaskList } = useContext(TaskListOperateContext);
  return (
    <Box>
      <Fab color="primary" aria-label="add">
        <AddIcon />
      </Fab>
      <Grid
        container
        direction="column"
        alignItems="center"
        justify="center"
        mt={1}
      >
        <Grid item>
          <Typography2>
            参加グループ設定 {state.selected_group.group_id}
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
