import React, { createContext, useReducer } from "react";
import GroupJoinedReducer from "../reducers/GroupJoinedReducer";

export const GroupJoinedOperateContext = createContext({
  stateGroupjoined: {},
  dispatchGroupJoined: null,
});

export const initState = {
  joinedGroups: [],
  toPath: null,
};

export const GroupjoinedContext = ({ children }) => {
  const [stateGroupjoined, dispatchGroupJoined] = useReducer(
    GroupJoinedReducer,
    initState
  );

  return (
    <GroupJoinedOperateContext.Provider
      value={{ stateGroupjoined, dispatchGroupJoined }}
    >
      {children}
    </GroupJoinedOperateContext.Provider>
  );
};
