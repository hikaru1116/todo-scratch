import { login } from "../repositories/LoginRepository";
import { setUserDataAction } from "../actions/UserAction";
import { getAccount } from "../repositories/AccountRepository";
import { setIsLogin } from "../utils/UserStorage";
import { successlJudge } from "../actions/SignInJudgeAction";
const loading = {
  type: "loading",
};

export const signInAction = (
  dispatch,
  dispatchUser,
  dispatchSignInJudge,
  navigate,
  identifier,
  password
) => {
  // ローディング
  dispatch(loading);

  // 入力値のバリデーション
  if (identifier == null || identifier.length <= 0) {
    const action = {
      type: "fail_sign_in",
      data: {
        message: "ユーザ名またはメールアドレスが空白です。入力してください",
      },
    };
    dispatch(action);
    return;
  }

  if (password == null || password.length <= 0) {
    const action = {
      type: "fail_sign_in",
      data: { message: "パスワードが空白です。入力してください" },
    };
    dispatch(action);
    return;
  }

  // ログイン処理
  login(identifier, password)
    .then((data) => {
      if (data == null) {
        const action = {
          type: "fail_sign_in",
          data: { message: "認証に失敗しました" },
        };
        dispatch(action);
        return;
      }
      setIsLogin(true);
      // アカウント情報の取得
      getAccount().then((user) => {
        setUserDataAction(dispatchUser, user).then(() => {
          const action = {
            type: "success_sign_in",
          };
          dispatch(action);
          successlJudge(dispatchSignInJudge, "/");
          navigate("/");
        });
      });
    })
    .catch((error) => {
      console.log(error);
      const action = {
        type: "fail_sign_in",
        data: { message: "認証処理でエラーが発生しました" },
      };
      dispatch(action);
      return;
    });
};
