import { changeSelectedGroupAction } from "../actions/AuthAction";
import { getJoinedGroupList } from "../repositories/GroupRepository";

export const getJoinedGroupAction = (dispatch) => {
  getJoinedGroupList().then((groups) => {
    console.log(groups);
    const action = {
      type: "get_joined_group",
      data: groups,
    };

    dispatch(action);
  });
};

export const changeGroupAction = (dispatch, dispatchAuth, groupId) => {
  console.log("change group!!");
  console.log(groupId);
  const action = {
    type: "change_group",
  };
  dispatch(action);
  changeSelectedGroupAction(dispatchAuth, groupId);
};
