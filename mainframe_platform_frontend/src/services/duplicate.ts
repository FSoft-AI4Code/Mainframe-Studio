/* eslint-disable no-console */
import { useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, duplicateApi } from "@api";
import { DuplicateFilesRequest } from "@types";

export const useDuplicateFilesQuery = (params: DuplicateFilesRequest) => {
  const { data, isLoading, refetch } = useQuery({
    queryKey: [API_ENPOINTS.DUPLICATE_FILES, params.repoId, params.limit, params.skip],
    queryFn: () => duplicateApi.getDuplicateFiles(params),
    enabled: !!params.repoId
  });
  return {
    duplicateNameGroup: data?.data?.duplicate_name_groups ?? [],
    totalDuplicateByContent: data?.data?.total_duplicate_by_content,
    totalDuplicateFiles: data?.data?.total,
    loading: isLoading,
    refetch
  };
};
