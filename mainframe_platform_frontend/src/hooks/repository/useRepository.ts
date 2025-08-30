import { useRepositoryQuery } from "@services";

import { useProjectsQuery } from "./../../services/project";

export function useRepository() {
  const { project, isLoading: loadingProject } = useProjectsQuery();
  const { repository, isLoading: loadingRepository } = useRepositoryQuery({
    projectId: project?.id || ""
  });

  return {
    projectId: project?.id,
    loadingProject,
    repository,
    loadingRepository: loadingRepository
  };
}
