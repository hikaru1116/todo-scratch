import React from "react";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";

const SignUp = () => {
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
        <Box
          component="form"
          onSubmit={() => console.log("submit")}
          noValidate
          sx={{ mt: 1 }}
        >
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            label="ユーザ名を入力"
            name="email"
            autoComplete="email"
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
          <Button
            type="submit"
            fullWidth
            variant="outlined"
            sx={{ mt: 2, mb: 2 }}
            href="/signin"
          >
            <Typography
              sx={{
                color: "#C4C4C4",
              }}
            >
              Back
            </Typography>
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default SignUp;
