import React from "react";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import { GroupjoinedContext } from "../../contexts/GroupJoinedContext";
import GroupJoinedListDisplay from "../compornents/GroupJoinedListDisplay";

const GroupJoinedList = () => {
  return (
    <GroupSettingFrame>
      <GroupjoinedContext>
        <GroupJoinedListDisplay />
      </GroupjoinedContext>
    </GroupSettingFrame>
  );
};

export default GroupJoinedList;
