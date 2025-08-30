import { useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, projectApi } from "@api";
import { ProjectApiResponse } from "@types";
import { useAuth } from "@hooks";

export const useProjectsQuery = () => {
  const { isAuthorized } = useAuth();
  const { data, isLoading } = useQuery<ProjectApiResponse, Error>({
    queryKey: [API_ENPOINTS.PROJECTS, "list-project"],
    queryFn: projectApi.getProjectList,
    enabled: isAuthorized
  });

  return { project: data?.data?.projects?.[0], isLoading };
};
