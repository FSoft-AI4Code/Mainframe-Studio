import { File, FileBlobModel } from "@types";

export type State = {
  data?: FileBlobModel;
  treeFileSelected?: File;
  treeMatchingFileSelected?: File;
  cobolMatchingFileSelected?: FileBlobModel;
  loading?: boolean;
  fileContents: FileBlobModel[];
};
