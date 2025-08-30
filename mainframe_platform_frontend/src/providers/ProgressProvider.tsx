import { EventSourcePolyfill } from "event-source-polyfill";
import { createContext, useContext, useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import { useDispatch } from "react-redux";
import { Outlet, useNavigate, useParams } from "react-router-dom";

import { ROUTERS, storage } from "@defines";
import { appActions } from "@store";

const ProgressContext = createContext<{ progressPercent: number }>({ progressPercent: 0 });

export const useProgress = () => {
  return useContext(ProgressContext);
};

export function ProgressProvider() {
  const { t } = useTranslation();
  const dispatch = useDispatch();
  const { repoId } = useParams();
  const navigate = useNavigate();

  const [progressPercent, setProgressPercent] = useState<number>(0);

  useEffect(() => {
    if (repoId) {
      dispatch(
        appActions.setNotificationData({
          message: t("notification.parsing_blobs"),
          type: "pending"
        })
      );
      const eventSource = new EventSourcePolyfill(
        `${process.env.REACT_APP_API_URL}/api/repository/${repoId}/status_analyzed_blobs`,
        { headers: { Authorization: `Bearer ${localStorage.getItem(storage.TOKEN)}` } }
      );

      const closeEventSource = () => {
        eventSource.close();
      };

      eventSource.onmessage = async event => {
        const response = JSON.parse(event.data);

        setProgressPercent(response.progress);
        if (response.progress === 100) {
          closeEventSource();
          dispatch(
            appActions.setNotificationData({
              message: t("notification.success_parsing_blobs"),
              type: "success",
              timeout: 3000
            })
          );
        }
      };

      eventSource.onerror = closeEventSource;

      return () => {
        dispatch(appActions.setNotificationData());
        closeEventSource();
      };
    } else {
      navigate(ROUTERS.WORKSPACE_REPOSITORIES);
    }
  }, [repoId]);

  return (
    <ProgressContext.Provider value={{ progressPercent }}>
      <Outlet />
    </ProgressContext.Provider>
  );
}
