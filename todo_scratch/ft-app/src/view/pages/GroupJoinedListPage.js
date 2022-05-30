import React from "react";
import GroupSettingFrame from "../compornents/GroupSettingFrame";
import { GroupjoinedContext } from "../../contexts/GroupJoinedContext";
import GroupJoinedListDisplay from "../compornents/GroupJoinedList/GroupJoinedListDisplay";

const GroupJoinedListPage = () => {
  return (
    <GroupSettingFrame>
      <GroupjoinedContext>
        <GroupJoinedListDisplay />
      </GroupjoinedContext>
    </GroupSettingFrame>
  );
};

export default GroupJoinedListPage;
