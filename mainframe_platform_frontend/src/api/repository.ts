/* eslint-disable @typescript-eslint/no-explicit-any */
import queryString from "query-string";

import {
  ClusterDataType,
  CreateReponsitoryInput,
  CrudRepoInput,
  CrudRepositoryResponse,
  DependencyGraphInput,
  DependencyGraphResponse,
  DetailEntryPointInput,
  DetailEntryPointResponse,
  DetailRepositoryInput,
  DetailRepositoryResponse,
  EntryPointByRepositoryResponse,
  EntryPointInput,
  // NetworkingDataType,
  QueryParamsInput,
  RepoModel,
  RepositoriesResponse,
  Repository,
  RepositoryProjectResponse,
  UpdateReponsitoryInput
} from "@types";

import { API_ENPOINTS } from "./endpoints";
import { HttpClient } from "./httpClient";
export default class RespositoryApi {
  static getRepositoryRequest = (repoId: string) => {
    return HttpClient.get<any>(`${API_ENPOINTS.REPOSITORIES}${repoId}`);
  };

  static postRepositoryRequest = (payload: { url: string; token: string }) => {
    return HttpClient.post<any>(API_ENPOINTS.REPOSITORIES, payload);
  };

  static createRepository = (payload: CreateReponsitoryInput) => {
    return HttpClient.post(API_ENPOINTS.REPOSITORIES, payload);
  };

  static updateRepository = ({ repository_id, ...payload }: UpdateReponsitoryInput) => {
    return HttpClient.put<Repository>(`${API_ENPOINTS.REPOSITORIES}${repository_id}`, payload);
  };

  static deleteRepository = ({ repository_id }: { repository_id: string }) => {
    return HttpClient.delete(`${API_ENPOINTS.REPOSITORIES}${repository_id}`);
  };

  static getEmbedStatusRepositories = (repoId: string) => {
    return HttpClient.post<{ status: string }>(`${API_ENPOINTS.REPOSITORIES}${repoId}/embedd`, {});
  };

  static getProcessStatusRepositories = (repoId: string) => {
    return HttpClient.post(`${API_ENPOINTS.REPOSITORIES}${repoId}/blobs`, {});
  };

  static getDetailFileRepositories = (repoId: string, fileId: string) => {
    return HttpClient.get(`${API_ENPOINTS.REPOSITORIES}${repoId}/blob/${fileId}`);
  };

  static getChatRepositories = (repoId: string, payload: { prompt: string; history: string[] }) => {
    return HttpClient.post(`${API_ENPOINTS.REPOSITORIES}${repoId}/chat`, payload);
  };

  static getGraphRepositories = (repoId: string) => {
    return HttpClient.get(`${API_ENPOINTS.REPOSITORIES_GRAPHS}/${repoId}`);
  };

  static uploadRepositoryRequest = (name: string, form: FormData) => {
    return HttpClient.post<RepoModel>(`${API_ENPOINTS.REPOSITORIES_UPLOAD}?name=${name}`, form, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  };

  static getClusterChartDataRequest = (repoId: string) => {
    return HttpClient.get<ClusterDataType>(`/api/repository/${repoId}/clustering`);
  };

  static getGraphChartDataRequest = (repoId: string) => {
    return HttpClient.get<any>(`/api/repository/${repoId}/copy_graph`);
  };

  static getTreeViewDataRequest = (repoId: string) => {
    return HttpClient.get<any>(`/api/repository/${repoId}/tree_view`);
  };

  static postRepositoryMatchingRequest = (payload: {
    repoId: string;
    url: string;
    token?: string;
  }) => {
    return HttpClient.post<RepoModel>(`api/repository/${payload.repoId}/matching/`, payload);
  };

  static getMatchingScoreDataRequest = (treeId: string) => {
    return HttpClient.get<any>(`/api/tree/${treeId}/matching_score`);
  };

  static getComplexityDataRequest = (repoId: string) => {
    return HttpClient.get<any>(`/api/repository/${repoId}/complexity`);
  };

  static getListRepositories = (params: QueryParamsInput) => {
    return HttpClient.get<RepositoriesResponse>(API_ENPOINTS.REPOSITORIES, params);
  };

  static getDetailRepository = ({ repositoryId }: DetailRepositoryInput) => {
    return HttpClient.get<DetailRepositoryResponse>(`${API_ENPOINTS.REPOSITORIES}${repositoryId}`);
  };

  static postTriggerRepository = (repoId: string) => {
    return HttpClient.post(`/api/repository/${repoId}/export_file`, {});
  };

  static getFileExcelRepository = (repoId: string, isCheckStatus?: boolean) => {
    return HttpClient.get(
      `/api/repository/${repoId}/export_file`,
      !isCheckStatus ? { responseType: "blob" } : {}
    ) as unknown as Promise<Blob>;
  };

  static getReportDeadcodeRepository = (repoId: string) => {
    return HttpClient.get(`/api/repository/${repoId}/deadcode`, {
      responseType: "blob"
    }) as unknown as Promise<Blob>;
  };

  static getAssessmentRepository = (repoId: string) => {
    return HttpClient.get(`/api/repository/${repoId}/assessment`, {
      responseType: "blob"
    }) as unknown as Promise<Blob>;
  };

  static getRepositoriesProject = (projectId: string) => {
    return HttpClient.get<RepositoryProjectResponse>(`/repositories/project/${projectId}`);
  };

  static parseRepositoryData = (repoId: string) => {
    return HttpClient.post(`/repositories/${repoId}/parsed_data`, { repository_id: repoId });
  };

  static getDependencyGraph = ({ repoId, ...params }: DependencyGraphInput) => {
    const queryStr = queryString.stringify(params, { skipEmptyString: true, skipNull: true });
    return HttpClient.get<DependencyGraphResponse>(
      `${API_ENPOINTS.REPOSITORIES}${repoId}/dependency_graph?${queryStr}`
    );
  };

  static getEntryPoints = ({ repoId, ...params }: EntryPointInput) => {
    return HttpClient.get<EntryPointByRepositoryResponse>(
      `/repositories/${repoId}/entrypoints`,
      params
    );
  };

  static getCrudRepository = ({ repository_id }: CrudRepoInput) => {
    return HttpClient.get<CrudRepositoryResponse>(
      `${API_ENPOINTS.REPOSITORIES}${repository_id}/crud`
    );
  };

  static getDetailEntryPointByName = ({
    repository_id,
    name,
    ...params
  }: DetailEntryPointInput) => {
    return HttpClient.get<DetailEntryPointResponse>(
      `repositories/${repository_id}/entrypoints/${name}`,
      params
    );
  };
}
