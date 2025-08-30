import { ApiResponse, Repository } from "@types";

export type ReverseRepositoryResponse = ApiResponse<ReverseRepository>;
export type ReverseRepositoryInput = {
  repoId: string;
  type: string;
  name: string;
};
export interface ReverseRepository {
  status: string;
  output: Output;
}

export interface Output {
  overview: Overview;
  step_list: StepList[];
}

export interface Overview {
  job_name: string;
  class: string;
  msgclass: string;
  notify: string;
  time: null;
  description: string;
}

export type JCLStep = {
  step_name: string;
  program_executed: string;
  description: string;
  dd_statement: Array<{
    ddname: string;
    parameters_map: Record<string, string>;
    dataset_map_list: Array<{
      dataset_name: string;
      variable_name: string;
      dd_statement: string;
      program_id: string;
    }>;
    logic: string | null;
  }>;
  io_statements: string[];
  property: string | null;
};

export interface StepList {
  step_name: string;
  program_executed: string;
  description: null;
  dd_statement: DDStatement[];
  io_statements: unknown[];
  property: null;
}

export interface DDStatement {
  ddname: string;
  parameters_map: ParametersMapReverse;
  dataset_map_list: unknown[];
  logic: null | string;
}

export interface ParametersMapReverse {
  SYSOUT?: string;
  UNNAMED_1?: string;
}

// For listing reverses by repository and type
export interface ReverseListResponse {
  data: Array<ReverseItem>;
}
export type ReverseItem = {
  name: string;
  type: string;
  status: string;
  is_reversed: string;
  output: {
    copy_length: string;
    table_descriptors: Array<DatabaseItem>;
  };
};
export type Operator = "READ" | "CREATE" | "UPDATE" | "DELETE";
export interface DatabaseItem {
  database_name: string;
  table_name: string;
  invoke_names: string[];
  operations: Operator[];
}
export enum ReverseTypeEnum {
  DEFAULT = "DEFAULT",
  COBOL = "COBOL",
  COPY = "COPY",
  BMS = "BMS",
  JCL = "JCL"
}

export interface ReverseListInput {
  repoId: string;
  type?: ReverseTypeEnum;
}

// For getting specific reverse file
export interface ReverseFileInput {
  repoId: string;
  type: ReverseTypeEnum;
  name: string;
}

export interface Variable {
  level: string;
  name: string;
  business_name?: string;
  data_type: string;
  length: string;
  byte_length: number;
  variable_position: number;
  remarks: string;
}

export interface ReverseCopybookResponse {
  data: ReverseCopybookData;
}
export interface ReverseCopybookData {
  output: {
    variables_declaration: Variable[];
    copy_length: string;
  };
  name: string;
  status: Repository["status"];
}

interface WorkingStorageVariable {
  level: string;
  name: string;
  data_type: string;
  length: string;
  default_value: string;
  remarks: string;
}

export type OpenType = "INPUT" | "OUTPUT" | "I-O";
export interface IOFile {
  name: string;
  access_mode: string;
  open_type: OpenType;
  copybooks: Array<{
    copybook_name: string;
    line_number: number;
    replacing: Array<{
      replaceable: string;
      replacement: string;
    }>;
  }>;
}

interface Subroutine {
  name: string;
  business_name: string;
}

export interface VariableFlow {
  name: string;
  data_type: string;
  length: string;
  src_variable: string;
  src_data_type: string;
  src_length: string;
}

export interface CobolProgram {
  program_id: string;
  description: string;
  io_files: IOFile[];
  working_storage_variables: WorkingStorageVariable[];
  subroutines_called: Subroutine[];
  variables_flow: VariableFlow[];
  copybook_list: string[];
  called_program_list: {
    program_id: string;
    line_number: number;
    parameters: string[];
    call_type: string;
  }[];
  exec_flow: ExecFlowData;
  exec_flow_tree: TreeNode;
}

export interface ExecFlowData {
  nodes: {
    id: string;
    type: string;
    name: string;
    section: string | null;
  }[];
  edges: {
    source: string;
    target: string;
    type: string;
  }[];
}

export interface ReverseCobolData {
  status: Repository["status"];
  output: CobolProgram;
}

export enum TypeNodeEnum {
  program,
  subroutine,
  perform,
  paragraph,
  other
}
export type TreeNode = {
  id: string;
  label: string;
  type: keyof typeof TypeNodeEnum;
  children?: TreeNode[];
  name?: string;
  section?: string;
  isRoot: boolean;
  level?: number;
  isExecFlow?: boolean;
  summarization?: string;
};
export interface ReverseBMSData {
  status: Repository["status"];
  output: {
    screen_string: string;
    data: BMSRow[];
  };
}
export interface JCLReportData {
  output: { overview: Overview; step_list: JCLStep[] };
  status: Repository["status"];
}
export interface ReverseDataResponse<T> {
  data: T;
}

// Union type for different response types
export type ReverseFileResponse = ReverseDataResponse<
  ReverseCobolData | ReverseCopybookData | ReverseBMSData | JCLReportData
>;

// For getting specific reverse coverage
export type ReverseCoverageResponse = ApiResponse<ReverseCoverage>;

export interface ReverseCoverage {
  total_coverage: number;
  by_types: CoverageByType[];
}

export interface CoverageByType {
  type: string;
  coverage: number;
}

export interface ReverseCoverageInput {
  repoId: string;
}

// For getting specific BMS report
export type BMSOverview = {
  name: string;
  file_name: string;
  related_pgms: string[];
};

export type BMSRow = {
  no?: number;
  name: string;
  item_type: string;
  length: number;
  attribute: string;
  color: string;
  initial_value: string;
  comment: string;
  position: number[] | null;
  size: number[] | null;
};

export type CopySession = {
  level: string;
  name: string;
  picture_clause: string | null;
  default_value: null;
  redefine: string | null;
  occur: null;
  data_type: string | null;
};

// For trigger report cobol
export interface ReverseReportInput {
  repository_id: string;
  type: string;
  name: string;
}

export type SummarizationDataResponse = ApiResponse<{ summarization: SummarizationData }>;

export interface SummarizationData {
  [key: string]: SummarizationValue;
}

export interface SummarizationValue {
  paragraph_name: string;
  section: null;
  paragraph_code: string;
  paragraph_lines: number[];
  paragraph_logic: string[];
}
