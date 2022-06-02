import React, { createContext, useReducer } from "react";
import TaskListReducer from "../reducers/TaskListReducer";

export const TaskListOperateContext = createContext({
  stateTaskList: {},
  dispatchTaskList: null,
});

export const initState = {
  taskList: [],
};

export const TaskListContext = ({ children }) => {
  const [stateTaskList, dispatchTaskList] = useReducer(
    TaskListReducer,
    initState
  );

  return (
    <TaskListOperateContext.Provider
      value={{ stateTaskList, dispatchTaskList }}
    >
      {children}
    </TaskListOperateContext.Provider>
  );
};
