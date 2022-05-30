import React from "react";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import { GroupSettingsContext } from "../../contexts/GroupSettingsContext";
import GroupSettingsDisplay from "../compornents/GroupSettings/GroupSettingsDisplay";

const GroupSettingsPage = () => {
  return (
    <GroupSettingFrame>
      <GroupSettingsContext>
        <GroupSettingsDisplay />
      </GroupSettingsContext>
    </GroupSettingFrame>
  );
};

export default GroupSettingsPage;
