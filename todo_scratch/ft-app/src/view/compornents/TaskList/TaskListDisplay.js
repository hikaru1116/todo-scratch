import React, { useContext, useState, useEffect } from "react";
import { UserOperateContext } from "../../../contexts/UserContext";
import Typography2 from "../../compornents/Typographies/Typography2";
import { TaskListOperateContext } from "../../../contexts/TaskListContext";
import Box from "@mui/material/Box";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Fab from "@mui/material/Fab";
import AddIcon from "@mui/icons-material/Add";
import { useNavigate } from "react-router-dom";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/swiper-bundle.min.css";
import "swiper/swiper.min.css";
import { getTaskListDivideByStatusAction } from "../../../actions/TaskListAction";
import TaskListColum from "./TaskListColum";
import { getTaskStatusColor } from "../../../utils/TaskStatusUtil";

const TaskListDisplay = () => {
  const { stateUser } = useContext(UserOperateContext);
  const { stateTaskList, dispatchTaskList } = useContext(
    TaskListOperateContext
  );
  const navigate = useNavigate();

  const toTaskCreate = () => navigate("/task/create");

  const [swiper, setSwiper] = useState(null);
  const [value, setValue] = useState(67);

  const slideChange = (index) => {
    setValue(taskStatusSwipeMap[index]);
  };

  const tabChange = (event, index) => {
    setValue(index);
    swiper.slideTo(taskStatusTabMap[index]);
  };

  let taskStatusTabMap = {};
  let taskStatusSwipeMap = {};
  let taskStatuTabIndex = -1;

  const createTaskListTab = (taskStatus) => {
    taskStatuTabIndex = taskStatuTabIndex + 1;
    taskStatusTabMap[taskStatus.task_status_id] = taskStatuTabIndex;
    taskStatusSwipeMap[taskStatuTabIndex] = taskStatus.task_status_id;
    return (
      <Tab
        label={taskStatus.task_status_name}
        value={taskStatus.task_status_id}
      />
    );
  };

  const createTaskList = (taskInfo) => {
    return (
      <SwiperSlide>
        <TaskListColum
          taskList={taskInfo.task_list}
          statusColor={getTaskStatusColor(
            stateUser.selectedGroup.taskStatusList,
            taskInfo.task_status_id
          )}
        />
      </SwiperSlide>
    );
  };
  useEffect(() => {
    if (stateUser.selectedGroup.groupId == null) {
      return;
    }
    setValue(stateUser.selectedGroup.taskStatusList[0].task_status_id);
    getTaskListDivideByStatusAction(
      dispatchTaskList,
      stateUser.selectedGroup.groupId
    );
  }, [stateUser.selectedGroup.groupId]);

  return (
    <Box>
      {stateTaskList.taskList.length <= 0 ? (
        <Box
          sx={{ width: "80%", maxWidth: 600 }}
          ml={"auto"}
          mr={"auto"}
          mt={1}
        ></Box>
      ) : (
        <Box
          sx={{ width: "80%", maxWidth: 600 }}
          ml={"auto"}
          mr={"auto"}
          mt={1}
        >
          <Box sx={{ width: "100%", bgcolor: "background.paper" }} mt={1}>
            <Tabs
              value={value}
              onChange={tabChange}
              scrollButtons="auto"
              variant="fullWidth"
            >
              {stateUser.selectedGroup.taskStatusList.length > 0 &&
                stateUser.selectedGroup.taskStatusList.map((taskStatus) =>
                  createTaskListTab(taskStatus)
                )}
            </Tabs>
          </Box>
          <Box>
            <Swiper
              spaceBetween={50}
              slidesPerView={1}
              onSlideChange={(index) => slideChange(index.activeIndex)}
              onSwiper={(swiper) => {
                const swiperInstance = swiper;
                setSwiper(swiperInstance);
              }}
            >
              {stateUser.selectedGroup.taskStatusList.map((taskStatus) => {
                for (let i = 0; i < stateTaskList.taskList.length; i++) {
                  if (
                    taskStatus.task_status_id ===
                    stateTaskList.taskList[i].task_status_id
                  ) {
                    return createTaskList(stateTaskList.taskList[i]);
                  }
                }
                return (
                  <SwiperSlide>
                    <Typography2>タスクなし</Typography2>
                  </SwiperSlide>
                );
              })}
            </Swiper>
          </Box>
          {stateUser.selectedGroup.groupId !== null && (
            <Box
              sx={{
                margin: 0,
                top: "auto",
                right: 30,
                bottom: 20,
                left: "auto",
                position: "fixed",
                zIndex: 999,
              }}
            >
              <Fab color="primary" aria-label="add" onClick={toTaskCreate}>
                <AddIcon />
              </Fab>
            </Box>
          )}
        </Box>
      )}
    </Box>
  );
};

export default TaskListDisplay;
