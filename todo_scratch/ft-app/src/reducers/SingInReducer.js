export default function SingInReducer(state, action) {
  console.log(action.type);
  switch (action.type) {
    case "success_sign_in":
      return {
        ...state,
        isSignIn: true,
        isLoading: false,
        validate: {
          isValidate: false,
          message: "",
        },
      };
    case "fail_sign_in":
      return {
        ...state,
        isSignIn: false,
        isLoading: false,
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
