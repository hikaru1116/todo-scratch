import {
  getSelectedGroupId,
  setSelectedGroupId,
} from "../utils/SelectedGroupStorage";
import { getTaskStatusInfoByGroupId } from "../repositories/GroupRepository";
import { setIsLogin } from "../utils/UserStorage";
import { postSingOut } from "../repositories/LoginRepository";

export const setUserDataAction = async (dispatch, user) => {
  const selectedGroupId = getSelectedGroupId();

  if (selectedGroupId === null || selectedGroupId == "null") {
    const action = {
      type: "set_user_data",
      data: {
        user: user,
        selectedGroup: {
          groupId: null,
          taskStatusList: [],
        },
      },
    };
    dispatch(action);
    return;
  }

  // タスクステータス情報の同期
  getTaskStatusInfoByGroupId(selectedGroupId).then((taskStatusList) => {
    const action = {
      type: "set_user_data",
      data: {
        user: user,
        selectedGroup: {
          groupId: selectedGroupId,
          taskStatusList: taskStatusList,
        },
      },
    };
    dispatch(action);
  });
};

export const clearUserDataAction = (dispatch) => {
  postSingOut().then(() => {
    setIsLogin(false);
    setSelectedGroupId(null);
    const action = {
      type: "clear_user_data",
    };
    dispatch(action);
  });
};

export const setSelectedGroup = (dispatch, groupId) => {
  getTaskStatusInfoByGroupId(groupId).then((taskStatusList) => {
    setSelectedGroupId(groupId);
    const action = {
      type: "set_selected_group",
      data: {
        selectedGroup: {
          groupId: groupId,
          taskStatusList: taskStatusList,
        },
      },
    };
    dispatch(action);
  });
};
