import React, { useContext } from "react";
import { useForm } from "react-hook-form";
import { LoginContext } from "../../contexts/LoginContext";
import { ADD_1, MULTIPLE_3, reset } from "../../actions/LoginAction";
import { login } from "../../repositories/LoginRepository";

const LoginForm = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    login();
    console.log({
      data: data,
    });
  };

  const { dispatch } = useContext(LoginContext);

  return (
    <div>
      <div>
        <h3>Login</h3>
        <button onClick={() => dispatch(ADD_1)}>ADD+1</button>
        <button onClick={() => dispatch(MULTIPLE_3)}>MULTIPLE*3</button>
        <button onClick={() => reset(dispatch, 0)}>RESET</button>
      </div>
      <h3>Sample Form</h3>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input defaultValue="test" {...register("example")} />
        <input {...register("exampleRequired", { required: true })} />
        {errors.exampleRequired && <span>This field is required</span>}
        <input type="submit" />
      </form>
    </div>
  );
};

export default LoginForm;
