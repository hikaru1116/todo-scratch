import { getApprovalRequestGroupList } from "../repositories/GroupRepository";
import { postApprovalRequest } from "../repositories/GroupRepository";

export const getRequestApprovalGroup = (dispatch) => {
  console.log("hakka");
  getApprovalRequestGroupList().then((groups) => {
    console.log(groups);
    const action = {
      type: "get_approval_request_group",
      data: groups,
    };

    dispatch(action);
  });
};

export const requestApprovalGroup = (dispatch, groupId) => {
  postApprovalRequest(groupId).then((data) => {
    console.log(data);
    if (data == null) {
      const action = {
        type: "fail_request_approval",
      };
      dispatch(action);
    } else {
      const action = {
        type: "success_request_approval",
      };
      dispatch(action);
    }
  });
};
