export default function TaskDetailReducer(state, action) {
  switch (action.type) {
    case "get_task_detail":
      return {
        ...state,
        task: {
          taskId: action.data.task_id,
          groupId: action.data.group_id,
          userId: action.data.user_id,
          userName: action.data.user_name,
          title: action.data.title,
          context: action.data.context,
          deadlineAt: action.data.deadline_at,
          taskStatusId: action.data.task_status_id,
          history: action.data.history,
        },
      };
    case "fail_get_task_detail":
      return state;
    case "put_task":
      return {
        ...state,
        task: {
          title: action.data.title,
          context: action.data.context,
          deadlineAt: action.data.deadline_at,
          taskStatusId: action.data.task_status_id,
        },
        isEdit: false,
      };
    case "change_task_status":
      return {
        ...state,
        task: {
          taskStatusId: action.data,
        },
        taskStateChangeCount: state.taskStateChangeCount + 1,
      };
    case "to_edit":
      return {
        ...state,
        isEdit: true,
      };
    case "to_view":
      return {
        ...state,
        isEdit: false,
      };
    default:
      return state;
  }
}
