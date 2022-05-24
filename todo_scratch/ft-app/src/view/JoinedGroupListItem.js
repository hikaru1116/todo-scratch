import React from "react";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import Box from "@mui/material/Box";
import Typography3 from "./compornents/Typographies/Typography3";
import Grid from "@mui/material/Grid";
import { Button } from "@mui/material";

const JoinedGroupListItem = ({
  group,
  selectedGroupId,
  changeGroupFunction,
}) => {
  const change = () => {
    changeGroupFunction(group.group_id);
  };
  return (
    <React.Fragment key={group.group_id}>
      <ListItem>
        <ListItemText
          primary={
            <Box>
              <Grid
                container
                direction="row"
                justifyContent="space-between"
                alignItems="center"
              >
                <Grid item>
                  <Typography3>{group.group_name}</Typography3>
                </Grid>
                <Grid item>
                  {group.group_id == selectedGroupId ? (
                    <Typography3>Selected</Typography3>
                  ) : (
                    <Button variant="outlined" onClick={change}>
                      <Typography3>Change</Typography3>
                    </Button>
                  )}
                </Grid>
              </Grid>
            </Box>
          }
        />
      </ListItem>
    </React.Fragment>
  );
};

export default JoinedGroupListItem;
