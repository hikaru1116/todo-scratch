import { login } from "../repositories/LoginRepository";
import { getAccount } from "../repositories/AccountRepository";

const loading = {
  type: "loading",
};

export const getUserInfo = (dispatch, path) => {
  getAccount().then((user) => {
    const action = {
      type: "get_user_info",
      data: {
        user: user,
        path: path,
      },
    };
    dispatch(action);
  });
};

export const singIn = (dispatch, identifier, password) => {
  // ローディング
  dispatch(loading);

  // 入力値のバリデーション
  if (identifier == null || identifier.length <= 0) {
    const action = {
      type: "validate",
      data: "ユーザ名またはメールアドレスが空白です。入力してください",
    };
    dispatch(action);
    return;
  }

  if (password == null || password.length <= 0) {
    const action = {
      type: "validate",
      data: "パスワードが空白です。入力してください",
    };
    dispatch(action);
    return;
  }

  // ログイン処理
  login(identifier, password)
    .then((data) => {
      if (data == null) {
        const action = {
          type: "validate",
          data: "認証に失敗しました",
        };
        dispatch(action);
        return;
      }
      // アカウント情報の取得
      getAccount().then((user) => {
        const action = {
          type: "sign_in",
          data: {
            user: user,
          },
        };
        dispatch(action);
      });
    })
    .catch((error) => {
      console.log(error);
      const action = {
        type: "validate",
        data: "認証処理でエラーが発生しました",
      };
      dispatch(action);
      return;
    });
};
