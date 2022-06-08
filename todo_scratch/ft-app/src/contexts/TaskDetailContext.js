import React, { createContext, useReducer } from "react";
import TaskDetailReducer from "../reducers/TaskDetailReducer";

export const TaskDetailOperateContext = createContext({
  stateTaskDetail: {},
  dispatchTaskDetail: null,
});

export const initState = {
  taskId: null,
  task: {
    taskId: null,
    groupId: null,
    userId: null,
    userName: null,
    title: null,
    context: null,
    deadlineAt: null,
    taskStatusId: null,
    history: [],
  },
  isEdit: false,
  validate: {
    isValidate: false,
    message: "",
  },
  taskStateChangeCount: 0,
};

export const TaskDetailContext = ({ children }) => {
  const [stateTaskDetail, dispatchTaskDetail] = useReducer(
    TaskDetailReducer,
    initState
  );

  return (
    <TaskDetailOperateContext.Provider
      value={{ stateTaskDetail, dispatchTaskDetail }}
    >
      {children}
    </TaskDetailOperateContext.Provider>
  );
};
