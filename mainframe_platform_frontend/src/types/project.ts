import { ApiResponse, Paginate } from "./common";

export interface Project {
  id: string;
  name: string;
  description: string;
  user_id: string;
}

export interface PaginatedProjectsData<T> extends Paginate {
  projects: T[];
}

export type ProjectApiResponse = ApiResponse<PaginatedProjectsData<Project>>;
