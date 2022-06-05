import React, { useContext } from "react";
import Grid from "@mui/material/Grid";
import { TaskDetailOperateContext } from "../../../contexts/TaskDetailContext";
import Typography3 from "../../compornents/Typographies/Typography3";
import Box from "@mui/material/Box";
import { UserOperateContext } from "../../../contexts/UserContext";
import AccessTimeIcon from "@mui/icons-material/AccessTime";
import {
  getTaskStateName,
  getTaskStatusColor,
} from "../../../utils/TaskStatusUtil";
import Button from "@mui/material/Button";
import EditIcon from "@mui/icons-material/Edit";
import { changeDisplayModeToEdit } from "../../../actions/TaskDetailAction";

const TaskDetailViewDisplay = () => {
  const { stateTaskDetail, dispatchTaskDetail } = useContext(
    TaskDetailOperateContext
  );
  const { stateUser } = useContext(UserOperateContext);

  const toEdit = () => changeDisplayModeToEdit(dispatchTaskDetail);

  return (
    <Box sx={{ width: "80%", maxWidth: 600 }} ml={"auto"} mr={"auto"}>
      <Grid container direction="column" spacing={3.5} mt={2}>
        <Grid item>
          {stateTaskDetail.task.taskStatusId && (
            <Box
              textAlign={"center"}
              p={1}
              borderRadius={"16px"}
              sx={{
                color: "#ffffff",
                backgroundColor: getTaskStatusColor(
                  stateUser.selectedGroup.taskStatusList,
                  stateTaskDetail.task.taskStatusId
                ),
              }}
            >
              {getTaskStateName(
                stateUser.selectedGroup.taskStatusList,
                stateTaskDetail.task.taskStatusId
              )}
            </Box>
          )}
        </Grid>
        <Grid item>
          <Typography3>{stateTaskDetail.task.title}</Typography3>
          <Box
            mt={1}
            border={0.5}
            borderColor={(theme) => theme.palette.primary.main}
          />
        </Grid>
        <Grid item>
          <Grid
            container
            direction="row"
            justifyContent="flex-end"
            alignItems="center"
          >
            <Grid item>
              <AccessTimeIcon
                sx={{ color: (theme) => theme.palette.primary.main }}
              />
            </Grid>
            <Grid item>
              <Typography3
                align={"right"}
                color={(theme) => theme.palette.primary.main}
              >
                {stateTaskDetail.task.deadlineAt}
              </Typography3>
            </Grid>
          </Grid>
        </Grid>
        <Grid item>
          {stateTaskDetail.task.context &&
          stateTaskDetail.task.context.length > 0 ? (
            <Box
              p={1}
              border={1}
              borderColor={(theme) => theme.palette.primary.main}
              borderRadius={"16px"}
            >
              <Typography3>{stateTaskDetail.task.context}</Typography3>
            </Box>
          ) : (
            <Box
              height={"100"}
              p={1}
              border={1}
              borderColor={(theme) => theme.palette.primary.main}
              borderRadius={"16px"}
            >
              <Typography3 color={(theme) => theme.palette.primary.main}>
                コンテンツはありません
              </Typography3>
            </Box>
          )}
        </Grid>
        <Grid item>
          <Box textAlign="center" mt={2}>
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
    </Box>
  );
};

export default TaskDetailViewDisplay;
