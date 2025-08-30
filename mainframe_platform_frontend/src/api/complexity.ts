import {
  ComplexityDistributionInput,
  ComplexityDistributionResponse,
  ComplexityRepositoryResponse
} from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class ComplexityApi {
  static getComplexitiesByRepository = async (repoId: string) => {
    return HttpClient.get<ComplexityRepositoryResponse>(
      `${API_ENPOINTS.COMPLEXITIES_REPOSITORY}/${repoId}`
    );
  };

  static getComplexitiesDistribution = async ({
    repoId,
    ...params
  }: ComplexityDistributionInput) => {
    return HttpClient.get<ComplexityDistributionResponse>(
      `${API_ENPOINTS.COMPLEXITIES_REPOSITORY}/${repoId}/dist`,
      params
    );
  };
}
