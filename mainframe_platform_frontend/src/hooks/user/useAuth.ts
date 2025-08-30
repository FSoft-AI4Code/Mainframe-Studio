import { useSelector, useDispatch } from "react-redux";

import { userActions, userSelector } from "@store";
import { getAuthToken, setAuthToken, removeAuthToken } from "@utils";

export function useAuth() {
  const isAuthorized = useSelector(userSelector.selectIsAuthorized);
  const dispatch = useDispatch();
  const setAuthorized = (authorized: boolean) => dispatch(userActions.setIsAuthorized(authorized));
  return {
    setToken: setAuthToken,
    getToken: getAuthToken,
    isAuthorized,
    authorize(token: string) {
      setAuthToken(token);
      setAuthorized(true);
    },
    unauthorize() {
      setAuthorized(false);
      removeAuthToken();
    }
  };
}
