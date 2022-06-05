import React, { useContext } from "react";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import BackButton from "../BackButton";
import { signUpAction } from "../../../actions/SignUpAction";
import { SignUpOperateContext } from "../../../contexts/SignUpContext";
import Typography3 from "../Typographies/Typography3";
import { Navigate } from "react-router-dom";

const SignUpDisplay = () => {
  const { stateSignUp, dispatchSignUp } = useContext(SignUpOperateContext);
  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    console.log(`formData.get("userName") ${formData.get("userName")}`);
    console.log(`formData.get("email") ${formData.get("email")}`);
    console.log(`formData.get("password") ${formData.get("password")}`);
    signUpAction(
      dispatchSignUp,
      formData.get("userName"),
      formData.get("email"),
      formData.get("password")
    );
  };

  return stateSignUp.isSignUp ? (
    <Navigate to={"/signin"} />
  ) : (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box mt={3}>
        <BackButton />
      </Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Box component="form" onSubmit={handleSubmit} noValidate>
          {stateSignUp.validate.isValidate && (
            <Typography3 color={"red"}>
              {stateSignUp.validate.message}
            </Typography3>
          )}

          <TextField
            margin="normal"
            required
            fullWidth
            id="userName"
            label="ユーザ名を入力"
            name="userName"
            autoComplete="name"
            autoFocus
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="email"
            label="メールアドレスを入力"
            type="email"
            id="email"
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="パスワードを入力"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 4, mb: 2, color: "#FFFFFF", backgroundColor: "#5CB5A5" }}
          >
            <Typography>Sign Up</Typography>
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default SignUpDisplay;
