import React, { createContext, useReducer } from "react";
import GroupJoinedReducer from "../reducers/GroupJoinedReducer";

export const GroupJoinedOperateContext = createContext({
  stateGroupjoined: {},
  dispatchGroupJoined: null,
});

export const groupJoinedInitStste = {
  joinedGroups: [],
  toPath: null,
};

export const GroupjoinedContext = ({ children }) => {
  const [stateGroupjoined, dispatchGroupJoined] = useReducer(
    GroupJoinedReducer,
    groupJoinedInitStste
  );

  return (
    <GroupJoinedOperateContext.Provider
      value={{ stateGroupjoined, dispatchGroupJoined }}
    >
      {children}
    </GroupJoinedOperateContext.Provider>
  );
};
