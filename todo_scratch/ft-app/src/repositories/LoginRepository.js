import axios from "axios";

export const login = (identifier, password) => {
  axios.defaults.headers.post["Access-Control-Allow-Origin"] =
    "http://localhost:3000/";

  return axios
    .post(
      "http://localhost:8000/api/signin",
      {
        identifier: identifier,
        password: password,
      },
      { withCredentials: true }
    )
    .then((res) => {
      if (res.status === 200) {
        return res.data;
      }
      return null;
    })
    .catch(() => {
      return null;
    });
};

export const postSingOut = () => {
  axios.defaults.headers.post["Access-Control-Allow-Origin"] =
    "http://localhost:3000/";

  return axios
    .post("http://localhost:8000/api/signout", {}, { withCredentials: true })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};
