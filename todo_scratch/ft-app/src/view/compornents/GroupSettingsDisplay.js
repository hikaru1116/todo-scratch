import React, { useEffect, useContext } from "react";
import { GroupSettingsOperateContext } from "../../contexts/GroupSettingsContext";
import { getGroupInfoAction } from "../../actions/GroupSettingsAction";
import { AuthOperateContext } from "../../contexts/AuthContext";
import GroupSettingsViewDisplay from "./GroupSettingsViewDisplay";
import GroupSettingsEditDisplay from "./GroupSettingsEditDisplay";

const GroupSettingsDisplay = () => {
  const { dispatchGroupSettings, stateGroupSettings } = useContext(
    GroupSettingsOperateContext
  );
  const { state } = useContext(AuthOperateContext);

  useEffect(() => {
    if (state.selected_group.group_id == null) {
      return;
    }
    getGroupInfoAction(dispatchGroupSettings, state.selected_group.group_id);
  }, []);

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
