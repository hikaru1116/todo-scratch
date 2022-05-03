import axios from "axios";

export const login = () => {
  axios.get("https://jsonplaceholder.typicode.com/posts").then((res) => {
    console.log(res.data);
  });
};
