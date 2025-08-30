import { File, Folder, MetaData, TreeView } from "@types";

export const flatRepository = (tree: TreeView, parentId?: string, metadata?: MetaData): File[] => {
  const blobDirs: File[] = [];
  const folderDirs: Folder[] = [];
  tree.forEach(o => {
    if (o.type === "blob") blobDirs.push({ ...o, parentId, metadata });
    else if (o.type === "tree") {
      folderDirs.push({ ...o, parentId });
    }
  });

  const blobFromFolder: File[] = folderDirs.reduce(
    (r, o) => [...r, ...(o.children ? flatRepository(o.children, o.id, o.metadata) : [])],
    [] as File[]
  );
  return [...blobDirs, ...blobFromFolder];
};

export const flatFolderRepository = (tree: TreeView): Folder[] => {
  const folderDirs: Folder[] = [];
  tree.forEach(o => {
    if (o.type === "tree") folderDirs.push(o);
  });
  const blobFromFolder: Folder[] = folderDirs.reduce(
    (r, o) => [...r, ...(o.children ? flatFolderRepository(o.children) : [])],
    [] as Folder[]
  );
  return [...folderDirs, ...blobFromFolder];
};

export const getTreeFiles = (tree: TreeView): Array<File> => {
  const files: File[] = [];

  function traverse(node: Folder | File) {
    if (node.type === "blob") {
      files.push(node);
    } else if (node.type === "tree" && node.children) {
      for (const child of node.children) {
        traverse(child);
      }
    }
  }

  for (const node of tree) {
    traverse(node);
  }

  return files;
};
