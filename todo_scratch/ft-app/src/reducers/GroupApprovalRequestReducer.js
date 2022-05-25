export default function GroupApprovalRequestReducer(state, action) {
  switch (action.type) {
    case "get_approval_request_group":
      return {
        ...state,
        approvalRequestGroups: action.data,
      };
    case "success_request_approval":
      return {
        ...state,
        requestCount: state.requestCount + 1,
      };
    case "fail_request_approval":
      return state;
    default:
      return state;
  }
}
