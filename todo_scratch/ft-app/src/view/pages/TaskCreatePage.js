import React from "react";
import { TaskCreateContext } from "../../contexts/TaskCreateContexts";
import TaskCreateDisplay from "../compornents/TaskCreate/TaskCreateDisplay";

const TaskCreatePage = () => {
  return (
    <TaskCreateContext>
      <TaskCreateDisplay />
    </TaskCreateContext>
  );
};

export default TaskCreatePage;
