import {
  ReverseRepositoryInput,
  ReverseRepositoryResponse,
  ReverseListResponse,
  ReverseListInput,
  ReverseFileInput,
  ReverseFileResponse,
  ReverseCoverageInput,
  ReverseCoverageResponse,
  ReverseReportInput,
  SummarizationDataResponse
} from "@types";

import { HttpClient } from "./httpClient";
import { API_ENPOINTS } from "./endpoints";

export default class ReverseApi {
  static getReverseFile = ({ repoId, ...params }: ReverseRepositoryInput) => {
    return HttpClient.get<ReverseRepositoryResponse>(
      `${API_ENPOINTS.REVERSE_REPOSITORY}/${repoId}`,
      params
    );
  };

  static getReverseByPath = ({ repoId, type, name }: ReverseFileInput) => {
    return HttpClient.get<ReverseFileResponse>(
      `${API_ENPOINTS.REVERSE_REPOSITORY}/${repoId}/type/${type}/name/${name}`
    );
  };

  static listReverses = ({ repoId, ...params }: ReverseListInput) => {
    return HttpClient.get<ReverseListResponse>(
      `${API_ENPOINTS.REVERSE_REPOSITORY}/${repoId}`,
      params
    );
  };

  static getReverseCoverage = ({ repoId }: ReverseCoverageInput) => {
    return HttpClient.get<ReverseCoverageResponse>(
      `${API_ENPOINTS.REVERSE_REPOSITORY}/${repoId}/coverage`
    );
  };

  static triggerReportsCobol = (params: ReverseReportInput) => {
    return HttpClient.post(API_ENPOINTS.REVERSE_REPORTS, params);
  };

  static startInferenceSummarizations = (params: ReverseReportInput) => {
    return HttpClient.post<SummarizationDataResponse>(
      API_ENPOINTS.INFERENCE_SUMMARIZATIONS,
      params
    );
  };
}
