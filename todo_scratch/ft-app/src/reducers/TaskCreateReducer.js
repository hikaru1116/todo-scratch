export default function TaskCreateReducer(state, action) {
  switch (action.type) {
    case "create_task":
      return {
        ...state,
        toPath: "/",
        validate: {
          isValidate: false,
          message: "",
        },
      };

    case "validate":
      return {
        ...state,
        validate: {
          isValidate: true,
          message: action.data.validateMessage,
        },
      };
    default:
      return state;
  }
}
