import React, { useContext } from "react";
import { SignInJudgeOperateContext } from "../../contexts/SignInJudgeContext";
import { Navigate } from "react-router-dom";

const PrivateRoute = ({ element }) => {
  const { stateSignInJudge } = useContext(SignInJudgeOperateContext);
  if (!stateSignInJudge.doneJudge) {
    return <Navigate to="/signing" />;
  }

  if (stateSignInJudge.isJudgeSingIn) {
    return element;
  } else {
    return <Navigate to="/signin" />;
  }
};

export default PrivateRoute;
