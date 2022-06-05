import React from "react";
import SignUpDisplay from "../compornents/SignUp/SignUpDisplay";
import { SignUpContext } from "../../contexts/SignUpContext";

const SignUpPage = () => {
  return (
    <SignUpContext>
      <SignUpDisplay />
    </SignUpContext>
  );
};

export default SignUpPage;
