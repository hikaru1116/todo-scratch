export default function AccountReducer(state, action) {
  switch (action.type) {
    case "success_edit_account":
      return {
        ...state,
        isSuccessEdit: true,
        validate: {
          isValidate: false,
          message: "",
        },
      };
    case "fail_edit_account":
      return {
        ...state,
        isSuccessEdit: false,
        validate: {
          isValidate: true,
          message: action.data.message,
        },
      };
    default:
      return state;
  }
}
