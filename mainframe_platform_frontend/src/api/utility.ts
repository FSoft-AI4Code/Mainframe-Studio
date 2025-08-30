import queryString from "query-string";

import {
  UtilitiesFilesResponse,
  UtilitiesFileRequest,
  CreateUtilityRequest,
  UpdateUtilityRequest,
  CategoryUtilityResponse,
  LabelEnum,
  FieldsUtilityByTypeResponse
} from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class UtilityApi {
  static createUtilityFile = ({ repository_id, ...body }: CreateUtilityRequest) => {
    return HttpClient.post(
      `${API_ENPOINTS.UTILITIES_REPOSITORIES}/${repository_id}`,
      {},
      { params: body }
    );
  };

  static updateUtilityFile = ({ utility_id, ...body }: UpdateUtilityRequest) => {
    return HttpClient.put(`${API_ENPOINTS.UTILITIES}/${utility_id}`, body);
  };

  static deleteUtilityFile = (utilityId: string) => {
    return HttpClient.delete(`${API_ENPOINTS.UTILITIES}/${utilityId}`);
  };

  static exportUtilitesExcelReport = (repoId: string) => {
    return HttpClient.get(`${API_ENPOINTS.UTILITIES_REPOSITORIES}/${repoId}/excel`, null, {
      responseType: "blob"
    });
  };

  static getUtilitiesFile = ({ repoId, ...params }: UtilitiesFileRequest) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<UtilitiesFilesResponse>(
      `${API_ENPOINTS.UTILITIES_REPOSITORIES}/${repoId}?${queryStr}`
    );
  };

  static processUtilitiesFile = (repoId: string) => {
    return HttpClient.post(
      `${API_ENPOINTS.UTILITIES_REPOSITORIES}/${repoId}/process-utilities`,
      {}
    );
  };

  static getCategoryUtilityByRepo = (repoId: string) => {
    return HttpClient.get<CategoryUtilityResponse>(
      `${API_ENPOINTS.UTILITIES_REPOSITORIES_CATEGORY}/${repoId}/category`
    );
  };

  static getFieldUtilityByType = (utilityType: LabelEnum) => {
    return HttpClient.get<FieldsUtilityByTypeResponse>(
      `${API_ENPOINTS.UTILITIES_FIELDS_BY_TYPE}/${utilityType}`
    );
  };
}
