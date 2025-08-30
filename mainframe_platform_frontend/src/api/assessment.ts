import { AssessmentFileCountRepositoryResponse, AssessmentRepositoryResponse } from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class AssessmentApi {
  static triggerAssessment = (repoId: string) => {
    return HttpClient.post(API_ENPOINTS.ASSESSMENTS, { repository_id: repoId });
  };

  static getAssessmentRepository = (repoId: string) => {
    return HttpClient.get<AssessmentRepositoryResponse>(
      `${API_ENPOINTS.ASSESSMENTS_REPOSITORY}/${repoId}`
    );
  };

  static getAssessmentFileCountByRepository = (repoId: string) => {
    return HttpClient.get<AssessmentFileCountRepositoryResponse>(
      `${API_ENPOINTS.ASSESSMENTS_REPOSITORY}/${repoId}/files`
    );
  };

  static exportStatisticReport = (repoId: string) => {
    return HttpClient.get(`${API_ENPOINTS.REPOSITORIES}${repoId}/source-stats`, null, {
      responseType: "blob"
    });
  };
}
