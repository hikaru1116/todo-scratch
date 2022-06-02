export default function TaskListReducer(state, action) {
  switch (action.type) {
    case "get_task_list_divide_by_status":
      return {
        ...state,
        taskList: action.data,
      };
    default:
      return state;
  }
}
