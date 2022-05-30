import { setSelectedGroup } from "../actions/UserAction";
import { getJoinedGroupList } from "../repositories/GroupRepository";

export const getJoinedGroupAction = (dispatch) => {
  getJoinedGroupList().then((groups) => {
    const action = {
      type: "get_joined_group",
      data: groups,
    };

    dispatch(action);
  });
};

export const changeGroupAction = (dispatch, dispatchUser, groupId) => {
  const action = {
    type: "change_group",
  };
  setSelectedGroup(dispatchUser, groupId);
  dispatch(action);
};
