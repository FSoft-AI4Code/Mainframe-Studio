import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";

import { userApi } from "@api";
import { ROUTERS } from "@defines";

export const useLogin = () => {
  return useMutation({ mutationFn: userApi.doLoginRequest });
};

export const useLogout = () => {
  const navigate = useNavigate();
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: userApi.doLogoutRequest,
    onSettled() {
      queryClient.clear();
      const search = new URLSearchParams(`redirect=${location.pathname}`);
      const queries = search.toString();
      navigate(`${ROUTERS.LOGIN}${queries ? `?${queries}` : ""}`);
    }
  });
};
