import { CopyGraphBlob, FileBlobModel, IoParamsDef, OverviewBlob, Reference } from "@types";

import { Api, api } from "./config";

class BlobFile {
  instance: Api;

  constructor(params: Api) {
    this.instance = params;
  }

  public getFileDetailRequest = (repoId: string) => {
    return this.instance.get<FileBlobModel>(`/api/blob/${repoId}`);
  };

  public getFileOverview = (repoId: string) => {
    return this.instance.get<OverviewBlob>(`/api/blob/${repoId}/overview`);
  };

  public getFileIOParams = (repoId: string) => {
    return this.instance.get<IoParamsDef>(`/api/blob/${repoId}/io_params`);
  };

  public getFileCopygraph = (repoId: string) => {
    return this.instance.get<CopyGraphBlob>(`/api/blob/${repoId}/copy_graph`);
  };

  public getFileProcessLogic = (repoId: string) => {
    return this.instance.get<Array<string>>(`/api/blob/${repoId}/process_logic`);
  };

  public getFileReferences = (repoId: string) => {
    return this.instance.get<Array<Reference>>(`/api/blob/${repoId}/references`);
  };

  public getBlobFile = (blobFile: string, isCheckStatus?: boolean) => {
    return this.instance.get(
      `/api/blob/${blobFile}/export_report`,
      !isCheckStatus ? { responseType: "blob" } : {}
    ) as unknown as Promise<Blob>;
  };
}

export const blobApi = new BlobFile(api);
