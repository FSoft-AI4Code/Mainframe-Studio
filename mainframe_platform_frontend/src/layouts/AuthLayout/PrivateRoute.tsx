import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

import { OverflowLoading } from "@components";
import { ROUTERS } from "@defines";
import { useAuth } from "@hooks";

export function PrivateRoute({ children }: React.PropsWithChildren) {
  const { isAuthorized } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!isAuthorized) {
      navigate(ROUTERS.LOGIN, { replace: true });
    }
  }, [isAuthorized]);

  if (isAuthorized) {
    return <>{children}</>;
  }
  return (
    <div style={{ height: "100vh" }}>
      <OverflowLoading />
    </div>
  );
}
