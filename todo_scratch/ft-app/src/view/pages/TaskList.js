import React from "react";
import { TaskListContext } from "../../contexts/TaskListContext";
import TaskListDisplay from "../compornents/TaskListDisplay";

const TaskList = () => {
  return (
    <TaskListContext>
      <TaskListDisplay />
    </TaskListContext>
  );
};

export default TaskList;
