import React, { createContext, useReducer, useEffect } from "react";
import AuthReducer from "../reducers/AuthReducer";
import { initUserInfo } from "../actions/AuthAction";

export const TaskListOperateContext = createContext({
  stateTaskList: {},
  dispatch: null,
});

export const initState = {
  taskList: null,
};

export const AuthContext = ({ path, children }) => {
  useEffect(() => {
    initUserInfo(dispatch, path);
  }, []);

  const [stateTaskList, dispatch] = useReducer(AuthReducer, initState);

  return (
    <TaskListOperateContext.Provider value={{ stateTaskList, dispatch }}>
      {children}
    </TaskListOperateContext.Provider>
  );
};
