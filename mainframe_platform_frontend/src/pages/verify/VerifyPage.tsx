import React, { lazy } from "react";

const AuthLayout = lazy(() => import("@layouts/AuthLayout"));

export const VerifyPage: React.FC = () => {
  return <AuthLayout>VerifyPage</AuthLayout>;
};
