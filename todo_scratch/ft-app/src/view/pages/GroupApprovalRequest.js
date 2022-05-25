import React from "react";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import { GroupApprovalRequestContext } from "../../contexts/GroupApprovalRequestContext";
import GroupApprovalRequestDisplay from "../compornents/GroupApprovalRequestDisplay";

const GroupApprovalRequest = () => {
  return (
    <GroupSettingFrame>
      <GroupApprovalRequestContext>
        <GroupApprovalRequestDisplay />
      </GroupApprovalRequestContext>
    </GroupSettingFrame>
  );
};

export default GroupApprovalRequest;
