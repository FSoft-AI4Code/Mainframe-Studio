import { ApiResponse } from "@types";

//For getting inference modernization
export type ModernizationInput = {
  repository_id: string;
  type: string;
  name: string;
};

export type ModernizationResponse = ApiResponse<{ url: string }>;

//For trigger summarization
export type SummarizationBmsInput = {
  repository_id: string;
  file_name: string;
};

export type SummarizationBmsResponse = ApiResponse<{ url: string }>;
