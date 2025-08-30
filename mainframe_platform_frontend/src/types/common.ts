export type Status = "active" | "inactive";

export type SortType = "descending" | "ascending";

export type Isignal = { signal?: AbortSignal };

// eslint-disable-next-line
export type Pagination<T = {}> = {
  items: T[] | null;
  pagination: {
    totalRecords: number;
    totalPages: number;
    currentPage: number;
  };
};

export type PaginationSortItem = {
  field: string;
  sort: SortType;
};

export type PaginationQueries = {
  page: number;
  pageSize: number;
  keyword?: string;
  sort?: PaginationSortItem[];
  filter?: [string, string[]][];
};

export interface ApiResponse<T> {
  success: boolean;
  message: string;
  data: T;
}

export interface Paginate {
  total: number;
  skip: number;
  limit: number;
}
export interface QueryParamsInput {
  skip?: number;
  limit?: number;
}
