export default function AuthReducer(state, action) {
  switch (action.type) {
    case "get_user_info":
      return {
        ...state,
        user: action.data.user,
        selected_group: {
          group_id: action.data.selected_group.group_id,
        },
        judgeLogin: {
          isJudgeLogin: true,
          toPath: action.data.user != null ? action.data.path : "/signin",
        },
      };
    case "loading":
      return {
        ...state,
        isLoading: true,
      };
    case "sign_in": {
      return {
        ...state,
        isLoading: false,
        user: action.data,
        validate: {
          isValidate: false,
          message: "",
        },
      };
    }
    case "sign_up":
      console.log(action.data);
      return {
        ...state,
        isLoading: false,
        validate: {
          isValidate: false,
          message: "",
        },
      };
    case "validate":
      return {
        ...state,
        isLoading: false,
        validate: {
          isValidate: true,
          message: action.data,
        },
      };
    case "change_selected_group":
      return {
        ...state,
        selected_group: {
          group_id: action.data,
        },
      };
    default:
      return state;
  }
}
