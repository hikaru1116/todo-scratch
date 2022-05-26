import React, { createContext, useReducer } from "react";
import GroupSettingsReducer from "../reducers/GroupSettingsReducer";

export const GroupSettingsOperateContext = createContext({
  stateGroupSettings: {},
  dispatchGroupSettings: null,
});

export const groupSettingsInitStste = {
  group_id: null,
  group_name: null,
  description: null,
  users: [],
  isEdit: false,
};

export const GroupSettingsContext = ({ children }) => {
  const [stateGroupSettings, dispatchGroupSettings] = useReducer(
    GroupSettingsReducer,
    groupSettingsInitStste
  );

  return (
    <GroupSettingsOperateContext.Provider
      value={{ stateGroupSettings, dispatchGroupSettings }}
    >
      {children}
    </GroupSettingsOperateContext.Provider>
  );
};