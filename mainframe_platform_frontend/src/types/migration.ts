export type MigrationStructureQuery = {
  repository_id: string;
  bms_file_name: string;
  enabled?: boolean;
};
export interface MigrationStructureResponse {
  repository_id: string;
  bms_file_name: string;
  structure: FSNode;
}

export type FSNode = DirectoryNode | FileNode;

interface BaseNode {
  name: string;
  path: string;
}

export interface DirectoryNode extends BaseNode {
  type: "directory";
  children: FSNode[];
}

export interface FileNode extends BaseNode {
  type: "file";
  children: null;
}

//For getting file content
export type MigrationFileContentQuery = {
  repository_id: string;
  bms_file_name: string;
  file_path: string;
};

export type MigrationFileContentData = {
  repository_id: string;
  bms_file_name: string;
  file_path: string;
  content: string;
};

export type MigrationTriggerQuery = {
  repository_id: string;
  bms_file_name: string;
};

export type MigrationDownloadQuery = {
  repository_id: string;
  cobol_file_name?: string;
  bms_file_name?: string;
  copybook_file_name?: string;
};
