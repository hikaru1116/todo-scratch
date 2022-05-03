export const ADD_1 = {
  type: "add_1",
};
export const MULTIPLE_3 = {
  type: "multiple_3",
};
export function reset(dispatch, initialState) {
  const action = {
    type: "reset",
    initialState: initialState,
  };
  dispatch(action);
}
