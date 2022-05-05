import axios from "axios";

export const login = () => {
  axios
    .get("http://localhost:8000")
    .then((res) => {
      console.log(res.data);
      console.log(res);
    })
    .catch((error) => {
      console.log(error.response);
    });
};
