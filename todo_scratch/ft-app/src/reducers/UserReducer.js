export default function UserReducer(state, action) {
  switch (action.type) {
    case "set_user_data":
      return {
        ...state,
        user: action.data.user,
        selectedGroup: {
          groupId: action.data.selectedGroup.groupId,
          taskStatusList: action.data.selectedGroup.taskStatusList,
        },
      };
    case "set_selected_group":
      return {
        ...state,
        selectedGroup: {
          groupId: action.data.selectedGroup.groupId,
          taskStatusList: action.data.selectedGroup.taskStatusList,
        },
      };
    case "clear_user_data":
      return {
        user: null,
        selectedGroup: {
          groupId: null,
          taskStatusList: [],
        },
      };
    default:
      return state;
  }
}
