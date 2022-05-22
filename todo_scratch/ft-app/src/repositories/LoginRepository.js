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
      return res.data;
    })
    .catch(() => {
      return null;
    });
};
