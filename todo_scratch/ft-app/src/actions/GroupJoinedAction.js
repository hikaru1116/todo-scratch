import { changeSelectedGroup } from "../actions/AuthAction";
import { getJoinedGroupList } from "../repositories/GroupRepository";

export const getJoinedGroup = (dispatch) => {
  getJoinedGroupList().then((groups) => {
    console.log(groups);
    const action = {
      type: "get_joined_group",
      data: groups,
    };

    dispatch(action);
  });
};

export const changeGroup = (dispatch, dispatchAuth, groupId) => {
  console.log("change group!!");
  console.log(groupId);
  const action = {
    type: "change_group",
  };
  dispatch(action);
  changeSelectedGroup(dispatchAuth, groupId);
};
