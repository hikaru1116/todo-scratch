import { createUser } from "../repositories/AccountRepository";

export const signUpAction = (dispatch, userName, email, password) => {
  // 入力値のバリデーション
  if (
    userName == null ||
    userName.length <= 0 ||
    email == null ||
    email.length <= 0 ||
    password == null ||
    password.length <= 0
  ) {
    const action = {
      type: "fail_sign_up",
      data: {
        message:
          "ユーザ名、メールアドレス、パスワードのいづれかが空白です。入力してください",
      },
    };
    dispatch(action);
    return;
  }

  const regex =
    /^[a-zA-Z0-9_.+-]+@([a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]*\.)+[a-zA-Z]{2,}$/;

  if (!regex.test(email)) {
    const action = {
      type: "fail_sign_up",
      data: {
        message: "メールアドレスの形式が不正です。",
      },
    };
    dispatch(action);
    return;
  }
  createUser(userName, email, password).then((isSuccess) => {
    if (isSuccess) {
      const action = {
        type: "success_sign_up",
      };

      dispatch(action);
    } else {
      const action = {
        type: "fail_sign_up",
        data: {
          message: "ユーザ登録に失敗しました。再度お試しください。",
        },
      };
      dispatch(action);
    }
  });
};
