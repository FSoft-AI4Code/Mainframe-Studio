/* eslint-disable unused-imports/no-unused-imports */
/* eslint-disable @typescript-eslint/no-unused-vars */
import {
  CaretRightOutlined,
  DownloadOutlined,
  FileOutlined,
  FileTextOutlined,
  FolderOutlined
} from "@ant-design/icons";
import type { CollapseProps, PaginationProps } from "antd";
import { Collapse, Empty, Input, Pagination, Select, Tag } from "antd";
import React, { CSSProperties, useMemo, useState } from "react";
import { useParams } from "react-router-dom";

import { SearchSvg } from "@assets/svg";
import { Button, CustomCard, Flex, Typography } from "@components";
import { allColors, v2CommonColors } from "@style";
import { capitalize } from "@utils";
import { useDuplicateFilesQuery } from "@services";
import { DuplicateNameGroup } from "@types";

const contentDuplicate = {
  name: "Same Name",
  content: "Same Content",
  both: "Same Name & Content",
  "n/a": "N/A"
};

const getDuplicateTypeKey = (
  isName: boolean,
  isContent: boolean
): keyof typeof contentDuplicate => {
  if (isName && isContent) return "both";
  if (isContent) return "content";
  if (isName) return "name";
  return "n/a";
};

function applyDuplicateType(groups: DuplicateNameGroup[]) {
  return groups.map(group => {
    const isName = group.files.length > 1;
    const isContent = group.has_content_duplicates && group.content_duplicates.length > 0;
    const groupTypeKey = getDuplicateTypeKey(isName, isContent);

    const contentDuplicateIds = new Set(group.content_duplicates.flat().map(file => file._id));

    const files = group.files.map(file => {
      const fileTypeKey = getDuplicateTypeKey(isName, contentDuplicateIds.has(file._id));
      return {
        ...file,
        duplicateType: fileTypeKey,
        duplicateContentType: contentDuplicate[fileTypeKey]
      };
    });

    return {
      ...group,
      duplicateType: groupTypeKey,
      duplicateContentType: contentDuplicate[groupTypeKey],
      files
    };
  });
}
export const panelStyles: React.CSSProperties = {
  marginBottom: 24,
  background: allColors.neutral2,
  borderRadius: 8,
  border: `1px solid ${allColors.neutral6}`
};

export const getItems = (
  panelStyle: CSSProperties,
  data: DuplicateNameGroup[]
): CollapseProps["items"] => {
  return data?.map((p, i) => ({
    key: i,
    label: (
      <Flex style={{ fontWeight: "bold" }}>
        <Flex
          style={{
            marginRight: 8
          }}
          gap={4}
        >
          <FileTextOutlined /> {capitalize(p?.name)}
        </Flex>
        <Tag
          style={{
            minWidth: 60
          }}
          color='success'
        >
          {p.label}
        </Tag>
        <Tag
          style={{
            minWidth: 60
          }}
          color='cyan'
        >
          {capitalize(p?.duplicateType as string)} Type
        </Tag>
        <Tag
          style={{
            minWidth: 60
          }}
          color='blue'
        >
          {p?.files?.length} files
        </Tag>
        {/* <Tag
          style={{
            minWidth: 60
          }}
          color='success'
        >
          {p?.files?.[0]?.loc?.toLocaleString()} Loc
        </Tag> */}
      </Flex>
    ),
    children: (
      <Flex direction='column' style={{ marginLeft: "12px" }} gap={12}>
        {p?.files?.map(f => {
          const segments = f?.path?.split("/");
          const fileName = segments?.pop();
          const directoryPath = segments?.join("/");
          return (
            <Flex
              gap={4}
              style={{ borderLeft: `1px solid ${allColors.neutral6}`, paddingLeft: "12px" }}
              direction='column'
              key={f._id}
            >
              <Flex gap={4}>
                <FolderOutlined /> <strong>{directoryPath}</strong>{" "}
                <Tag style={{ whiteSpace: "nowrap" }} color='gold'>
                  <strong>{f?.duplicateContentType}</strong>
                </Tag>
              </Flex>
              <Flex style={{ paddingLeft: 8 }} gap={4}>
                <FileOutlined /> <strong>{fileName}</strong>
              </Flex>

              <Flex style={{ paddingLeft: 8 }} gap={2}>
                <strong>{f?.loc?.toLocaleString()}</strong> Loc
              </Flex>
            </Flex>
          );
        })}
      </Flex>
    ),
    style: panelStyle
  }));
};

function PageContent() {
  const [selectTypeFilter, setSelectTypeFilter] = useState<string>("all");
  const [searchText, setSearchText] = useState<string>("");
  const [sortOption, setSortOption] = useState<string>("most");
  const [pagination, setPagination] = useState({ current: 1, pageSize: 10 });
  const { current: currentPage, pageSize } = pagination || {};
  const { repoId = "" } = useParams();
  const { duplicateNameGroup } = useDuplicateFilesQuery({
    repoId,
    skip: (pagination.current - 1) * pagination.pageSize,
    limit: pagination.pageSize
  });

  const handleTableChange = (page: number, size: number) => {
    setPagination({
      current: page,
      pageSize: size
    });
  };
  const formatedDuplicateFiles = applyDuplicateType(duplicateNameGroup);

  const { data: paginatedData, total: totalItems } = useMemo(() => {
    const totalLoc = (group: (typeof formatedDuplicateFiles)[0]) =>
      group.files.reduce((sum, file) => sum + (file.loc || 0), 0);

    const firstName = (group: (typeof formatedDuplicateFiles)[0]) => group.files[0]?.name || "";

    const filtered = formatedDuplicateFiles.filter(group => {
      const matchType = selectTypeFilter === "all" || group.duplicateType === selectTypeFilter;

      const matchSearch =
        !searchText ||
        group.files.some(
          f =>
            f.name.toLowerCase().includes(searchText.toLowerCase()) ||
            f.path.toLowerCase().includes(searchText.toLowerCase())
        );

      return matchType && matchSearch;
    });

    const sorted = [...filtered].sort((a, b) => {
      switch (sortOption) {
        case "most":
          return b.files.length - a.files.length;
        case "fewest":
          return a.files.length - b.files.length;
        case "locDesc":
          return totalLoc(b) - totalLoc(a);
        case "locAsc":
          return totalLoc(a) - totalLoc(b);
        case "nameAsc":
          return firstName(a).localeCompare(firstName(b));
        case "nameDesc":
          return firstName(b).localeCompare(firstName(a));
        default:
          return 0;
      }
    });

    const startIndex = (currentPage - 1) * pageSize;
    const endIndex = startIndex + pageSize;

    return {
      total: sorted.length,
      data: sorted.slice(startIndex, endIndex)
    };
  }, [formatedDuplicateFiles, selectTypeFilter, sortOption, searchText, pageSize, currentPage]);

  return (
    <Flex
      gap={24}
      direction='column'
      style={{
        padding: 24,
        width: "100%"
      }}
    >
      <Flex
        justify='space-between'
        style={{
          background: v2CommonColors.neutral1,
          padding: 24,
          borderRadius: 8
        }}
        align='center'
        gap={12}
      >
        <Flex direction='column'>
          <Typography style={{ fontWeight: 700 }} level='h5-subtitles' color='primary10'>
            Duplicate File Report
          </Typography>
          <Typography color='primary10' level='body-14b'>
            View and analyze duplicate files across directories
          </Typography>
        </Flex>
      </Flex>
      <CustomCard
        title={
          <Flex direction='column'>
            <Typography level='body-16b' color='primary10'>
              Duplicate File Result
            </Typography>
            <Typography level='body-14r' color='primary9'>
              Found {paginatedData?.length ?? 0} duplicate files
            </Typography>
          </Flex>
        }
        extra={
          <Button
            style={{
              height: 36,
              borderRadius: 8,
              width: 135
            }}
            shape='default'
            type='primary'
            icon={<DownloadOutlined />}
          >
            Export Report
          </Button>
        }
        style={{ height: "100%" }}
        colProps={{
          style: {
            marginBottom: 72
          }
        }}
        bodyStyle={{
          height: "100%",
          overflowX: "auto"
        }}
      >
        <Flex gap={24} direction='column'>
          <Flex align='center' gap={12} justify='space-between'>
            <Input
              placeholder='Search by name or path...'
              value={searchText}
              onChange={e => setSearchText(e.target.value)}
              prefix={<SearchSvg />}
              style={{ height: 32, background: allColors.neutral1, width: 480 }}
            />
            <Select
              value={sortOption}
              onChange={setSortOption}
              style={{ width: 200, marginLeft: "auto" }}
              options={[
                { label: "Most duplicate", value: "most" },
                { label: "Fewest duplicate", value: "fewest" },
                { label: "Largest Loc", value: "locDesc" },
                { label: "Smallest Loc", value: "locAsc" },
                { label: "Name (A-Z)", value: "nameAsc" },
                { label: "Name (Z-A)", value: "nameDesc" }
              ]}
            />

            <Select
              value={selectTypeFilter}
              onChange={value => setSelectTypeFilter(value)}
              style={{ width: 200 }}
              options={[
                { label: "All Types", value: "all" },
                { label: "Same Name", value: "name" },
                { label: "Same Content", value: "content" },
                { label: "Same Name & Content", value: "both" },
                { label: "Mixed Type", value: "mixed" }
              ]}
            />
          </Flex>
          <>
            {paginatedData.length === 0 ? (
              <Empty description='No data available' />
            ) : (
              <Collapse
                bordered={false}
                expandIcon={({ isActive }) => <CaretRightOutlined rotate={isActive ? 90 : 0} />}
                style={{ background: allColors.neutral1 }}
                items={getItems(panelStyles, paginatedData as unknown as DuplicateNameGroup[])}
                expandIconPosition='end'
              />
            )}
          </>
          <Pagination
            current={currentPage}
            pageSize={pageSize}
            total={totalItems}
            style={{
              marginTop: -12,
              marginLeft: "auto"
            }}
            showSizeChanger
            pageSizeOptions={["5", "10", "20", "50"]}
            onChange={handleTableChange}
            showTotal={(total, range) => `${range[0]}–${range[1]} of ${total} items`}
          />
        </Flex>
      </CustomCard>
    </Flex>
  );
}

export const DuplicatePage: React.FC = () => {
  return (
    <Flex
      direction='column'
      style={{ width: "100%", minHeight: "100vh", overflowY: "auto", marginBottom: 24 }}
    >
      <PageContent />
    </Flex>
  );
};
