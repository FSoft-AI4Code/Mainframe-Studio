import queryString from "query-string";

import { DuplicateFilesResponse, DuplicateFilesRequest } from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class DuplicateApi {
  static getDuplicateFiles = ({ repoId, ...params }: DuplicateFilesRequest) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<DuplicateFilesResponse>(
      `${API_ENPOINTS.DUPLICATE_FILES}/${repoId}?${queryStr}`
    );
  };
}
