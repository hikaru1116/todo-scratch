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
import GroupSettings from "./view/pages/GroupSettings";
import GroupCreate from "./view/pages/GroupCreate";
import GroupJoinedList from "./view/pages/GroupJoinedList";

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
    color: "#111111",
  },
});

root.render(
  <ThemeProvider theme={theme}>
    <AuthContext path={location.pathname}>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<ProvateRoute element={<TodoList />} />} />
          <Route
            path="/account"
            element={<ProvateRoute element={<Account />} />}
          />
          <Route
            path="/group-settings"
            element={<ProvateRoute element={<GroupSettings />} />}
          />
          <Route
            path="/group/create"
            element={<ProvateRoute element={<GroupCreate />} />}
          />
          <Route
            path="/group/joined"
            element={<ProvateRoute element={<GroupJoinedList />} />}
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
