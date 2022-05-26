import React, { createContext, useReducer, useEffect } from "react";
import AuthReducer from "../reducers/AuthReducer";
import { initUserInfoAction } from "../actions/AuthAction";

export const AuthOperateContext = createContext({
  state: {},
  dispatch: null,
});

export const initState = {
  user: null,
  selected_group: {
    group_id: null,
  },
  isLoading: false,
  validate: {
    isValidate: false,
    message: "",
  },
  judgeLogin: {
    isJudgeLogin: false,
    toPath: "",
  },
};

export const AuthContext = ({ path, children }) => {
  useEffect(() => {
    initUserInfoAction(dispatch, path);
  }, []);

  const [state, dispatch] = useReducer(AuthReducer, initState);

  return (
    <AuthOperateContext.Provider value={{ state, dispatch }}>
      {children}
    </AuthOperateContext.Provider>
  );
};
