import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TodoList from "./view/pages/TodoList";
import Login from "./view/pages/Login";
import Page404 from "./view/pages/Page404";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { amber } from "@mui/material/colors";
import Navbar from "./view/compornents/Navbar";

const root = ReactDOM.createRoot(document.getElementById("root"));

const theme = createTheme({
  palette: {
    primary: amber,
    secondary: {
      main: "#f44336",
    },
  },
  typography: {
    fontFamily: "Comic Neue",
  },
});

root.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <Navbar />
      <Router>
        <Routes>
          <Route path="/" element={<TodoList />} />
          <Route path="/login" element={<Login />} />
          <Route path="/*" element={<Page404 />} />
        </Routes>
      </Router>
    </ThemeProvider>
  </React.StrictMode>
);
