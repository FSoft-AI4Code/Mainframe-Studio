import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, reverseApi } from "@api";
import {
  ReverseRepositoryInput,
  ReverseFileInput,
  ReverseListInput,
  ReverseFileResponse,
  ReverseCoverageInput,
  ReverseTypeEnum
} from "@types";

export const useGetReverseFile = (params: ReverseRepositoryInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.REVERSE_REPOSITORY, params],
    queryFn: () => reverseApi.getReverseFile(params),
    enabled: !!params.repoId
  });
  return { reverseFile: data?.data, isLoading };
};

export const getTypedResponse = <T>(response: ReverseFileResponse, type: ReverseTypeEnum) => ({
  type: Object.values(ReverseTypeEnum).includes(type) ? type : ReverseTypeEnum.DEFAULT,
  data: response as T
});

export const useGetReverseByPath = (params: ReverseFileInput) => {
  const { type, repoId, name } = params || {};
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.REVERSE_REPOSITORY, "byPath", params],
    queryFn: () => reverseApi.getReverseByPath(params),
    enabled: !!(repoId && type && name),
    select: response => {
      return getTypedResponse<ReverseFileResponse>(response, type);
    }
  });
  return {
    reverseFile: data?.data,
    fileType: data?.type,
    isLoading,
    refetch
  };
};

export const useListReverses = (params: ReverseListInput, enabled = true) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.REVERSE_REPOSITORY, "list", params],
    queryFn: () => reverseApi.listReverses(params),
    enabled: !!params.repoId && enabled
  });

  return {
    files: data?.data ?? [],
    isLoading,
    refetch
  };
};

export const useReverseCoverage = (params: ReverseCoverageInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.REVERSE_REPOSITORY, "coverage", params],
    queryFn: () => reverseApi.getReverseCoverage(params),
    enabled: !!params.repoId,
    refetchOnWindowFocus: false
  });

  return {
    totalCoverage: data?.data.total_coverage ?? 0,
    coverageByTypes: data?.data?.by_types ?? [],
    isLoading
  };
};

export const useTriggerReportCobol = () => {
  return useMutation({ mutationFn: reverseApi.triggerReportsCobol });
};

export const useTriggerSummariztions = () => {
  return useMutation({ mutationFn: reverseApi.startInferenceSummarizations });
};
