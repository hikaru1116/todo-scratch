import React from "react";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import GroupSettingsDisplay from "../compornents/GroupSettingsDisplay";
import { GroupSettingsContext } from "../../contexts/GroupSettingsContext";

const GroupSettings = () => {
  return (
    <GroupSettingFrame>
      <GroupSettingsContext>
        <GroupSettingsDisplay />
      </GroupSettingsContext>
    </GroupSettingFrame>
  );
};

export default GroupSettings;
