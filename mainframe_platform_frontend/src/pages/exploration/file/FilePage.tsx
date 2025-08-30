import { Menu, Tabs } from "antd";
import { lazy, useEffect, useMemo, useState } from "react";
import { useTranslation } from "react-i18next";
import { useSelector } from "react-redux";
import { Route, Routes, useNavigate, useParams } from "react-router-dom";

import { repositoryApi } from "@api";
import { ArrowDownSvg, ArrowRightSvg, ArrowUpSvg } from "@assets/svg";
import { Flex } from "@components";
import { useBreadcrumb, useMenuRepository } from "@hooks";
import { fileSelector } from "@store";
import { TreeView } from "@types";
import { handleDownloadFile } from "@utils";
import { useProjectsQuery } from "@services";

import { genTabItemsRender } from "./config";
import { useHandle, useRouter } from "./hooks";
import { ExportBtn, WrapTabs } from "./styles";

const SidebarLayout = lazy(() => import("@layouts/SidebarLayout"));

export const Content: React.FC = () => {
  const navigate = useNavigate();
  const { t } = useTranslation();
  const tabItemsRender = genTabItemsRender(t);
  const { project } = useProjectsQuery();
  const { repoId } = useParams();
  const treeFileSelected = useSelector(fileSelector.selectTreeFileSelected);
  const fileData = useSelector(fileSelector.selectData);
  // const { progressPercent } = useProgress();

  // eslint-disable-next-line unused-imports/no-unused-vars, @typescript-eslint/no-unused-vars
  const [fileReport, setFileReport] = useState<Blob | null>(null);
  const initialTreeData = localStorage.getItem(`${repoId}_tree_data`);
  const [treeData, setTreeData] = useState<TreeView | null>(
    initialTreeData ? JSON.parse(initialTreeData) : null
  );
  const { fileCategory, onClickTab } = useRouter(treeData);
  useHandle(treeData);

  const breadcrumbProps = useBreadcrumb({
    project: project!,
    treeFileSelected
  });

  const menuProps = useMenuRepository({
    tree: treeData,
    menuEvent: info => {
      navigate(`/exploration/${repoId}/file/${info?.key || ""}`);
    }
  });

  const renderFileCategory = useMemo(() => {
    // COBOL_TODO: fetch file data at initial loading
    if (!fileData || !fileCategory) return () => null;
    return tabItemsRender[fileData.group][fileCategory].render;
  }, [fileCategory, fileData]);

  const handleExportFile = () => {
    try {
      if (!fileReport) return;

      handleDownloadFile(fileReport, treeFileSelected?.name);
    } catch (error) {
      // eslint-disable-next-line
      console.log(error);
    }
  };

  // useEffect(() => {
  //   if (!treeFileSelected?.id) return;
  //   const fetchFileReport = async () => {
  //     const res = await blobApi.getBlobFile(treeFileSelected.id);

  //     if (!res) return;
  //     setFileReport(res);
  //   };

  //   fetchFileReport();
  //   return () => setFileReport(null);
  // }, [progressPercent, treeFileSelected?.id]);

  const tabItems = useMemo(
    () =>
      // map key and label from key and value
      // optimize to retrieve key-label by using dictionary instead of array
      fileData
        ? Object.entries(tabItemsRender[fileData.group]).map(([key, value]) => ({
            key,
            label: value.label
          }))
        : [],
    [fileData]
  );
  // eslint-disable-next-line no-console
  useEffect(() => {
    const fetchTreeData = async () => {
      if (!repoId) return;
      if (treeData) return;
      const res = await repositoryApi.getTreeViewDataRequest(repoId);

      if (!res?.data) throw new Error();
      const treeView = res.data;

      setTreeData(treeView);
      localStorage.setItem(`${repoId}_tree_data`, JSON.stringify(treeView));
    };

    fetchTreeData();
  }, [repoId]);

  return (
    <SidebarLayout
      breadcrumb={breadcrumbProps}
      type='narrow'
      existHeader
      renderContent={() => (
        <Flex
          direction='column'
          justify='space-between'
          align='center'
          style={{ height: "100%" }}
          gap={32}
        >
          <Menu
            mode='inline'
            expandIcon={props => (props.isOpen ? <ArrowUpSvg /> : <ArrowDownSvg />)}
            {...menuProps}
          />
        </Flex>
      )}
    >
      <Flex
        gap={24}
        direction='column'
        style={{ padding: "28px 32px", position: "relative", minHeight: 280 }}
      >
        <WrapTabs>
          <Tabs
            activeKey={fileCategory}
            items={tabItems}
            onChange={onClickTab}
            tabBarStyle={{ margin: 0 }}
          />
        </WrapTabs>
        {fileReport ? (
          <ExportBtn type='primary' onClick={handleExportFile} disabled={!fileReport}>
            <div>
              <span>{t("button.export")}</span> <ArrowRightSvg className='icon' />
            </div>
          </ExportBtn>
        ) : null}
        {renderFileCategory()}
      </Flex>
    </SidebarLayout>
  );
};

export const FilePage: React.FC = () => {
  return (
    <Routes>
      <Route index element={<Content />} />
      <Route path={"/:fileId/:fileCategory?"} element={<Content />} />
    </Routes>
  );
};
