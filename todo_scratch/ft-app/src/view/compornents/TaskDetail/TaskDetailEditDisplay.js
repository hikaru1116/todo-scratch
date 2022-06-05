import React, { useState, useContext, useEffect } from "react";
import Grid from "@mui/material/Grid";
import { TaskDetailOperateContext } from "../../../contexts/TaskDetailContext";
import Typography2 from "../../compornents/Typographies/Typography2";
import Typography3 from "../../compornents/Typographies/Typography3";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import SaveIcon from "@mui/icons-material/Save";
import { LocalizationProvider, DateTimePicker } from "@mui/x-date-pickers";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import ja from "date-fns/locale/ja";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import { Navigate, useParams } from "react-router-dom";
import { UserOperateContext } from "../../../contexts/UserContext";
import { putTaskAction } from "../../../actions/TaskDetailAction";

const TaskDetailEditDisplay = () => {
  const params = useParams();
  const { stateTaskDetail, dispatchTaskDetail } = useContext(
    TaskDetailOperateContext
  );
  const { stateUser } = useContext(UserOperateContext);

  const [expired, setExpired] = useState(new Date());
  const [taskStatus, setTaskStatus] = useState(0);
  const [title, setTitle] = useState("");
  const [context, setContext] = useState("");

  const handleChangeExpired = (newValue) => {
    setExpired(newValue);
  };

  const handleChangeTsaskStatus = (event) => {
    setTaskStatus(event.target.value);
  };

  const updateTask = () => {
    putTaskAction(
      dispatchTaskDetail,
      params.groupId,
      params.taskId,
      title,
      context,
      expired,
      taskStatus
    );
  };

  useEffect(() => {
    setExpired(new Date(stateTaskDetail.task.deadlineAt));
    setTaskStatus(stateTaskDetail.task.taskStatusId);
    setTitle(stateTaskDetail.task.title);
    setContext(stateTaskDetail.task.context);
  }, [stateTaskDetail.task]);

  return (
    <LocalizationProvider dateAdapter={AdapterDateFns} adapterLocale={ja}>
      <Grid
        container
        direction="column"
        justify="center"
        sx={{ width: "80%", maxWidth: 600 }}
        m={"auto"}
        spacing={2.5}
      >
        <Grid item>
          <Typography2>タスク作成</Typography2>
        </Grid>
        {stateTaskDetail.validate.isValidate && (
          <Grid item>
            <Typography3 color={"red"}>
              {stateTaskDetail.validate.message}
            </Typography3>
          </Grid>
        )}
        <Grid item>
          <Box>
            <Typography3>ステータス</Typography3>
            <Select
              value={taskStatus}
              onChange={handleChangeTsaskStatus}
              sx={{ width: "100%" }}
            >
              {stateUser.selectedGroup.taskStatusList.map((taskInfo) => (
                <MenuItem
                  key={taskInfo.task_status_id}
                  value={taskInfo.task_status_id}
                >
                  {taskInfo.task_status_name}
                </MenuItem>
              ))}
            </Select>
          </Box>
        </Grid>
        <Grid item>
          <Box>
            <Typography3>タイトル</Typography3>
            <TextField
              required
              id="standard-basic"
              variant="standard"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="タイトルを入力してください"
              sx={{ width: "100%" }}
            />
          </Box>
        </Grid>
        <Grid item>
          <Box>
            <Typography3>期限</Typography3>
            <DateTimePicker
              value={expired}
              onChange={handleChangeExpired}
              renderInput={(params) => (
                <TextField {...params} sx={{ width: "100%" }} />
              )}
            />
          </Box>
        </Grid>
        <Grid item>
          <Box>
            <Typography3>内容</Typography3>
            <TextField
              required
              multiline
              rows={5}
              value={context}
              id="standard-basic"
              onChange={(e) => setContext(e.target.value)}
              placeholder="タスク内容を入力"
              sx={{ width: "100%" }}
            />
          </Box>
        </Grid>
        <Grid item>
          <Box textAlign="center" mt={2} mb={2}>
            <Button
              onClick={updateTask}
              variant="contained"
              startIcon={<SaveIcon />}
              sx={{
                width: "50%",
                backgroundColor: "#5CB5A5",
                color: "#ffffff",
              }}
            >
              UPDATE
            </Button>
          </Box>
        </Grid>
      </Grid>
    </LocalizationProvider>
  );
};

export default TaskDetailEditDisplay;
