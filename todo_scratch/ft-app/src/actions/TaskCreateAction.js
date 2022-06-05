import { postTask } from "../repositories/TaskRepository";
import { formatDate } from "../utils/DatetimeUtil";

export const createTaskAction = (
  dispatch,
  groupId,
  taskStatusId,
  title,
  expired,
  context
) => {
  // 入力値のバリデーション
  if (taskStatusId == 0) {
    const action = {
      type: "validate",
      data: {
        validateMessage: "ステータスが未選択です",
      },
    };
    dispatch(action);
    return;
  }

  if (title == null || title.length <= 0) {
    const action = {
      type: "validate",
      data: {
        validateMessage: "タイトルが未入力です",
      },
    };
    dispatch(action);
    return;
  }

  const task = {
    title: title,
    context: context,
    deadline_at: formatDate(expired, "yyyy-MM-dd HH:mm:ss"),
    task_status_id: taskStatusId,
  };
  postTask(groupId, task).then(() => {
    const action = {
      type: "create_task",
    };
    dispatch(action);
  });
};

// 2022-05-21 12:00:00
