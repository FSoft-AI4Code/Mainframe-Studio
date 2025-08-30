import styled from "@emotion/styled";
import { message as messageApi } from "antd";
import { useEffect, useRef, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { blobApi } from "@api";
import { DialogChartData } from "@components";
import { fileActions, fileSelector, repositorySelector } from "@store";
import { File, FileBlobModel } from "@types";
import { flatRepository } from "@utils";

type Props = {
  selectedId?: string;
  close: () => void;
};

const Wrapper = styled.div`
  white-space: pre-line;
`;

export const DialogChart: React.FC<Props> = ({ selectedId, close }) => {
  const dispatch = useDispatch();
  const treeview = useSelector(repositorySelector.selectRepositoryTreeView);
  const fileContents = useSelector(fileSelector.selectFileContents);
  const refFileContents = useRef<typeof fileContents>([]);
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState<FileBlobModel>();
  const [fileInfo, setFileInfo] = useState<File>();

  useEffect(() => {
    if (!treeview) return;
    const files = flatRepository(treeview);
    const fileDataInfo = files.find(o => o.path === selectedId);
    setFileInfo(fileDataInfo);
  }, [treeview, selectedId]);

  const fetchFileDetailRequest = async (id: string) => {
    try {
      setLoading(true);
      const res = await blobApi.getFileDetailRequest(id);
      dispatch(fileActions.setFileContent(res.data));
      setData(res.data);
    } catch (error) {
      messageApi.error(String(error));
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    refFileContents.current = fileContents;
  }, [fileContents]);

  useEffect(() => {
    if (!fileInfo) return;
    const cacheFile = refFileContents.current.find(o => o._id === fileInfo.id);
    if (cacheFile) {
      setData(cacheFile);
    } else {
      fetchFileDetailRequest(fileInfo.id);
    }
  }, [fileInfo]);

  return (
    <DialogChartData
      width={data?.meta?.code ? 800 : undefined}
      height={data?.meta?.code ? 400 : undefined}
      open={Boolean(fileInfo)}
      onCancel={close}
      loading={loading}
      left={
        !data ? null : (
          <Wrapper>
            {`    
1. File Path: ${data.path}
2. Section: ${data.name}
${data.meta?.explanation ? `3. Summarization:\n${data.meta.explanation}` : ""}
  `}
          </Wrapper>
        )
      }
      right={data?.meta?.code ? <Wrapper>{`${data.meta.code}`}</Wrapper> : undefined}
    />
  );
};
