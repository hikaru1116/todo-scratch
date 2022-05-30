import React, { useContext } from "react";
import { UserOperateContext } from "../../contexts/UserContext";
import TaskListDisplay from "../compornents/TaskList/TaskListDisplay";

const TaskListPage = () => {
  const { stateUser } = useContext(UserOperateContext);
  return (
    <div>
      <TaskListDisplay />
      <div>
        {stateUser.selectedGroup.taskStatusList.map((taskStatus) => (
          <h3>{taskStatus.task_status_id}</h3>
        ))}
      </div>
    </div>
  );
};

export default TaskListPage;
