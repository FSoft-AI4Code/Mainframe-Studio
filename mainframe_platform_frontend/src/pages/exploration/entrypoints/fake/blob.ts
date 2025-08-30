/* eslint-disable @typescript-eslint/no-explicit-any */
import { FileGroup } from "@types";

export type IORow = {
  index: number;
  item_name: string;
  physical_name: string;
  type: string;
  crud_op: string;
  access_mode: string;
  notes: string;
};

export type ParagraphLevel = {
  paragraph_name: string;
  section: string;
  paragraph_code: string;
  paragraph_lines: number[];
  ref_paragraphs: string[];
  paragraph_logic: string[];
};

export type CopyGraphProgram = {
  index: number;
  program_id: string;
  program_type: string;
  program_name: string;
  call_type: string;
  notes: string;
  locations: string;
  paragraph: string;
  identifier: any[];
};

export type OverviewProgram = {
  programe_name: string;
  io_files: string[];
  db_accesses: string[];
  copy_files: string[];
  call_files: string[];
  summarization: string;
  io_table: IORow[];
};

export type IOParams = {
  input_table: Array<any>;
  input_note: string;
  output_table: Array<any>;
  output_note: string;
};

export type BlobData = {
  id: string;
  name: string;
  path: string;
  label: FileGroup;
  overview: OverviewProgram;
  io_params_def: IOParams;
  process_logic: {
    paragraph_level: Record<string, ParagraphLevel>;
  };
  copy_graph: {
    programs: CopyGraphProgram[];
    details: string[];
  };
};

export type BMSOverview = {
  name: string;
  file_name: string;
  related_pgms: string[];
};

// export type BMSRow = {
//   no?: number;
//   name: string;
//   item_type: string;
//   length: number;
//   attribute: string;
//   color: string;
//   initial_value: string;
//   comment: string;
//   position: number[] | null;
//   size: number[] | null;
// };

// export type JCLStep = {
//   step_name: string;
//   program_executed: string;
//   description: string;
//   dd_statement: Array<{
//     ddname: string;
//     parameters_map: Record<string, string>;
//     dataset_map_list: Array<{
//       dataset_name: string;
//       variable_name: string;
//       dd_statement: string;
//       program_id: string;
//     }>;
//     logic: string | null;
//   }>;
//   io_statements: string[];
//   property: string | null;
// };

// export type CopySession = {
//   level: string;
//   name: string;
//   picture_clause: string | null;
//   default_value: null;
//   redefine: string | null;
//   occur: null;
//   data_type: string | null;
// };

// export const copyBlobData: Array<CopySession> = [
//   {
//     level: "01",
//     name: "COUSR3AI",
//     picture_clause: null,
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(12)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "TRNNAMEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "TRNNAMEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEI",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01L",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "TITLE01F",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "TITLE01F",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "TITLE01A",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01I",
//     picture_clause: "X(40)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "CURDATEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "CURDATEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "CURDATEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEI",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "PGMNAMEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "PGMNAMEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEI",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02L",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "TITLE02F",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "TITLE02F",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "TITLE02A",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02I",
//     picture_clause: "X(40)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "CURTIMEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "CURTIMEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "CURTIMEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEI",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "USRIDINF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "USRIDINF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "USRIDINA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINI",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "FNAMEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "FNAMEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "FNAMEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEI",
//     picture_clause: "X(20)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "LNAMEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "LNAMEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "LNAMEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEI",
//     picture_clause: "X(20)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "USRTYPEF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "USRTYPEF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "USRTYPEA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEI",
//     picture_clause: "X(1)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGL",
//     picture_clause: "S9(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "numeric"
//   },
//   {
//     level: "02",
//     name: "ERRMSGF",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: null,
//     default_value: null,
//     redefine: "ERRMSGF",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "03",
//     name: "ERRMSGA",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGI",
//     picture_clause: "X(78)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "01",
//     name: "COUSR3AO",
//     picture_clause: null,
//     default_value: null,
//     redefine: "COUSR3AI",
//     occur: null,
//     data_type: null
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(12)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TRNNAMEO",
//     picture_clause: "X(4)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01C",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01P",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01H",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01V",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE01O",
//     picture_clause: "X(40)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURDATEO",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "PGMNAMEO",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02C",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02P",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02H",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02V",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "TITLE02O",
//     picture_clause: "X(40)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "CURTIMEO",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRIDINO",
//     picture_clause: "X(8)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FNAMEO",
//     picture_clause: "X(20)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "LNAMEO",
//     picture_clause: "X(20)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "USRTYPEO",
//     picture_clause: "X(1)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "FILLER",
//     picture_clause: "X(3)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGC",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGP",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGH",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGV",
//     picture_clause: "X",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   },
//   {
//     level: "02",
//     name: "ERRMSGO",
//     picture_clause: "X(78)",
//     default_value: null,
//     redefine: null,
//     occur: null,
//     data_type: "char"
//   }
// ];

// export const jclBlobData: Array<JCLStep> = [
//   {
//     step_name: "STEP05",
//     program_executed: "IDCAMS",
//     description: "Access Method Services",
//     dd_statement: [
//       {
//         ddname: "SYSPRINT",
//         parameters_map: {
//           SYSOUT: "*"
//         },
//         dataset_map_list: [],
//         logic: null
//       },
//       {
//         ddname: "SYSIN",
//         parameters_map: {
//           UNNAMED_1: "*"
//         },
//         dataset_map_list: [],
//         logic:
//           "   DELETE FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS -\r\n          CLUSTER\r\n   IF MAXCC LE 08 THEN SET MAXCC = 0\r\n"
//       }
//     ],
//     io_statements: [],
//     property: null
//   },
//   {
//     step_name: "STEP10",
//     program_executed: "IDCAMS",
//     description: "Access Method Services",
//     dd_statement: [
//       {
//         ddname: "SYSPRINT",
//         parameters_map: {
//           SYSOUT: "*"
//         },
//         dataset_map_list: [],
//         logic: null
//       },
//       {
//         ddname: "SYSIN",
//         parameters_map: {
//           UNNAMED_1: "*"
//         },
//         dataset_map_list: [],
//         logic:
//           "   DEFINE CLUSTER (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS)     -\r\n          CYLINDERS(1 5)                                              -\r\n          VOLUMES(USER04)                                             -\r\n          KEYS(11 0)                                                  -\r\n          RECORDSIZE(300 300)                                         -\r\n          SHAREOPTIONS(2 3)                                           -\r\n          ERASE                                                       -\r\n          INDEXED                                                     -\r\n          )                                                           -\r\n          DATA (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.DAT))   -\r\n          INDEX (NAME(FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS.IDX))\r\n"
//       }
//     ],
//     io_statements: [],
//     property: null
//   },
//   {
//     step_name: "STEP15",
//     program_executed: "IDCAMS",
//     description: "Access Method Services",
//     dd_statement: [
//       {
//         ddname: "SYSPRINT",
//         parameters_map: {
//           SYSOUT: "*"
//         },
//         dataset_map_list: [],
//         logic: null
//       },
//       {
//         ddname: "ACCTDATA",
//         parameters_map: {
//           DISP: "SHR",
//           DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS"
//         },
//         dataset_map_list: [
//           {
//             dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS",
//             variable_name: "ACCTDATA",
//             dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS",
//             program_id: "IDCAMS"
//           }
//         ],
//         logic: null
//       },
//       {
//         ddname: "ACCTVSAM",
//         parameters_map: {
//           DISP: "SHR",
//           DSN: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS"
//         },
//         dataset_map_list: [
//           {
//             dataset_name: "FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
//             variable_name: "ACCTVSAM",
//             dd_statement: "DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS",
//             program_id: "IDCAMS"
//           }
//         ],
//         logic: null
//       },
//       {
//         ddname: "SYSIN",
//         parameters_map: {
//           UNNAMED_1: "*"
//         },
//         dataset_map_list: [],
//         logic: "   REPRO INFILE(ACCTDATA) OUTFILE(ACCTVSAM)\r\n"
//       }
//     ],
//     io_statements: [
//       "ACCTDATA: DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.PS\n",
//       "ACCTVSAM: DSN=FPTLT01.DEMO.CARDDEMO.ACCTDATA.VSAM.KSDS\n"
//     ],
//     property:
//       "STEP15 uses IDCAMS to copy data from a sequential file (ACCTDATA) to a VSAM KSDS file (ACCTVSAM)."
//   }
// ];

// export const bmsBlobData: {
//   overview: BMSOverview;
//   data: BMSRow[];
//   screen_string: string;
// } = {
//   overview: {
//     name: "COACTUP",
//     file_name: "COACTUP",
//     related_pgms: []
//   },
//   data: [
//     {
//       name: "COACTUP",
//       item_type: "DFHMSD",
//       position: null,
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "CACTUPA",
//       item_type: "DFHMDI",
//       position: null,
//       size: [24, 80],
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [1, 1],
//       size: null,
//       length: 5,
//       attribute: "(ASKIP,NORM)",
//       color: "BLUE",
//       initial_value: "Tran:",
//       comment: ""
//     },
//     {
//       name: "TRNNAME",
//       item_type: "DFHMDF",
//       position: [1, 21],
//       size: null,
//       length: 40,
//       attribute: "",
//       color: "YELLOW",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [1, 65],
//       size: null,
//       length: 5,
//       attribute: "(ASKIP,NORM)",
//       color: "BLUE",
//       initial_value: "Date:",
//       comment: ""
//     },
//     {
//       name: "CURDATE",
//       item_type: "DFHMDF",
//       position: [1, 71],
//       size: null,
//       length: 8,
//       attribute: "(ASKIP,NORM)",
//       color: "BLUE",
//       initial_value: "mm/dd/yy",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [2, 1],
//       size: null,
//       length: 5,
//       attribute: "(ASKIP,NORM)",
//       color: "BLUE",
//       initial_value: "Prog:",
//       comment: ""
//     },
//     {
//       name: "PGMNAME",
//       item_type: "DFHMDF",
//       position: [2, 21],
//       size: null,
//       length: 40,
//       attribute: "",
//       color: "YELLOW",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [2, 65],
//       size: null,
//       length: 5,
//       attribute: "(ASKIP,NORM)",
//       color: "BLUE",
//       initial_value: "Time:",
//       comment: ""
//     },
//     {
//       name: "CURTIME",
//       item_type: "DFHMDF",
//       position: [2, 71],
//       size: null,
//       length: 8,
//       attribute: "(ASKIP,NORM)",
//       color: "BLUE",
//       initial_value: "hh:mm:ss",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [4, 33],
//       size: null,
//       length: 14,
//       attribute: "",
//       color: "NEUTRAL",
//       initial_value: "Update Account",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [5, 19],
//       size: null,
//       length: 16,
//       attribute: "(ASKIP,NORM)",
//       color: "TURQUOISE",
//       initial_value: "Account Number :",
//       comment: ""
//     },
//     {
//       name: "ACCTSID",
//       item_type: "DFHMDF",
//       position: [5, 38],
//       size: null,
//       length: 11,
//       attribute: "(IC,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [5, 50],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [5, 57],
//       size: null,
//       length: 12,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Active Y/N: ",
//       comment: ""
//     },
//     {
//       name: "ACSTTUS",
//       item_type: "DFHMDF",
//       position: [5, 70],
//       size: null,
//       length: 1,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [5, 72],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [6, 8],
//       size: null,
//       length: 8,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Opened :",
//       comment: ""
//     },
//     {
//       name: "OPNYEAR",
//       item_type: "DFHMDF",
//       position: [6, 17],
//       size: null,
//       length: 4,
//       attribute: "(FSET,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [6, 22],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "OPNMON",
//       item_type: "DFHMDF",
//       position: [6, 24],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [6, 27],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "OPNDAY",
//       item_type: "DFHMDF",
//       position: [6, 29],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [6, 32],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [6, 39],
//       size: null,
//       length: 21,
//       attribute: "(ASKIP,NORM)",
//       color: "TURQUOISE",
//       initial_value: "Credit Limit        :",
//       comment: ""
//     },
//     {
//       name: "ACRDLIM",
//       item_type: "DFHMDF",
//       position: [6, 61],
//       size: null,
//       length: 15,
//       attribute: "(FSET,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [6, 77],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [7, 8],
//       size: null,
//       length: 8,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Expiry :",
//       comment: ""
//     },
//     {
//       name: "EXPYEAR",
//       item_type: "DFHMDF",
//       position: [7, 17],
//       size: null,
//       length: 4,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [7, 22],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "EXPMON",
//       item_type: "DFHMDF",
//       position: [7, 24],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [7, 27],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "EXPDAY",
//       item_type: "DFHMDF",
//       position: [7, 29],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [7, 32],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [7, 39],
//       size: null,
//       length: 21,
//       attribute: "(ASKIP,NORM)",
//       color: "TURQUOISE",
//       initial_value: "Cash credit Limit   :",
//       comment: ""
//     },
//     {
//       name: "ACSHLIM",
//       item_type: "DFHMDF",
//       position: [7, 61],
//       size: null,
//       length: 15,
//       attribute: "(FSET,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [7, 77],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [8, 8],
//       size: null,
//       length: 8,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Reissue:",
//       comment: ""
//     },
//     {
//       name: "RISYEAR",
//       item_type: "DFHMDF",
//       position: [8, 17],
//       size: null,
//       length: 4,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [8, 22],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "RISMON",
//       item_type: "DFHMDF",
//       position: [8, 24],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [8, 27],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "RISDAY",
//       item_type: "DFHMDF",
//       position: [8, 29],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [8, 32],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [8, 39],
//       size: null,
//       length: 21,
//       attribute: "(ASKIP,NORM)",
//       color: "TURQUOISE",
//       initial_value: "Current Balance     :",
//       comment: ""
//     },
//     {
//       name: "ACURBAL",
//       item_type: "DFHMDF",
//       position: [8, 61],
//       size: null,
//       length: 15,
//       attribute: "(FSET,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [8, 77],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [9, 39],
//       size: null,
//       length: 21,
//       attribute: "(ASKIP,NORM)",
//       color: "TURQUOISE",
//       initial_value: "Current Cycle Credit:",
//       comment: ""
//     },
//     {
//       name: "ACRCYCR",
//       item_type: "DFHMDF",
//       position: [9, 61],
//       size: null,
//       length: 15,
//       attribute: "(FSET,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [9, 77],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [10, 8],
//       size: null,
//       length: 14,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Account Group:",
//       comment: ""
//     },
//     {
//       name: "AADDGRP",
//       item_type: "DFHMDF",
//       position: [10, 23],
//       size: null,
//       length: 10,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [10, 34],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [10, 39],
//       size: null,
//       length: 21,
//       attribute: "(ASKIP,NORM)",
//       color: "TURQUOISE",
//       initial_value: "Current Cycle Debit :",
//       comment: ""
//     },
//     {
//       name: "ACRCYDB",
//       item_type: "DFHMDF",
//       position: [10, 61],
//       size: null,
//       length: 15,
//       attribute: "(FSET,UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [10, 77],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [11, 32],
//       size: null,
//       length: 16,
//       attribute: "",
//       color: "NEUTRAL",
//       initial_value: "Customer Details",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [12, 8],
//       size: null,
//       length: 14,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Customer id  :",
//       comment: ""
//     },
//     {
//       name: "ACSTNUM",
//       item_type: "DFHMDF",
//       position: [12, 23],
//       size: null,
//       length: 9,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [12, 33],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [12, 49],
//       size: null,
//       length: 4,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "SSN:",
//       comment: ""
//     },
//     {
//       name: "ACTSSN1",
//       item_type: "DFHMDF",
//       position: [12, 55],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "999",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [12, 59],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "ACTSSN2",
//       item_type: "DFHMDF",
//       position: [12, 61],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "99",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [12, 64],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "ACTSSN3",
//       item_type: "DFHMDF",
//       position: [12, 66],
//       size: null,
//       length: 4,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "9999",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [12, 71],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [13, 8],
//       size: null,
//       length: 14,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Date of birth:",
//       comment: ""
//     },
//     {
//       name: "DOBYEAR",
//       item_type: "DFHMDF",
//       position: [13, 23],
//       size: null,
//       length: 4,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [13, 28],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "DOBMON",
//       item_type: "DFHMDF",
//       position: [13, 30],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [13, 33],
//       size: null,
//       length: 1,
//       attribute: "",
//       color: "",
//       initial_value: "-",
//       comment: ""
//     },
//     {
//       name: "DOBDAY",
//       item_type: "DFHMDF",
//       position: [13, 35],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [13, 38],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [13, 49],
//       size: null,
//       length: 11,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "FICO Score:",
//       comment: ""
//     },
//     {
//       name: "ACSTFCO",
//       item_type: "DFHMDF",
//       position: [13, 62],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [13, 66],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [14, 1],
//       size: null,
//       length: 10,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "First Name",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [14, 28],
//       size: null,
//       length: 13,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Middle Name: ",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [14, 55],
//       size: null,
//       length: 12,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Last Name : ",
//       comment: ""
//     },
//     {
//       name: "ACSFNAM",
//       item_type: "DFHMDF",
//       position: [15, 1],
//       size: null,
//       length: 25,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [15, 27],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSMNAM",
//       item_type: "DFHMDF",
//       position: [15, 28],
//       size: null,
//       length: 25,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [15, 54],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSLNAM",
//       item_type: "DFHMDF",
//       position: [15, 55],
//       size: null,
//       length: 25,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [16, 1],
//       size: null,
//       length: 8,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Address:",
//       comment: ""
//     },
//     {
//       name: "ACSADL1",
//       item_type: "DFHMDF",
//       position: [16, 10],
//       size: null,
//       length: 50,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [16, 61],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [16, 63],
//       size: null,
//       length: 6,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "State ",
//       comment: ""
//     },
//     {
//       name: "ACSSTTE",
//       item_type: "DFHMDF",
//       position: [16, 73],
//       size: null,
//       length: 2,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [16, 76],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSADL2",
//       item_type: "DFHMDF",
//       position: [17, 10],
//       size: null,
//       length: 50,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [17, 61],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [17, 63],
//       size: null,
//       length: 3,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Zip",
//       comment: ""
//     },
//     {
//       name: "ACSZIPC",
//       item_type: "DFHMDF",
//       position: [17, 73],
//       size: null,
//       length: 5,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [17, 79],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [18, 1],
//       size: null,
//       length: 5,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "City ",
//       comment: ""
//     },
//     {
//       name: "ACSCITY",
//       item_type: "DFHMDF",
//       position: [18, 10],
//       size: null,
//       length: 50,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [18, 61],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [18, 63],
//       size: null,
//       length: 7,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Country",
//       comment: ""
//     },
//     {
//       name: "ACSCTRY",
//       item_type: "DFHMDF",
//       position: [18, 73],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [18, 77],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [19, 1],
//       size: null,
//       length: 8,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Phone 1:",
//       comment: ""
//     },
//     {
//       name: "ACSPH1A",
//       item_type: "DFHMDF",
//       position: [19, 10],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSPH1B",
//       item_type: "DFHMDF",
//       position: [19, 14],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSPH1C",
//       item_type: "DFHMDF",
//       position: [19, 18],
//       size: null,
//       length: 4,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [19, 23],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [19, 24],
//       size: null,
//       length: 30,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Government Issued Id Ref    : ",
//       comment: ""
//     },
//     {
//       name: "ACSGOVT",
//       item_type: "DFHMDF",
//       position: [19, 58],
//       size: null,
//       length: 20,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [19, 79],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [20, 1],
//       size: null,
//       length: 8,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Phone 2:",
//       comment: ""
//     },
//     {
//       name: "ACSPH2A",
//       item_type: "DFHMDF",
//       position: [20, 10],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSPH2B",
//       item_type: "DFHMDF",
//       position: [20, 14],
//       size: null,
//       length: 3,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ACSPH2C",
//       item_type: "DFHMDF",
//       position: [20, 18],
//       size: null,
//       length: 4,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [20, 23],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [20, 24],
//       size: null,
//       length: 16,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "EFT Account Id: ",
//       comment: ""
//     },
//     {
//       name: "ACSEFTC",
//       item_type: "DFHMDF",
//       position: [20, 41],
//       size: null,
//       length: 10,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [20, 52],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [20, 53],
//       size: null,
//       length: 24,
//       attribute: "",
//       color: "TURQUOISE",
//       initial_value: "Primary Card Holder Y/N:",
//       comment: ""
//     },
//     {
//       name: "ACSPFLG",
//       item_type: "DFHMDF",
//       position: [20, 78],
//       size: null,
//       length: 1,
//       attribute: "(UNPROT)",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [20, 80],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "INFOMSG",
//       item_type: "DFHMDF",
//       position: [22, 23],
//       size: null,
//       length: 45,
//       attribute: "(ASKIP)",
//       color: "NEUTRAL",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [22, 69],
//       size: null,
//       length: 0,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "",
//       item_type: "DFHMDF",
//       position: [1, 1],
//       size: null,
//       length: 9,
//       attribute: "",
//       color: "",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "ERRMSG",
//       item_type: "DFHMDF",
//       position: [23, 1],
//       size: null,
//       length: 78,
//       attribute: "(ASKIP,BRT,FSET)",
//       color: "RED",
//       initial_value: "",
//       comment: ""
//     },
//     {
//       name: "FKEYS",
//       item_type: "DFHMDF",
//       position: [24, 1],
//       size: null,
//       length: 21,
//       attribute: "(ASKIP,NORM)",
//       color: "YELLOW",
//       initial_value: "ENTER=Process F3=Exit",
//       comment: ""
//     },
//     {
//       name: "FKEY05",
//       item_type: "DFHMDF",
//       position: [24, 23],
//       size: null,
//       length: 7,
//       attribute: "(ASKIP,DRK)",
//       color: "YELLOW",
//       initial_value: "F5=Save",
//       comment: ""
//     },
//     {
//       name: "FKEY12",
//       item_type: "DFHMDF",
//       position: [24, 31],
//       size: null,
//       length: 10,
//       attribute: "(ASKIP,DRK)",
//       color: "YELLOW",
//       initial_value: "F12=Cancel",
//       comment: ""
//     }
//   ],
//   screen_string:
//     "XXXXXXXXX           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Date: mm/dd/yy  \nProg:               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    Time: hh:mm:ss  \n                                                                                \n                                Update Account                                  \n                  Account Number :   XXXXXXXXXXX        Active Y/N:  X          \n       Opened : XXXX - XX - XX        Credit Limit        : XXXXXXXXXXXXXXX     \n       Expiry : XXXX - XX - XX        Cash credit Limit   : XXXXXXXXXXXXXXX     \n       Reissue: XXXX - XX - XX        Current Balance     : XXXXXXXXXXXXXXX     \n                                      Current Cycle Credit: XXXXXXXXXXXXXXX     \n       Account Group: XXXXXXXXXX      Current Cycle Debit : XXXXXXXXXXXXXXX     \n                               Customer Details                                 \n       Customer id  : XXXXXXXXX                 SSN:  999 - 99 - 9999           \n       Date of birth: XXXX - XX - XX            FICO Score:  XXX                \nFirst Name                 Middle Name:               Last Name :               \nXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXX \nAddress: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   State     XX      \n         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   Zip       XXXXX   \nCity     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   Country   XXX     \nPhone 1: XXX XXX XXXX  Government Issued Id Ref    :     XXXXXXXXXXXXXXXXXXXX   \nPhone 2: XXX XXX XXXX  EFT Account Id:  XXXXXXXXXX  Primary Card Holder Y/N: X  \n                                                                                \n                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             \nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  \nENTER=Process F3=Exit F5=Save F12=Cancel                                        "
// };

// export const cobolBlobData: BlobData = {
//   id: "4e4370744eb74705aee51851289cd98c",
//   name: "CBACT01C",
//   path: "DEMO.CARDDEMO.CBL/CBACT01C",
//   label: "COBOL",
//   overview: {
//     programe_name: "CBACT01C",
//     io_files: [],
//     db_accesses: [],
//     copy_files: ["CVACT01Y"],
//     call_files: ["'CEE3ABD'::static"],
//     summarization:
//       "This COBOL program, named CBACT01C, processes a VSAM KSDS (Key-Sequenced Data Set) named `ACCTFILE-FILE` to read and display account records. The main flow of the program is as follows:\n\n1. **Initialization and File Open**:\n    - The program starts execution by displaying a start message.\n    - It performs the routine `0000-ACCTFILE-OPEN` to open the `ACCTFILE-FILE` for input. The file open status is checked, and if an error occurs, appropriate error handling routines are called.\n\n2. **Reading and Displaying Records**:\n    - Using a `PERFORM UNTIL` loop, the program continuously reads records from the file until the end-of-file condition (`END-OF-FILE = 'Y'`) is reached.\n    - For each record:\n        - The routine `1000-ACCTFILE-GET-NEXT` is called to read the next account record into `ACCOUNT-RECORD`.\n        - If a record is successfully read (`ACCTFILE-STATUS = '00'`), the program calls `1100-DISPLAY-ACCT-RECORD` to display the account details (such as account ID, status, balance, credit limits, and various dates).\n        - If an end-of-file status (`ACCTFILE-STATUS = '10'`) is encountered, it sets the `END-OF-FILE` flag to 'Y'.\n        - For other file read errors, it displays an error message and abends the program using the routine `9999-ABEND-PROGRAM`.\n\n3. **File Close and Termination**:\n    - After processing all records, the program performs the routine `9000-ACCTFILE-CLOSE` to close the `ACCTFILE-FILE`. Similar to the open routine, it checks the close status and handles any errors accordingly.\n    - Finally, the program displays an end message and terminates.\n\n4. **Supporting Subroutines**:\n    - `1100-DISPLAY-ACCT-RECORD` - Displays detailed information about each account record.\n    - `9999-ABEND-PROGRAM` - Handles abnormal termination of the program.\n    - `9910-DISPLAY-IO-STATUS` - Displays detailed I/O status for error diagnosis.\n\nThis structured approach ensures that the account records are systematically read and displayed, with robust error handling for file operations.",
//     io_table: [
//       {
//         index: 1,
//         item_name: "ACCTFILE-FILE",
//         physical_name: "ACCTFILE",
//         type: "",
//         crud_op: "",
//         access_mode: "",
//         notes: ""
//       }
//     ]
//   },
//   io_params_def: {
//     input_table: [
//       {
//         item_name: "",
//         cobol_level: "01",
//         cobol_dtype: "",
//         length: "",
//         access_mode: "INPUT",
//         dtype: "",
//         default_value: "",
//         remarks: "Java DTO class equivalence"
//       },
//       {
//         item_name: "",
//         cobol_level: "05",
//         cobol_dtype: "9",
//         length: "",
//         access_mode: "INPUT",
//         dtype: "Int",
//         default_value: "",
//         remarks: "Java Int data type equivalence"
//       },
//       {
//         item_name: "",
//         cobol_level: "05",
//         cobol_dtype: "X",
//         length: "",
//         access_mode: "INPUT",
//         dtype: "String",
//         default_value: "",
//         remarks: "Java String data type equivalence"
//       }
//     ],
//     input_note: "",
//     output_table: [],
//     output_note: ""
//   },
//   process_logic: {
//     paragraph_level: {
//       "1000-ACCTFILE-GET-NEXT": {
//         paragraph_name: "1000-ACCTFILE-GET-NEXT",
//         section: "procedure division",
//         paragraph_code:
//           "1000-ACCTFILE-GET-NEXT.\n           READ ACCTFILE-FILE INTO ACCOUNT-RECORD.\n           IF  ACCTFILE-STATUS = '00'\n               MOVE 0 TO APPL-RESULT\n               PERFORM 1100-DISPLAY-ACCT-RECORD\n           ELSE\n               IF  ACCTFILE-STATUS = '10'\n                   MOVE 16 TO APPL-RESULT\n               ELSE\n                   MOVE 12 TO APPL-RESULT\n               END-IF\n           END-IF\n           IF  APPL-AOK\n               CONTINUE\n           ELSE\n               IF  APPL-EOF\n                   MOVE 'Y' TO END-OF-FILE\n               ELSE\n                   DISPLAY 'ERROR READING ACCOUNT FILE'\n                   MOVE ACCTFILE-STATUS TO IO-STATUS\n                   PERFORM 9910-DISPLAY-IO-STATUS\n                   PERFORM 9999-ABEND-PROGRAM\n               END-IF\n           END-IF\n           EXIT.\n",
//         paragraph_lines: [92, 116],
//         ref_paragraphs: [
//           "1100-DISPLAY-ACCT-RECORD",
//           "9910-DISPLAY-IO-STATUS",
//           "9999-ABEND-PROGRAM"
//         ],
//         paragraph_logic: [
//           "Reads the next record from the account file into the account record area.",
//           "Checks if the read operation was successful with ACCTFILE-STATUS being 00; if successful, move 0 to APPL-RESULT and call [account display process]<1100-DISPLAY-ACCT-RECORD>.",
//           "If the read status is 10, move 16 to APPL-RESULT; otherwise, move 12 to APPL-RESULT.",
//           "If application result is okay, continue processing; otherwise, if it\u2019s the end of file, mark END-OF-FILE.",
//           "If an error occurs during the read, display an error message, move the status to IO-STATUS, and call [IO status display process]<9910-DISPLAY-IO-STATUS> and [program abend process]<9999-ABEND-PROGRAM>."
//         ]
//       },
//       "1100-DISPLAY-ACCT-RECORD": {
//         paragraph_name: "1100-DISPLAY-ACCT-RECORD",
//         section: "procedure division",
//         paragraph_code:
//           "1100-DISPLAY-ACCT-RECORD.\n           DISPLAY 'ACCT-ID                 :'   ACCT-ID\n           DISPLAY 'ACCT-ACTIVE-STATUS      :'   ACCT-ACTIVE-STATUS\n           DISPLAY 'ACCT-CURR-BAL           :'   ACCT-CURR-BAL\n           DISPLAY 'ACCT-CREDIT-LIMIT       :'   ACCT-CREDIT-LIMIT\n           DISPLAY 'ACCT-CASH-CREDIT-LIMIT  :'   ACCT-CASH-CREDIT-LIMIT\n           DISPLAY 'ACCT-OPEN-DATE          :'   ACCT-OPEN-DATE\n           DISPLAY 'ACCT-EXPIRAION-DATE     :'   ACCT-EXPIRAION-DATE\n           DISPLAY 'ACCT-REISSUE-DATE       :'   ACCT-REISSUE-DATE\n           DISPLAY 'ACCT-CURR-CYC-CREDIT    :'   ACCT-CURR-CYC-CREDIT\n           DISPLAY 'ACCT-CURR-CYC-DEBIT     :'   ACCT-CURR-CYC-DEBIT\n           DISPLAY 'ACCT-GROUP-ID           :'   ACCT-GROUP-ID\n           DISPLAY '-------------------------------------------------'\n           EXIT.\n",
//         paragraph_lines: [118, 131],
//         ref_paragraphs: [],
//         paragraph_logic: [
//           "Displays the account ID.<ACCT-ID>",
//           "Displays the active status of the account.<ACCT-ACTIVE-STATUS>",
//           "Displays the current balance of the account.<ACCT-CURR-BAL>",
//           "Displays the credit limit of the account.<ACCT-CREDIT-LIMIT>",
//           "Displays the cash credit limit of the account.<ACCT-CASH-CREDIT-LIMIT>"
//         ]
//       },
//       "0000-ACCTFILE-OPEN": {
//         paragraph_name: "0000-ACCTFILE-OPEN",
//         section: "procedure division",
//         paragraph_code:
//           "0000-ACCTFILE-OPEN.\n           MOVE 8 TO APPL-RESULT.\n           OPEN INPUT ACCTFILE-FILE\n           IF  ACCTFILE-STATUS = '00'\n               MOVE 0 TO APPL-RESULT\n           ELSE\n               MOVE 12 TO APPL-RESULT\n           END-IF\n           IF  APPL-AOK\n               CONTINUE\n           ELSE\n               DISPLAY 'ERROR OPENING ACCTFILE'\n               MOVE ACCTFILE-STATUS TO IO-STATUS\n               PERFORM 9910-DISPLAY-IO-STATUS\n               PERFORM 9999-ABEND-PROGRAM\n           END-IF\n           EXIT.\n",
//         paragraph_lines: [133, 149],
//         ref_paragraphs: ["9910-DISPLAY-IO-STATUS", "9999-ABEND-PROGRAM"],
//         paragraph_logic: [
//           "Moves 8 to APPL-RESULT, marking the initial state for file opening.",
//           "Attempts to open the ACCTFILE-FILE for input access.",
//           "If the ACCTFILE-STATUS is 00, indicating success, moves 0 to APPL-RESULT.",
//           "If the ACCTFILE-STATUS is not 00, indicating failure, moves 12 to APPL-RESULT.",
//           "If APPL-AOK indicates no errors, continues processing.",
//           "If APPL-AOK indicates errors, displays an error message, moves ACCTFILE-STATUS to IO-STATUS, calls [IO status display routine]<9910-DISPLAY-IO-STATUS>, and calls [program abend routine]<9999-ABEND-PROGRAM>."
//         ]
//       },
//       "9000-ACCTFILE-CLOSE": {
//         paragraph_name: "9000-ACCTFILE-CLOSE",
//         section: "procedure division",
//         paragraph_code:
//           "9000-ACCTFILE-CLOSE.\n           ADD 8 TO ZERO GIVING APPL-RESULT.\n           CLOSE ACCTFILE-FILE\n           IF  ACCTFILE-STATUS = '00'\n               SUBTRACT APPL-RESULT FROM APPL-RESULT\n           ELSE\n               ADD 12 TO ZERO GIVING APPL-RESULT\n           END-IF\n           IF  APPL-AOK\n               CONTINUE\n           ELSE\n               DISPLAY 'ERROR CLOSING ACCOUNT FILE'\n               MOVE ACCTFILE-STATUS TO IO-STATUS\n               PERFORM 9910-DISPLAY-IO-STATUS\n               PERFORM 9999-ABEND-PROGRAM\n           END-IF\n           EXIT.\n\n",
//         paragraph_lines: [151, 167],
//         ref_paragraphs: ["9910-DISPLAY-IO-STATUS", "9999-ABEND-PROGRAM"],
//         paragraph_logic: [
//           "Calculates the initial result for application result handling.",
//           "Closes the account file after operations are completed.",
//           "Checks if the account file was closed successfully and resets the application result if so.",
//           "Handles errors by reporting the error and updating the IO status.",
//           "Calls the [display IO status process]<9910-DISPLAY-IO-STATUS> to show the current IO status in case of an error.",
//           "Calls the [abend program process]<9999-ABEND-PROGRAM> to terminate the program if the account file could not be closed properly."
//         ]
//       },
//       "9999-ABEND-PROGRAM": {
//         paragraph_name: "9999-ABEND-PROGRAM",
//         section: "procedure division",
//         paragraph_code:
//           "9999-ABEND-PROGRAM.\n           DISPLAY 'ABENDING PROGRAM'\n           MOVE 0 TO TIMING\n           MOVE 999 TO ABCODE\n           CALL 'CEE3ABD'.\n\n",
//         paragraph_lines: [169, 173],
//         ref_paragraphs: [],
//         paragraph_logic: [
//           "Displays the message ABENDING PROGRAM to indicate an abnormal program termination.",
//           "Resets the timing indicator by moving zero to the TIMING variable.",
//           "Sets the abnormal termination code by moving 999 to the ABCODE variable.",
//           "Calls the CEE3ABD routine to abend (abnormally end) the program."
//         ]
//       },
//       "9910-DISPLAY-IO-STATUS": {
//         paragraph_name: "9910-DISPLAY-IO-STATUS",
//         section: "procedure division",
//         paragraph_code:
//           "9910-DISPLAY-IO-STATUS.\n           IF  IO-STATUS NOT NUMERIC\n           OR  IO-STAT1 = '9'\n               MOVE IO-STAT1 TO IO-STATUS-04(1:1)\n               MOVE 0        TO TWO-BYTES-BINARY\n               MOVE IO-STAT2 TO TWO-BYTES-RIGHT\n               MOVE TWO-BYTES-BINARY TO IO-STATUS-0403\n               DISPLAY 'FILE STATUS IS: NNNN' IO-STATUS-04\n           ELSE\n               MOVE '0000' TO IO-STATUS-04\n               MOVE IO-STATUS TO IO-STATUS-04(3:2)\n               DISPLAY 'FILE STATUS IS: NNNN' IO-STATUS-04\n           END-IF\n           EXIT.\n\n",
//         paragraph_lines: [176, 189],
//         ref_paragraphs: [],
//         paragraph_logic: [
//           "Checks if the IO-STATUS is non-numeric or if IO-STAT1 is 9.",
//           "If either condition is true, updates IO-STATUS to reflect non-numeric status, moves status parts to appropriate fields, and displays the non-numeric file status.",
//           "If neither condition is true, sets IO-STATUS to 0000, updates it with the appropriate numeric status, and displays the numeric file status."
//         ]
//       }
//     }
//   },
//   copy_graph: {
//     programs: [
//       {
//         index: 0,
//         program_id: "CEE3ABD",
//         program_type: "Cobol",
//         program_name: "CEE3ABD",
//         call_type: "Static Call",
//         notes: "",
//         locations: "",
//         paragraph: "9999-ABEND-PROGRAM",
//         identifier: []
//       },
//       {
//         index: 0,
//         program_id: "CVACT01Y",
//         program_type: "Copy",
//         program_name: "CVACT01Y",
//         call_type: "Static Call",
//         notes: "",
//         locations: "",
//         paragraph: "",
//         identifier: []
//       }
//     ],
//     details: [""]
//   }
// };
