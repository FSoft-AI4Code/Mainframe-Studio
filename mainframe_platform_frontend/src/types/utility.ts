import { ApiResponse, Paginate, QueryParamsInput } from "@types";

export type UtilitiesFileRequest = QueryParamsInput & {
  repoId: string;
};

export interface PaginatedUtilitiesData<T> extends Paginate {
  utilities: T[];
}

export type UtilitiesFilesResponse = ApiResponse<PaginatedUtilitiesData<UtilityFile>>;

export interface UtilityFile {
  name: string;
  description: string;
  category: string;
  node_id: string;
  repository_id: string;
  comment: string;
  created_at: string;
  updated_at: string;
  _id: string;
}

export interface CreateUtilityRequest {
  repository_id: string;
  file_name: string;
  label: string;
  category_name: string;
  description: string;
  comment: string;
}
export interface UpdateUtilityRequest {
  description: string;
  category: string;
  utility_id: string;
  comment: string;
  updated_at?: string;
}
export type CategoryUtilityResponse = ApiResponse<CategoryUtilityData>;

export type CategoryUtilityData = Record<string, number>;

export type InputType = "input" | "select" | "textarea" | "switch";
export type DataType = "string" | "string[]";
export type Mode = "single" | "multiple" | null;
export interface FormField {
  name: string;
  inputType: InputType;
  dataType: DataType;
  required: boolean;
  options?: string[];
  mode: Mode;
}

export type FieldsUtilityByTypeResponse = ApiResponse<FormField[]>;
