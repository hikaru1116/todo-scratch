export default function GroupJoinedReducer(state, action) {
  switch (action.type) {
    case "get_joined_group":
      return {
        ...state,
        joinedGroups: action.data,
      };
    case "change_group":
      return {
        ...state,
        toPath: "/group-settings",
      };
    default:
      return state;
  }
}
