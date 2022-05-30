import React, { createContext, useReducer } from "react";
import TaskCreateReducer from "../reducers/TaskCreateReducer";

export const TaskCreateOperateContext = createContext({
  stateTaskCreate: {},
  dispatchTaskCreate: null,
});

export const initState = {
  toPath: null,
  validate: {
    isValidate: false,
    message: "",
  },
};

export const TaskCreateContext = ({ children }) => {
  const [stateTaskCreate, dispatchTaskCreate] = useReducer(
    TaskCreateReducer,
    initState
  );

  return (
    <TaskCreateOperateContext.Provider
      value={{ stateTaskCreate, dispatchTaskCreate }}
    >
      {children}
    </TaskCreateOperateContext.Provider>
  );
};
