import React, { createContext, useReducer } from "react";
import AccountReducer from "../reducers/AccountReducer";

export const AccountOperateContext = createContext({
  stateAccount: {},
  dispatchAccount: null,
});

export const initState = {
  isSuccessEdit: false,
  validate: {
    isValidate: false,
    message: "",
  },
};

export const AccountContext = ({ children }) => {
  const [stateAccount, dispatchAccount] = useReducer(AccountReducer, initState);
  return (
    <AccountOperateContext.Provider value={{ stateAccount, dispatchAccount }}>
      {children}
    </AccountOperateContext.Provider>
  );
};
