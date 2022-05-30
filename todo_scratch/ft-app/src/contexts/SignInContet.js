import React, { createContext, useReducer } from "react";
import SingInReducer from "../reducers/SingInReducer";

export const SignInOperateContext = createContext({
  stateSignIn: {},
  dispatchSignIn: null,
});

export const initState = {
  isSignIn: false,
  isLoading: false,
  validate: {
    isValidate: false,
    message: "",
  },
};

export const SingInContext = ({ children }) => {
  const [stateSignIn, dispatchSignIn] = useReducer(SingInReducer, initState);
  return (
    <SignInOperateContext.Provider value={{ stateSignIn, dispatchSignIn }}>
      {children}
    </SignInOperateContext.Provider>
  );
};
