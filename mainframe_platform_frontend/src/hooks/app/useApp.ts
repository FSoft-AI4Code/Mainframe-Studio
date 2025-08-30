import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";

import { ENVIRONMENT, storage } from "@defines";
import { appActions, userActions } from "@store";

export const useApp = () => {
  const dispatch = useDispatch();
  const [inited, setInited] = useState(false);

  const initEnvironment = () => {
    const environment = localStorage.getItem(storage.ENVIRONMENT);
    dispatch(appActions.setDevelopMode(environment === ENVIRONMENT.DEVELOPMENT));
  };

  const initialize = () => {
    try {
      initEnvironment();
      const token = localStorage.getItem(storage.TOKEN);
      if (token) {
        dispatch(
          userActions.setUser({
            id: "1",
            email: "fpt@fpt.com",
            username: "fpt",
            firstName: "A",
            lastName: "Nguyen Van",
            isVerified: true,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString(),
            status: "active"
          })
        );
      }
    } catch (error) {
      // eslint-disable-next-line
      console.error(error);
    } finally {
      setInited(true);
    }
  };

  useEffect(() => {
    initialize();
  }, []);

  return { inited };
};
