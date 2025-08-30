import { useMutation } from "@tanstack/react-query";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";

import { userApi } from "@api";
import { ROUTERS } from "@defines";
import { userActions } from "@store";
import { LoginParams } from "@types";
import { getQueryParam, handleErrorMessage } from "@utils";

import { useAuth } from "./useAuth";

export const useLogin = () => {
  const dispatch = useDispatch();
  const { authorize } = useAuth();
  const { isPending: loading, mutate: onLogin } = useMutation({
    mutationFn: userApi.doLoginRequest
  });
  const navigate = useNavigate();

  const handleLogin = async ({ password, username }: LoginParams) => {
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    onLogin(formData, {
      onSuccess({ access_token }) {
        if (!access_token) return;
        authorize(access_token);
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
        const redirect = getQueryParam("redirect");
        if (redirect && redirect !== ROUTERS.LOGIN) {
          navigate(redirect);
        } else {
          navigate(ROUTERS.WORKSPACE_REPOSITORIES);
        }
      },
      onError(error) {
        handleErrorMessage(error, { show: true });
      }
    });
  };

  return { handleLogin, loading };
};
