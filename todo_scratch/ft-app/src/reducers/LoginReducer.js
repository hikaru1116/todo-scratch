export function LoginReducer(state, action) {
  switch (action.type) {
    case "add_1":
      return {
        ...state,
        value: state.value + 1,
      };
    case "multiple_3":
      console.log("multi");
      return {
        ...state,
        value: state.value * 3,
      };
    case "reset":
      return {
        ...state,
        value: action.initialState,
      };
    default:
      return state;
  }
}
