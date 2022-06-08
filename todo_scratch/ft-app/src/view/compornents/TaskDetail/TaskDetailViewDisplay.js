import React, { useState, useContext } from "react";
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
import {
  changeDisplayModeToEdit,
  changeTaskStatusAction,
} from "../../../actions/TaskDetailAction";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import BackButton from "../BackButton";
import { useNavigate } from "react-router-dom";
import Modal from "@mui/material/Modal";
import { useParams } from "react-router-dom";

const TaskDetailViewDisplay = () => {
  const params = useParams();
  const navigate = useNavigate();
  const { stateTaskDetail, dispatchTaskDetail } = useContext(
    TaskDetailOperateContext
  );
  const { stateUser } = useContext(UserOperateContext);

  const [open, setOpen] = useState(false);
  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const toEdit = () => changeDisplayModeToEdit(dispatchTaskDetail);

  const changeTaskStatus = (taskStatusId) => {
    changeTaskStatusAction(
      dispatchTaskDetail,
      params.groupId,
      params.taskId,
      taskStatusId
    );
    handleClose();
  };

  return (
    <Box sx={{ width: "80%", maxWidth: 600 }} ml={"auto"} mr={"auto"}>
      <Modal open={open} onClose={handleClose}>
        <Box
          p={3}
          style={{
            backgroundColor: "#ffffff",
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: "40%",
          }}
        >
          <Grid justifyContent="space-between" alignItems="center">
            {stateUser.selectedGroup.taskStatusList.map((taskStatus) => {
              return (
                <Grid item>
                  <Box
                    onClick={() => changeTaskStatus(taskStatus.task_status_id)}
                    mt={2}
                    mb={2}
                    borderRadius={"16px"}
                    sx={{
                      backgroundColor: taskStatus.status_color,
                    }}
                  >
                    <Typography3
                      align={"center"}
                      lineHeight={"5"}
                      color={"#ffffff"}
                    >
                      {taskStatus.task_status_name}
                    </Typography3>
                  </Box>
                </Grid>
              );
            })}
          </Grid>
        </Box>
      </Modal>
      <Grid container direction="column" spacing={3.5} mt={2}>
        <Grid item>
          <BackButton onClick={() => navigate("/")} />
        </Grid>
        <Grid item>
          {stateTaskDetail.task.taskStatusId && (
            <Box
              onClick={handleOpen}
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
              <Typography3 align={"center"} color={"#ffffff"}>
                {getTaskStateName(
                  stateUser.selectedGroup.taskStatusList,
                  stateTaskDetail.task.taskStatusId
                )}
              </Typography3>
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
          <Grid container direction="row" justifyContent="space-between">
            <Grid item>
              <Grid
                container
                direction="row"
                justifyContent="flex-end"
                alignItems="center"
              >
                <Grid item>
                  <AccountCircleIcon
                    sx={{ color: (theme) => theme.palette.primary.main }}
                  />
                </Grid>

                <Grid item>
                  <Typography3
                    align={"right"}
                    color={(theme) => theme.palette.primary.main}
                  >
                    {stateTaskDetail.task.userName}
                  </Typography3>
                </Grid>
              </Grid>
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
        {stateUser.user != null &&
          stateTaskDetail.task.userId != null &&
          stateTaskDetail.task.userId === stateUser.user.user_id && (
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
          )}
      </Grid>
    </Box>
  );
};

export default TaskDetailViewDisplay;
