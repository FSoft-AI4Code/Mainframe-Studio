import { useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { blobApi } from "@api";
import { fileActions, fileSelector } from "@store";
import { TreeView } from "@types";
import { flatRepository } from "@utils";

export const useHandle = (treeview: TreeView | null) => {
  const dispatch = useDispatch();
  const { fileId } = useParams();
  const fileContents = useSelector(fileSelector.selectFileContents);
  const refFileContents = useRef<typeof fileContents>([]);

  const fetchFileDetailRequest = async (id: string) => {
    try {
      dispatch(fileActions.setLoading(true));
      const res = await blobApi.getFileDetailRequest(id);
      dispatch(fileActions.setData(res.data));
    } catch (error) {
      // eslint-disable-next-line
      console.log(error);
    } finally {
      dispatch(fileActions.setLoading(false));
    }
  };

  useEffect(() => {
    refFileContents.current = fileContents;
  }, [fileContents]);

  useEffect(() => {
    if (!fileId) return;
    const cacheFile = refFileContents.current.find(o => o._id === fileId);
    if (cacheFile) {
      dispatch(fileActions.setData(cacheFile));
    } else {
      fetchFileDetailRequest(fileId);
    }
  }, [fileId]);

  useEffect(() => {
    if (!treeview || !fileId) return;
    const files = flatRepository(treeview);
    const file = files.find(o => o.id === fileId);
    if (file) dispatch(fileActions.setTreeFileSelected(file));
  }, [treeview, fileId]);
};
