import React, { useContext, useEffect } from "react";
import { TaskDetailOperateContext } from "../../../contexts/TaskDetailContext";
import TaskDetailEditDisplay from "./TaskDetailEditDisplay";
import TaskDetailViewDisplay from "./TaskDetailViewDisplay";
import { useParams } from "react-router-dom";
import { getTaskDetailAction } from "../../../actions/TaskDetailAction";

const TaskDitailDisplay = () => {
  const params = useParams();
  const { stateTaskDetail, dispatchTaskDetail } = useContext(
    TaskDetailOperateContext
  );

  useEffect(() => {
    getTaskDetailAction(dispatchTaskDetail, params.groupId, params.taskId);
  }, []);

  return stateTaskDetail.isEdit ? (
    <TaskDetailEditDisplay />
  ) : (
    <TaskDetailViewDisplay />
  );
};

export default TaskDitailDisplay;
