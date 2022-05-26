import { postGroup } from "../repositories/GroupRepository";
import { changeSelectedGroupAction } from "../actions/AuthAction";

export const createGroupAction = (
  dispatch,
  dispatchAuth,
  groupName,
  description,
  adUserList
) => {
  // 入力値のバリデーション
  if (groupName == null || groupName.length <= 0) {
    const action = {
      type: "validate",
      data: "グループ名が空白です。",
    };
    dispatch(action);
    return;
  }
  if (description == null || description.length <= 0) {
    const action = {
      type: "validate",
      data: "グループの説明が空白です。",
    };
    dispatch(action);
    return;
  }

  const inviteUsers = [];
  adUserList.map((data) => {
    inviteUsers.push({
      identifier: data.identifer,
    });
  });
  const createGroupInfo = {
    group_name: groupName,
    description: description,
    invite_users: inviteUsers,
  };

  postGroup(createGroupInfo).then((data) => {
    if (data != null) {
      changeSelectedGroupAction(dispatchAuth, data.group_id);

      const action = {
        type: "create_group_success",
      };
      dispatch(action);
    } else {
      const action = {
        type: "create_group_fail",
        data: "グループ新規作成に失敗しました",
      };
      dispatch(action);
    }
  });
};
