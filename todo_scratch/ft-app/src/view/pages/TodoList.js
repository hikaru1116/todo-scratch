import { Box } from "@mui/material";
import React, { useContext, useEffect } from "react";
import { AuthOperateContext } from "../../contexts/AuthContext";
import Typography3 from "../compornents/Typographies/Typography3";
import { useNavigate } from "react-router-dom";

function TodoList() {
  const { state } = useContext(AuthOperateContext);
  const navigate = useNavigate();

  useEffect(() => {
    console.log(state.selected_group.group_id);
    if (state.selected_group.group_id == null) {
      // グループ設定画面へ遷移
      navigate("/group-settings");
    }
  }, []);
  return (
    <div>
      <Box
        sx={{
          m: "auto",
          width: 300,
          height: 300,
        }}
      >
        <h1>TODO LIST</h1>
        <Typography3>{state.user.user_name}</Typography3>
      </Box>
    </div>
  );
}

export default TodoList;
