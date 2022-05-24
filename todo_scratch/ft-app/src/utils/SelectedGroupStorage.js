export const setSelectedGroupId = (groupId) => {
  console.log("save localstorage");
  console.log(groupId);
  localStorage.setItem("selected_group_id", groupId);
};

export const getSelectedGroupId = () => {
  return localStorage.getItem("selected_group_id");
};
