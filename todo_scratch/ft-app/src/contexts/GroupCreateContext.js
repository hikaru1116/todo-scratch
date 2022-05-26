import React, { createContext, useReducer } from "react";
import GroupCreateReducer from "../reducers/GroupCreateReducer";

export const GroupCreateOperateContext = createContext({
  stateGroupCreate: {},
  dispatchGroupCreate: null,
});

export const initState = {
  validate: {
    isValidate: false,
    message: "",
  },
  toPath: null,
};

export const GroupCreateContext = ({ children }) => {
  const [stateGroupCreate, dispatchGroupCreate] = useReducer(
    GroupCreateReducer,
    initState
  );

  return (
    <GroupCreateOperateContext.Provider
      value={{ stateGroupCreate, dispatchGroupCreate }}
    >
      {children}
    </GroupCreateOperateContext.Provider>
  );
};
