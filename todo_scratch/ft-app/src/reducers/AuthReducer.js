export default function AuthReducer(state, action) {
  switch (action.type) {
    case "get_user_info":
      return {
        ...state,
        user: action.data.user,
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
    default:
      return state;
  }
}
