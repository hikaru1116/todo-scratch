import React, { useEffect, useContext } from "react";
import { GroupSettingsOperateContext } from "../../../contexts/GroupSettingsContext";
import { getGroupInfoAction } from "../../../actions/GroupSettingsAction";
import { UserOperateContext } from "../../../contexts/UserContext";
import GroupSettingsViewDisplay from "./GroupSettingsViewDisplay";
import GroupSettingsEditDisplay from "./GroupSettingsEditDisplay";

const GroupSettingsDisplay = () => {
  const { dispatchGroupSettings, stateGroupSettings } = useContext(
    GroupSettingsOperateContext
  );
  const { stateUser } = useContext(UserOperateContext);

  useEffect(() => {
    if (stateUser.selectedGroup.groupId == null) {
      return;
    }
    getGroupInfoAction(dispatchGroupSettings, stateUser.selectedGroup.groupId);
  }, [stateUser.selectedGroup.groupId, stateGroupSettings.updateCount]);
  return (
    <>
      {!stateGroupSettings.isEdit ? (
        <GroupSettingsViewDisplay />
      ) : (
        <GroupSettingsEditDisplay />
      )}
    </>
  );
};

export default GroupSettingsDisplay;
