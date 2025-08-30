import { message as messageApi } from "antd";
import { AxiosError } from "axios";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";

import { repositoryApi } from "@api";
import { GlobalLoading } from "@components";
import { ROUTERS, storage } from "@defines";
import { fileActions, migrationRepositoryActions, repositoryActions } from "@store";

export const SharePage: React.FC = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { repoId } = useParams();
  const [searchParams] = useSearchParams();
  const matchingId = searchParams.get("matchingId");

  const handle = async (id: string) => {
    try {
      const token = localStorage.getItem(storage.TOKEN);
      if (!token) {
        return;
      }
      if (!matchingId) {
        dispatch(migrationRepositoryActions.clean());
        localStorage.removeItem(storage.MIGRATION_REPO);
      }
      const res = await repositoryApi.getRepositoryRequest(id);

      if (!res?.data) return;
      const responseData = res.data;
      dispatch(fileActions.clean());
      dispatch(repositoryActions.setRepositoryData(responseData));

      localStorage.setItem(
        storage.REPO,
        JSON.stringify({ ...responseData, done: responseData.status === "processed" })
      );
      if (responseData.status === "processed") {
        dispatch(repositoryActions.setDone());
      }
      const messageContent = `You have successfully retrieved the information for the project ${responseData.name}.`;
      messageApi.success({
        content: messageContent,
        duration: 2,
        key: messageContent,
        onClick: () => messageApi.destroy(messageContent)
      });
      if (matchingId) {
        const matchingRes = await repositoryApi.getRepositoryRequest(matchingId);

        if (!matchingRes?.data) return;
        const matchingData = matchingRes.data;
        dispatch(migrationRepositoryActions.setMigrationRepositoryData(matchingData));
        localStorage.setItem(storage.MIGRATION_REPO, JSON.stringify(matchingData));
        navigate(ROUTERS.MIGRATION_HOME);
        const messageContent2 = `You have successfully retrieved the information for the project ${String(
          matchingData?.name
        )}.`;
        messageApi.success({
          content: messageContent2,
          duration: 5,
          key: messageContent2,
          onClick: () => messageApi.destroy(messageContent2)
        });
      } else {
        navigate(ROUTERS.EXPLORATION_HOME);
      }
    } catch (error) {
      const goToErrorPage = () =>
        navigate(ROUTERS.SERVER_ERROR, {
          state: { message: "There was an error while retrieving project information." }
        });
      if (error instanceof AxiosError) {
        const { status } = error.response || {};
        const { detail, message } = error.response?.data || {};

        if (status === 404) {
          navigate(ROUTERS.NOT_FOUND, {
            state: { message: "No information found for this project." }
          });
        } else if (status === 500 && detail) {
          if (detail) navigate(ROUTERS.SERVER_ERROR, { state: { message: detail } });
          else if (message) navigate(ROUTERS.SERVER_ERROR, { state: { message: message } });
          else goToErrorPage();
        } else {
          goToErrorPage();
        }
      } else {
        goToErrorPage();
      }
    }
  };

  const handleException = () => {};

  useEffect(() => {
    if (repoId) handle(repoId);
    else handleException();
  }, [repoId]);

  return <GlobalLoading />;
};
