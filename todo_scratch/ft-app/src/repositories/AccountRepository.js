import axios from "axios";

export const getAccount = () => {
  axios.defaults.withCredentials = true;
  return axios
    .get("http://localhost:8000/api/account", { withCredentials: true })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};
