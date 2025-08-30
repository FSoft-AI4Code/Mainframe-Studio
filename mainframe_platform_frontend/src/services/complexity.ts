import { useQuery } from "@tanstack/react-query";

import { API_ENPOINTS, complexityApi } from "@api";
import { ComplexityDistributionInput, ResultComplexity } from "@types";

export const useGetComplexitiesByRepository = ({
  repoId,
  enabled = true
}: {
  repoId: string;
  enabled?: boolean;
}) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.COMPLEXITIES_REPOSITORY, repoId],
    queryFn: () => complexityApi.getComplexitiesByRepository(repoId),
    enabled: !!repoId && enabled
  });
  return {
    complexitiesByRepository: data?.data.complexities ?? [],
    predictComplexity: data?.data.complexities?.[0]?.result?.complexity || [],
    isLoading
  };
};

export const useComplexitiesDistributionQuery = (params: ComplexityDistributionInput) => {
  const { data, isLoading } = useQuery({
    queryKey: [API_ENPOINTS.COMPLEXITIES_REPOSITORY, "dist", params],
    queryFn: () => complexityApi.getComplexitiesDistribution(params),
    enabled: !!params?.repoId
  });

  return {
    complexitiesDistribution: data?.data?.result.dist ?? ({} as ResultComplexity),
    averageComplexity: data?.data?.result?.average_complexity ?? 0,
    isLoading
  };
};
