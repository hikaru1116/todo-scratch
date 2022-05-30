import React, { useContext } from "react";
import CircularProgress from "@mui/material/CircularProgress";
import { SignInJudgeOperateContext } from "../../contexts/SignInJudgeContext";
import { Navigate } from "react-router-dom";
import Box from "@mui/material/Box";

const Signing = () => {
  const { stateSignInJudge } = useContext(SignInJudgeOperateContext);

  if (!stateSignInJudge.doneJudge) {
    // ログイン判定前画面の表示
    return (
      <div>
        <Box sx={{ m: "auto" }}>
          <CircularProgress />
        </Box>
      </div>
    );
  }

  // アクセス先ページへ遷移
  return <Navigate to={stateSignInJudge.path} />;
};

export default Signing;
