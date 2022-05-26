import React, { createContext, useReducer } from "react";
import TaskListReducer from "../reducers/TaskListReducer";

export const TaskListOperateContext = createContext({
  stateTaskList: {},
  dispatch: null,
});

export const initState = {
  taskList: null,
};

export const TaskListContext = ({ children }) => {
  const [stateTaskList, dispatch] = useReducer(TaskListReducer, initState);

  return (
    <TaskListOperateContext.Provider value={{ stateTaskList, dispatch }}>
      {children}
    </TaskListOperateContext.Provider>
  );
};
