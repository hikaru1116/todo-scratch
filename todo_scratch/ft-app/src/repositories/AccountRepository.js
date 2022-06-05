import axios from "axios";
import { endpoint } from "../utils/endpoint";

export const getAccount = () => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + "/account", { withCredentials: true })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};

export const createUser = (userName, email, password) => {
  axios.defaults.headers.post["Access-Control-Allow-Origin"] =
    "http://localhost:3000/";

  return axios
    .post(
      endpoint + "/signup",
      {
        user_name: userName,
        email: email,
        password: password,
      },
      { withCredentials: true }
    )
    .then((res) => {
      return res.status == "200";
    })
    .catch(() => {
      return false;
    });
};

export const putAccount = (userName, email) => {
  axios.defaults.headers.post["Access-Control-Allow-Origin"] =
    "http://localhost:3000/";

  return axios
    .put(
      endpoint + "/account",
      {
        user_name: userName,
        email: email,
      },
      { withCredentials: true }
    )
    .then((res) => {
      return res.status == "200";
    })
    .catch(() => {
      return false;
    });
};
