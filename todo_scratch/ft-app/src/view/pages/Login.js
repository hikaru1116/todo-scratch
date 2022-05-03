import React, { useReducer } from "react";
import { LoginContext } from "../../contexts/LoginContext";
import { LoginReducer } from "../../reducers/LoginReducer";
import LoginForm from "../compornents/LoginForm";

const initialState = {
  title: "login form",
  value: 0,
};

const Login = () => {
  const [state, dispatch] = useReducer(LoginReducer, initialState);

  return (
    <LoginContext.Provider value={{ state, dispatch }}>
      <div>
        <h4>COUNT:{state.value}</h4>
        <LoginForm />
      </div>
    </LoginContext.Provider>
  );
};

export default Login;
