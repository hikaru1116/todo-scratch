import { getGroupById } from "../repositories/GroupRepository";

export const getGroupInfoAction = (dispatch, group_id) => {
  getGroupById(group_id).then((data) => {
    const action = {
      type: "get_group_info",
      group_id: data.group_id,
      group_name: data.group_name,
      description: data.description,
      users: data.users,
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
