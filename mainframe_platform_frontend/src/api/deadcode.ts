import { DeadCodeInput, DeadcodeResponse } from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";

export default class DeadCodeApi {
  static getDeadcodeFile = ({ repoId, ...params }: DeadCodeInput) => {
    return HttpClient.put<DeadcodeResponse>(`${API_ENPOINTS.DEADCODE}/${repoId}/files`, params);
  };
}
