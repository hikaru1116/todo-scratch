import React from "react";
import List from "@mui/material/List";
import TaskListItem from "./TaskListItem";
import Box from "@mui/material/Box";

const TaskListColum = ({ taskList, statusColor }) => {
  return taskList.length <= 0 ? (
    <Box />
  ) : (
    <List>
      {taskList.map((task) => (
        <TaskListItem
          key={task.task_id}
          task={task}
          statusColor={statusColor}
        />
      ))}
    </List>
  );
};

export default TaskListColum;
