import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, summarizationApi } from "@api";
import { ModernizationInput } from "@types";

export const useInferenceModernization = () =>
  useMutation({
    mutationFn: summarizationApi.inferenceModernization,
    mutationKey: [API_ENPOINTS.INFERENCE_MODERNIZATION]
  });

export const useInferenceModernizationQuery = (params: ModernizationInput) => {
  const { data, isLoading, refetch, error } = useQuery({
    queryFn: () => summarizationApi.inferenceModernization(params),
    queryKey: [API_ENPOINTS.INFERENCE_MODERNIZATION, params],
    enabled: !!params?.repository_id && !!params?.type && !!params?.name,
    retry: 1
  });

  return {
    url: data?.data.url,
    loading: isLoading,
    refetch,
    error
  };
};

export const useSummarizationBmsMutation = () =>
  useMutation({
    mutationFn: summarizationApi.striggerSummarizationBMS,
    mutationKey: [API_ENPOINTS.SUMMARIZATION_BMS]
  });
