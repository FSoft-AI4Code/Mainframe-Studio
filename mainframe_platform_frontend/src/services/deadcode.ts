import { useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, deadcodeApi } from "@api";
import { DeadCodeInput } from "@types";

export const useDeadCodeFile = (input: DeadCodeInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.DEADCODE, "files", input],
    queryFn: () => deadcodeApi.getDeadcodeFile(input),
    enabled: !!input.repoId
  });
  return {
    deadAndTotal: data?.data.dead_total,
    files: data?.data?.files,
    complexityReduction: data?.data?.complexity_reduction_percentage ?? 0,
    isLoading
  };
};
