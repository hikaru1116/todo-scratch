import axios from "axios";
import { endpoint } from "../utils/endpoint";

export const getTaskListDivideByStatus = (groupId) => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + `/group/${String(groupId)}/task/divide-by-status`, {
      withCredentials: true,
    })
    .then((res) => {
      return res.data;
    })
    .catch(() => {
      return null;
    });
};

export const getTaskDetail = (groupId, taskId) => {
  axios.defaults.withCredentials = true;
  return axios
    .get(endpoint + `/group/${String(groupId)}/task/${String(taskId)}/detail`, {
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

export const putTask = (groupId, taskId, task) => {
  axios.defaults.withCredentials = true;
  return axios
    .put(endpoint + `/group/${String(groupId)}/task/${taskId}`, task)
    .then((res) => {
      return res.status == 200;
    })
    .catch(() => {
      return false;
    });
};

export const changeTaskStatus = (groupId, taskId, taskStatusId) => {
  axios.defaults.withCredentials = true;
  return axios
    .put(
      endpoint +
        `/group/${String(groupId)}/task/${String(taskId)}/change-status`,
      {
        task_status_id: taskStatusId,
      }
    )
    .then((res) => {
      return res.status == 200;
    })
    .catch(() => {
      return false;
    });
};
