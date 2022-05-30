import React, { useState, useContext } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography2 from "../../compornents/Typographies/Typography2";
import Typography3 from "../../compornents/Typographies/Typography3";
import TextField from "@mui/material/TextField";
import { TaskCreateOperateContext } from "../../../contexts/TaskCreateContexts";
import { createTaskAction } from "../../../actions/TaskCreateAction";
import Button from "@mui/material/Button";
import SaveIcon from "@mui/icons-material/Save";
import { UserOperateContext } from "../../../contexts/UserContext";
import { LocalizationProvider, DateTimePicker } from "@mui/x-date-pickers";
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import ja from "date-fns/locale/ja";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import { Navigate } from "react-router-dom";

const TaskCreateDisplay = () => {
  const { stateTaskCreate, dispatchTaskCreate } = useContext(
    TaskCreateOperateContext
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

  const createTask = () => {
    createTaskAction(
      dispatchTaskCreate,
      stateUser.selectedGroup.groupId,
      taskStatus,
      title,
      expired,
      context
    );
  };

  return stateTaskCreate.toPath != null ? (
    <Navigate to={stateTaskCreate.toPath} />
  ) : (
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
        {stateTaskCreate.validate.isValidate && (
          <Grid item>
            <Typography3 color={"red"}>
              {stateTaskCreate.validate.message}
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
              rows={4}
              id="standard-basic"
              onChange={(e) => setContext(e.target.value)}
              placeholder="タスク内容を入力"
              sx={{ width: "100%" }}
            />
          </Box>
        </Grid>
        <Grid item>
          <Box textAlign="center" mt={5}>
            <Button
              onClick={createTask}
              variant="contained"
              startIcon={<SaveIcon />}
              sx={{ width: "50%", backgroundColor: "#5CB5A5" }}
            >
              Create
            </Button>
          </Box>
        </Grid>
      </Grid>
    </LocalizationProvider>
  );
};

export default TaskCreateDisplay;
