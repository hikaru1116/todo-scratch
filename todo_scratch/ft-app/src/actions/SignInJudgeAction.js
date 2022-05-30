import { getIsLogin } from "../utils/UserStorage";
import { getAccount } from "../repositories/AccountRepository";
import { setUserDataAction } from "../actions/UserAction";

export const judgeSingInAction = (dispatch, dispatchUser, path) => {
  const isLogin = getIsLogin();

  if (isLogin === null || isLogin === "false") {
    failJudge(dispatch);
    return;
  }

  getAccount().then((user) => {
    if (user === null) {
      failJudge(dispatch);
    }
    setUserDataAction(dispatchUser, user).then(() => {
      successlJudge(dispatch, path);
    });
  });
};

export const successlJudge = (dispatch, path) => {
  const action = {
    type: "success_sign_in",
    data: {
      path: path,
    },
  };
  dispatch(action);
};

export const failJudge = (dispatch) => {
  const action = {
    type: "fail_sign_in",
  };
  dispatch(action);
};
