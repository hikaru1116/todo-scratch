export const setIsLogin = (isLogin) => {
  localStorage.setItem("is_login", isLogin);
};

export const getIsLogin = () => {
  return localStorage.getItem("is_login");
};
