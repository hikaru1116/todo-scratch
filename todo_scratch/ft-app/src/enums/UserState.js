export const toUserStateStr = (userState) => {
  if (userState == 0) {
    return "承認済み";
  } else if (userState == 1) {
    return "未承認";
  }
};
