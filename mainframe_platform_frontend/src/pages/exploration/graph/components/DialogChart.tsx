import { LoadingOutlined } from "@ant-design/icons";
import styled from "@emotion/styled";
import { Tabs as AntdTabs, Table, TabsProps } from "antd";
import { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";

import { ReactComponent as CheckSuccess } from "@assets/svg/check-success.svg";
import { ReactComponent as XRedIcon } from "@assets/svg/x-red.svg";
import { ReactComponent as XIcon } from "@assets/svg/x.svg";
import { DialogChartData, Flex, Typography } from "@components";
import { fileSelector } from "@store";
import { NetworkingDataType } from "@types";

import { NODE_BY_TYPE } from "../config";

import {
  ExportBtn,
  WrapAction,
  WrapClose,
  WrapContent,
  WrapDeadcode,
  WrapExport,
  WrapInfo
} from "./styles";

type NodeType = NetworkingDataType["nodes"][number];

type Props = {
  selectedId?: string;
  colorByType?: string;
  close: () => void;
  nodes: NodeType[];
};

const Tabs = styled(AntdTabs)`
  gap: 24px;
  & .ant-tabs-tab {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
  }
`;

export const DialogChart: React.FC<Props> = ({ selectedId, nodes, colorByType, close }) => {
  // const dispatch = useDispatch()
  const { t } = useTranslation();
  const fileContents = useSelector(fileSelector.selectFileContents);
  const refFileContents = useRef<typeof fileContents>([]);
  const [activeTab, setActiveTab] = useState("detail");
  const data = nodes?.find(node => node.id === selectedId);

  // const fetchFileDetailRequest = async (id: string) => {
  //   try {
  //     setLoading(true)
  //     const res = await blobApi.getFileDetailRequest(id)
  //     dispatch(fileActions.setFileContent(res))
  //     setData(res)
  //   } catch (error) {
  //     messageApi.error(String(error))
  //   } finally {
  //     setLoading(false)
  //   }
  // }

  useEffect(() => {
    refFileContents.current = fileContents;
  }, [fileContents]);

  const TAB_ITEMS: TabsProps["items"] = [
    {
      key: "detail",
      label: t("component.dialog_tab.detail"),
      children: (
        <Flex direction='column' gap={10}>
          <WrapInfo>
            <Typography level='h5-subtitles'>{`${t("component.dialog.name")}: ${
              data?.name
            }`}</Typography>
          </WrapInfo>
          {(NODE_BY_TYPE as any)?.[data?.type || ""] && (
            <WrapInfo>
              <Typography level='h5-subtitles'>
                {`${t("component.dialog.type")}: ${(NODE_BY_TYPE as any)?.[data?.type || ""]}`}
              </Typography>
            </WrapInfo>
          )}
        </Flex>
      )
    }
    // {
    //   key: "graph1",
    //   label: t("component.dialog_tab.graph"),
    //   children: (
    //     <div>
    //       <SmallGraph id={selectedId} />
    //     </div>
    //   )
    // }
  ];

  return (
    <DialogChartData
      width={860}
      height={535}
      open={Boolean(selectedId)}
      onCancel={close}
      borderColor={colorByType}
      footer={null}
      closeIcon={
        <WrapAction onClick={close}>
          <XIcon />
        </WrapAction>
      }
      loading={false}
      left={
        <>
          <Tabs
            tabBarGutter={24}
            tabBarStyle={{ margin: 0 }}
            activeKey={activeTab}
            items={TAB_ITEMS}
            onChange={e => setActiveTab(e)}
          />

          <WrapContent thumbColor={colorByType}>
            <WrapDeadcode isDeadCode={data?.is_deadcode}>
              <Typography level='h6-body1m'>{`${t("component.dialog.deadcode")} `}</Typography>
              {data?.is_deadcode ? (
                <WrapClose>
                  <CheckSuccess />
                </WrapClose>
              ) : (
                <WrapClose>
                  <XRedIcon />
                </WrapClose>
              )}
            </WrapDeadcode>
            <div className='content'>
              <div>
                {" "}
                {data?.summarization ? (
                  <Typography level='h6-body1r' color='grey300'>
                    {`1. Content
              - Summarization:\n${data?.summarization}`}
                    <br />
                  </Typography>
                ) : (
                  ""
                )}
                {data?.db_table?.length ? (
                  <div>
                    <div>- Database -</div>
                    <br />
                    <Table
                      columns={[
                        {
                          title: "Name",
                          dataIndex: "name"
                        },
                        {
                          title: "Type",
                          dataIndex: "type"
                        }
                      ]}
                      dataSource={data?.db_table}
                      pagination={false}
                    />
                    <br />
                  </div>
                ) : null}
                {data?.copy_table?.length ? (
                  <div>
                    <br />
                    <div>- Copy -</div>
                    <br />
                    <Table
                      columns={[
                        {
                          title: "Name",
                          dataIndex: "name"
                        },
                        {
                          title: "Type",
                          dataIndex: "type"
                        }
                      ]}
                      dataSource={data?.copy_table}
                      pagination={false}
                    />
                    <br />
                  </div>
                ) : null}
              </div>
            </div>
            {/* {data?.summarization} */}
          </WrapContent>
          <WrapExport>
            <ExportBtn type='primary'>
              <div>
                {`${t("button.running")} ...`} <LoadingOutlined />
              </div>
            </ExportBtn>
          </WrapExport>
        </>
      }
    />
  );
};
