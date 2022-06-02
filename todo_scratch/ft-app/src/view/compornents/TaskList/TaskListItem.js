import React from "react";
import ListItem from "@mui/material/ListItem";
import Typography3 from "./../Typographies/Typography3";
import Typography4 from "./../Typographies/Typography4";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import UpdateIcon from "@mui/icons-material/Update";
import AccessTimeIcon from "@mui/icons-material/AccessTime";

const TaskListItem = ({ key, task, statusColor }) => {
  return (
    <ListItem key={key} onClick={() => console.log(task.title)}>
      <Box border={0.5} borderColor={"#C4C4C4"} sx={{ width: "100%" }}>
        <Grid container direction="row">
          <Grid item xs={1}>
            <Box sx={{ backgroundColor: statusColor, height: "100%" }} />
          </Grid>
          <Grid item xs={11}>
            <Box p={0.5}>
              <Grid container direction="row" alignItems={"center"}>
                <Grid item xs={12}>
                  <Box mb={2} mt={1}>
                    <Typography3 fontWeight={"bold"}>{task.title}</Typography3>
                  </Box>
                </Grid>
                <Grid item xs={12} sm={8}>
                  <Box>
                    <Grid container direction="row" alignItems={"center"}>
                      <Grid item>
                        <AccountCircleIcon />
                      </Grid>
                      <Grid item>
                        <Typography3>{task.user_name}</Typography3>
                      </Grid>
                    </Grid>
                  </Box>
                </Grid>
                <Grid item xs={12} sm={4}>
                  <Box
                    mt={1}
                    p={0.2}
                    sx={{
                      borderRadius: "16px",
                      backgroundColor: task.is_expired
                        ? "#FF6464"
                        : (theme) => theme.palette.primary.main,
                    }}
                  >
                    <Grid
                      container
                      direction="row"
                      alignItems={"center"}
                      justifyContent="center"
                    >
                      <Grid item>
                        <AccessTimeIcon />
                      </Grid>
                      <Grid item>
                        <Typography4 align={"right"}>
                          {task.deadline_at}
                        </Typography4>
                      </Grid>
                    </Grid>
                  </Box>
                </Grid>
              </Grid>
            </Box>
          </Grid>
        </Grid>
      </Box>
    </ListItem>
  );
};

export default TaskListItem;
