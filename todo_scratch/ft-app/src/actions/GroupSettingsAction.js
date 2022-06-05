import { getGroupById, putGroup } from "../repositories/GroupRepository";

export const getGroupInfoAction = (dispatch, groupId) => {
  getGroupById(groupId).then((data) => {
    const action = {
      type: "get_group_info",
      groupId: data.group_id,
      groupName: data.group_name,
      description: data.description,
      users: data.users,
    };
    dispatch(action);
  });
};

export const putGroupInfoAction = (
  dispatch,
  groupId,
  groupName,
  description,
  updateUserList,
  addUserList
) => {
  const group = {
    group_name: groupName,
    description: description,
    update_users: updateUserList,
    add_users: addUserList,
  };

  putGroup(groupId, group).then((isSuccess) => {
    const action = {
      type: "put_group",
    };
    dispatch(action);
  });
};

export const toEditStateAction = (dispatch) => {
  const action = {
    type: "to_edit_state",
  };
  dispatch(action);
};

export const toViewStateAction = (dispatch) => {
  const action = {
    type: "to_view_state",
  };
  dispatch(action);
};
