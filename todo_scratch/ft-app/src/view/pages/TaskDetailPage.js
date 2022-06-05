import React from "react";
import { TaskDetailContext } from "../../contexts/TaskDetailContext";
import TaskDitailDisplay from "../compornents/TaskDetail/TaskDitailDisplay";

const TaskDetailPage = () => {
  return (
    <TaskDetailContext>
      <TaskDitailDisplay />
    </TaskDetailContext>
  );
};

export default TaskDetailPage;
