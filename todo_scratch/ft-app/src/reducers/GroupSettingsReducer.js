export default function GroupSettingsReducer(state, action) {
  switch (action.type) {
    case "get_group_info":
      return {
        ...state,
        groupId: action.groupId,
        groupName: action.groupName,
        description: action.description,
        users: action.users,
      };
    case "put_group":
      return {
        ...state,
        updateCount: state.updateCount + 1,
        isEdit: false,
      };
    case "to_view_state":
      return {
        ...state,
        isEdit: false,
      };
    case "to_edit_state":
      return {
        ...state,
        isEdit: true,
      };
    case "loading":
      return {
        ...state,
        isLoading: true,
      };
    default:
      return state;
  }
}
