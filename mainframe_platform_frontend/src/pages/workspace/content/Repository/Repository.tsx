import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

import { repositorySelector } from "@store";
import { ROUTERS } from "@defines";

import { Information } from "./Information";

export const Repository: React.FC = () => {
  const data = useSelector(repositorySelector.selectRepositoryData);
  const [isOnEdit, setIsOnEdit] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (!data?.id) navigate(ROUTERS.WORKSPACE_REPOSITORIES);
  }, [data]);
  return <Information setIsOnEdit={setIsOnEdit} data={data as any} isOnEdit={isOnEdit} />;
};
