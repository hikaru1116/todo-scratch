export default function SignUpReducer(state, action) {
  switch (action.type) {
    case "success_sign_up":
      return {
        ...state,
        isSignUp: true,
        validate: {
          isValidate: false,
          message: "",
        },
      };
    case "fail_sign_up":
      return {
        ...state,
        isSignUp: false,
        validate: {
          isValidate: true,
          message: action.data.message,
        },
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
