import { ApiResponse, FileGroup, Paginate, QueryParamsInput } from "@types";

export interface Repository {
  id: string;
  name: string;
  status: keyof typeof RepositoryStatusEnum;
  is_assessed: boolean;
  is_reversed: boolean;
  project_id: string;
  url: string;
  description: string;
}

export interface CreateReponsitoryInput {
  url: string;
  token: string;
  name: string;
  project_id: string;
  description: string;
  system_type: keyof typeof SystemTypeEnum;
}

export enum SystemTypeEnum {
  IBM,
  UNISYS,
  FUJITSU,
  DNP
}

export interface UpdateReponsitoryInput {
  name: string;
  description: string;
  url: string;
  token: string;
  status: keyof typeof RepositoryStatusEnum;
  is_assessed: boolean;
  is_reversed: boolean;
  repository_id: string;
}

export interface DetailRepositoryInput {
  repositoryId: string;
}

export interface PaginatedRepositoriesData<T> extends Paginate {
  repositories: T[];
}

export type RepositoriesResponse = ApiResponse<PaginatedRepositoriesData<Repository>>;

export type DetailRepositoryResponse = ApiResponse<Repository>;

export type RepositoryStatus =
  | "init"
  | "uploaded"
  | "readed"
  | "classified"
  | "parsed"
  | "summarized"
  | "migrated";

export enum RepositoryStatusEnum {
  "init" = 0,
  "uploaded",
  "readed",
  "classified",
  "parsed",
  "running",
  "summarizing",
  "migrating",
  "summarized",
  "migrated"
}

export type RepositoryProject = {
  id: string;
  name: string;
  status: "parsed" | "readed";
  is_assessed: boolean;
  is_reversed: boolean;
};

export type RepositoryProjectResponse = ApiResponse<RepositoryProject>;

export interface DependencyGraphData<T> {
  graph: T;
}
export type DependencyGraphResponse = ApiResponse<DependencyGraphData<DependencyGraph>>;

export interface DependencyGraph {
  repository_id: string;
  nodes: Node[];
  edges: Edge[];
  entry_points: EntryPoint[];
  page: number;
  page_size: number;
  total: number;
}

export interface DependencyGraphInput {
  repoId: string;
  node_limit?: number | null;
  complexity_filter?: number | null;
  loc_filter?: number | null;
  page_number?: number;
  page_limit?: number;
}

export interface Edge {
  _id: string;
  source: string;
  target: string;
  type: Type;
  group: string[];
  properties: Properties;
}
export interface Node {
  _id: string;
  label: string;
  data: { label: string };
  fileType: FileGroup;
  line_of_code?: number | null;
  complexity?: number | null;
  group: string[];
  name: string;
  status: "ALIVE" | "DEAD" | "MISSING";
  is_entry_point: boolean;
}
export interface NodeWithPosition extends Node {
  position: { x: number; y: number };
}

export interface Properties {
  label: Type;
  steps?: Step[];
  calls?: Call[];
}

export interface Call {
  paragraph: string;
  identifier: string[];
  programName: string;
}

export enum Type {
  ExecPgm = "EXEC_PGM",
  HasCopybook = "HAS_COPYBOOK",
  HasInteract = "HAS_INTERACT",
  StaticCall = "STATIC_CALL"
}

export interface Step {
  step_name: string;
  code: Code;
  statements: Statement[];
}

export interface Code {
  content: string;
  start_line: number;
  end_line: number;
}

export interface Statement {
  ddname: string;
  parameters_map: ParametersMap;
  dataset_map_list: DatasetMapList[];
  logic: null | string;
}

export interface DatasetMapList {
  dataset_name: string;
  variable_name: string;
  dd_statement: string;
  program_id: string;
}

export interface ParametersMap {
  SYSOUT?: Sysout;
  UNNAMED_1?: Sysout;
  DISP?: string;
  DSN?: string;
  UNIT?: Unit;
  SPACE?: string;
  DCB?: string;
  LRECL?: string;
  RECFM?: string;
  BLKSIZE?: string;
  SYMBOLS?: string;
  DSORG?: string;
  DLM?: string;
  UNNAMED_2?: Sysout;
}

export enum Sysout {
  Cyl11Rlse = "(CYL,(1,1),RLSE)",
  Dummy = "DUMMY",
  Empty = "*",
  Pend = "PEND"
}

export enum Unit {
  NewCatlgDelete = "(NEW,CATLG,DELETE)",
  Sysda = "SYSDA"
}

export interface EntryPoint {
  _id: string;
  refer_id: string;
  name: string;
  label: LabelEnum;
  group: string[];
  status: StatusEnum;
  is_entry_point: boolean;
  number_of_files: number;
  complexity: number;
  line_of_code: number;
  criticality: Criticality;
}

export interface EntryPointDetail {
  _id: string;
  name: string;
  label: string;
  number_of_files: number;
  complexity: number;
  line_of_code: number;
  criticality: string;
  status: Repository["status"];
}

export enum LabelEnum {
  COBOL = "COBOL",
  JCL = "JCL",
  JCL_IBM = "JCL_IBM",
  JCL_FUJITSU = "JCL_FUJITSU",
  COPY = "COPY",
  DB = "DB",
  SQL = "SQL",
  SCREEN = "SCREEN",
  OTHER = "OTHER",
  BMS = "BMS",
  Utility = "UTILITY",
  CSD = "CSD",
  PLI = "PLI"
}

export enum StatusEnum {
  Alive = "ALIVE",
  Missing = "MISSING",
  Dead = "DEAD"
}

//For getting entry point by repository Id
export interface EntryPointData {
  entry_points: DistributionEntryPoint[];
}
export type EntryPointByRepositoryResponse = ApiResponse<Paginate & EntryPointData>;

export interface DistributionEntryPoint {
  _id: string;
  name: string;
  number_of_files: number;
  complexity: number;
  line_of_code: number;
  criticality: string;
  label: string;
}
export type Criticality = "LOW" | "MEDIUM" | "HIGH";
export interface EntryPointInput extends QueryParamsInput {
  repoId: string;
  loc_filter?: number | null;
  complexity_filter?: number | null;
  number_of_files_filter?: number | null;
  criticality_filter?: Criticality;
  type_filter?: string;
}

export interface DetailEntryPointInput {
  repository_id: string;
  name: string;
  label: string;
}

export type DetailEntryPointResponse = ApiResponse<{ entry_point: EntryPointDetail }>;

export interface CrudRepoInput {
  repository_id: string;
}

export type CrudRepositoryResponse = ApiResponse<CrudItem[]>;
export interface CrudItem {
  program_name: string;
  database_name: string;
  table_name: string;
  invoke_names: string[];
  operations: Operation[];
}

export enum Operation {
  Create = "CREATE",
  Delete = "DELETE",
  Read = "READ",
  Update = "UPDATE"
}
