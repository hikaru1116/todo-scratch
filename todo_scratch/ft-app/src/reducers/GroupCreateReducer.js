export default function GroupSettingsReducer(state, action) {
  switch (action.type) {
    case "create_group_success":
      return {
        ...state,
        validate: {
          isValidate: false,
          message: "",
        },
        toPath: "/group-settings",
      };
    case "create_group_fail":
      return {
        ...state,
        validate: {
          isValidate: true,
          message: action.data,
        },
      };
    case "validate":
      return {
        ...state,
        validate: {
          isValidate: true,
          message: action.data,
        },
      };
    default:
      return state;
  }
}
