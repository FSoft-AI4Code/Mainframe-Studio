import { useMutation, useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, assessmentApi } from "@api";
import { exportDataToCsv, handleErrorMessage } from "@utils";

export const useTriggerAssessment = () =>
  useMutation({
    mutationFn: assessmentApi.triggerAssessment
  });

export const useGetAssessmentRepository = ({ repoId }: { repoId: string }) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.ASSESSMENTS_REPOSITORY, repoId],
    queryFn: () => assessmentApi.getAssessmentRepository(repoId),
    enabled: !!repoId
  });
  return {
    assessmentRepository: data?.data.assessments ?? [],
    inventoryData: data?.data.assessments?.[0]?.result,
    isLoading
  };
};

export const useAssessmentFileCountRepository = ({ repoId }: { repoId: string }) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.ASSESSMENTS_REPOSITORY, "files", repoId],
    queryFn: () => assessmentApi.getAssessmentFileCountByRepository(repoId),
    enabled: !!repoId
  });
  return {
    assessmentFileCount: data?.data.file_counts,
    assessmentTotal: data?.data?.total,
    isLoading
  };
};

export const useExportStatisticReport = () => {
  return useMutation({
    mutationFn: assessmentApi.exportStatisticReport,
    onSuccess(data) {
      exportDataToCsv(data, "report", "xlsx");
    },
    onError(error) {
      handleErrorMessage(error, { show: true });
    }
  });
};
