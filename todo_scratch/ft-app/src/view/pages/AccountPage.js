import React from "react";
import { AccountContext } from "../../contexts/AccountContext";
import AccountDisplay from "../compornents/Account/AccountDisplay";

const AccountPage = () => {
  return (
    <AccountContext>
      <AccountDisplay />
    </AccountContext>
  );
};

export default AccountPage;
