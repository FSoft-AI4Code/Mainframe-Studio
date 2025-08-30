import { ApiResponse, QueryParamsInput } from "@types";

export type DuplicateFilesRequest = QueryParamsInput & {
  repoId: string;
};

export type DuplicateFilesResponse = ApiResponse<DuplicateFilesData>;

export interface DuplicateFilesData {
  duplicate_name_groups: DuplicateNameGroup[];
  total_duplicate_files: number;
  total_duplicate_by_content: number;
  total: number;
}

export interface DuplicateNameGroup {
  duplicateType?: "N/A" | "content" | "name" | "both";
  duplicateContentType?: string;
  name: string;
  label: string;
  files: DuplicateFile[];
  has_content_duplicates: boolean;
  content_duplicates: Array<DuplicateFile[]>;
}

export interface DuplicateFile {
  _id: string;
  repository_id: string;
  name: string;
  label: string;
  path: string;
  encoding: string;
  duplicateContentType?: string;
  loc?: number;
}
