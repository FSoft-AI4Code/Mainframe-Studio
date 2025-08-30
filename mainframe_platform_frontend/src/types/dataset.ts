import { ApiResponse, Paginate, QueryParamsInput } from "@types";

export interface PaginatedDatasetData<T> extends Paginate {
  dataset_assignments: T[];
}
export type DatasetResponse = ApiResponse<PaginatedDatasetData<DataSetInfo>>;

export type AccessOperation = {
  open_by_program_id: string;
  open_mode: "INPUT" | "OUTPUT" | "INOUT";
};

export type DataSetInfo = {
  repository_id: string;
  step: string;
  jcl_name: string;
  exec_program_id: string;
  dataset_name: string;
  ddname: string;
  dataset_type: string;
  access_operations: AccessOperation[];
};

export interface DatasetsInput extends QueryParamsInput {
  repository_id: string;
  file_name?: string | null;
  job_name?: string | null;
  program_name?: string | null;
  step_name?: string | null;
  assign_name?: string | null;
  file_type?: string | null;
  open_mode?: string | null;
  enabled?: boolean;
}
export interface StatisticDatasetsInput {
  repository_id: string;
  file_name?: string | null;
  job_name?: string | null;
  program_name?: string | null;
  step_name?: string | null;
  assign_name?: string | null;
  file_type?: string | null;
  open_mode?: string | null;
  enabled?: boolean;
}
export type ViewExportType = "job" | "file";
export interface ExportDatasetsInput {
  repository_id: string;
  file_name?: string | null;
  view: ViewExportType;
  job_name?: string | null;
  program_name?: string | null;
  step_name?: string | null;
  assign_name?: string | null;
  file_type?: string | null;
  open_mode?: string | null;
  enabled?: boolean;
}

export type StatisticDatasetsResponse = ApiResponse<StatisticDatasets>;

export interface StatisticDatasets {
  files: number;
  vsam_files: number;
  flat_files: number;
  steps: number;
  programs: number;
  jobs: number;
}

export interface AvailableFilterData {
  dataset_type: string[];
  open_mode: string[];
}

export interface AvailableFilterParams {
  repository_id: string;
}

export type AvailableFilterResponse = ApiResponse<AvailableFilterData>;
