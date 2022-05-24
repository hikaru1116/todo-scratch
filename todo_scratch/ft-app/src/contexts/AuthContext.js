import React, { createContext, useReducer, useEffect } from "react";
import AuthReducer from "../reducers/AuthReducer";
import { initUserInfo } from "../actions/AuthAction";

export const AuthOperateContext = createContext({
  state: {},
  dispatch: null,
});

export const authInitState = {
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
    initUserInfo(dispatch, path);
  }, []);

  const [state, dispatch] = useReducer(AuthReducer, authInitState);

  return (
    <AuthOperateContext.Provider value={{ state, dispatch }}>
      {children}
    </AuthOperateContext.Provider>
  );
};
