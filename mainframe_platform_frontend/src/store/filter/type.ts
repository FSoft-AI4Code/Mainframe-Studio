export interface DatabaseFilterState {
  searchText: string;
  searchTable: string;
  type: string[];
  status: string | null;
  page?: number;
}
export type ReportFilter = {
  searchText: string;
  type: string | null;
  status: string | null;
  page?: number;
};

export interface GlobalFilterState {
  reports: ReportFilter;
  database: DatabaseFilterState;
}
