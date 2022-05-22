import { Box } from "@mui/material";
import React from "react";
// import { AuthOperateContext } from "../../contexts/AuthContext";
import { Link } from "react-router-dom";

function TodoList() {
  // const { state } = useContext(AuthOperateContext);
  console.log("todo list");
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
        <Link to="/account">アカウント</Link>
      </Box>
    </div>
  );
}

export default TodoList;
