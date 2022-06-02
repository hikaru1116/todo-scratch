export const getTaskStatusColor = (taskStatusList, taskStatusId) => {
  return taskStatusList.filter(
    (taskStatus) => taskStatus.task_status_id == taskStatusId
  )[0].status_color;
};
