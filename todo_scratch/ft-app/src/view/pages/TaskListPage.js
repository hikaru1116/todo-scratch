import React from "react";
import { TaskListContext } from "../../contexts/TaskListContext";
import TaskListDisplay from "../compornents/TaskList/TaskListDisplay";

const TaskListPage = () => {
  return (
    <TaskListContext>
      <TaskListDisplay />
    </TaskListContext>
  );
};

export default TaskListPage;
