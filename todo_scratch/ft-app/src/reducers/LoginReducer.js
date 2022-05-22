export function LoginReducer(state, action) {
  switch (action.type) {
    case "loading":
      return {
        ...state,
        isLoading: true,
      };
    case "sign_in":
      console.log("SignIn");
      return {
        ...state,
        isLoading: true,
        user: action.data,
      };
    case "validate":
      return {
        ...state,
        isLoading: false,
      };
    default:
      return state;
  }
}
