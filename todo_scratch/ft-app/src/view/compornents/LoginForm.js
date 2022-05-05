import React, { useContext } from "react";
import { useForm } from "react-hook-form";
import { LoginContext } from "../../contexts/LoginContext";
import { SIGN_IN } from "../../actions/LoginAction";

const LoginForm = () => {
  const {
    register,
    handleSubmit,
    // formState: { errors },
  } = useForm();

  const { dispatch } = useContext(LoginContext);

  const onSubmit = () => {
    dispatch(SIGN_IN);
  };

  return (
    <div>
      <h3>Sample Form</h3>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input defaultValue="test" {...register("example")} />
        {/* <input {...register("exampleRequired", { required: true })} />
        {errors.exampleRequired && <span>This field is required</span>} */}
        <input type="submit" />
      </form>
    </div>
  );
};

export default LoginForm;
