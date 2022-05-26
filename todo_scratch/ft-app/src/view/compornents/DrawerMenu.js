import React, { useContext } from "react";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import { Link, useNavigate } from "react-router-dom";
import Button from "@mui/material/Button";
import LogoutIcon from "@mui/icons-material/Logout";
import { AuthOperateContext } from "../../contexts/AuthContext";
import { signOutAction } from "../../actions/AuthAction";

const DrawerMenu = ({ user_name }) => {
  const { dispatch } = useContext(AuthOperateContext);

  const navigate = useNavigate();

  const signOut = () => {
    signOutAction(dispatch, navigate);
  };

  return (
    <div>
      <Box borderBottom={1} borderColor="primary.main">
        <Grid
          container
          direction="column"
          justifyContent="center"
          alignItems="center"
        >
          <Grid item>
            <Box>
              <Box
                borderBottom={1}
                borderColor="primary.main"
                pl={2}
                pr={2}
                pb={1}
                mt={2}
                mb={2}
              >
                <Typography>グループを選択</Typography>
              </Box>
            </Box>
          </Grid>
          <Grid item>
            <Box mb={2}>
              <Grid
                container
                direction="row"
                justifyContent="center"
                alignItems="center"
                rowSpacing={1}
              >
                <AccountCircleIcon />
                <Typography ml={0.5}>{user_name}</Typography>
              </Grid>
            </Box>
          </Grid>
        </Grid>
      </Box>
      <Box>
        <Grid
          mt={2}
          spacing={2.5}
          container
          direction="column"
          justifyContent="center"
          alignItems="center"
        >
          <Grid item>
            <Link to="/" style={{ textDecoration: "none" }}>
              <Typography>Todo List</Typography>
            </Link>
          </Grid>
          <Grid item>
            <Link to="/account" style={{ textDecoration: "none" }}>
              <Typography>Account</Typography>
            </Link>
          </Grid>
          <Grid item>
            <Link to="/group-settings" style={{ textDecoration: "none" }}>
              <Typography>Group Setting</Typography>
            </Link>
          </Grid>
          <Grid item>
            <Button
              variant="outlined"
              startIcon={<LogoutIcon />}
              onClick={signOut}
            >
              Log Out
            </Button>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
};

export default DrawerMenu;
