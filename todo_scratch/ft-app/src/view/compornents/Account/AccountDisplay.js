import React, { useState, useContext, useEffect } from "react";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Typography3 from "../Typographies/Typography3";
import { editAccountAction } from "../../../actions/AccountAction";
import { AccountOperateContext } from "../../../contexts/AccountContext";
import { UserOperateContext } from "../../../contexts/UserContext";
import Typography2 from "../Typographies/Typography2";

const AccountDisplay = () => {
  const { stateAccount, dispatchAccount } = useContext(AccountOperateContext);
  const { stateUser } = useContext(UserOperateContext);

  const [userName, setUserName] = useState("");
  const [email, setEmail] = useState("");

  const submit = () => {
    editAccountAction(dispatchAccount, userName, email);
  };

  useEffect(() => {
    if (!stateUser.user) {
      return;
    }
    setUserName(stateUser.user.user_name);
    setEmail(stateUser.user.email);
  }, [stateUser.user]);

  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        mt={4}
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Box>
          <Box mb={3}>
            <Typography2>アカウント情報</Typography2>
          </Box>

          {stateAccount.isSuccessEdit && (
            <Typography3 color={"#5CB5A5"}>更新しました</Typography3>
          )}
          {stateAccount.validate.isValidate && (
            <Typography3 color={"red"}>
              {stateAccount.validate.message}
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
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="email"
            label="メールアドレスを入力"
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <Button
            type="submit"
            fullWidth
            onClick={submit}
            variant="contained"
            sx={{ mt: 4, mb: 2, color: "#FFFFFF", backgroundColor: "#5CB5A5" }}
          >
            <Typography>Update</Typography>
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default AccountDisplay;
