import { ApiResponse } from "@types";

export interface ComplexityRepository {
  id: string;
  repository_id: string;
  status: string;
  result?: {
    complexity: ComplexityResult[];
  };
  created_at: Date;
  updated_at: Date;
}

export interface ComplexityResult {
  name: string;
  path: string;
  label: string;
  complexity: number;
  complexity_category: string;
}

export interface PaginatedComplexityRepositoryData<T> {
  complexities: T[];
}

export type ComplexityRepositoryResponse = ApiResponse<
  PaginatedComplexityRepositoryData<ComplexityRepository>
>;

//For getting complexity distribution
export interface ComplexityDistributionInput {
  repoId: string;
  reprocess: boolean;
}

export interface ResultComplexity {
  dist: DistComplexity;
  average_complexity: number;
  number_of_complexities: number;
}

export interface DistComplexity {
  frequencies: number[];
  log_frequencies: number[];
  bins: number[];
}

export interface ComplexityDistributionData {
  _id: string;
  repository_id: string;
  result: ResultComplexity;
  status: string;
  created_at: string;
  updated_at: string;
}

export type ComplexityDistributionResponse = ApiResponse<ComplexityDistributionData>;
