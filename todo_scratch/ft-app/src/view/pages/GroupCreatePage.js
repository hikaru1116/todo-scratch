import React from "react";
import { GroupCreateContext } from "../../contexts/GroupCreateContext";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import GroupCreateDisplay from "../compornents/GroupCreate/GroupCreateDisplay";

const GroupCreatePage = () => {
  return (
    <GroupSettingFrame>
      <GroupCreateContext>
        <GroupCreateDisplay />
      </GroupCreateContext>
    </GroupSettingFrame>
  );
};

export default GroupCreatePage;
