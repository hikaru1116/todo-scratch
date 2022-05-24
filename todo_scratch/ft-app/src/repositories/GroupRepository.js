import axios from "axios";
import { endpoint } from "../utils/endpoint";

export const getGroupById = (group_id) => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + "/group/" + group_id, { withCredentials: true })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};

export const postGroup = (group) => {
  axios.defaults.withCredentials = true;
  return axios
    .post(endpoint + "/group", group)
    .then((res) => {
      if (res.status == 200) {
        return res.data;
      } else {
        return null;
      }
    })
    .catch(() => {
      return null;
    });
};

export const getJoinedGroupList = () => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + "/group/joined", { withCredentials: true })
    .then((res) => {
      if (res.status == 200) {
        return res.data;
      }
      return null;
    })
    .catch(() => {
      return null;
    });
};
