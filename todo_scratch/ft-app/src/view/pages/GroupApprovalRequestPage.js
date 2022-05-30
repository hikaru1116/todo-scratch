import React from "react";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import { GroupApprovalRequestContext } from "../../contexts/GroupApprovalRequestContext";
import GroupApprovalRequestDisplay from "../compornents/GroupApprovalRequest/GroupApprovalRequestDisplay";

const GroupApprovalRequestPage = () => {
  return (
    <GroupSettingFrame>
      <GroupApprovalRequestContext>
        <GroupApprovalRequestDisplay />
      </GroupApprovalRequestContext>
    </GroupSettingFrame>
  );
};

export default GroupApprovalRequestPage;
