export default function GroupSettingsReducer(state, action) {
  switch (action.type) {
    case "get_group_info":
      return {
        ...state,
        group_id: action.group_id,
        group_name: action.group_name,
        description: action.description,
        users: action.users,
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
