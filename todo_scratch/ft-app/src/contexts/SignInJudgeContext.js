import React, { createContext, useReducer, useEffect, useContext } from "react";
import { UserOperateContext } from "./UserContext";
import SignInJudgeReducer from "../reducers/SignInJudgeReducer";
import { judgeSingInAction } from "../actions/SignInJudgeAction";

export const SignInJudgeOperateContext = createContext({
  stateSignInJudge: {},
  dispatchSignInJudge: null,
});

export const initState = {
  doneJudge: false,
  isJudgeSingIn: false,
  path: null,
};

export const SignInJudgeContext = ({ path, children }) => {
  const { dispatchUser } = useContext(UserOperateContext);

  useEffect(() => {
    judgeSingInAction(dispatchSignInJudge, dispatchUser, path);
  }, []);

  const [stateSignInJudge, dispatchSignInJudge] = useReducer(
    SignInJudgeReducer,
    initState
  );

  return (
    <SignInJudgeOperateContext.Provider
      value={{ stateSignInJudge, dispatchSignInJudge }}
    >
      {children}
    </SignInJudgeOperateContext.Provider>
  );
};
