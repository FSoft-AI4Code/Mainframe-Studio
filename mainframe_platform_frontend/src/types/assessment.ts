import { ApiResponse, LabelEnum } from "@types";

export interface AssesmentRepository {
  id: string;
  repository_id: string;
  status: string;
  result: AssesmentResult;
  created_at: Date;
  updated_at: Date;
}

export interface AssesmentResult {
  assessment: AssessmentItem[];
  code_dist: CodeDist;
}

export interface AssessmentItem {
  name: string;
  path: string;
  label: LabelEnum;
  code: number;
  comment: number;
}

export interface CodeDist {
  frequencies: number[];
  log_frequencies: number[];
  bins: number[];
}

export interface PaginatedAssesmentRepositoryData<T> {
  assessments: T[];
}

export type AssessmentRepositoryResponse = ApiResponse<
  PaginatedAssesmentRepositoryData<AssesmentRepository>
>;

// For assessment file count by repository and type
export type AssessmentFileCountRepositoryResponse = ApiResponse<AssesmentFileCount>;

export interface AssesmentFileCount {
  total: number;
  file_counts: FileCount[];
}

export interface FileCount {
  count: number;
  label: string;
}
