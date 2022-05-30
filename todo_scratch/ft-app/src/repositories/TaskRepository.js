import axios from "axios";
import { endpoint } from "../utils/endpoint";

export const getGroupById = (group_id) => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + "/group/{0}/".format(String(group_id)), {
      withCredentials: true,
    })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};

export const postTask = (groupId, task) => {
  axios.defaults.withCredentials = true;
  return axios
    .post(endpoint + "/group/" + String(groupId) + "/task", task)
    .then((res) => {
      return res.status == 200;
    })
    .catch(() => {
      return false;
    });
};
