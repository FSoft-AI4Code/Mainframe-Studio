import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, datasetsApi } from "@api";
import {
  AvailableFilterParams,
  DatasetsInput,
  StatisticDatasets,
  StatisticDatasetsInput,
  StatisticDatasetsResponse
} from "@types";
import { exportDataToCsv, handleErrorMessage } from "@utils";

export const useDatasetsQuery = ({ enabled, ...params }: DatasetsInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.DATASETS, params],
    queryFn: () => datasetsApi.getDatasets(params),
    enabled: !!params?.repository_id && enabled
  });
  return {
    datasetAssignments: data?.data.dataset_assignments ?? [],
    isLoading,
    skip: data?.data?.skip,
    limit: data?.data?.limit,
    total: data?.data?.total ?? 0
  };
};

export const useStatisticDatasetsQuery = (params: StatisticDatasetsInput) => {
  const { data, isLoading } = useQuery<StatisticDatasetsResponse>({
    queryKey: [API_ENPOINTS.DATASETS_STATISTIC, params],
    queryFn: () => datasetsApi.getStatisticDatasets(params),
    enabled: !!params?.repository_id
  });
  return {
    statisticDataset: data?.data ?? ({} as StatisticDatasets),
    isLoading
  };
};

export const useAvailabledFilterDatasetsQuery = (params: AvailableFilterParams) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.DATASETS_AVAILABLE_FILTER, params],
    queryFn: () => datasetsApi.getListAvailabeFilterDataset(params),
    enabled: !!params?.repository_id
  });
  return {
    datasetType: data?.data.dataset_type ?? [],
    openMode: data?.data.open_mode ?? [],
    isLoading
  };
};

export const useExportDatasetFile = () => {
  return useMutation({
    mutationFn: datasetsApi.exportDataset,
    onSuccess(data, variables) {
      exportDataToCsv(data, variables.view);
    },
    onError(error) {
      handleErrorMessage(error, { show: true });
    }
  });
};
