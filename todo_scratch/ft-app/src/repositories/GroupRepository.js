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
      if (res.status === 200) {
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
      if (res.status === 200) {
        return res.data;
      }
      return null;
    })
    .catch(() => {
      return null;
    });
};

export const getApprovalRequestGroupList = () => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + "/group/approval-request", { withCredentials: true })
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

export const postApprovalRequest = (groupId) => {
  axios.defaults.withCredentials = true;
  return axios
    .post(endpoint + "/group/approval-request", {
      group_id: groupId,
    })
    .then((res) => {
      if (res.status === 200) {
        return res.data;
      } else {
        return null;
      }
    })
    .catch(() => {
      return null;
    });
};

export const getTaskStatusInfoByGroupId = (groupId) => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + `/group/${String(groupId)}/task/status-info`, {
      withCredentials: true,
    })
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

export const putGroup = (groupId, group) => {
  axios.defaults.withCredentials = true;
  return axios
    .put(endpoint + `/group/${groupId}`, group)
    .then((res) => {
      return res.status === 200;
    })
    .catch(() => {
      return false;
    });
};
