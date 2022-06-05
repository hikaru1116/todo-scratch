export const getTaskStatusColor = (taskStatusList, taskStatusId) => {
  return taskStatusList.filter(
    (taskStatus) => taskStatus.task_status_id == taskStatusId
  )[0].status_color;
};

export const getTaskStateName = (taskStatusList, taskStatusId) => {
  console.log(
    `getTaskStateName ${taskStatusId} ${taskStatusList[0].task_status_name}`
  );
  return taskStatusList.filter(
    (taskStatus) => taskStatus.task_status_id == taskStatusId
  )[0].task_status_name;
};
