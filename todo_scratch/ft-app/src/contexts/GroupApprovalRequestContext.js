import React, { createContext, useReducer } from "react";
import GroupApprovalRequestReducer from "../reducers/GroupApprovalRequestReducer";

export const GroupApprovalRequestOperateContext = createContext({
  stateGroupApprovalRequest: {},
  dispatchGroupApprovalRequest: null,
});

export const initState = {
  approvalRequestGroups: [],
  requestCount: 0,
};

export const GroupApprovalRequestContext = ({ children }) => {
  const [stateGroupApprovalRequest, dispatchGroupApprovalRequest] = useReducer(
    GroupApprovalRequestReducer,
    initState
  );

  return (
    <GroupApprovalRequestOperateContext.Provider
      value={{ stateGroupApprovalRequest, dispatchGroupApprovalRequest }}
    >
      {children}
    </GroupApprovalRequestOperateContext.Provider>
  );
};
