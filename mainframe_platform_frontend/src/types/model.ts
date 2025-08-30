import { ElementViews } from "@store";

import { Status } from "./common";

export type FileGroup =
  | "COBOL"
  | "JCL"
  | "JCL_IBM"
  | "JCL_FUJITSU"
  | "COPY"
  | "DB"
  | "SQL"
  | "SCREEN"
  | "OTHER"
  | "BMS"
  | "UTILITY"
  | "CSD"
  | "PLI";

export type UserModel = {
  id: string;
  email: string;
  firstName: string;
  lastName: string;
  isVerified: boolean;
  createdAt: string;
  username?: string;
  updatedAt: string;
  avatar?: string;
  status: Status;
  token?: string | null;
};

export type TokenModel = UserModel & {
  exp: number;
};

export type ClusterDataType = {
  cluster: Record<string, number>;
  path: Record<string, string>;
  x1: Record<string, number>;
  x2: Record<string, number>;
  name: Record<string, string>;
  start_line: Record<string, string>;
};

export type NodeGraphType = {
  id: string;
  group: FileGroup;
  name: string;
  path: string;
  type?: "blob";
  is_deadcode?: boolean;
  mime_type: string;
  summarization?: string;
  display_name?: string;
  db_table?: {
    name?: string;
    type?: string;
  }[];
  copy_table?: {
    name?: string;
    type?: string;
  }[];
  short_description?: string;
};

export type LinkGraphType = {
  source: string;
  target: string;
  content?: string;
};

export type NetworkingDataType = {
  nodes: Array<NodeGraphType>;
  links: Array<LinkGraphType>;
};

export type MetaData = {
  cobol_blob_id: string;
  cobol_repo_id?: string;
  matching_score: number;
};

export type File = {
  id: string;
  type: "blob";
  name: string;
  path: string;
  mime_type: string;
  content?: string;
  parentId?: string;
  brothers?: File[] | Folder[];
  metadata?: MetaData;
};

export type Folder = {
  type: "tree";
  id: string;
  name: string;
  path: string;
  children?: (Folder | File)[];
  parentId?: string;
  metadata?: MetaData;
};

export type TreeView = (Folder | File)[];

type StatKeys =
  | "tokens"
  | "lines"
  | "sections"
  | "paragraphs"
  | "statements"
  | "ifstatements"
  | "gotostatements"
  | "performstatements";
export type Stats = Record<StatKeys, [[number, string]]>;

export type ComplexityModel = {
  C_cobol: number;
  C_jcl: number;
  C_asm: number;
  C_sum: number;
  diff: string;
  num_Cobol_files: number;
  avg_Cobol_LOCs: number;
  avg_Cobol_Cyc: number;
  avg_Cobol_n_tokens: number;
  avg_Cobol_n_operators: number;
  num_JCL_files: number;
  avg_JCL_LOCs: number;
  avg_JCL_Cyc: number;
  avg_JCL_n_tokens: number;
  avg_JCL_n_operators: number;
  num_ASMs: number;
  avg_ASM_LOCs: number;
  avg_ASM_Cyc: number;
  avg_ASM_n_tokens: number;
  avg_ASM_n_operators: number;
};

export type RepoStatus = "processing" | "processed" | "error";

export type RepoOverviewModel = {
  id: string;
  name: string;
  url: string;
  type: "cobol";
  created_at: string;
  status: RepoStatus;
};

export type DataAssetModel = {
  dataset_name: string;
  variable_name: string;
  jcl_path: string;
  dd_statement: string;
  program_id: string;
  program_path: string;
  access_mode: string;
  copybook: string;
  copybook_path: string;
  data_structure: string;
};

export type Message = {
  id?: string;
  content: string;
  role: "user" | "assistant";
  type?: ElementViews;
  action?:
    | "upload_repository"
    | "assess_repository"
    | "reverse_repository"
    | "check_assessment_status"
    | "response_success";
  loading?: boolean;
  isPending?: boolean;
  isTyping?: boolean;
};

export type RepoModel = {
  created_at: string;
  name: string;
  status: RepoStatus;
  updated_at: string;
  metadata?: MetaData;
  url: string;
  id: string;
  done?: boolean;
  stats: Stats | null;
  tree_view: TreeView | null;
  clusters: ClusterDataType | null;
  copy_graph: NetworkingDataType | null;
  complexity: ComplexityModel | null;
};

export type NodeModel = {
  name: string;
  start_line: string;
  end_line: string;
  type: string;
  code_content: string;
  shapeRendering?: string;
  summarization: string[] | string;
};

type Iotable = {
  index: number;
  item_name: string;
  physical_name: string;
  type: string;
  crud_op: string;
  access_mode: string;
  notes: string;
};

export type Inputtable = {
  item_name: string;
  cobol_level: string;
  cobol_dtype?: string;
  length?: string;
  access_mode: string;
  dtype?: string;
  default_value?: string;
  remarks: string;
};

export type IoParamsDef = {
  input_table: Inputtable[];
  input_note: string;
  output_table: Inputtable[];
  output_note: string;
};

export type Program = {
  index: number;
  program_id: string;
  program_type: string;
  program_name: string;
  call_type: string;
  notes: string;
  locations: string;
};
export type CopyGraphBlob = {
  programs: Program[];
  details: string[];
};

export type OverviewBlob = {
  program_name: string;
  io_files: never[];
  db_accesses: Array<{
    file: string;
    library: string;
    name: string;
    type: string;
    usage_number: string;
  }>;
  copy_files: never[];
  call_files: never[];
  summarization: string;
  io_table: Iotable[];
};

type SubReference = {
  command: string;
  explain: string;
};

export type Reference = SubReference & {
  sub_commands?: Array<SubReference>;
};

export type OverviewDatabaseColumn = {
  item_name: string;
  data_type: string;
  nallable: boolean;
  cobol_item_name: string;
  cobol_level: number;
  cobol_data_type: string;
  length: number;
  default_value: string;
  comment: string;
};

export type DatabaseOverview = {
  database_name: string;
  database_file: string;
  related_pgs: string;
  table: Array<OverviewDatabaseColumn>;
};

export type DatabaseAccessColumn = {
  file_name: string;
  nallable: string;
  query: string;
};

export type DatabaseAccessBlob = {
  table: Array<DatabaseAccessColumn>;
};

export type CopybookDataColumn = {
  item_name: string;
  cobol_level: string;
  cobol_data_type: string;
  length: number;
  default_value: string;
  comment: string;
};

export type CopybookOverview = {
  name: string;
  subset: string;
  superset: string;
  related_pgms: string;
  table: Array<CopybookDataColumn>;
};

export type FileBlobModel = {
  _id: string;
  repo_id: string;
  type: "blob";
  name: string;
  path: string;
  display_name?: string;
  mime_type: string;
  updated_at: string;
  created_at: string;
  status: string;
  content: string;
  deadcode?: boolean;
  group: FileGroup;
  overview?: OverviewBlob | DatabaseOverview | CopybookOverview;
  references: Reference[];
  io_params_def?: IoParamsDef;
  process_logic?: string[];
  copy_graph?: CopyGraphBlob;
  access?: DatabaseAccessBlob;
  meta: {
    copy_files: string[];
    select_files: string[];
    call_files: string[];
    "input/output": string;
    flow: string;
    explanation: string;
    sections: {
      name: string;
      start_line: string;
      end_line: string;
      section_type: string;
      code: string;
      embeddings: number[];
    }[];
    code: string;
  } | null;
  stats: {
    NTokens: number;
    NSections: number;
    NLines: number;
    N_programIdParagraphs: number;
    N_specialNamesParagraphs: number;
    N_specialNameStatements: number;
    N_fileControlParagraphs: number;
    N_copyStatements: number;
    N_paragraphs: number;
    N_statements: number;
    N_acceptStatements: number;
    N_performStatements: number;
    N_ifStatements: number;
    N_goToStatements: number;
    N_moveStatements: number;
    N_callStatements: number;
    N_displayStatements: number;
    N_stopStatements: number;
    N_openStatements: number;
    N_rewriteStatements: number;
    N_unlockStatements: number;
    N_closeStatements: number;
    N_cancelStatements: number;
    N_stringStatements: number;
    N_exitStatements: number;
    N_compilerStatements: number;
    N_evaluateStatements: number;
    N_computeStatements: number;
    N_readStatements: number;
    N_writeStatements: number;
    N_addStatements: number;
  } | null;
  flow_graph: {
    nodes: NodeModel[];
    links: {
      source: string;
      target: string;
      label: string;
    }[];
  } | null;
};
