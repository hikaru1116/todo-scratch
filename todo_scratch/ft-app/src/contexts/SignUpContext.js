import React, { createContext, useReducer } from "react";
import SignUpReducer from "../reducers/SignUpReducer";

export const SignUpOperateContext = createContext({
  stateSignUp: {},
  dispatchSignUp: null,
});

export const initState = {
  isSignUp: false,
  validate: {
    isValidate: false,
    message: "",
  },
};

export const SignUpContext = ({ children }) => {
  const [stateSignUp, dispatchSignUp] = useReducer(SignUpReducer, initState);
  return (
    <SignUpOperateContext.Provider value={{ stateSignUp, dispatchSignUp }}>
      {children}
    </SignUpOperateContext.Provider>
  );
};
