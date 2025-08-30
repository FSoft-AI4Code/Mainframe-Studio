import { useEffect } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

import { ROUTERS } from "@defines";
import { userSelector } from "@store";
import { OverflowLoading } from "@components";

export const EmptyRouter: React.FC = () => {
  const navigate = useNavigate();
  const userData = useSelector(userSelector.selectData);

  useEffect(() => {
    if (!userData) {
      navigate(ROUTERS.WORKSPACE_HOME, { replace: true });
    }
  }, [userData]);

  return (
    <div style={{ height: "100vh" }}>
      <OverflowLoading />
    </div>
  );
};
