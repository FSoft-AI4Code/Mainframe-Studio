/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
import {
  DownloadOutlined,
  ExclamationCircleFilled,
  GithubOutlined,
  MenuFoldOutlined,
  MenuUnfoldOutlined,
  ReloadOutlined
} from "@ant-design/icons";
import { Dropdown, Empty, Layout, MenuProps, Modal, Spin, Tree } from "antd";
import { useState } from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";
import { DataNode, EventDataNode, TreeProps } from "antd/es/tree";
import { useParams } from "react-router-dom";

import { Button, Flex, Typography } from "@components";
import { allColors, v2CommonColors } from "@style";
import {
  useDownloadMigrationMutation,
  useFileContentQuery,
  useStructureMigrationQuery
} from "@services";
import { FSNode, Repository } from "@types";

import CloneRepoModal from "./CloneRepoModal";
import ProgressConvertBMS from "./ProgressConvertBMS";
const { confirm, success } = Modal;

const { Sider, Content } = Layout;

const convertToTreeData = (node: FSNode): DataNode => ({
  title: node?.name,
  key: node?.path,
  isLeaf: node?.type === "file",
  children: node?.children ? node?.children?.map(convertToTreeData) : undefined
});

interface SourceExplorerBMSProps {
  status: Repository["status"];
  refetchStatus: () => void;
}

export default function SourceExplorerBMS({ status, refetchStatus }: SourceExplorerBMSProps) {
  const [collapsed, setCollapsed] = useState(false);
  const [retryConvert, setRetryConvert] = useState(false);
  const [selectedFile, setSelectedFile] = useState<string>("");
  const [open, setOpen] = useState(false);
  const { type: fileType = "", name = "", repoId = "" } = useParams();
  const isConverted = status === "migrated";

  const { migrationStructure, loading: loadingStructure } = useStructureMigrationQuery({
    repository_id: repoId,
    bms_file_name: name,
    enabled: isConverted
  });

  const { fileContent, loading } = useFileContentQuery({
    repository_id: repoId,
    bms_file_name: name,
    file_path: selectedFile
  });
  const treeData = [convertToTreeData(migrationStructure as FSNode)];

  // eslint-disable-next-line no-console
  console.log("treeData", treeData);

  const onSelect: TreeProps<EventDataNode<DataNode>>["onSelect"] = async (_, info) => {
    const node = info.node;
    if (node.isLeaf && node.key) {
      setSelectedFile(node.key as string);
    }
  };

  const { mutate: downloadMigration } = useDownloadMigrationMutation();

  const handleDownloadMigration = () => {
    if (!repoId) return;
    downloadMigration({
      repository_id: repoId,
      bms_file_name: name
    });
  };
  const handleRetryConvert = () => setRetryConvert(true);
  const handleCancelRetryConvert = () => setRetryConvert(false);
  const handleConfirmRetryConvert = () => {
    confirm({
      title: (
        <>
          <Typography
            style={{
              color: v2CommonColors.primary9
            }}
            level='body-16b'
          >
            Are you sure to regenerate convert code ?
          </Typography>
          <Typography
            style={{
              color: v2CommonColors.primary10
            }}
            level='body-14r'
          >
            Everything will be replace!
          </Typography>
        </>
      ),
      icon: <ExclamationCircleFilled />,
      closable: true,
      onOk: handleRetryConvert,
      onCancel() {
        // eslint-disable-next-line no-console
        console.log("Cancel");
      }
    });
  };

  const items: MenuProps["items"] = [
    {
      label: "Download as Zip",
      key: "download-zip",
      icon: <DownloadOutlined />,
      onClick: handleDownloadMigration
    },
    {
      label: "Git Clone",
      key: "git-clone",
      icon: <GithubOutlined />,
      onClick: () => setOpen(true)
    }
  ];

  return (
    <>
      {isConverted && !retryConvert ? (
        <>
          <Flex
            style={{
              padding: "8px 16px",
              border: `1px solid ${allColors.neutral6}`,
              background: allColors.neutral4
            }}
            justify='space-between'
            align='center'
          >
            <Typography level={"title-18b"}>Source Code Explorer</Typography>
            <Flex gap={12}>
              <Button
                style={{
                  borderRadius: 8
                }}
                icon={<ReloadOutlined />}
                type='primary'
                onClick={handleConfirmRetryConvert}
              >
                Regenerate
              </Button>
              <Dropdown menu={{ items }} trigger={["click"]}>
                <Button
                  icon={<DownloadOutlined />}
                  type='primary'
                  style={{
                    borderRadius: 8
                  }}
                >
                  DownLoad
                </Button>
              </Dropdown>
            </Flex>
          </Flex>
          <Layout
            style={{
              minHeight: "calc(100vh - 200px)",
              border: `1px solid ${allColors.neutral6}`,
              background: `${allColors.neutral8}`
            }}
          >
            <Sider
              width={250}
              collapsedWidth={64}
              style={{
                borderRight: `1px solid ${allColors.neutral6}`
              }}
              color='red'
              trigger={null}
              collapsible
              collapsed={collapsed}
            >
              <div
                style={{
                  padding: 16,
                  display: "flex",
                  overflowX: "hidden",
                  justifyContent: "space-between",
                  alignItems: "center"
                }}
              >
                {!collapsed && (
                  <Typography
                    style={{
                      whiteSpace: "nowrap"
                    }}
                    color='primary9'
                    level={"body-16m"}
                  >
                    📁 Source Code
                  </Typography>
                )}
                <Button
                  type='text'
                  icon={collapsed ? <MenuUnfoldOutlined /> : <MenuFoldOutlined />}
                  onClick={() => setCollapsed(!collapsed)}
                />
              </div>

              <Spin spinning={loadingStructure}>
                {!collapsed && treeData?.length > 0 ? (
                  <Tree.DirectoryTree
                    virtual
                    showLine
                    multiple
                    blockNode
                    defaultExpandAll={collapsed}
                    treeData={treeData as unknown as EventDataNode<DataNode>[]}
                    onSelect={onSelect}
                    selectedKeys={[selectedFile]}
                    style={{
                      paddingInline: 4,
                      whiteSpace: "nowrap",
                      width: "100%",
                      height: "100%",
                      overflowX: "auto"
                    }}
                  />
                ) : (
                  <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} />
                )}
              </Spin>
            </Sider>
            <Layout>
              <Content
                style={{
                  overflow: "auto",
                  position: "relative"
                }}
              >
                <Spin style={{ height: "100%" }} wrapperClassName='full_height' spinning={loading}>
                  {fileContent ? (
                    <Flex style={{ height: "100%" }} direction='column'>
                      <Flex
                        align='center'
                        style={{
                          height: 36,
                          padding: "2px 16px",
                          background: allColors.neutral3,
                          borderBottom: `1px solid ${allColors.neutral6}`
                        }}
                      >
                        <Typography level={"body-16m"}>{selectedFile}</Typography>
                      </Flex>
                      <SyntaxHighlighter
                        language='tsx'
                        style={oneDark}
                        customStyle={{ fontSize: 14, borderRadius: 0, margin: 0, height: "100%" }}
                        showLineNumbers
                      >
                        {fileContent}
                      </SyntaxHighlighter>
                    </Flex>
                  ) : (
                    <Flex
                      style={{
                        marginTop: "20%"
                      }}
                      align='center'
                      justify='center'
                    >
                      <Empty description='Please select a file to view its content.' />
                    </Flex>
                  )}
                </Spin>
              </Content>
            </Layout>
          </Layout>
          <CloneRepoModal open={open} onClose={() => setOpen(false)} />
        </>
      ) : (
        <ProgressConvertBMS
          cancelRetryConvert={handleCancelRetryConvert}
          retryConvert={handleRetryConvert}
          status={status as Repository["status"]}
          refetchReport={refetchStatus}
        />
      )}
    </>
  );
}
