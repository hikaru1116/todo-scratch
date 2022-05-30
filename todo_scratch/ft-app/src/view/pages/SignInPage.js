import React from "react";
import { SingInContext } from "../../contexts/SignInContet";
import SingInDisplay from "../compornents/SignIn/SingInDisplay";

export default function SignIn() {
  return (
    <SingInContext>
      <SingInDisplay />
    </SingInContext>
  );
}
