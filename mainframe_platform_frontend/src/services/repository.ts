import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, repositoryApi } from "@api";
import {
  CrudRepoInput,
  DependencyGraphInput,
  DetailEntryPointInput,
  DetailRepositoryInput,
  EntryPointInput,
  QueryParamsInput
} from "@types";

export const useCreateRepository = () => {
  return useMutation({ mutationFn: repositoryApi.createRepository });
};

export const useDeleteRepository = () => {
  return useMutation({ mutationFn: repositoryApi.deleteRepository });
};

export const useUpdateRepository = () => {
  return useMutation({ mutationFn: repositoryApi.updateRepository });
};

export const useRepositoryQuery = ({ projectId }: { projectId: string }) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.PROJECTS, projectId],
    queryFn: () => repositoryApi.getRepositoriesProject(projectId),
    enabled: !!projectId
  });
  return { repository: data?.data, isLoading };
};

export const useGetRepositories = ({
  enabled = true,
  ...params
}: QueryParamsInput & { enabled?: boolean }) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.REPOSITORIES, params],
    queryFn: () => repositoryApi.getListRepositories(params),
    enabled: enabled
  });
  return { repositories: data?.data?.repositories ?? [], isLoading, refetch };
};

export const useDetailRepository = ({ repositoryId }: DetailRepositoryInput) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.REPOSITORIES, repositoryId],
    queryFn: () => repositoryApi.getDetailRepository({ repositoryId }),
    enabled: !!repositoryId
  });
  return { repositoryInfo: data?.data, isLoading, refetch };
};
export const useGetDependencyGraph = ({ repoId, ...params }: DependencyGraphInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [`${API_ENPOINTS.REPOSITORIES}${repoId}/dependency_graph`, params],
    queryFn: () => repositoryApi.getDependencyGraph({ repoId, ...params }),
    enabled: !!repoId
  });
  return {
    graphData: data?.data?.graph,
    total: data?.data?.graph?.total ?? 0,
    pageSize: data?.data?.graph?.page_size ?? 0,
    isLoading
  };
};
export const useEntryPointByRepository = ({ repoId, ...input }: EntryPointInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [`${API_ENPOINTS.REPOSITORIES}${repoId}/entrypoints`, input],
    queryFn: () => repositoryApi.getEntryPoints({ repoId, ...input }),
    enabled: !!repoId
  });

  return {
    entryPoints: data?.data?.entry_points ?? [],
    total: data?.data.total,
    pageSize: data?.data.limit,
    isLoading
  };
};

export const useDetailEntryPointByName = (params: DetailEntryPointInput) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [
      `repositories/${params?.repository_id}/entrypoints/${params?.name}?label=${params.label}`
    ],
    queryFn: () => repositoryApi.getDetailEntryPointByName(params),
    enabled: !!params.repository_id && !!params.name && !!params.label,
    staleTime: 0
  });

  return {
    entryPoint: data?.data?.entry_point,
    isLoading,
    refetchDetailEntrypoint: refetch
  };
};
export const useCrudRepositoryQuery = (params: CrudRepoInput) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [`${API_ENPOINTS.REPOSITORIES}${params?.repository_id}/crud`],
    queryFn: () => repositoryApi.getCrudRepository(params),
    enabled: !!params.repository_id
  });

  return {
    crudItems: data?.data ?? [],
    isLoading,
    refetch
  };
};
