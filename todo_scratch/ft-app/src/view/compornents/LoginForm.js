import React, { useContext } from "react";
import { useForm } from "react-hook-form";
import { LoginContext } from "../../contexts/LoginContext";
import { LOGIN } from "../../actions/LoginAction";

const LoginForm = () => {
  const { register, handleSubmit } = useForm();

  const { dispatch } = useContext(LoginContext);

  const onSubmit = () => {
    dispatch(LOGIN);
  };

  return (
    <div>
      <h3>Sample Form</h3>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input defaultValue="test" {...register("example")} />
        <input type="submit" />
      </form>
    </div>
  );
};

export default LoginForm;
