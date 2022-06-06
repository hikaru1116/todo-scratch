import {
  changeTaskStatus,
  getTaskDetail,
  putTask,
} from "../repositories/TaskRepository";
import { formatDate } from "../utils/DatetimeUtil";

export const getTaskDetailAction = (dispatch, groupId, taskId) => {
  getTaskDetail(groupId, taskId).then((task) => {
    console.log(task);
    if (task == null) {
      const action = {
        type: "fail_get_task_detail",
      };
      dispatch(action);
      return;
    }
    const action = {
      type: "get_task_detail",
      data: task,
    };
    dispatch(action);
  });
};

export const putTaskAction = (
  dispatch,
  groupId,
  taskId,
  title,
  context,
  expired,
  taskStatusId
) => {
  // バリデーション処理

  console.log(typeof expired);
  const task = {
    title: title,
    context: context,
    deadline_at: formatDate(expired, "yyyy-MM-dd HH:mm:ss"),
    task_status_id: taskStatusId,
  };

  putTask(groupId, taskId, task).then((isSuccess) => {
    const action = {
      type: "put_task",
      data: task,
    };
    dispatch(action);
  });
};

export const changeDisplayModeToEdit = (dispatch) => {
  const action = {
    type: "to_edit",
  };
  dispatch(action);
};

export const changeDisplayModeToView = (dispatch) => {
  const action = {
    type: "to_view",
  };
  dispatch(action);
};

export const changeTaskStatusAction = (
  dispatch,
  groupId,
  taskId,
  taskStatusId
) => {
  console.log(`changeTaskStatusAction ${taskId}`);
  changeTaskStatus(groupId, taskId, taskStatusId).then((isSuccess) => {
    if (!isSuccess) {
      return;
    }
    const action = {
      type: "change_task_status",
      data: taskStatusId,
    };

    dispatch(action);
  });
};

const deleteTaskACtion = (dispatch) => {
  const action = {
    type: "delete_task",
  };
  dispatch(action);
};
