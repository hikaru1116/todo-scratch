export const toAuthTypeStr = (authType) => {
  if (authType === 0) {
    return "ホストユーザ";
  } else if (authType === 1) {
    return "ユーザ";
  } else {
    return "ユーザ";
  }
};
