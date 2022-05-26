import React, { useContext, useEffect } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Typography2 from "../compornents/Typographies/Typography2";
import Typography3 from "../compornents/Typographies/Typography3";
import { GroupApprovalRequestOperateContext } from "../../contexts/GroupApprovalRequestContext";
import List from "@mui/material/List";
import ApprovalRequestGroupListItem from "./ApprovalRequestGroupListItem";
import {
  getApprovalRequestGroupsAction,
  approvalGroupAction,
} from "../../actions/GroupApprovalRequestAction";

const GroupApprovalRequestDisplay = () => {
  const {
    stateGroupApprovalRequest,
    dispatchGroupApprovalRequest,
  } = useContext(GroupApprovalRequestOperateContext);

  useEffect(() => {
    console.log(stateGroupApprovalRequest.requestCount);
    getApprovalRequestGroupsAction(dispatchGroupApprovalRequest);
  }, [stateGroupApprovalRequest.requestCount]);

  const requestApproval = (groupId) => {
    approvalGroupAction(dispatchGroupApprovalRequest, groupId);
  };

  return (
    <>
      <Grid container direction="column" spacing={3.5} mt={2}>
        <Grid item>
          <Typography2>参加承認依頼グループ</Typography2>
        </Grid>
        <Grid item>
          <Box sx={{ color: "#c4c4c4" }}>
            <Box border={1} sx={{ borderRadius: "16px" }} p={2}>
              {stateGroupApprovalRequest.approvalRequestGroups.length > 0 ? (
                <List>
                  {stateGroupApprovalRequest.approvalRequestGroups.map(
                    (group) => (
                      <ApprovalRequestGroupListItem
                        key={group.group_id}
                        group={group}
                        requestApproval={requestApproval}
                      />
                    )
                  )}
                </List>
              ) : (
                <Box>
                  <Typography3 color={"#c4c4c4"}>
                    参加承認依頼のあるグループはありません
                  </Typography3>
                </Box>
              )}
            </Box>
          </Box>
        </Grid>
      </Grid>
    </>
  );
};

export default GroupApprovalRequestDisplay;
