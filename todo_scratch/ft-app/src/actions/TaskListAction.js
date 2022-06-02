import { getTaskListDivideByStatus } from "../repositories/TaskRepository";

export const getTaskListDivideByStatusAction = (dispatch, groupId) => {
  getTaskListDivideByStatus(groupId).then((taskList) => {
    if (taskList == null) {
      return;
    }

    const action = {
      type: "get_task_list_divide_by_status",
      data: taskList,
    };
    dispatch(action);
  });
};
