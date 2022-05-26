import axios from "axios";
import { endpoint } from "../utils/endpoint";

export const getGroupById = (group_id) => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + "/group/{0}/".format(str(group_id)), {
      withCredentials: true,
    })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};
