import { Progress, Tabs } from "antd";
import type { ColumnsType } from "antd/es/table";
import { useEffect, useMemo, useRef, useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { LoadingOutlined } from "@ant-design/icons";

import { repositoryApi } from "@api";
import { OverflowEmpty } from "@components";
import { ROUTERS } from "@defines";
import { fileSelector } from "@store";
import { File } from "@types";

import { CustomTable, MatchingProcess, Title, WrapLoading, WrapTabs, Wrapper } from "./styles";

type DataType = {
  java: string;
  cobol: string;
};

type Props = {
  onChangeAdditionalIds?: (ids: string[]) => void;
  treeFileSelected?: File;
  additionalKeys?: string[];
};

export const MatchingContent: React.FC<Props> = ({
  onChangeAdditionalIds,
  treeFileSelected,
  additionalKeys
}) => {
  const refQueue = useRef<NodeJS.Timeout>();
  const [score, setScore] = useState<number>(0);

  const fileData = useSelector(fileSelector.selectData);
  const fileCobolData = useSelector(fileSelector.selectCobolMatchingFileSelected);
  const navigate = useNavigate();

  const existCobolData = useMemo(
    () => !!treeFileSelected?.metadata?.cobol_blob_id,
    [treeFileSelected]
  );

  const clearRefQueue = () => {
    if (refQueue.current) {
      clearTimeout(refQueue.current);
      refQueue.current = undefined;
    }
  };

  const tryFetch = async (handle: () => Promise<void>, options?: { time?: number }) => {
    let success = false;
    try {
      await handle();
      success = true;
    } catch (error: any) {
      if (error?.response?.status === 401) {
        success = true;
      }
      // eslint-disable-next-line
      console.log(error);
    } finally {
      if (!success) {
        clearRefQueue();
        refQueue.current = setTimeout(() => {
          clearRefQueue();
          tryFetch(handle, options);
        }, options?.time || 1000);
      }
    }
  };

  const columns: ColumnsType<DataType> = [
    {
      title: "JAVA",
      dataIndex: "java",
      defaultSortOrder: "descend",
      width: "50%",
      align: "left",
      render: text => (
        <WrapTabs>
          {existCobolData && treeFileSelected?.brothers?.length ? (
            <Tabs
              activeKey={additionalKeys?.[0] || treeFileSelected.id}
              size={"small"}
              onChange={item => {
                navigate(ROUTERS.MIGRATION_FILE_MATCHING.replace(":fileId", item || ""));
              }}
              items={treeFileSelected?.brothers?.map(item => {
                return {
                  label: `${item.name}`,
                  key: String(item.id),
                  children: <Wrapper>{text || <OverflowEmpty />}</Wrapper>
                };
              })}
            />
          ) : (
            <Wrapper>{text || <OverflowEmpty />}</Wrapper>
          )}
        </WrapTabs>
      )
    },
    {
      title: "COBOL",
      align: "left",
      width: "50%",
      dataIndex: "cobol",
      defaultSortOrder: "descend",
      render: cobol => <Wrapper>{cobol || <OverflowEmpty />}</Wrapper>
    }
  ];

  const fetchFolderScoreRequest = async () => {
    if (!treeFileSelected?.metadata?.cobol_blob_id) {
      return;
    }
    if (!treeFileSelected?.parentId) {
      return;
    }
    if (treeFileSelected?.metadata?.matching_score) {
      setScore(treeFileSelected?.metadata?.matching_score * 100);
      return;
    }
    tryFetch(
      async () => {
        const res = await repositoryApi.getMatchingScoreDataRequest(
          String(treeFileSelected?.parentId)
        );
        if (res?.data?.matching_score) {
          setScore((res?.data?.matching_score as number) * 100);
        } else {
          throw new Error("Caculating score");
        }
      },
      {
        time: 15000
      }
    );
  };

  useEffect(() => {
    fetchFolderScoreRequest();
  }, [treeFileSelected]);

  useEffect(() => {
    return () => {
      onChangeAdditionalIds?.([]);
      clearRefQueue();
    };
  }, []);

  return (
    <div>
      {existCobolData && (
        <>
          {score ? (
            <>
              <Title>Matching</Title>
              <MatchingProcess>
                <Progress percent={Number(Number(score)?.toFixed(2))} />
              </MatchingProcess>
            </>
          ) : (
            <WrapLoading>
              Caculating score ... <LoadingOutlined />
            </WrapLoading>
          )}
        </>
      )}

      <CustomTable
        columns={columns}
        dataSource={[
          {
            java: fileData?.content || "",
            cobol: existCobolData ? fileCobolData?.content : ""
          }
        ]}
        pagination={false}
      />
    </div>
  );
};
