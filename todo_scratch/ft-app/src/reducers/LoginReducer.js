import { login } from "../repositories/LoginRepository";

export function LoginReducer(state, action) {
  switch (action) {
    case "sign_in":
      // サインイン処理発火
      login();
      return {
        ...state,
        isLoading: true,
      };
    case "sign_up":
      return {
        ...state,
        isLoading: true,
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
