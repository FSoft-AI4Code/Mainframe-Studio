import { useEffect } from "react";
import { useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";

import { fileSelector } from "@store";
import { TreeView } from "@types";
import { flatRepository } from "@utils";

import { DEFAULT_TAB } from "../config";

export const useRouter = (treeView: TreeView | null) => {
  const navigate = useNavigate();
  const treeFileSelected = useSelector(fileSelector.selectTreeFileSelected);
  const { repoId, fileId, fileCategory } = useParams();

  const onClickTab = (key: string) => {
    navigate(`/exploration/${repoId}/file/${fileId}/${key}`);
  };

  useEffect(() => {
    if (!treeFileSelected) return;
    navigate(`/exploration/${repoId}/file/${treeFileSelected.id}/${DEFAULT_TAB}`);
  }, [treeFileSelected]);

  useEffect(() => {
    if (!treeView) return;
    const files = flatRepository(treeView);

    if (!files.length) return;
    navigate(`/exploration/${repoId}/file/${files[0].id}/${DEFAULT_TAB}`);
  }, [treeView]);

  return { fileId, fileCategory, onClickTab };
};
