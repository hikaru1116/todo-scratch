import React, { useContext } from "react";
import { AuthOperateContext } from "../../contexts/AuthContext";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ element }) => {
  const { state } = useContext(AuthOperateContext);
  const isSingIn = state.user != null;

  if (!state.judgeLogin.isJudgeLogin) {
    return <Navigate to="/signing" />;
  }

  if (isSingIn) {
    return element;
  } else {
    return <Navigate to="/signin" />;
  }
};

export default PrivateRoute;
