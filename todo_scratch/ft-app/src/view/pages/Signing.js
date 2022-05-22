import React, { useContext } from "react";
import CircularProgress from "@mui/material/CircularProgress";
import { AuthOperateContext } from "../../contexts/AuthContext";
import { Navigate } from "react-router-dom";
import Box from "@mui/material/Box";

const Signing = () => {
  const { state } = useContext(AuthOperateContext);
  if (!state.judgeLogin.isJudgeLogin) {
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
  return <Navigate to={state.judgeLogin.toPath} />;
};

export default Signing;
