import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TodoList from "./view/pages/TodoList";
import Page404 from "./view/pages/Page404";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Navbar from "./view/compornents/Navbar";
import SignIn from "./view/pages/SignIn";
import { AuthContext } from "./contexts/AuthContext";
import ProvateRoute from "./view/compornents/PrivateRoute";
import SignUp from "./view/pages/SignUp";
import Account from "./view/pages/Account";
import Signing from "./view/pages/Signing";

const root = ReactDOM.createRoot(document.getElementById("root"));

const theme = createTheme({
  palette: {
    primary: {
      main: "#C4C4C4",
    },
    secondary: {
      main: "#EF7F74",
    },
  },
  typography: {
    fontFamily: "Comic Neue",
  },
});

root.render(
  <ThemeProvider theme={theme}>
    <AuthContext path={location.pathname}>
      <Navbar />
      <Router>
        <Routes>
          <Route path="/" element={<ProvateRoute element={<TodoList />} />} />
          <Route
            path="/account"
            element={<ProvateRoute element={<Account />} />}
          />
          <Route path="/signin" element={<SignIn />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/*" element={<Page404 />} />
          <Route path="/signing" element={<Signing />} />
        </Routes>
      </Router>
    </AuthContext>
  </ThemeProvider>
);
