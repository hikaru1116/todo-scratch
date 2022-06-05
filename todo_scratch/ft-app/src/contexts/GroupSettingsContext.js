import React, { createContext, useReducer } from "react";
import GroupSettingsReducer from "../reducers/GroupSettingsReducer";

export const GroupSettingsOperateContext = createContext({
  stateGroupSettings: {},
  dispatchGroupSettings: null,
});

export const initState = {
  groupId: null,
  groupName: null,
  description: null,
  users: [],
  isEdit: false,
  updateCount: 0,
  validate: {
    isValidate: false,
    message: "",
  },
};

export const GroupSettingsContext = ({ children }) => {
  const [stateGroupSettings, dispatchGroupSettings] = useReducer(
    GroupSettingsReducer,
    initState
  );

  return (
    <GroupSettingsOperateContext.Provider
      value={{ stateGroupSettings, dispatchGroupSettings }}
    >
      {children}
    </GroupSettingsOperateContext.Provider>
  );
};
