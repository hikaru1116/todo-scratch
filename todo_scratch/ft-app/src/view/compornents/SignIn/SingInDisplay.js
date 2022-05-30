import React, { useContext } from "react";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import { SignInOperateContext } from "../../../contexts/SignInContet";
import { useNavigate } from "react-router-dom";
import LoadingButton from "@mui/lab/LoadingButton";
import { UserOperateContext } from "../../../contexts/UserContext";
import { signInAction } from "../../../actions/SignInAction";
import { SignInJudgeOperateContext } from "../../../contexts/SignInJudgeContext";

const SingInDisplay = () => {
  const { dispatchSignIn, stateSignIn } = useContext(SignInOperateContext);
  const { dispatchUser } = useContext(UserOperateContext);
  const { dispatchSignInJudge } = useContext(SignInJudgeOperateContext);

  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    signInAction(
      dispatchSignIn,
      dispatchUser,
      dispatchSignInJudge,
      navigate,
      formData.get("identifier"),
      formData.get("password")
    );
  };

  return (
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
          {stateSignIn.validate.isValidate && (
            <Typography sx={{ color: "red" }}>
              {stateSignIn.validate.message}
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
          {stateSignIn.isLoading ? (
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
};

export default SingInDisplay;
