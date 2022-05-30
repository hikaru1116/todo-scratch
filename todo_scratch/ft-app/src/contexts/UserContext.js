import React, { createContext, useReducer } from "react";
import UserReducer from "../reducers/UserReducer";

export const UserOperateContext = createContext({
  stateUser: {},
  dispatchUser: null,
});

export const initState = {
  user: null,
  selectedGroup: {
    groupId: null,
    taskStatusList: [],
  },
};

export const UserContext = ({ children }) => {
  const [stateUser, dispatchUser] = useReducer(UserReducer, initState);

  return (
    <UserOperateContext.Provider value={{ stateUser, dispatchUser }}>
      {children}
    </UserOperateContext.Provider>
  );
};
