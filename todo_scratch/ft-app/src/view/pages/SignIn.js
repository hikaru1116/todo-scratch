import React, { useContext } from "react";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import { AuthOperateContext } from "../../contexts/AuthContext";
import { singIn } from "../../actions/AuthAction";
import { Navigate } from "react-router-dom";
import LoadingButton from "@mui/lab/LoadingButton";

export default function SignIn() {
  const { state, dispatch } = useContext(AuthOperateContext);

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    singIn(dispatch, formData.get("identifier"), formData.get("password"));
  };

  return state.user ? (
    <Navigate to="/" />
  ) : (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          {state.validate.isValidate && (
            <Typography sx={{ color: "red" }}>
              {state.validate.message}
            </Typography>
          )}
          <TextField
            margin="normal"
            required
            fullWidth
            id="identifier"
            label="ユーザ名または、メールアドレス"
            name="identifier"
            autoComplete="identifier"
            autoFocus
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="パスワード"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          {state.isLoading ? (
            <LoadingButton
              loading
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 4, mb: 2 }}
            >
              <Typography>Sign In</Typography>
            </LoadingButton>
          ) : (
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 4, mb: 2 }}
            >
              <Typography>Sign In</Typography>
            </Button>
          )}
        </Box>
        <Button
          type="submit"
          fullWidth
          variant="outlined"
          sx={{ mt: 2, mb: 2 }}
          href="/signup"
        >
          <Typography
            sx={{
              color: "#C4C4C4",
            }}
          >
            Sign Up
          </Typography>
        </Button>
      </Box>
    </Container>
  );
}
