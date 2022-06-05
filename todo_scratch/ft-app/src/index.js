import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Navbar from "./view/compornents/Navbar";
import { UserContext } from "./contexts/UserContext";
import { SignInJudgeContext } from "./contexts/SignInJudgeContext";
import ProvateRoute from "./view/compornents/PrivateRoute";
import SignInPage from "./view/pages/SignInPage";
import TaskListPage from "./view/pages/TaskListPage";
import Page404Page from "./view/pages/Page404Page";
import Signing from "./view/pages/Signing";
import GroupSettingsPage from "./view/pages/GroupSettingsPage";
import GroupJoinedListPage from "./view/pages/GroupJoinedListPage";
import GroupCreatePage from "./view/pages/GroupCreatePage";
import GroupApprovalRequestPage from "./view/pages/GroupApprovalRequestPage";
import TaskCreatePage from "./view/pages/TaskCreatePage";
import TaskDetailPage from "./view/pages/TaskDetailPage";
import SignUpPage from "./view/pages/SignUpPage";

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
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 768,
      lg: 1025,
      xl: 1536,
    },
  },
});

root.render(
  <ThemeProvider theme={theme}>
    <UserContext>
      <SignInJudgeContext path={window.location.pathname}>
        <Router>
          <Navbar />
          <Routes>
            <Route
              path="/"
              element={<ProvateRoute element={<TaskListPage />} />}
            />
            <Route
              path="/group-settings"
              element={<ProvateRoute element={<GroupSettingsPage />} />}
            />
            <Route
              path="/group/joined"
              element={<ProvateRoute element={<GroupJoinedListPage />} />}
            />
            <Route
              path="/group/create"
              element={<ProvateRoute element={<GroupCreatePage />} />}
            />
            <Route
              path="/group/approval-request"
              element={<ProvateRoute element={<GroupApprovalRequestPage />} />}
            />
            <Route
              path="/task/create"
              element={<ProvateRoute element={<TaskCreatePage />} />}
            />
            <Route
              exact
              path="/:groupId/task/detail/:taskId"
              element={<ProvateRoute element={<TaskDetailPage />} />}
            />
            <Route path="/signin" element={<SignInPage />} />
            <Route path="/signup" element={<SignUpPage />} />
            <Route path="/signing" element={<Signing />} />
            <Route path="/*" element={<Page404Page />} />
          </Routes>
        </Router>
      </SignInJudgeContext>
    </UserContext>
  </ThemeProvider>
);
