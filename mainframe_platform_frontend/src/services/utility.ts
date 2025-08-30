/* eslint-disable no-console */
import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, utilityApi } from "@api";
import { exportDataToCsv, handleErrorMessage } from "@utils";
import { CategoryUtilityData, LabelEnum, UtilitiesFileRequest } from "@types";

export const useCreateUtility = () =>
  useMutation({
    mutationFn: utilityApi.createUtilityFile
  });

export const useUpdateUtility = () =>
  useMutation({
    mutationFn: utilityApi.updateUtilityFile
  });

export const useDeleteUtility = () =>
  useMutation({
    mutationFn: utilityApi.deleteUtilityFile
  });

export const useUtilitiesFileQuery = (params: UtilitiesFileRequest) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [
      API_ENPOINTS.UTILITIES_REPOSITORIES,
      "files",
      params.repoId,
      params.limit,
      params.skip
    ],
    queryFn: async () => {
      const response = await utilityApi.getUtilitiesFile(params);
      if (response?.data?.utilities?.length) return response;
      await utilityApi.processUtilitiesFile(params.repoId);
      return utilityApi.getUtilitiesFile(params);
    },
    enabled: !!params
  });
  return {
    utilitiesFile: data?.data?.utilities ?? [],
    total: data?.data?.total,
    skip: data?.data?.skip,
    loading: isLoading,
    refetchUtilitiesFile: refetch
  };
};

export const useCategoryUtilityQuery = ({ repoId }: { repoId: string }) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [`${API_ENPOINTS.UTILITIES_REPOSITORIES_CATEGORY}/${repoId}/category`],
    queryFn: () => utilityApi.getCategoryUtilityByRepo(repoId),
    enabled: !!repoId
  });
  return {
    categoryUtility: data?.data ?? ({} as CategoryUtilityData),
    total: data?.data?.total,
    skip: data?.data?.skip,
    loading: isLoading,
    refetchUtilitiesFile: refetch
  };
};

export const useExportUtilitiesReport = () => {
  return useMutation({
    mutationFn: utilityApi.exportUtilitesExcelReport,
    onSuccess(data) {
      exportDataToCsv(data, "utilities-report", "xlsx");
    },
    onError(error) {
      handleErrorMessage(error, { show: true });
    }
  });
};

export const useFieldsUtilitiesByTypeQuery = (type: LabelEnum) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [`${API_ENPOINTS.UTILITIES_FIELDS_BY_TYPE}/${type}`],
    queryFn: () => utilityApi.getFieldUtilityByType(type),
    enabled: !!type
  });
  return {
    fieldsUtility: data?.data ?? [],
    loading: isLoading,
    refetch
  };
};
