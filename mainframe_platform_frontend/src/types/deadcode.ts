import { ApiResponse, Paginate, QueryParamsInput } from "@types";

//For getting deadcode
export type DeadCodeInput = QueryParamsInput & {
  repoId: string;
};
export type DeadcodeResponse = ApiResponse<DeadcodeData>;

export interface DeadcodeData extends Paginate {
  dead_total: DeadTotal;
  complexity_reduction_percentage: number;
  files: FileDeadCode[];
}

export interface DeadTotal {
  dead: number;
  total: number;
}

export interface FileDeadCode {
  file_name: string;
  lines_of_code: number;
  complexity: number;
}
