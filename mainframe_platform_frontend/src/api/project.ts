import { ProjectApiResponse } from "@types";

import { HttpClient } from "./httpClient";
import { API_ENPOINTS } from "./endpoints";

export default class ProjectApi {
  static getProjectList = () => {
    return HttpClient.get<ProjectApiResponse>(API_ENPOINTS.PROJECTS);
  };
}
