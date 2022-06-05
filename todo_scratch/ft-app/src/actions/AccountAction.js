import { putAccount } from "../repositories/AccountRepository";

export const editAccountAction = (dispatch, userName, email) => {
  // 入力値のバリデーション
  if (
    userName == null ||
    userName.length <= 0 ||
    email == null ||
    email.length <= 0
  ) {
    const action = {
      type: "fail_edit_account",
      data: {
        message:
          "ユーザ名、メールアドレスのいずれかが空白です。入力してください",
      },
    };
    dispatch(action);
    return;
  }

  const regex =
    /^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/;

  if (!regex.test(email)) {
    const action = {
      type: "fail_edit_account",
      data: {
        message: "メールアドレスの形式が不正です。",
      },
    };
    dispatch(action);
    return;
  }
  putAccount(userName, email).then((isSuccess) => {
    if (isSuccess) {
      const action = {
        type: "success_edit_account",
      };

      dispatch(action);
    } else {
      const action = {
        type: "fail_edit_account",
        data: {
          message: "ユーザ情報の編集に失敗しました。再度お試しください。",
        },
      };
      dispatch(action);
    }
  });
};
