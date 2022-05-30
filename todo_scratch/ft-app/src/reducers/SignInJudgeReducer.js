export default function SignInJudgeReducer(state, action) {
  switch (action.type) {
    case "success_sign_in":
      return {
        doneJudge: true,
        isJudgeSingIn: true,
        path: action.data.path,
      };
    case "fail_sign_in":
      return {
        doneJudge: true,
        isJudgeSingIn: false,
        path: "/signin",
      };
    default:
      return state;
  }
}
